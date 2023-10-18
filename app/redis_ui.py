import redis
from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer, Header, Input

redis = redis.Redis()


class RedisUI(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    KEY_HEADERS = ['No', 'Key', 'Type']
    KEYS = []

    def compose(self) -> ComposeResult:
        yield Header()

        yield Input()

        for id, key in enumerate(redis.keys('*'), 1):
            self.KEYS.append((id, key.decode('utf-8'), redis.type(key).decode('utf-8')))

        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*self.KEY_HEADERS)

        table.add_rows(self.KEYS)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        table = self.query_one(DataTable)
        table.clear()

        self.KEYS = []
        for id, key in enumerate(redis.keys(event.input.value), 1):
            self.KEYS.append((id, key.decode('utf-8'), redis.type(key).decode('utf-8')))

        table.add_rows(self.KEYS)

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
