---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchGetRumMetricDefinitions.html
---

# BatchGetRumMetricDefinitions
<a name="API_BatchGetRumMetricDefinitions"></a>

Retrieves the list of metrics and dimensions that a RUM app monitor is sending to a single destination.

## Request Syntax
<a name="API_BatchGetRumMetricDefinitions_RequestSyntax"></a>

```
GET /rummetrics/{{AppMonitorName}}/metrics?destination={{Destination}}&destinationArn={{DestinationArn}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BatchGetRumMetricDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppMonitorName](#API_BatchGetRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchGetRumMetricDefinitions-request-uri-AppMonitorName"></a>
The name of the CloudWatch RUM app monitor that is sending the metrics.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

 ** [Destination](#API_BatchGetRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchGetRumMetricDefinitions-request-uri-Destination"></a>
The type of destination that you want to view metrics for. Valid values are `CloudWatch` and `Evidently`.
Valid Values: `CloudWatch | Evidently`
Required: Yes

 ** [DestinationArn](#API_BatchGetRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchGetRumMetricDefinitions-request-uri-DestinationArn"></a>
This parameter is required if `Destination` is `Evidently`. If `Destination` is `CloudWatch`, do not use this parameter.
This parameter specifies the ARN of the Evidently experiment that corresponds to the destination.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

 ** [MaxResults](#API_BatchGetRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchGetRumMetricDefinitions-request-uri-MaxResults"></a>
The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.
To retrieve the remaining results, make another call with the returned `NextToken` value.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_BatchGetRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchGetRumMetricDefinitions-request-uri-NextToken"></a>
Use the token returned by the previous operation to request the next page of results.

## Request Body
<a name="API_BatchGetRumMetricDefinitions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BatchGetRumMetricDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MetricDefinitions": [
      {
         "DimensionKeys": {
            "string" : "string"
         },
         "EventPattern": "string",
         "MetricDefinitionId": "string",
         "Name": "string",
         "Namespace": "string",
         "UnitLabel": "string",
         "ValueKey": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_BatchGetRumMetricDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetricDefinitions](#API_BatchGetRumMetricDefinitions_ResponseSyntax) **   <a name="cloudwatchrum-BatchGetRumMetricDefinitions-response-MetricDefinitions"></a>
An array of structures that display information about the metrics that are sent by the specified app monitor to the specified destination.
Type: Array of [MetricDefinition](API_MetricDefinition.md) objects

 ** [NextToken](#API_BatchGetRumMetricDefinitions_ResponseSyntax) **   <a name="cloudwatchrum-BatchGetRumMetricDefinitions-response-NextToken"></a>
A token that you can use in a subsequent operation to retrieve the next set of results.
Type: String

## Errors
<a name="API_BatchGetRumMetricDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal service exception.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ValidationException **
One of the arguments for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetRumMetricDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/BatchGetRumMetricDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/BatchGetRumMetricDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/BatchGetRumMetricDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/BatchGetRumMetricDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/BatchGetRumMetricDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/BatchGetRumMetricDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/BatchGetRumMetricDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/BatchGetRumMetricDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/BatchGetRumMetricDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/BatchGetRumMetricDefinitions)
