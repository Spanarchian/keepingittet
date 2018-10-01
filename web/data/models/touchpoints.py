from .gdb import gdb

from py2neo import Graph
graph = Graph()


test_touchpoints = [
  {
    "touchpoint": "Touchpoint1",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint2",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint3",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint4",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint5",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint6",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers cost": 25.00,
    "sellers_cost_updates": 2.50
  },
  {
    "touchpoint": "Touchpoint7",
    "conversion_rate": 6.35,
    "campaign_cost": 100,
    "sellers cost": 25.00,
    "sellers_cost_updates": 2.50
  }
]

    
def get_touchpoints_test():
    return test_touchpoints


def read_touchpoints():
    x = gdb.get_db()
    data = x.data("MATCH (n:TOUCHPOINT) RETURN n")

    for elem in data:
        print("Element : {}".format(elem))


def read_touchpoints_by(ref, cat):
    x = gdb.get_db()
    result = ref+cat
    return result


def create_touchpoint(camp):
    x = gdb.get_db()
    print(camp)
    x.run("""
            create (c :TOUCHPOINT) set c += {props}
          """, {"props": camp})


def load_touchpoints():
    x = gdb.get_db()
    data = x.data("MATCH (a:TOUCHPOINT) RETURN a")
    for elem in data:
        print("Element : {}".format(elem))


def report_touchpoints():
    x = gdb.get_db()
    resp = x.data("MATCH (a:TOUCHPOINT)-[]->(i) RETURN i.type as Industry, count(a) as Campaigns")

    print("RESP = {}".format(resp))
