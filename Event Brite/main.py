import requests
import json
import csv


class EventBrite():
    def __init__(self, url, headers, payload):
        self.url = url
        self.headers = headers
        self.payload = payload
        self.send_request()

        self.names = []
        self.minimum_ticket_price = []
        self.maximum_ticket_price = []
        self.start_date = []
        self.start_time = []
        self.end_time = []

    def send_request(self):
        self.response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
        if self.response.status_code != 200:
            raise Exception ("Something wrong from the server")

    def to_csv(self):
        with open('events.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['Name', 'Minimum_Price', 'Maximum_Price', 'Start_Time', 'End_Time', 'Start_Date'])
            for name, min_price, max_price, start_time, end_time, start_date in zip(self.names, self.minimum_ticket_price, self.maximum_ticket_price, self.start_time, self.end_time, self.start_date):
                writer.writerow([name, min_price, max_price, start_time, end_time, start_date])

    def parse(self):
        event_data = json.loads(self.response.text.encode('utf-8'))

        for event in event_data.get('events').get('results'):
            self.names.append(event.get('name'))
            self.minimum_ticket_price.append(event.get('ticket_availability').get('minimum_ticket_price').get('major_value'))
            self.maximum_ticket_price.append(event.get('ticket_availability').get('maximum_ticket_price').get('major_value'))
            self.start_time.append(event.get('start_time'))
            self.end_time.append(event.get('end_time'))
            self.start_date.append(event.get('start_date'))

        self.to_csv()


url = "https://www.eventbrite.com/api/v3/destination/search/"
payload = "{\n    \"event_search\": {\n        \"dates\": \"current_future\",\n        \"date_range\": {\n            \"to\": \"2020-03-09\",\n            \"from\": \"2020-03-01\"\n        },\n        \"places\": [\n            \"85922583\"\n        ],\n        \"tags\": [\n            \"EventbriteCategory/105\"\n        ],\n        \"page\": 1,\n        \"page_size\": 20,\n        \"online_events_only\": false\n    },\n    \"expand.destination_event\": [\n        \"primary_venue\",\n        \"image\",\n        \"ticket_availability\",\n        \"saves\",\n        \"series\",\n        \"my_collections\",\n        \"event_sales_status\"\n    ]\n}"
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'mgrefby=; G=v%3D2%26i%3D04a6a593-b419-451f-9ac7-8912a963e9b4%26a%3Dc6c%26s%3Dd5758d1aa25c0cfb0796627ab2a0d2e3b3e89548; ebEventToTrack=; SS=AE3DLHRJvw4_G1PP1g-NPUptbcQJqC4HfQ; eblang=lo%3Den_US%26la%3Den-us; AS=d5bd31b0-4eb7-41c6-a320-5a9f750c6984; AN=; mgref=typeins; csrftoken=dbb779f036e411eab665ef1f6bf713f4; _ga=GA1.2.687545818.1579016719; _gid=GA1.2.793628407.1579016719; ebGAClientId=687545818.1579016719; SERVERID=djc21; _gaexp=GAX1.2.VMDdMrAiSGGJcy4TVI4fsA.18364.1; _gat=1; SP=AGQgbblddF5PazpGFBt4lRLZZGqYlCMU_rLMpzVUm3oy-Yx7eEuBr0dEY8JREJbcvuqQGTybS9L9qyHtNIKm5dkQYpmO52JXbNFjh0Gc_oRKGL641yAaMwrS3dU0qMT79jcVQyAyJXGd0Zfu1vf_sp_A_1fDhCoXpXALtN8iqckveFRigHG19AZv0l3bssn25vFEXPY2uunn9xOoo6ppm6_Ai8qk5eZOV-7gr66NHg66xQVzvt2en70; janus=v%3D1%26exp_eb_127335_derank_sold_out_events_in_search%3DNone%26exp_eb_search_experiment_1%3DNone%26exp_eb_search_experiment_10%3DNone%26exp_eb_search_experiment_2%3DNone%26exp_eb_search_experiment_3%3DNone%26exp_eb_search_experiment_4%3DNone%26exp_eb_search_experiment_5%3DNone%26exp_eb_search_experiment_6%3DNone%26exp_eb_search_experiment_7%3DNone%26exp_eb_search_experiment_8%3DNone%26exp_eb_search_experiment_9%3DNone',
  'X-Requested-With': 'XMLHttpRequest',
  'X-CSRFToken': 'dbb779f036e411eab665ef1f6bf713f4',
  'Referer': 'https://www.eventbrite.com/d/ca--san-francisco/arts--events/?end_date=2020-03-09&page=4&start_date=2020-03-01'
}

brite = EventBrite(url, headers, payload)
brite.parse()