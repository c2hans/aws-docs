---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteMetric.html
---

# DeleteMetric
<a name="API_DeleteMetric"></a>

Deletes an existing metric from the specified Connect Customer instance. This operation fails with `ResourceConflictException` if the metric is currently in use in a dashboard.

## Request Syntax
<a name="API_DeleteMetric_RequestSyntax"></a>

```
DELETE /metrics/definitions/{{InstanceId}}/{{MetricId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DeleteMetric_RequestSyntax) **   <a name="connect-DeleteMetric-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MetricId](#API_DeleteMetric_RequestSyntax) **   <a name="connect-DeleteMetric-request-uri-MetricId"></a>
The identifier of the metric to delete.
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

## Request Body
<a name="API_DeleteMetric_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteMetric_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteMetric_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceInUseException **
That resource is already in use (for example, you're trying to add a record with the same name as an existing record). If you are trying to delete a resource (for example, DeleteHoursOfOperation or DeletePredefinedAttribute), remove its reference from related resources and then try again.
 ** ResourceId **
The identifier for the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_DeleteMetric_Examples"></a>

### Example
<a name="API_DeleteMetric_Example_1"></a>

The following example deletes a custom metric.

#### Sample Request
<a name="API_DeleteMetric_Example_1_Request"></a>

```
DELETE /metrics/definitions/12345678-1234-1234-1234-123456789012/87654321-4321-4321-4321-210987654321
```

#### Sample Response
<a name="API_DeleteMetric_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteMetric)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteMetric)
