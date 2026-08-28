---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html
---

# PutRumMetricsDestination
<a name="API_PutRumMetricsDestination"></a>

Creates or updates a destination to receive extended metrics from CloudWatch RUM. You can send extended metrics to CloudWatch or to a CloudWatch Evidently experiment.

For more information about extended metrics, see [BatchCreateRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.html).

## Request Syntax
<a name="API_PutRumMetricsDestination_RequestSyntax"></a>

```
POST /rummetrics/{{AppMonitorName}}/metricsdestination HTTP/1.1
Content-type: application/json

{
   "Destination": "{{string}}",
   "DestinationArn": "{{string}}",
   "IamRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutRumMetricsDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppMonitorName](#API_PutRumMetricsDestination_RequestSyntax) **   <a name="cloudwatchrum-PutRumMetricsDestination-request-uri-AppMonitorName"></a>
The name of the CloudWatch RUM app monitor that will send the metrics.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_PutRumMetricsDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Destination](#API_PutRumMetricsDestination_RequestSyntax) **   <a name="cloudwatchrum-PutRumMetricsDestination-request-Destination"></a>
Defines the destination to send the metrics to. Valid values are `CloudWatch` and `Evidently`. If you specify `Evidently`, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.
Type: String
Valid Values: `CloudWatch | Evidently`
Required: Yes

 ** [DestinationArn](#API_PutRumMetricsDestination_RequestSyntax) **   <a name="cloudwatchrum-PutRumMetricsDestination-request-DestinationArn"></a>
Use this parameter only if `Destination` is `Evidently`. This parameter specifies the ARN of the Evidently experiment that will receive the extended metrics.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: No

 ** [IamRoleArn](#API_PutRumMetricsDestination_RequestSyntax) **   <a name="cloudwatchrum-PutRumMetricsDestination-request-IamRoleArn"></a>
This parameter is required if `Destination` is `Evidently`. If `Destination` is `CloudWatch`, don't use this parameter.
This parameter specifies the ARN of an IAM role that RUM will assume to write to the Evidently experiment that you are sending metrics to. This role must have permission to write to that experiment.
If you specify this parameter, you must be signed on to a role that has [PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) permissions attached to it, to allow the role to be passed. The [ CloudWatchAmazonCloudWatchRUMFullAccess](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html#managed-policies-cloudwatch-RUM) policy doesn't include `PassRole` permissions.
Type: String
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: No

## Response Syntax
<a name="API_PutRumMetricsDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutRumMetricsDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutRumMetricsDestination_Errors"></a>

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
<a name="API_PutRumMetricsDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/PutRumMetricsDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/PutRumMetricsDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/PutRumMetricsDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/PutRumMetricsDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/PutRumMetricsDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/PutRumMetricsDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/PutRumMetricsDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/PutRumMetricsDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/PutRumMetricsDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/PutRumMetricsDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
