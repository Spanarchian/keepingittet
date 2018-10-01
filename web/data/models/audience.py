from gdb import gdb

from py2neo import Graph
graph = Graph()


def get_audience():
    x = gdb.get_db()
    data = x.data("MATCH (a:CAMPAIGN) RETURN a.ref")

    for elem in data:
        print("Element : {}".format(elem))

