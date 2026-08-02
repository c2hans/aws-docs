---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/kinesis-analytics-v2_example_kinesis-analytics-v2_DataGenerator_Stagger_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Generate a Kinesis stream with stagger data using an AWS SDK
<a name="kinesis-analytics-v2_example_kinesis-analytics-v2_DataGenerator_Stagger_section"></a>

The following code example shows how to generate a Kinesis stream with stagger data.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
import datetime
import json
import random
import time
import boto3

STREAM_NAME = "ExampleInputStream"

def get_data():
    event_time = datetime.datetime.utcnow() - datetime.timedelta(seconds=10)
    return {
        "EVENT_TIME": event_time.isoformat(),
        "TICKER": random.choice(["AAPL", "AMZN", "MSFT", "INTC", "TBV"]),
    }

def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        # Send six records, ten seconds apart, with the same event time and ticker
        for _ in range(6):
            print(data)
            kinesis_client.put_record(
                StreamName=stream_name,
                Data=json.dumps(data),
                PartitionKey="partitionkey",
            )
            time.sleep(10)

if __name__ == "__main__":
    generate(STREAM_NAME, boto3.client("kinesis"))
```

------
