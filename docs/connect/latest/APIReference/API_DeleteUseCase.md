---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteUseCase.html
---

# DeleteUseCase
<a name="API_DeleteUseCase"></a>

Deletes a use case from an integration association.

## Request Syntax
<a name="API_DeleteUseCase_RequestSyntax"></a>

```
DELETE /instance/{{InstanceId}}/integration-associations/{{IntegrationAssociationId}}/use-cases/{{UseCaseId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteUseCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DeleteUseCase_RequestSyntax) **   <a name="connect-DeleteUseCase-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [IntegrationAssociationId](#API_DeleteUseCase_RequestSyntax) **   <a name="connect-DeleteUseCase-request-uri-IntegrationAssociationId"></a>
The identifier for the integration association.
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** [UseCaseId](#API_DeleteUseCase_RequestSyntax) **   <a name="connect-DeleteUseCase-request-uri-UseCaseId"></a>
The identifier for the use case.
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## Request Body
<a name="API_DeleteUseCase_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteUseCase_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteUseCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteUseCase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DeleteUseCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteUseCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteUseCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteUseCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteUseCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteUseCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteUseCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteUseCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteUseCase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteUseCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteUseCase)
