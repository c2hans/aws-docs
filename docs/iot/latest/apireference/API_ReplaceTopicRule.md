---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ReplaceTopicRule.html
---

# ReplaceTopicRule
<a name="API_ReplaceTopicRule"></a>

Replaces the rule. You must specify all parameters for the new rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.

Requires permission to access the [ReplaceTopicRule](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ReplaceTopicRule_RequestSyntax"></a>

```
PATCH /rules/{{ruleName}} HTTP/1.1
Content-type: application/json

{
   "actions": [
      {
         "cloudwatchAlarm": {
            "alarmName": "{{string}}",
            "roleArn": "{{string}}",
            "stateReason": "{{string}}",
            "stateValue": "{{string}}"
         },
         "cloudwatchLogs": {
            "batchMode": {{boolean}},
            "logGroupName": "{{string}}",
            "roleArn": "{{string}}"
         },
         "cloudwatchMetric": {
            "metricName": "{{string}}",
            "metricNamespace": "{{string}}",
            "metricTimestamp": "{{string}}",
            "metricUnit": "{{string}}",
            "metricValue": "{{string}}",
            "roleArn": "{{string}}"
         },
         "dynamoDB": {
            "hashKeyField": "{{string}}",
            "hashKeyType": "{{string}}",
            "hashKeyValue": "{{string}}",
            "operation": "{{string}}",
            "payloadField": "{{string}}",
            "rangeKeyField": "{{string}}",
            "rangeKeyType": "{{string}}",
            "rangeKeyValue": "{{string}}",
            "roleArn": "{{string}}",
            "tableName": "{{string}}"
         },
         "dynamoDBv2": {
            "putItem": {
               "tableName": "{{string}}"
            },
            "roleArn": "{{string}}"
         },
         "elasticsearch": {
            "endpoint": "{{string}}",
            "id": "{{string}}",
            "index": "{{string}}",
            "roleArn": "{{string}}",
            "type": "{{string}}"
         },
         "firehose": {
            "batchMode": {{boolean}},
            "deliveryStreamName": "{{string}}",
            "roleArn": "{{string}}",
            "separator": "{{string}}"
         },
         "http": {
            "auth": {
               "sigv4": {
                  "roleArn": "{{string}}",
                  "serviceName": "{{string}}",
                  "signingRegion": "{{string}}"
               }
            },
            "batchConfig": {
               "batchAcrossTopics": {{boolean}},
               "maxBatchOpenMs": {{number}},
               "maxBatchSize": {{number}},
               "maxBatchSizeBytes": {{number}}
            },
            "confirmationUrl": "{{string}}",
            "enableBatching": {{boolean}},
            "headers": [
               {
                  "key": "{{string}}",
                  "value": "{{string}}"
               }
            ],
            "url": "{{string}}"
         },
         "iotAnalytics": {
            "batchMode": {{boolean}},
            "channelArn": "{{string}}",
            "channelName": "{{string}}",
            "roleArn": "{{string}}"
         },
         "iotEvents": {
            "batchMode": {{boolean}},
            "inputName": "{{string}}",
            "messageId": "{{string}}",
            "roleArn": "{{string}}"
         },
         "iotSiteWise": {
            "putAssetPropertyValueEntries": [
               {
                  "assetId": "{{string}}",
                  "entryId": "{{string}}",
                  "propertyAlias": "{{string}}",
                  "propertyId": "{{string}}",
                  "propertyValues": [
                     {
                        "quality": "{{string}}",
                        "timestamp": {
                           "offsetInNanos": "{{string}}",
                           "timeInSeconds": "{{string}}"
                        },
                        "value": {
                           "booleanValue": "{{string}}",
                           "doubleValue": "{{string}}",
                           "integerValue": "{{string}}",
                           "stringValue": "{{string}}"
                        }
                     }
                  ]
               }
            ],
            "roleArn": "{{string}}"
         },
         "kafka": {
            "clientProperties": {
               "{{string}}" : "{{string}}"
            },
            "destinationArn": "{{string}}",
            "headers": [
               {
                  "key": "{{string}}",
                  "value": "{{string}}"
               }
            ],
            "key": "{{string}}",
            "partition": "{{string}}",
            "topic": "{{string}}"
         },
         "kinesis": {
            "partitionKey": "{{string}}",
            "roleArn": "{{string}}",
            "streamName": "{{string}}"
         },
         "lambda": {
            "functionArn": "{{string}}"
         },
         "location": {
            "deviceId": "{{string}}",
            "latitude": "{{string}}",
            "longitude": "{{string}}",
            "roleArn": "{{string}}",
            "timestamp": {
               "unit": "{{string}}",
               "value": "{{string}}"
            },
            "trackerName": "{{string}}"
         },
         "openSearch": {
            "endpoint": "{{string}}",
            "id": "{{string}}",
            "index": "{{string}}",
            "roleArn": "{{string}}",
            "type": "{{string}}"
         },
         "republish": {
            "headers": {
               "contentType": "{{string}}",
               "correlationData": "{{string}}",
               "messageExpiry": "{{string}}",
               "payloadFormatIndicator": "{{string}}",
               "responseTopic": "{{string}}",
               "userProperties": [
                  {
                     "key": "{{string}}",
                     "value": "{{string}}"
                  }
               ]
            },
            "qos": {{number}},
            "roleArn": "{{string}}",
            "topic": "{{string}}"
         },
         "s3": {
            "bucketName": "{{string}}",
            "cannedAcl": "{{string}}",
            "key": "{{string}}",
            "roleArn": "{{string}}"
         },
         "salesforce": {
            "token": "{{string}}",
            "url": "{{string}}"
         },
         "sns": {
            "messageFormat": "{{string}}",
            "roleArn": "{{string}}",
            "targetArn": "{{string}}"
         },
         "sqs": {
            "queueUrl": "{{string}}",
            "roleArn": "{{string}}",
            "useBase64": {{boolean}}
         },
         "stepFunctions": {
            "executionNamePrefix": "{{string}}",
            "roleArn": "{{string}}",
            "stateMachineName": "{{string}}"
         },
         "timestream": {
            "databaseName": "{{string}}",
            "dimensions": [
               {
                  "name": "{{string}}",
                  "value": "{{string}}"
               }
            ],
            "roleArn": "{{string}}",
            "tableName": "{{string}}",
            "timestamp": {
               "unit": "{{string}}",
               "value": "{{string}}"
            }
         }
      }
   ],
   "awsIotSqlVersion": "{{string}}",
   "description": "{{string}}",
   "errorAction": {
      "cloudwatchAlarm": {
         "alarmName": "{{string}}",
         "roleArn": "{{string}}",
         "stateReason": "{{string}}",
         "stateValue": "{{string}}"
      },
      "cloudwatchLogs": {
         "batchMode": {{boolean}},
         "logGroupName": "{{string}}",
         "roleArn": "{{string}}"
      },
      "cloudwatchMetric": {
         "metricName": "{{string}}",
         "metricNamespace": "{{string}}",
         "metricTimestamp": "{{string}}",
         "metricUnit": "{{string}}",
         "metricValue": "{{string}}",
         "roleArn": "{{string}}"
      },
      "dynamoDB": {
         "hashKeyField": "{{string}}",
         "hashKeyType": "{{string}}",
         "hashKeyValue": "{{string}}",
         "operation": "{{string}}",
         "payloadField": "{{string}}",
         "rangeKeyField": "{{string}}",
         "rangeKeyType": "{{string}}",
         "rangeKeyValue": "{{string}}",
         "roleArn": "{{string}}",
         "tableName": "{{string}}"
      },
      "dynamoDBv2": {
         "putItem": {
            "tableName": "{{string}}"
         },
         "roleArn": "{{string}}"
      },
      "elasticsearch": {
         "endpoint": "{{string}}",
         "id": "{{string}}",
         "index": "{{string}}",
         "roleArn": "{{string}}",
         "type": "{{string}}"
      },
      "firehose": {
         "batchMode": {{boolean}},
         "deliveryStreamName": "{{string}}",
         "roleArn": "{{string}}",
         "separator": "{{string}}"
      },
      "http": {
         "auth": {
            "sigv4": {
               "roleArn": "{{string}}",
               "serviceName": "{{string}}",
               "signingRegion": "{{string}}"
            }
         },
         "batchConfig": {
            "batchAcrossTopics": {{boolean}},
            "maxBatchOpenMs": {{number}},
            "maxBatchSize": {{number}},
            "maxBatchSizeBytes": {{number}}
         },
         "confirmationUrl": "{{string}}",
         "enableBatching": {{boolean}},
         "headers": [
            {
               "key": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "url": "{{string}}"
      },
      "iotAnalytics": {
         "batchMode": {{boolean}},
         "channelArn": "{{string}}",
         "channelName": "{{string}}",
         "roleArn": "{{string}}"
      },
      "iotEvents": {
         "batchMode": {{boolean}},
         "inputName": "{{string}}",
         "messageId": "{{string}}",
         "roleArn": "{{string}}"
      },
      "iotSiteWise": {
         "putAssetPropertyValueEntries": [
            {
               "assetId": "{{string}}",
               "entryId": "{{string}}",
               "propertyAlias": "{{string}}",
               "propertyId": "{{string}}",
               "propertyValues": [
                  {
                     "quality": "{{string}}",
                     "timestamp": {
                        "offsetInNanos": "{{string}}",
                        "timeInSeconds": "{{string}}"
                     },
                     "value": {
                        "booleanValue": "{{string}}",
                        "doubleValue": "{{string}}",
                        "integerValue": "{{string}}",
                        "stringValue": "{{string}}"
                     }
                  }
               ]
            }
         ],
         "roleArn": "{{string}}"
      },
      "kafka": {
         "clientProperties": {
            "{{string}}" : "{{string}}"
         },
         "destinationArn": "{{string}}",
         "headers": [
            {
               "key": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "key": "{{string}}",
         "partition": "{{string}}",
         "topic": "{{string}}"
      },
      "kinesis": {
         "partitionKey": "{{string}}",
         "roleArn": "{{string}}",
         "streamName": "{{string}}"
      },
      "lambda": {
         "functionArn": "{{string}}"
      },
      "location": {
         "deviceId": "{{string}}",
         "latitude": "{{string}}",
         "longitude": "{{string}}",
         "roleArn": "{{string}}",
         "timestamp": {
            "unit": "{{string}}",
            "value": "{{string}}"
         },
         "trackerName": "{{string}}"
      },
      "openSearch": {
         "endpoint": "{{string}}",
         "id": "{{string}}",
         "index": "{{string}}",
         "roleArn": "{{string}}",
         "type": "{{string}}"
      },
      "republish": {
         "headers": {
            "contentType": "{{string}}",
            "correlationData": "{{string}}",
            "messageExpiry": "{{string}}",
            "payloadFormatIndicator": "{{string}}",
            "responseTopic": "{{string}}",
            "userProperties": [
               {
                  "key": "{{string}}",
                  "value": "{{string}}"
               }
            ]
         },
         "qos": {{number}},
         "roleArn": "{{string}}",
         "topic": "{{string}}"
      },
      "s3": {
         "bucketName": "{{string}}",
         "cannedAcl": "{{string}}",
         "key": "{{string}}",
         "roleArn": "{{string}}"
      },
      "salesforce": {
         "token": "{{string}}",
         "url": "{{string}}"
      },
      "sns": {
         "messageFormat": "{{string}}",
         "roleArn": "{{string}}",
         "targetArn": "{{string}}"
      },
      "sqs": {
         "queueUrl": "{{string}}",
         "roleArn": "{{string}}",
         "useBase64": {{boolean}}
      },
      "stepFunctions": {
         "executionNamePrefix": "{{string}}",
         "roleArn": "{{string}}",
         "stateMachineName": "{{string}}"
      },
      "timestream": {
         "databaseName": "{{string}}",
         "dimensions": [
            {
               "name": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "roleArn": "{{string}}",
         "tableName": "{{string}}",
         "timestamp": {
            "unit": "{{string}}",
            "value": "{{string}}"
         }
      }
   },
   "ruleDisabled": {{boolean}},
   "sql": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ReplaceTopicRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ruleName](#API_ReplaceTopicRule_RequestSyntax) **   <a name="iot-ReplaceTopicRule-request-uri-ruleName"></a>
The name of the rule.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_]+$`
Required: Yes

## Request Body
<a name="API_ReplaceTopicRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_ReplaceTopicRule_RequestSyntax) **   <a name="iot-ReplaceTopicRule-request-actions"></a>
The actions associated with the rule.
Type: Array of [Action](API_Action.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** [awsIotSqlVersion](#API_ReplaceTopicRule_RequestSyntax) **   <a name="iot-ReplaceTopicRule-request-awsIotSqlVersion"></a>
The version of the SQL rules engine to use when evaluating the rule.
Type: String
Required: No

 ** [description](#API_ReplaceTopicRule_RequestSyntax) **   <a name="iot-ReplaceTopicRule-request-description"></a>
The description of the rule.
Type: String
Required: No

 ** [errorAction](#API_ReplaceTopicRule_RequestSyntax) **   <a name="iot-ReplaceTopicRule-request-errorAction"></a>
The action to take when an error occurs.
Type: [Action](API_Action.md) object
Required: No

 ** [ruleDisabled](#API_ReplaceTopicRule_RequestSyntax) **   <a name="iot-ReplaceTopicRule-request-ruleDisabled"></a>
Specifies whether the rule is disabled.
Type: Boolean
Required: No

 ** [sql](#API_ReplaceTopicRule_RequestSyntax) **   <a name="iot-ReplaceTopicRule-request-sql"></a>
The SQL statement used to query the topic. For more information, see [AWS IoT SQL Reference](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html) in the * AWS IoT Developer Guide*.
Type: String
Required: Yes

## Response Syntax
<a name="API_ReplaceTopicRule_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ReplaceTopicRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ReplaceTopicRule_Errors"></a>

 ** ConflictingResourceUpdateException **
A conflicting resource update exception. This exception is thrown when two pending updates cause a conflict.
 ** message **
The message for the exception.
HTTP Status Code: 409

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

 ** SqlParseException **
The Rule-SQL expression can't be parsed correctly.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_ReplaceTopicRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ReplaceTopicRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ReplaceTopicRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ReplaceTopicRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ReplaceTopicRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ReplaceTopicRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ReplaceTopicRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ReplaceTopicRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ReplaceTopicRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ReplaceTopicRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ReplaceTopicRule)
