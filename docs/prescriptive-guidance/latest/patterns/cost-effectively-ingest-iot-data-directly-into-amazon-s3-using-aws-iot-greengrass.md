---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass.html
---

# Cost-effectively ingest IoT data directly into Amazon S3 using AWS IoT Greengrass
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass"></a>

*Sebastian Viviani and Rizwan Syed, Amazon Web Services*

## Summary
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass-summary"></a>

This pattern shows you how to cost-effectively ingest Internet of Things (IoT) data directly into an Amazon Simple Storage Service (Amazon S3) bucket by using an AWS IoT Greengrass Version 2 device. The device runs a custom component that reads the IoT data and saves the data in persistent storage (that is, a local disk or volume). Then, the device compresses the IoT data into an Apache Parquet file and uploads the data periodically to an S3 bucket.

The amount and speed of IoT data that you ingest is limited only by your edge hardware capabilities and network bandwidth. You can use Amazon Athena to cost-effectively analyze your ingested data. Athena supports compressed Apache Parquet files and data visualization by using [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html).

## Prerequisites and limitations
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An [edge gateway](https://docs.aws.amazon.com/greengrass/v1/developerguide/quick-start.html) that runs on [AWS IoT Greengrass Version 2](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-v2-whats-new.html) and collects data from sensors (The data sources and the data collection process are beyond the scope of this pattern, but you can use nearly any type of sensor data. This pattern uses a local [MQTT](https://mqtt.org/) broker with sensors or gateways that publish data locally.)
+ AWS IoT Greengrass [component](https://docs.aws.amazon.com/greengrass/v2/developerguide/develop-greengrass-components.html), [roles](https://docs.aws.amazon.com/greengrass/v1/developerguide/service-role.html), and [SDK dependencies](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
+ A [stream manager component](https://docs.aws.amazon.com/greengrass/v2/developerguide/stream-manager-component.html) to upload the data to the S3 bucket
+ [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/), [AWS SDK for JavaScript](https://aws.amazon.com/sdk-for-javascript/), or [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/pythonsdk/) to run the APIs

**Limitations**
+ The data in this pattern isn’t uploaded in real time to the S3 bucket. There is a delay period, and you can configure the delay period. Data is buffered temporarily in the edge device and then uploaded once the period expires.
+ The SDK is available only in Java, Node.js, and Python.

## Architecture
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass-architecture"></a>

**Target technology stack**
+ Amazon S3
+ AWS IoT Greengrass
+ MQTT broker
+ Stream manager component

**Target architecture**

The following diagram shows an architecture designed to ingest IoT sensor data and store that data in an S3 bucket.

![Architecture diagram](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b9032ae2-fffb-4750-b161-09810e19d878/images/8c28e639-5dcf-4950-b4a6-8015ec1a2894.png)

The diagram shows the following workflow:

1. Multiple sensors (for example, temperature and valve) updates are published to a local MQTT broker.

1. The Parquet file compressor that's subscribed to these sensors updates topics and receives these updates.

1. The Parquet file compressor stores the updates locally.

1. After the period lapses, the stored files are compressed into Parquet files and passed on to the stream manager to get uploaded to the specified S3 bucket.

1. The stream manager uploads the Parquet files to the S3 bucket.

**Note**
The stream manager (`StreamManager`) is a managed component. For examples of how to export data to Amazon S3, see [Stream manager](https://docs.aws.amazon.com/greengrass/v2/developerguide/stream-manager-component.html) in the AWS IoT Greengrass documentation. You can use a local MQTT broker as a component or another broker like [Eclipse Mosquitto](https://mosquitto.org/).

## Tools
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass-tools"></a>

**AWS tools**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon S3 by using standard SQL.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) is an open source IoT edge runtime and cloud service that helps you build, deploy, and manage IoT applications on your devices.

**Other tools**
+ [Apache Parquet](https://parquet.apache.org/) is an open-source column-oriented data file format designed for storage and retrieval.
+ [MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) (Message Queuing Telemetry Transport) is a lightweight messaging protocol that's designed for constrained devices.

## Best practices
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass-best-practices"></a>

**Use the right partition format for uploaded data**

There are no specific requirements for the root prefix names in the S3 bucket (for example, `"myAwesomeDataSet/"` or `"dataFromSource"`), but we recommend that you use a meaningful partition and prefix so that it's easy to understand the purpose of the dataset.

We also recommend that you use the right partitioning in Amazon S3 so that the queries run optimally on the dataset. In the following example, the data is partitioned in HIVE format so that the amount of data scanned by each Athena query is optimized. This improves performance and reduces cost.

`s3://<ingestionBucket>/<rootPrefix>/year=YY/month=MM/day=DD/HHMM_<suffix>.parquet`

## Epics
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | 1. [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) or use an existing bucket.<br />2. Create a meaningful [prefix](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) for the S3 bucket where you want to ingest the IoT data (for example, `s3:\\<bucket>\<prefix>`).<br />3. Record your prefix for later use. | App developer |
| Add IAM permissions to the S3 bucket. | To grant users write access to the S3 bucket and prefix that you created earlier, add the following IAM policy to your AWS IoT Greengrass role:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "S3DataUpload",<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:List*",<br />                "s3:Put*"<br />            ],<br />            "Resource": [<br />                "arn:aws:s3:::<ingestionBucket>",<br />                "arn:aws:s3:::<ingestionBucket>/<prefix>/*"<br />            ]<br />        }<br />    ]<br />}</pre><br />For more information, see [Creating an IAM policy to access Amazon S3 resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.S3CreatePolicy.html) in the Aurora documentation.<br />Next, update the resource policy (if needed) for the S3 bucket to allow write access with the correct AWS [principals](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-bucket-user-policy-specifying-principal-intro.html). | App developer |

### Build and deploy the AWS IoT Greengrass component
<a name="build-and-deploy-the-aws-iot-greengrass-component"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the recipe of the component. | [Update the component configuration](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html) when you [create a deployment](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) based on the following example:<pre>{<br />  "region": "<region>",<br />  "parquet_period": <period>,<br />  "s3_bucket": "<s3Bucket>",<br />  "s3_key_prefix": "<s3prefix>"<br />}</pre><br />Replace `<region>` with your AWS Region, `<period>` with your periodic interval, `<s3Bucket>` with your S3 bucket, and `<s3prefix>` with your prefix. | App developer |
| Create the component. | Do one of the following:+ [Create the component](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-components.html).<br />+ Add the component to the CI/CD pipeline (if one exists). Be sure to copy the artifact from the artifact repository to the AWS IoT Greengrass artifact bucket. Then, create or update your AWS IoT Greengrass component.<br />+ Add the MQTT broker as a component or add it manually later. : This decision affects the authentication scheme that you can use with the broker. Manually adding a broker decouples the broker from AWS IoT Greengrass and enables any supported authentication scheme of the broker. The AWS provided broker components have predefined authentication schemes. For more information, see [MQTT 3.1.1 broker (Moquette)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-moquette-component.html) and [MQTT 5 broker (EMQX)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html). | App developer |
| Update the MQTT client. | The sample code doesn't use authentication because the component connects locally to the broker. If your scenario differs, update the MQTT client section as needed. Additionally, do the following:1. Update the MQTT topics in the subscription.<br />2. Update the MQTT message parser as needed as messages from each source may differ. | App developer |

### Add the component to the AWS IoT Greengrass Version 2 core device
<a name="add-the-component-to-the-aws-iot-greengrass-version-2-core-device"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the deployment of the core device. | If the deployment of the AWS IoT Greengrass Version 2 core device already exists, [revise the deployment](https://docs.aws.amazon.com/greengrass/v2/developerguide/revise-deployments.html). If the deployment doesn't exist, [create a new deployment](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html).<br />To give the component the correct name, [update the log manager configuration](https://docs.aws.amazon.com/greengrass/v2/developerguide/log-manager-component.html) for the new component (if needed) based on the following:<pre>{<br />  "logsUploaderConfiguration": {<br />    "systemLogsConfiguration": {<br />    ...<br />    },<br />    "componentLogsConfigurationMap": {<br />      "<com.iot.ingest.parquet>": {<br />        "minimumLogLevel": "INFO",<br />        "diskSpaceLimit": "20",<br />        "diskSpaceLimitUnit": "MB",<br />        "deleteLogFileAfterCloudUpload": "false"<br />      }<br />      ...<br />    }<br />  },<br />  "periodicUploadIntervalSec": "300"<br />}</pre><br />Finally, complete the revision of the deployment for your AWS IoT Greengrass core device. | App developer |

### Verify data ingestion into the S3 bucket
<a name="verify-data-ingestion-into-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check the logs for the AWS IoT Greengrass volume. | Check for the following:+ The MQTT client is successfully connected to the local MQTT broker.<br />+ The MQTT client is subscribed to the correct topics.<br />+ Sensor update messages are coming to the broker on the MQTT topics.<br />+ Parquet compression happens at every periodic interval. | App developer |
| Check the S3 bucket. | Verify if the data is being uploaded to the S3 bucket. You can see the files being uploaded at every period.<br />You can also verify if the data is uploaded to the S3 bucket by querying the data in the next section. | App developer |

### Set up querying from Athena
<a name="set-up-querying-from-athena"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a database and table. | 1. [Create an AWS Glue database](https://docs.aws.amazon.com/glue/latest/dg/console-databases.html) (if needed).<br />2. Create a table in AWS Glue [manually](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html) or by running a [crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) in AWS Glue. | App developer |
| Grant Athena access to the data. | 1. Update permissions to allow Athena to access the S3 bucket. For more information, see [Fine-grained access to databases and tables in the AWS Glue Data Catalog](https://docs.aws.amazon.com/athena/latest/ug/fine-grained-access-to-glue-resources.html) in the Athena documentation.<br />2. Query the table in your database. | App developer |

## Troubleshooting
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| MQTT client fails to connect | + Validate the permissions on the MQTT broker. If you have an MQTT broker from AWS, see [MQTT 3.1.1 broker (Moquette)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-moquette-component.html) and [MQTT 5 broker (EMQX)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html).<br />+ Validate the credentials on the MQTT client. If you have an MQTT broker from AWS, see [MQTT 3.1.1 broker (Moquette)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-moquette-component.html) and [MQTT 5 broker (EMQX)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html). |
| MQTT client fails to subscribe | Validate the permissions on the MQTT broker. If you have an MQTT broker from AWS, see [MQTT 3.1.1 broker (Moquette)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-moquette-component.html) and [MQTT 5 broker (EMQX)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html). |
| Parquet files don't get created | + Verify that the MQTT topics are correct.<br />+ Verify that the MQTT messages from the sensors are in the correct format. |
| Objects are not uploaded to the S3 bucket | + Verify that you have internet connectivity and endpoint connectivity.<br />+ Verify that the resource policy for your S3 bucket is correct.<br />+ Verify the permissions for the AWS IoT Greengrass Version 2 core device role. |

## Related resources
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass-resources"></a>
+ [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) (Pandas documentation)
+ [Apache Parquet Documentation](https://parquet.apache.org/docs/) (Parquet documentation)
+ [Develop AWS IoT Greengrass components](https://docs.aws.amazon.com/greengrass/v2/developerguide/develop-greengrass-components.html) (AWS IoT Greengrass Developer Guide, Version 2)
+ [Deploy AWS IoT Greengrass components to devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-deployments.html) (AWS IoT Greengrass Developer Guide, Version 2)
+ [Interact with local IoT devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/interact-with-local-iot-devices.html) (AWS IoT Greengrass Developer Guide, Version 2)
+ [MQTT 3.1.1 broker (Moquette)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-moquette-component.html) (AWS IoT Greengrass Developer Guide, Version 2)
+ [MQTT 5 broker (EMQX)](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-emqx-component.html) (AWS IoT Greengrass Developer Guide, Version 2)

## Additional information
<a name="cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass-additional"></a>

**Cost analysis**

The following cost analysis scenario demonstrates how the data ingestion approach covered in this pattern can impact data ingestion costs in the AWS Cloud. The pricing examples in this scenario are based on prices at the time of publication. Prices are subject to change. Additionally, your costs may vary depending on your AWS Region, AWS service quotas, and other factors related to your cloud environment.

*Input signal set*

This analysis uses the following set of input signals as the basis for comparing IoT ingestion costs with other available alternatives.

|
|
| Number of signals | Frequency | Data per signal |
| --- |--- |--- |
| 125 | 25 Hz | 8 bytes |

In this scenario, the system receives 125 signals. Each signal is 8 bytes and occurs every 40 milliseconds (25 Hz). These signals could come individually or grouped in a common payload. You have the option to split and pack these signals based on your needs. You can also determine the latency. Latency consists of the time period for receiving, accumulating, and ingesting the data.

For comparison purposes, the ingestion operation for this scenario is based in the `us-east-1` AWS Region. The cost comparison applies to AWS services only. Other costs, like hardware or connectivity, are not factored into the analysis.

*Cost comparisons*

The following table shows the monthly cost in US dollars (USD) for each ingestion method.

|
|
| Method | Monthly cost |
| --- |--- |
| AWS IoT SiteWise*\** | 331.77 USD |
| AWS IoT SiteWise Edge with data processing pack (keeping all data at the edge) | 200 USD |
| AWS IoT Core and Amazon S3 rules for accessing raw data | 84.54 USD |
| Parquet file compression at the edge and uploading to Amazon S3 | 0.5 USD |

\*Data must be downsampled to comply with service quotas. This means there is some data loss with this method.

*Alternative methods*

This section shows the equivalent costs for the following alternative methods:
+ **AWS IoT SiteWise** – Each signal must be uploaded in an individual message. Therefore, the total number of messages per month is 125×25×3600×24×30, or 8.1 billion messages per month. However, AWS IoT SiteWise can handle only 10 data points per second per property. Assuming the data is downsampled to 10 Hz, the number of messages per month is reduced to 125×10×3600×24×30, or 3.24 billion. If you use the publisher component that packs measurements in groups of 10 (at 1 USD per million messages), then you get a monthly cost of 324 USD per month. Assuming that each message is 8 bytes (1 Kb/125), that’s 25.92 Gb of data storage. This adds a monthly cost of 7.77 USD per month. The total cost for the first month is 331.77 USD and increases by 7.77 USD every month.
+ **AWS IoT SiteWise Edge with data processing pack, including all models and signals fully processed at the edge (that is, no cloud ingestion)** – You can use the data processing pack as an alternative to reduce costs and to configure all the models that get calculated at the edge. This can work just for storage and visualization, even if no real calculation is performed. In this case, it’s necessary to use powerful hardware for the edge gateway. There is a fixed cost of 200 USD per month.
+ **Direct ingestion to AWS IoT Core by MQTT and an IoT rule to store the raw data in Amazon S3** – Assuming all the signals are published in a common payload, the total number of messages published to AWS IoT Core is 25×3600×24×30, or 64.8 million per month. At 1 USD per million messages, that’s a monthly cost of 64.8 USD per month. At 0.15 USD per million rule activations and with one rule per message, that adds a monthly cost of 19.44 USD per month. At a cost of 0.023 USD per Gb of storage in Amazon S3, that adds another 1.5 USD per month (increasing every month to reflect the new data). The total cost for the first month is 84.54 USD and increases by 1.5 USD every month.
+ **Compressing data at the edge in a Parquet file and uploading to Amazon S3 (proposed method**) – The compression ratio depends on the type of data. With the same industrial data tested for MQTT, the total output data for a full month is 1.2 Gb. This costs 0.03 USD per month. Compression ratios (using random data) described in other benchmarks are on the order of 66 percent (closer to a worst-case scenario). The total data is 21 Gb and costs 0.5 USD per month.

**Parquet file generator**

The following code example shows the structure of a Parquet file generator that's written in Python. The code example is for illustration purposes only and won’t work if pasted into your environment.

```
import queue
import paho.mqtt.client as mqtt
import pandas as pd

#queue for decoupling the MQTT thread
messageQueue = queue.Queue()
client = mqtt.Client()
streammanager = StreamManagerClient()

def feederListener(topic, message):
    payload = {
        "topic" : topic,
        "payload" : message,
    }
    messageQueue.put_nowait(payload)

def on_connect(client_instance, userdata, flags, rc):
    client.subscribe("#",qos=0)

def on_message(client, userdata, message):
    feederListener(topic=str(message.topic), message=str(message.payload.decode("utf-8")))

filename = "tempfile.parquet"
streamname = "mystream"
destination_bucket= "DOC-EXAMPLE-BUCKET"
keyname="mykey"
period= 60

client.on_connect = on_connect
client.on_message = on_message
streammanager.create_message_stream(
            MessageStreamDefinition(name=streamname, strategy_on_full=StrategyOnFull.OverwriteOldestData)
        )

while True:
   try:
       message = messageQueue.get(timeout=myArgs.mqtt_timeout)
   except (queue.Empty):
       logger.warning("MQTT message reception timed out")

   currentTimestamp = getCurrentTime()
   if currentTimestamp >= nextUploadTimestamp:
       df = pd.DataFrame.from_dict(accumulator)
       df.to_parquet(filename)
       s3_export_task_definition = S3ExportTaskDefinition(input_url=filename, bucket=destination_bucket, key=key_name)
       streammanager.append_message(streamname, Util.validate_and_serialize_to_json_bytes(s3_export_task_definition))
       accumulator = {}
       nextUploadTimestamp += period
   else:
        accumulator.append(message)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
