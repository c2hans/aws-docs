---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-monitoring.html
---

# Monitoring Properties
<a name="clusters-clusterarn-monitoring"></a>

The options for monitoring an Amazon MSK cluster. You can specify which Apache Kafka metrics you want Amazon MSK to gather and send to Amazon CloudWatch. You can also configure open monitoring to gather metrics with Prometheus or Prometheus-compatible tools.

## URI
<a name="clusters-clusterarn-monitoring-url"></a>

`/v1/clusters/{{clusterArn}}/monitoring`

## HTTP methods
<a name="clusters-clusterarn-monitoring-http-methods"></a>

### PUT
<a name="clusters-clusterarn-monitoringput"></a>

**Operation ID:** `UpdateMonitoring`

Updates the monitoring settings for the cluster. You can use this operation to specify which Apache Kafka metrics you want Amazon MSK to send to Amazon CloudWatch. You can also specify settings for open monitoring with Prometheus. The following Python 3.6 example enables open monitoring with the Node Exporter. It also sets enhanced monitoring to `PER_BROKER`. For more information about monitoring, see [Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html).

```
import boto3
import time

client = boto3.client('kafka')

update_monitoring_response = client.update_monitoring(
    ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
    CurrentVersion='K12V3IB1VIZHHY',
    EnhancedMonitoring='PER_BROKER',
    OpenMonitoring={"Prometheus":{"JmxExporter":{"EnabledInBroker":False},"NodeExporter":{"EnabledInBroker":True}}}
)

operation_arn = update_monitoring_response['ClusterOperationArn']
print('The ARN of the update operation is ' + operation_arn)

describe_cluster_operation_response = client.describe_cluster_operation(ClusterOperationArn=operation_arn)

operation_state = describe_cluster_operation_response['ClusterOperationInfo']['OperationState']
print('The status of the update operation is ' + operation_state)

updated = False

while not updated:
    print('Sleeping for 15 seconds before checking to see if the monitoring update is done...')
    time.sleep(15)
    describe_cluster_operation_response = client.describe_cluster_operation(ClusterOperationArn=operation_arn)
    operation_state = describe_cluster_operation_response['ClusterOperationInfo']['OperationState']
    if 'UPDATE_COMPLETE' == operation_state:
        updated = True
        print('You have successfully updated the monitoring settings.')
```

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateMonitoringRequest | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-monitoringoptions"></a>

Enable CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-monitoring-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-monitoring-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-monitoring-request-body-put-example"></a>

