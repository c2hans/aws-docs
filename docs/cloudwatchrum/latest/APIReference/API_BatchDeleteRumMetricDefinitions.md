---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricDefinitions.html
---

# BatchDeleteRumMetricDefinitions
<a name="API_BatchDeleteRumMetricDefinitions"></a>

Removes the specified metrics from being sent to an extended metrics destination.

If some metric definition IDs specified in a `BatchDeleteRumMetricDefinitions` operations are not valid, those metric definitions fail and return errors, but all valid metric definition IDs in the same operation are still deleted.

The maximum number of metric definitions that you can specify in one `BatchDeleteRumMetricDefinitions` operation is 200.

## Request Syntax
<a name="API_BatchDeleteRumMetricDefinitions_RequestSyntax"></a>

```
DELETE /rummetrics/{{AppMonitorName}}/metrics?destination={{Destination}}&destinationArn={{DestinationArn}}&metricDefinitionIds={{MetricDefinitionIds}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BatchDeleteRumMetricDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppMonitorName](#API_BatchDeleteRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchDeleteRumMetricDefinitions-request-uri-AppMonitorName"></a>
The name of the CloudWatch RUM app monitor that is sending these metrics.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

 ** [Destination](#API_BatchDeleteRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchDeleteRumMetricDefinitions-request-uri-Destination"></a>
Defines the destination where you want to stop sending the specified metrics. Valid values are `CloudWatch` and `Evidently`. If you specify `Evidently`, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.
Valid Values: `CloudWatch | Evidently`
Required: Yes

 ** [DestinationArn](#API_BatchDeleteRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchDeleteRumMetricDefinitions-request-uri-DestinationArn"></a>
This parameter is required if `Destination` is `Evidently`. If `Destination` is `CloudWatch`, do not use this parameter.
This parameter specifies the ARN of the Evidently experiment that was receiving the metrics that are being deleted.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

 ** [MetricDefinitionIds](#API_BatchDeleteRumMetricDefinitions_RequestSyntax) **   <a name="cloudwatchrum-BatchDeleteRumMetricDefinitions-request-uri-MetricDefinitionIds"></a>
An array of structures which define the metrics that you want to stop sending.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_BatchDeleteRumMetricDefinitions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BatchDeleteRumMetricDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "MetricDefinitionId": "string"
      }
   ],
   "MetricDefinitionIds": [ "string" ]
}
```

## Response Elements
<a name="API_BatchDeleteRumMetricDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchDeleteRumMetricDefinitions_ResponseSyntax) **   <a name="cloudwatchrum-BatchDeleteRumMetricDefinitions-response-Errors"></a>
An array of error objects, if the operation caused any errors.
Type: Array of [BatchDeleteRumMetricDefinitionsError](API_BatchDeleteRumMetricDefinitionsError.md) objects

 ** [MetricDefinitionIds](#API_BatchDeleteRumMetricDefinitions_ResponseSyntax) **   <a name="cloudwatchrum-BatchDeleteRumMetricDefinitions-response-MetricDefinitionIds"></a>
The IDs of the metric definitions that were deleted.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_BatchDeleteRumMetricDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation attempted to create a resource that already exists.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 409

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

 ** ThrottlingException **
The request was throttled because of quota limits.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
One of the arguments for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteRumMetricDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/BatchDeleteRumMetricDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/BatchDeleteRumMetricDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/BatchDeleteRumMetricDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/BatchDeleteRumMetricDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/BatchDeleteRumMetricDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/BatchDeleteRumMetricDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/BatchDeleteRumMetricDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/BatchDeleteRumMetricDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/BatchDeleteRumMetricDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/BatchDeleteRumMetricDefinitions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
