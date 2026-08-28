---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateRumMetricDefinition.html
---

# UpdateRumMetricDefinition
<a name="API_UpdateRumMetricDefinition"></a>

Modifies one existing metric definition for CloudWatch RUM extended metrics. For more information about extended metrics, see [BatchCreateRumMetricsDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.html).

## Request Syntax
<a name="API_UpdateRumMetricDefinition_RequestSyntax"></a>

```
PATCH /rummetrics/{{AppMonitorName}}/metrics HTTP/1.1
Content-type: application/json

{
   "Destination": "{{string}}",
   "DestinationArn": "{{string}}",
   "MetricDefinition": {
      "DimensionKeys": {
         "{{string}}" : "{{string}}"
      },
      "EventPattern": "{{string}}",
      "Name": "{{string}}",
      "Namespace": "{{string}}",
      "UnitLabel": "{{string}}",
      "ValueKey": "{{string}}"
   },
   "MetricDefinitionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRumMetricDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppMonitorName](#API_UpdateRumMetricDefinition_RequestSyntax) **   <a name="cloudwatchrum-UpdateRumMetricDefinition-request-uri-AppMonitorName"></a>
The name of the CloudWatch RUM app monitor that sends these metrics.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateRumMetricDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Destination](#API_UpdateRumMetricDefinition_RequestSyntax) **   <a name="cloudwatchrum-UpdateRumMetricDefinition-request-Destination"></a>
The destination to send the metrics to. Valid values are `CloudWatch` and `Evidently`. If you specify `Evidently`, you must also specify the ARN of the CloudWatchEvidently experiment that will receive the metrics and an IAM role that has permission to write to the experiment.
Type: String
Valid Values: `CloudWatch | Evidently`
Required: Yes

 ** [DestinationArn](#API_UpdateRumMetricDefinition_RequestSyntax) **   <a name="cloudwatchrum-UpdateRumMetricDefinition-request-DestinationArn"></a>
This parameter is required if `Destination` is `Evidently`. If `Destination` is `CloudWatch`, do not use this parameter.
This parameter specifies the ARN of the Evidently experiment that is to receive the metrics. You must have already defined this experiment as a valid destination. For more information, see [PutRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: No

 ** [MetricDefinition](#API_UpdateRumMetricDefinition_RequestSyntax) **   <a name="cloudwatchrum-UpdateRumMetricDefinition-request-MetricDefinition"></a>
A structure that contains the new definition that you want to use for this metric.
Type: [MetricDefinitionRequest](API_MetricDefinitionRequest.md) object
Required: Yes

 ** [MetricDefinitionId](#API_UpdateRumMetricDefinition_RequestSyntax) **   <a name="cloudwatchrum-UpdateRumMetricDefinition-request-MetricDefinitionId"></a>
The ID of the metric definition to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_UpdateRumMetricDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateRumMetricDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRumMetricDefinition_Errors"></a>

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

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 402

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
<a name="API_UpdateRumMetricDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/UpdateRumMetricDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/UpdateRumMetricDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/UpdateRumMetricDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/UpdateRumMetricDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/UpdateRumMetricDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/UpdateRumMetricDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/UpdateRumMetricDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/UpdateRumMetricDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/UpdateRumMetricDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/UpdateRumMetricDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
