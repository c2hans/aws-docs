---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteRumMetricsDestination.html
---

# DeleteRumMetricsDestination
<a name="API_DeleteRumMetricsDestination"></a>

Deletes a destination for CloudWatch RUM extended metrics, so that the specified app monitor stops sending extended metrics to that destination.

## Request Syntax
<a name="API_DeleteRumMetricsDestination_RequestSyntax"></a>

```
DELETE /rummetrics/{{AppMonitorName}}/metricsdestination?destination={{Destination}}&destinationArn={{DestinationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRumMetricsDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppMonitorName](#API_DeleteRumMetricsDestination_RequestSyntax) **   <a name="cloudwatchrum-DeleteRumMetricsDestination-request-uri-AppMonitorName"></a>
The name of the app monitor that is sending metrics to the destination that you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

 ** [Destination](#API_DeleteRumMetricsDestination_RequestSyntax) **   <a name="cloudwatchrum-DeleteRumMetricsDestination-request-uri-Destination"></a>
The type of destination to delete. Valid values are `CloudWatch` and `Evidently`.
Valid Values: `CloudWatch | Evidently`
Required: Yes

 ** [DestinationArn](#API_DeleteRumMetricsDestination_RequestSyntax) **   <a name="cloudwatchrum-DeleteRumMetricsDestination-request-uri-DestinationArn"></a>
This parameter is required if `Destination` is `Evidently`. If `Destination` is `CloudWatch`, do not use this parameter. This parameter specifies the ARN of the Evidently experiment that corresponds to the destination to delete.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

## Request Body
<a name="API_DeleteRumMetricsDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRumMetricsDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteRumMetricsDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteRumMetricsDestination_Errors"></a>

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
<a name="API_DeleteRumMetricsDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/DeleteRumMetricsDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/DeleteRumMetricsDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/DeleteRumMetricsDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/DeleteRumMetricsDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/DeleteRumMetricsDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/DeleteRumMetricsDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/DeleteRumMetricsDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/DeleteRumMetricsDestination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/DeleteRumMetricsDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/DeleteRumMetricsDestination)
