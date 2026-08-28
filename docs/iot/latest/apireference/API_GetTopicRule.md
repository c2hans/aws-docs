---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetTopicRule.html
---

# GetTopicRule
<a name="API_GetTopicRule"></a>

Gets information about the rule.

Requires permission to access the [GetTopicRule](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetTopicRule_RequestSyntax"></a>

```
GET /rules/{{ruleName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTopicRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ruleName](#API_GetTopicRule_RequestSyntax) **   <a name="iot-GetTopicRule-request-uri-ruleName"></a>
The name of the rule.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_]+$`
Required: Yes

## Request Body
<a name="API_GetTopicRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTopicRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "rule": {
      "actions": [
         {
            "cloudwatchAlarm": {
               "alarmName": "string",
               "roleArn": "string",
               "stateReason": "string",
               "stateValue": "string"
            },
            "cloudwatchLogs": {
               "batchMode": boolean,
               "logGroupName": "string",
               "roleArn": "string"
            },
            "cloudwatchMetric": {
               "metricName": "string",
               "metricNamespace": "string",
               "metricTimestamp": "string",
               "metricUnit": "string",
               "metricValue": "string",
               "roleArn": "string"
            },
            "dynamoDB": {
               "hashKeyField": "string",
               "hashKeyType": "string",
               "hashKeyValue": "string",
               "operation": "string",
               "payloadField": "string",
               "rangeKeyField": "string",
               "rangeKeyType": "string",
               "rangeKeyValue": "string",
               "roleArn": "string",
               "tableName": "string"
            },
            "dynamoDBv2": {
               "putItem": {
                  "tableName": "string"
               },
               "roleArn": "string"
            },
            "elasticsearch": {
               "endpoint": "string",
               "id": "string",
               "index": "string",
               "roleArn": "string",
               "type": "string"
            },
            "firehose": {
               "batchMode": boolean,
               "deliveryStreamName": "string",
               "roleArn": "string",
               "separator": "string"
            },
            "http": {
               "auth": {
                  "sigv4": {
                     "roleArn": "string",
                     "serviceName": "string",
                     "signingRegion": "string"
                  }
               },
               "batchConfig": {
                  "batchAcrossTopics": boolean,
                  "maxBatchOpenMs": number,
                  "maxBatchSize": number,
                  "maxBatchSizeBytes": number
               },
               "confirmationUrl": "string",
               "enableBatching": boolean,
               "headers": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ],
               "url": "string"
            },
            "iotAnalytics": {
               "batchMode": boolean,
               "channelArn": "string",
               "channelName": "string",
               "roleArn": "string"
            },
            "iotEvents": {
               "batchMode": boolean,
               "inputName": "string",
               "messageId": "string",
               "roleArn": "string"
            },
            "iotSiteWise": {
               "putAssetPropertyValueEntries": [
                  {
                     "assetId": "string",
                     "entryId": "string",
                     "propertyAlias": "string",
                     "propertyId": "string",
                     "propertyValues": [
                        {
                           "quality": "string",
                           "timestamp": {
                              "offsetInNanos": "string",
                              "timeInSeconds": "string"
                           },
                           "value": {
                              "booleanValue": "string",
                              "doubleValue": "string",
                              "integerValue": "string",
                              "stringValue": "string"
                           }
                        }
                     ]
                  }
               ],
               "roleArn": "string"
            },
            "kafka": {
               "clientProperties": {
                  "string" : "string"
               },
               "destinationArn": "string",
               "headers": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ],
               "key": "string",
               "partition": "string",
               "topic": "string"
            },
            "kinesis": {
               "partitionKey": "string",
               "roleArn": "string",
               "streamName": "string"
            },
            "lambda": {
               "functionArn": "string"
            },
            "location": {
               "deviceId": "string",
               "latitude": "string",
               "longitude": "string",
               "roleArn": "string",
               "timestamp": {
                  "unit": "string",
                  "value": "string"
               },
               "trackerName": "string"
            },
            "openSearch": {
               "endpoint": "string",
               "id": "string",
               "index": "string",
               "roleArn": "string",
               "type": "string"
            },
            "republish": {
               "headers": {
                  "contentType": "string",
                  "correlationData": "string",
                  "messageExpiry": "string",
                  "payloadFormatIndicator": "string",
                  "responseTopic": "string",
                  "userProperties": [
                     {
                        "key": "string",
                        "value": "string"
                     }
                  ]
               },
               "qos": number,
               "roleArn": "string",
               "topic": "string"
            },
            "s3": {
               "bucketName": "string",
               "cannedAcl": "string",
               "key": "string",
               "roleArn": "string"
            },
            "salesforce": {
               "token": "string",
               "url": "string"
            },
            "sns": {
               "messageFormat": "string",
               "roleArn": "string",
               "targetArn": "string"
            },
            "sqs": {
               "queueUrl": "string",
               "roleArn": "string",
               "useBase64": boolean
            },
            "stepFunctions": {
               "executionNamePrefix": "string",
               "roleArn": "string",
               "stateMachineName": "string"
            },
            "timestream": {
               "databaseName": "string",
               "dimensions": [
                  {
                     "name": "string",
                     "value": "string"
                  }
               ],
               "roleArn": "string",
               "tableName": "string",
               "timestamp": {
                  "unit": "string",
                  "value": "string"
               }
            }
         }
      ],
      "awsIotSqlVersion": "string",
      "createdAt": number,
      "description": "string",
      "errorAction": {
         "cloudwatchAlarm": {
            "alarmName": "string",
            "roleArn": "string",
            "stateReason": "string",
            "stateValue": "string"
         },
         "cloudwatchLogs": {
            "batchMode": boolean,
            "logGroupName": "string",
            "roleArn": "string"
         },
         "cloudwatchMetric": {
            "metricName": "string",
            "metricNamespace": "string",
            "metricTimestamp": "string",
            "metricUnit": "string",
            "metricValue": "string",
            "roleArn": "string"
         },
         "dynamoDB": {
            "hashKeyField": "string",
            "hashKeyType": "string",
            "hashKeyValue": "string",
            "operation": "string",
            "payloadField": "string",
            "rangeKeyField": "string",
            "rangeKeyType": "string",
            "rangeKeyValue": "string",
            "roleArn": "string",
            "tableName": "string"
         },
         "dynamoDBv2": {
            "putItem": {
               "tableName": "string"
            },
            "roleArn": "string"
         },
         "elasticsearch": {
            "endpoint": "string",
            "id": "string",
            "index": "string",
            "roleArn": "string",
            "type": "string"
         },
         "firehose": {
            "batchMode": boolean,
            "deliveryStreamName": "string",
            "roleArn": "string",
            "separator": "string"
         },
         "http": {
            "auth": {
               "sigv4": {
                  "roleArn": "string",
                  "serviceName": "string",
                  "signingRegion": "string"
               }
            },
            "batchConfig": {
               "batchAcrossTopics": boolean,
               "maxBatchOpenMs": number,
               "maxBatchSize": number,
               "maxBatchSizeBytes": number
            },
            "confirmationUrl": "string",
            "enableBatching": boolean,
            "headers": [
               {
                  "key": "string",
                  "value": "string"
               }
            ],
            "url": "string"
         },
         "iotAnalytics": {
            "batchMode": boolean,
            "channelArn": "string",
            "channelName": "string",
            "roleArn": "string"
         },
         "iotEvents": {
            "batchMode": boolean,
            "inputName": "string",
            "messageId": "string",
            "roleArn": "string"
         },
         "iotSiteWise": {
            "putAssetPropertyValueEntries": [
               {
                  "assetId": "string",
                  "entryId": "string",
                  "propertyAlias": "string",
                  "propertyId": "string",
                  "propertyValues": [
                     {
                        "quality": "string",
                        "timestamp": {
                           "offsetInNanos": "string",
                           "timeInSeconds": "string"
                        },
                        "value": {
                           "booleanValue": "string",
                           "doubleValue": "string",
                           "integerValue": "string",
                           "stringValue": "string"
                        }
                     }
                  ]
               }
            ],
            "roleArn": "string"
         },
         "kafka": {
            "clientProperties": {
               "string" : "string"
            },
            "destinationArn": "string",
            "headers": [
               {
                  "key": "string",
                  "value": "string"
               }
            ],
            "key": "string",
            "partition": "string",
            "topic": "string"
         },
         "kinesis": {
            "partitionKey": "string",
            "roleArn": "string",
            "streamName": "string"
         },
         "lambda": {
            "functionArn": "string"
         },
         "location": {
            "deviceId": "string",
            "latitude": "string",
            "longitude": "string",
            "roleArn": "string",
            "timestamp": {
               "unit": "string",
               "value": "string"
            },
            "trackerName": "string"
         },
         "openSearch": {
            "endpoint": "string",
            "id": "string",
            "index": "string",
            "roleArn": "string",
            "type": "string"
         },
         "republish": {
            "headers": {
               "contentType": "string",
               "correlationData": "string",
               "messageExpiry": "string",
               "payloadFormatIndicator": "string",
               "responseTopic": "string",
               "userProperties": [
                  {
                     "key": "string",
                     "value": "string"
                  }
               ]
            },
            "qos": number,
            "roleArn": "string",
            "topic": "string"
         },
         "s3": {
            "bucketName": "string",
            "cannedAcl": "string",
            "key": "string",
            "roleArn": "string"
         },
         "salesforce": {
            "token": "string",
            "url": "string"
         },
         "sns": {
            "messageFormat": "string",
            "roleArn": "string",
            "targetArn": "string"
         },
         "sqs": {
            "queueUrl": "string",
            "roleArn": "string",
            "useBase64": boolean
         },
         "stepFunctions": {
            "executionNamePrefix": "string",
            "roleArn": "string",
            "stateMachineName": "string"
         },
         "timestream": {
            "databaseName": "string",
            "dimensions": [
               {
                  "name": "string",
                  "value": "string"
               }
            ],
            "roleArn": "string",
            "tableName": "string",
            "timestamp": {
               "unit": "string",
               "value": "string"
            }
         }
      },
      "ruleDisabled": boolean,
      "ruleName": "string",
      "sql": "string"
   },
   "ruleArn": "string"
}
```

## Response Elements
<a name="API_GetTopicRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [rule](#API_GetTopicRule_ResponseSyntax) **   <a name="iot-GetTopicRule-response-rule"></a>
The rule.
Type: [TopicRule](API_TopicRule.md) object

 ** [ruleArn](#API_GetTopicRule_ResponseSyntax) **   <a name="iot-GetTopicRule-response-ruleArn"></a>
The rule ARN.
Type: String

## Errors
<a name="API_GetTopicRule_Errors"></a>

 ** InternalException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_GetTopicRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetTopicRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetTopicRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetTopicRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetTopicRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetTopicRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetTopicRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetTopicRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetTopicRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetTopicRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetTopicRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
