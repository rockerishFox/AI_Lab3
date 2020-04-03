from Service.Service import Service
from Utils import show_communities, print_solution


def main():
    files = ["input/karate.gml", "input/dolphins.gml", "input/football.gml", "input/krebs.gml"]
    mine = ["input/lesmis.gml", "input/adjnoun.gml"]
    serv = Service(mine[0])
    rez = serv.create_solution(150)
    print_solution(rez)
    show_communities(rez[2], rez[3])


main()
