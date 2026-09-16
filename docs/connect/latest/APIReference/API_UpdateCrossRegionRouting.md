---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateCrossRegionRouting.html
---

# UpdateCrossRegionRouting
<a name="API_UpdateCrossRegionRouting"></a>

Updates the cross-region routing configuration for an Amazon Connect Global Resiliency instance enabled for global routing. When invoked with `IsolatedAll` set to `true`, this operation disables cross-region routing, meaning contacts originating in one Region will no longer be routed to agents in another Region.

**Note**
This operation is available only for Amazon Connect Global Resiliency instances enabled for global routing. Reporting and contact search continue to operate globally after you use this operation.

## Request Syntax
<a name="API_UpdateCrossRegionRouting_RequestSyntax"></a>

```
PUT /cross-region-routing/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "IsolatedAll": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateCrossRegionRouting_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateCrossRegionRouting_RequestSyntax) **   <a name="connect-UpdateCrossRegionRouting-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:([a-zA-Z0-9-]+):connect:[a-z]+-[a-z-]+-[0-9]+:[0-9]+:instance/)?[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_UpdateCrossRegionRouting_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IsolatedAll](#API_UpdateCrossRegionRouting_RequestSyntax) **   <a name="connect-UpdateCrossRegionRouting-request-IsolatedAll"></a>
Set to `true` to disable cross-region routing for all Regions associated with this instance. Set to `false` to re-enable cross-region routing.
Type: Boolean
Required: Yes

## Response Syntax
<a name="API_UpdateCrossRegionRouting_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateCrossRegionRouting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCrossRegionRouting_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateCrossRegionRouting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateCrossRegionRouting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateCrossRegionRouting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateCrossRegionRouting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateCrossRegionRouting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateCrossRegionRouting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateCrossRegionRouting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateCrossRegionRouting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateCrossRegionRouting)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateCrossRegionRouting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateCrossRegionRouting)
