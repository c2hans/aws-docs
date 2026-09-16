---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteContactFlowModuleVersion.html
---

# DeleteContactFlowModuleVersion
<a name="API_DeleteContactFlowModuleVersion"></a>

Removes a specific version of a contact flow module.

## Request Syntax
<a name="API_DeleteContactFlowModuleVersion_RequestSyntax"></a>

```
DELETE /contact-flow-modules/{{InstanceId}}/{{ContactFlowModuleId}}/version/{{ContactFlowModuleVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteContactFlowModuleVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowModuleId](#API_DeleteContactFlowModuleVersion_RequestSyntax) **   <a name="connect-DeleteContactFlowModuleVersion-request-uri-ContactFlowModuleId"></a>
The identifier of the flow module.
Required: Yes

 ** [ContactFlowModuleVersion](#API_DeleteContactFlowModuleVersion_RequestSyntax) **   <a name="connect-DeleteContactFlowModuleVersion-request-uri-ContactFlowModuleVersion"></a>
The version of the flow module to delete.
Valid Range: Minimum value of 1.
Required: Yes

 ** [InstanceId](#API_DeleteContactFlowModuleVersion_RequestSyntax) **   <a name="connect-DeleteContactFlowModuleVersion-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DeleteContactFlowModuleVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteContactFlowModuleVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteContactFlowModuleVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteContactFlowModuleVersion_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_DeleteContactFlowModuleVersion_Examples"></a>

### Sample Request
<a name="API_DeleteContactFlowModuleVersion_Example_1"></a>

This example illustrates one usage of DeleteContactFlowModuleVersion.

```
DELETE /contact-flow-modules/12345678-1234-1234-1234-123456789012/abcdefgh-1234-5678-9012-abcdefghijkl/version/2
```

### Sample Response
<a name="API_DeleteContactFlowModuleVersion_Example_2"></a>

This example illustrates one usage of DeleteContactFlowModuleVersion.

```
HTTP/1.1 200 OK
```

## See Also
<a name="API_DeleteContactFlowModuleVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteContactFlowModuleVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteContactFlowModuleVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteContactFlowModuleVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteContactFlowModuleVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteContactFlowModuleVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteContactFlowModuleVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteContactFlowModuleVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteContactFlowModuleVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteContactFlowModuleVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteContactFlowModuleVersion)
