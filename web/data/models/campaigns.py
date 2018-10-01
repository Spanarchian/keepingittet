from gdb import gdb

from py2neo import Graph
graph = Graph()


test_campaigns = [
  {
    "campaign": "Campaign1",
    "industry": "Nanotechnology",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal_Top": 999,
    "Predicted_Goal_Ideal": 777,
    "Predicted_Goal_Low": 555,
    "Actual Goal": "785",
    "Conversion Rate": 55.55,
    "Starting Budget": 500.50,
    "Cost": 275.45,
    "Improvements Cost": 150,
    "Success Fee": 75.50,
    "Budget Rollover": 2.50
  },
  {
    "campaign": "Campaign2",
    "industry": "Biotechnology",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal_Top": 999,
    "Predicted_Goal_Ideal": 777,
    "Predicted_Goal_Low": 555,
    "Actual Goal": "785",
    "Conversion Rate": 55.55,
    "Starting Budget": 500.50,
    "Cost": 275.45,
    "Improvements Cost": 150,
    "Success Fee": 75.50,
    "Budget Rollover": 2.50
  },
  {
    "campaign": "Campaign3",
    "industry": "Pharmaceuticals",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal_Top": 999,
    "Predicted_Goal_Ideal": 777,
    "Predicted_Goal_Low": 555,
    "Actual Goal": "785",
    "Conversion Rate": 55.55,
    "Starting Budget": 500.50,
    "Cost": 275.45,
    "Improvements Cost": 150,
    "Success Fee": 75.50,
    "Budget Rollover": 2.50
  },
  {
    "campaign": "Campaign4",
    "industry": "Maritime",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal_Top": 999,
    "Predicted_Goal_Ideal": 777,
    "Predicted_Goal_Low": 555,
    "Actual Goal": "785",
    "Conversion Rate": 55.55,
    "Starting Budget": 500.50,
    "Cost": 275.45,
    "Improvements Cost": 150,
    "Success Fee": 75.50,
    "Budget Rollover": 2.50
  },
  {
    "campaign": "Campaign5",
    "industry": "Pharmaceuticals",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal_Top": 999,
    "Predicted_Goal_Ideal": 777,
    "Predicted_Goal_Low": 555,
    "Actual Goal": "785",
    "Conversion Rate": 55.55,
    "Starting Budget": 500.50,
    "Cost": 275.45,
    "Improvements Cost": 150,
    "Success Fee": 75.50,
    "Budget Rollover": 2.50
  },
  {
    "campaign": "Campaign6",
    "industry": "Nanotechnology",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal_Top": 999,
    "Predicted_Goal_Ideal": 777,
    "Predicted_Goal_Low": 555,
    "Actual Goal": "785",
    "Conversion Rate": 55.55,
    "Starting Budget": 500.50,
    "Cost": 275.45,
    "Improvements Cost": 150,
    "Success Fee": 75.50,
    "Budget Rollover": 2.50
  },
  {
    "campaign": "Campaign7",
    "industry": "Biotechnology",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal_Top": 999,
    "Predicted_Goal_Ideal": 777,
    "Predicted_Goal_Low": 555,
    "Actual Goal": "785",
    "Conversion Rate": 55.55,
    "Starting Budget": 500.50,
    "Cost": 275.45,
    "Improvements Cost": 150,
    "Success Fee": 75.50,
    "Budget Rollover": 2.50
  }
]


camp1 = {
    "campaign": "Campaign99",
    "industry": "Biotechnology",
    "target": "BrandAwareness",
    "touchpoints": [
      "Touchpoint1",
      "Touchpoint2",
      "Touchpoint5"
    ],
    "Predicted_Goal_Top": 999,
    "Predicted_Goal_Ideal": 777,
    "Predicted_Goal_Low": 555,
    "Actual Goal": "785",
    "Conversion Rate": 99.99,
    "Starting Budget": 999.99,
    "Cost": 999.99,
    "Improvements Cost": 999.99,
    "Success Fee": 99.99,
    "Budget Rollover": 99.99
  }


def get_campaigns():
    return test_campaigns


def read_campaigns():
    return 5


def read_campaigns_by(ref, cat):
    result = ref+cat
    return result


def create_campaign(camp):
    x = gdb.get_db()
    print(camp)
    x.run("""
            create (c :CAMPAIGN) set c += {props}
          """, {"props": camp})


def load_campaigns():
    x = gdb.get_db()
    data = x.data("MATCH (a:CAMPAIGN) RETURN a.campaign")

    for elem in data:
        print("Element : {}".format(elem))


def report_campaigns():
    x = gdb.get_db()
    resp = x.data("MATCH (a:CAMPAIGN)-[]->(i) RETURN i.type as Industry, count(a) as Campaigns")

    print("RESP = {}".format(resp))


report_campaigns()
# create_campaign(camp1)
#
# load_campaigns()