```
{
  "enhancedMonitoring": enum,
  "loggingInfo": {
    "brokerLogs": {
      "s3": {
        "bucket": "string",
        "prefix": "string",
        "enabled": boolean
      },
      "firehose": {
        "deliveryStream": "string",
        "enabled": boolean
      },
      "cloudWatchLogs": {
        "logGroup": "string",
        "enabled": boolean
      }
    },
    "authorizerLogs": {
      "s3": {
        "bucket": "string",
        "prefix": "string",
        "enabled": boolean
      },
      "firehose": {
        "deliveryStream": "string",
        "enabled": boolean
      },
      "cloudWatchLogs": {
        "logGroup": "string",
        "enabled": boolean
      }
    }
  },
  "openMonitoring": {
    "prometheus": {
      "nodeExporter": {
        "enabledInBroker": boolean
      },
      "jmxExporter": {
        "enabledInBroker": boolean
      }
    }
  },
  "currentVersion": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-monitoring-response-examples"></a>

#### UpdateMonitoringRequest schema
<a name="clusters-clusterarn-monitoring-response-body-updatemonitoringresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-monitoring-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-monitoring-properties"></a>

### AuthorizerLogs
<a name="clusters-clusterarn-monitoring-model-authorizerlogs"></a>

Authorizer Logs details for cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#clusters-clusterarn-monitoring-model-cloudwatchlogs) | False | CloudWatch Log destination details. |
| firehose | [Firehose](#clusters-clusterarn-monitoring-model-firehose) | False | Firehose Log destination details. |
| s3 | [S3](#clusters-clusterarn-monitoring-model-s3) | False | S3 Log destination details. |

### BrokerLogs
<a name="clusters-clusterarn-monitoring-model-brokerlogs"></a>

The broker logs configuration for this MSK cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#clusters-clusterarn-monitoring-model-cloudwatchlogs) | False | Details of the CloudWatch Logs destination for broker logs. |
| firehose | [Firehose](#clusters-clusterarn-monitoring-model-firehose) | False | Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| s3 | [S3](#clusters-clusterarn-monitoring-model-s3) | False | Details of the Amazon S3 destination for broker logs. |

### CloudWatchLogs
<a name="clusters-clusterarn-monitoring-model-cloudwatchlogs"></a>

Details of the CloudWatch Logs destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified CloudWatch Logs destination. |
| logGroup | string | False | The CloudWatch log group that is the destination for broker logs. |

### EnhancedMonitoring
<a name="clusters-clusterarn-monitoring-model-enhancedmonitoring"></a>

Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster. This property has three possible values: `DEFAULT`, `PER_BROKER`, and `PER_TOPIC_PER_BROKER`. For a list of the metrics associated with each of these three levels of monitoring, see [Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html).
+ `DEFAULT`
+ `PER_BROKER`
+ `PER_TOPIC_PER_BROKER`
+ `PER_TOPIC_PER_PARTITION`

### Error
<a name="clusters-clusterarn-monitoring-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### Firehose
<a name="clusters-clusterarn-monitoring-model-firehose"></a>

Firehose details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | The Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Kinesis Data Firehose delivery stream. |

### JmxExporterInfo
<a name="clusters-clusterarn-monitoring-model-jmxexporterinfo"></a>

JMX Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | JMX Exporter being enabled in broker. |

### LoggingInfo
<a name="clusters-clusterarn-monitoring-model-logginginfo"></a>

You can configure your MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorizerLogs | [AuthorizerLogs](#clusters-clusterarn-monitoring-model-authorizerlogs) | False | Authorizer Logs details. |
| brokerLogs | [BrokerLogs](#clusters-clusterarn-monitoring-model-brokerlogs) | False | You can configure your MSK cluster to send broker logs to different destination types. This configuration specifies the details of these destinations. |

### NodeExporterInfo
<a name="clusters-clusterarn-monitoring-model-nodeexporterinfo"></a>

Node Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | Node Exporter being enabled in broker. |

### OpenMonitoringInfo
<a name="clusters-clusterarn-monitoring-model-openmonitoringinfo"></a>

JMX and Node monitoring for cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| prometheus | [PrometheusInfo](#clusters-clusterarn-monitoring-model-prometheusinfo) | True | Prometheus details. |

### PrometheusInfo
<a name="clusters-clusterarn-monitoring-model-prometheusinfo"></a>

Prometheus details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jmxExporter | [JmxExporterInfo](#clusters-clusterarn-monitoring-model-jmxexporterinfo) | False | JMX Exporter details. |
| nodeExporter | [NodeExporterInfo](#clusters-clusterarn-monitoring-model-nodeexporterinfo) | False | Node Exporter details. |

### S3
<a name="clusters-clusterarn-monitoring-model-s3"></a>

The details of the Amazon S3 destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | The name of the S3 bucket that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Amazon S3 destination. |
| prefix | string | False | The S3 prefix that is the destination for broker logs. |

### UpdateMonitoringRequest
<a name="clusters-clusterarn-monitoring-model-updatemonitoringrequest"></a>

Request body for UpdateMonitoring.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | string | True | The version of the MSK cluster to update. Cluster versions aren't simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.  |
| enhancedMonitoring | [EnhancedMonitoring](#clusters-clusterarn-monitoring-model-enhancedmonitoring) | False | Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster. |
| loggingInfo | [LoggingInfo](#clusters-clusterarn-monitoring-model-logginginfo) | False | LoggingInfo details. |
| openMonitoring | [OpenMonitoringInfo](#clusters-clusterarn-monitoring-model-openmonitoringinfo) | False | The settings for open monitoring. |

### UpdateMonitoringResponse
<a name="clusters-clusterarn-monitoring-model-updatemonitoringresponse"></a>

Request body for UpdateMonitoring.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

## See also
<a name="clusters-clusterarn-monitoring-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateMonitoring
<a name="UpdateMonitoring-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateMonitoring)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateMonitoring)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateMonitoring)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateMonitoring)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateMonitoring)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateMonitoring)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateMonitoring)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateMonitoring)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/UpdateMonitoring)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateMonitoring)
