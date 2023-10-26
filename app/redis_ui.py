import redis
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Input, OptionList

redis = redis.Redis()


class RedisUI(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    KEY_HEADERS = ['No', 'Key', 'Type']
    KEYS = []

    def compose(self) -> ComposeResult:
        yield Header()

        yield Input()

        for key in redis.keys('*'):
            self.KEYS.append(f"{key.decode('utf-8')} ({redis.type(key).decode('utf-8').upper()})")

        yield OptionList(*self.KEYS)

        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        option_list = self.query_one(OptionList)
        option_list.clear_options()

        self.KEYS = []
        for key in redis.keys(event.input.value):
            self.KEYS.append(f"{key.decode('utf-8')} ({redis.type(key).decode('utf-8').upper()})")

        option_list.add_options(self.KEYS)


    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
