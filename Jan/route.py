from dataclasses import dataclass

from Jan.GC import GameCoordinate
from Jan.speler import Speler
from Jan.terrein import Gras, Speelveld
from Jan.eenheid import Eenheid, LandmachtEenheid

SPEELVELD_BREEDTE = 20
SPEELVELD_HOOGTE = 15

@dataclass
class RouteSchakel:
    gc: GameCoordinate
    afstand_tot_begin: int




class Route:
    def __init__(self, gc: GameCoordinate):
        self.stappen = [gc] # lijst met tegelcoordinaten
        self.afstand = 0

    def begin(self):
        return self.stappen[0]

    def einde(self):
        return self.stappen[-1]

    def breidt_uit(self, gc: GameCoordinate, afstand):
        nieuwe_route = Route(None)
        nieuwe_route.stappen = self.stappen[:] + [gc] # copy and extend route
        nieuwe_route.afstand = afstand
        return nieuwe_route
    @staticmethod
    def get_best_route(eenheid: Eenheid, terrein: Speelveld, target_gc, max_afstand):
        routes = Route.explore_routes_from(eenheid, terrein, max_afstand)
        return routes[target_gc]


    @staticmethod
    def explore_routes_from(eenheid, terrein, max_afstand):
        # maak een leeg speelveld met potentiële routes
        routes = Speelveld(terrein.breedte, terrein.hoogte, None)
        startroute = Route(eenheid.gc)
        routes[eenheid.gc] = startroute

        routes_te_exploreren = [startroute]
        while len(routes_te_exploreren) > 0:
            routes_te_exploreren = Route.groei_routes(routes_te_exploreren, routes, eenheid, terrein, max_afstand)
        return routes

    @staticmethod
    def groei_routes(routes_te_exploreren, routes, eenheid, terrein, max_afstand):
        nieuwe_routes = []
        richtingen = [GameCoordinate(0, 1), GameCoordinate(0, -1), GameCoordinate(1, 0), GameCoordinate(-1, 0)]
        for route_te_exploreren in routes_te_exploreren:
            route_eindpunt = route_te_exploreren.einde()
            for richting in richtingen:
                coord = route_eindpunt + richting
                try:
                    veld = terrein[coord]
                except:
                    continue # buiten speelveld
                inspanning = eenheid.inspanning[veld]
                afstand = route_te_exploreren.afstand + inspanning
                if afstand <= max_afstand: # veld is bereikbaar volgens huidige route
                    if routes[coord] is None or afstand < routes[coord].afstand: # nog geen route naar deze coordinaat of nieuwe route is korter dan reeds gevonden
                        nieuwe_route = route_te_exploreren.breidt_uit(coord, afstand)
                        routes[coord] = nieuwe_route
                        nieuwe_routes.append(nieuwe_route)
        return nieuwe_routes






if __name__ == "__main__":
    eenheid = LandmachtEenheid(GameCoordinate(2, 2), Speler(4))


    best_route = Route.get_best_route(eenheid, Speelveld(SPEELVELD_BREEDTE, SPEELVELD_HOOGTE, Gras), GameCoordinate(5, 5), 20)
    print(best_route)