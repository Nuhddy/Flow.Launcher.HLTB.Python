import webbrowser

from flowlauncher import FlowLauncher
from howlongtobeatpy import HowLongToBeat


class Hltb(FlowLauncher):
    def query(self, param='') -> list:
        entries = []
        for r in self.search_hltb(param):
            entries.append(
                {
                    'Title': r.game_name,
                    'SubTitle': 'Main: {} | Main + Extra: {} | Completionist: {}'.format(
                        round(r.main_story),
                        round(r.main_extra),
                        round(r.completionist),
                        r.all_styles,
                    ),
                    'IcoPath': r.game_image_url,
                    'JsonRPCAction': {
                        'method': 'open_url',
                        'parameters': [r.game_web_link],
                    },
                }
            )

        return entries

    def open_url(self, url) -> None:
        webbrowser.open(url)

    def search_hltb(self, query) -> list:
        if query == '':
            return []

        results = HowLongToBeat().search(query)
        if results is None:
            return []

        return [r for r in results]
