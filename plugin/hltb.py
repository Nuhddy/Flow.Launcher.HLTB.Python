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
                    ),
                    'ContextData': [
                        r.game_image_url,
                        r.game_name,
                        r.game_type,
                        r.main_story,
                        r.main_extra,
                        r.completionist,
                    ],
                    'IcoPath': r.game_image_url,
                    'JsonRPCAction': {
                        'method': 'open_url',
                        'parameters': [r.game_web_link],
                    },
                }
            )

        return entries

    def format_game_type(self, game_type: str) -> str:
        if game_type == 'dlc':
            return game_type.upper()
        else:
            return game_type.capitalize()

    def context_menu(self, data) -> list:
        game = {
            'icon': data[0],
            'title': data[1],
            'type': self.format_game_type(data[2]),
            'main': data[3],
            'main_extra': data[4],
            'completionist': data[5],
        }

        return [
            {
                'Title': game['title'],
                'SubTitle': game['type'],
                'IcoPath': game['icon'],
            },
            {
                'Title': 'Main Story: {} Hours'.format(game['main']),
                'IcoPath': game['icon'],
            },
            {
                'Title': 'Main + Extra: {} Hours'.format(game['main_extra']),
                'IcoPath': game['icon'],
            },
            {
                'Title': 'Completionist: {} Hours'.format(
                    game['completionist']
                ),
                'IcoPath': game['icon'],
            },
        ]

    def open_url(self, url) -> None:
        webbrowser.open(url)

    def search_hltb(self, query) -> list:
        if query == '':
            return []

        results = HowLongToBeat().search(query)
        if results is None:
            return []

        return [r for r in results]
