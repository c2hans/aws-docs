---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TestTransformer.html
---

# TestTransformer
<a name="API_TestTransformer"></a>

Use this operation to test a log transformer. You enter the transformer configuration and a set of log events to test with. The operation responds with an array that includes the original log events and the transformed versions.

## Request Syntax
<a name="API_TestTransformer_RequestSyntax"></a>

```
{
   "logEventMessages": [ "{{string}}" ],
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
<a name="API_TestTransformer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [logEventMessages](#API_TestTransformer_RequestSyntax) **   <a name="CWL-TestTransformer-request-logEventMessages"></a>
An array of the raw log events that you want to use to test this transformer.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [transformerConfig](#API_TestTransformer_RequestSyntax) **   <a name="CWL-TestTransformer-request-transformerConfig"></a>
This structure contains the configuration of this log transformer that you want to test. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.
Type: Array of [Processor](API_Processor.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_TestTransformer_ResponseSyntax"></a>

```
{
   "transformedLogs": [
      {
         "eventMessage": "string",
         "eventNumber": number,
         "transformedEventMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_TestTransformer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [transformedLogs](#API_TestTransformer_ResponseSyntax) **   <a name="CWL-TestTransformer-response-transformedLogs"></a>
An array where each member of the array includes both the original version and the transformed version of one of the log events that you input.
Type: Array of [TransformedLogRecord](API_TransformedLogRecord.md) objects

## Errors
<a name="API_TestTransformer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidOperationException **
The operation is not valid on the specified resource.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## See Also
<a name="API_TestTransformer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/TestTransformer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/TestTransformer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/TestTransformer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/TestTransformer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/TestTransformer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/TestTransformer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/TestTransformer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/TestTransformer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/TestTransformer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/TestTransformer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
