---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html
---

# PutTransformer
<a name="API_PutTransformer"></a>

Creates or updates a *log transformer* for a single log group. You use log transformers to transform log events into a different format, making them easier for you to process and analyze. You can also transform logs from different sources into standardized formats that contains relevant, source-specific information.

After you have created a transformer, CloudWatch Logs performs the transformations at the time of log ingestion. You can then refer to the transformed versions of the logs during operations such as querying with CloudWatch Logs Insights or creating metric filters or subscription filers.

You can also use a transformer to copy metadata from metadata keys into the log events themselves. This metadata can include log group name, log stream name, account ID and Region.

A transformer for a log group is a series of processors, where each processor applies one type of transformation to the log events ingested into this log group. The processors work one after another, in the order that you list them, like a pipeline. For more information about the available processors to use in a transformer, see [ Processors that you can use](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors).

Having log events in standardized format enables visibility across your applications for your log analysis, reporting, and alarming needs. CloudWatch Logs provides transformation for common log types with out-of-the-box transformation templates for major AWS log sources such as VPC flow logs, Lambda, and Amazon RDS. You can use pre-built transformation templates or create custom transformation policies.

You can create transformers only for the log groups in the Standard log class.

You can also set up a transformer at the account level. For more information, see [PutAccountPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html). If there is both a log-group level transformer created with `PutTransformer` and an account-level transformer that could apply to the same log group, the log group uses only the log-group level transformer. It ignores the account-level transformer.

## Request Syntax
<a name="API_PutTransformer_RequestSyntax"></a>

```
{
   "logGroupIdentifier": "{{string}}",
   "transformerConfig": [
      {
         "addKeys": {
            "entries": [
               {
                  "key": "{{string}}",
                  "overwriteIfExists": {{boolean}},
                  "value": "{{string}}"
               }
            ]
         },
         "copyValue": {
            "entries": [
               {
                  "overwriteIfExists": {{boolean}},
                  "source": "{{string}}",
                  "target": "{{string}}"
               }
            ]
         },
         "csv": {
            "columns": [ "{{string}}" ],
            "delimiter": "{{string}}",
            "destination": "{{string}}",
            "quoteCharacter": "{{string}}",
            "source": "{{string}}"
         },
         "dateTimeConverter": {
            "locale": "{{string}}",
            "matchPatterns": [ "{{string}}" ],
            "source": "{{string}}",
            "sourceTimezone": "{{string}}",
            "target": "{{string}}",
            "targetFormat": "{{string}}",
            "targetTimezone": "{{string}}"
         },
         "deleteKeys": {
            "withKeys": [ "{{string}}" ]
         },
         "grok": {
            "match": "{{string}}",
            "source": "{{string}}"
         },
         "listToMap": {
            "flatten": {{boolean}},
            "flattenedElement": "{{string}}",
            "key": "{{string}}",
            "source": "{{string}}",
            "target": "{{string}}",
            "valueKey": "{{string}}"
         },
         "lowerCaseString": {
            "withKeys": [ "{{string}}" ]
         },
         "moveKeys": {
            "entries": [
               {
                  "overwriteIfExists": {{boolean}},
                  "source": "{{string}}",
                  "target": "{{string}}"
               }
            ]
         },
         "parseCloudfront": {
            "source": "{{string}}"
         },
         "parseJSON": {
            "destination": "{{string}}",
            "source": "{{string}}"
         },
         "parseKeyValue": {
            "destination": "{{string}}",
            "fieldDelimiter": "{{string}}",
            "keyPrefix": "{{string}}",
            "keyValueDelimiter": "{{string}}",
            "nonMatchValue": "{{string}}",
            "overwriteIfExists": {{boolean}},
            "source": "{{string}}"
         },
         "parsePostgres": {
            "source": "{{string}}"
         },
         "parseRoute53": {
            "source": "{{string}}"
         },
         "parseToOCSF": {
            "eventSource": "{{string}}",
            "mappingVersion": "{{string}}",
            "ocsfVersion": "{{string}}",
            "source": "{{string}}"
         },
         "parseVPC": {
            "source": "{{string}}"
         },
         "parseWAF": {
            "source": "{{string}}"
         },
         "renameKeys": {
            "entries": [
               {
                  "key": "{{string}}",
                  "overwriteIfExists": {{boolean}},
                  "renameTo": "{{string}}"
               }
            ]
         },
         "splitString": {
            "entries": [
               {
                  "delimiter": "{{string}}",
                  "source": "{{string}}"
               }
            ]
         },
         "substituteString": {
            "entries": [
               {
                  "from": "{{string}}",
                  "source": "{{string}}",
                  "to": "{{string}}"
               }
            ]
         },
         "trimString": {
            "withKeys": [ "{{string}}" ]
         },
         "typeConverter": {
            "entries": [
               {
                  "key": "{{string}}",
                  "type": "{{string}}"
               }
            ]
         },
         "upperCaseString": {
            "withKeys": [ "{{string}}" ]
         }
      }
   ]
}
```

## Request Parameters
<a name="API_PutTransformer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [logGroupIdentifier](#API_PutTransformer_RequestSyntax) **   <a name="CWL-PutTransformer-request-logGroupIdentifier"></a>
Specify either the name or ARN of the log group to create the transformer for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: Yes

 ** [transformerConfig](#API_PutTransformer_RequestSyntax) **   <a name="CWL-PutTransformer-request-transformerConfig"></a>
This structure contains the configuration of this log transformer. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.
Type: Array of [Processor](API_Processor.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Elements
<a name="API_PutTransformer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutTransformer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidOperationException **
The operation is not valid on the specified resource.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_PutTransformer_Examples"></a>

### To create a log transformer
<a name="API_PutTransformer_Example_1"></a>

The following example creates a log transformer for the specified log group.

#### Sample Request
<a name="API_PutTransformer_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.PutTransformer
{
    "logGroupIdentifier": "my-log-group-name",
    "transformerConfig": [
        {
            "parseJSON": {}
        },
        {
            "addKeys": {
                "entries": [
                    {
                        "key": "metadata.transformed_in",
                        "value": "CloudWatchLogs"
                    }
                ]
            }
        },
        {
            "trimString": {
                "withKeys": [
                    "status"
                ]
            }
        },
        {
            "lowerCaseString": {
                "withKeys": [
                    "status"
                ]
            }
        }
    ]
}
```

## See Also
<a name="API_PutTransformer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutTransformer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutTransformer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutTransformer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutTransformer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutTransformer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutTransformer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutTransformer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutTransformer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutTransformer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutTransformer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
