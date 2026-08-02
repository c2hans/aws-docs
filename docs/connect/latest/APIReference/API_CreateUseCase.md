---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateUseCase.html
---

# CreateUseCase
<a name="API_CreateUseCase"></a>

Creates a use case for an integration association.

## Request Syntax
<a name="API_CreateUseCase_RequestSyntax"></a>

```
PUT /instance/{{InstanceId}}/integration-associations/{{IntegrationAssociationId}}/use-cases HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "UseCaseType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateUseCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateUseCase_RequestSyntax) **   <a name="connect-CreateUseCase-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [IntegrationAssociationId](#API_CreateUseCase_RequestSyntax) **   <a name="connect-CreateUseCase-request-uri-IntegrationAssociationId"></a>
The identifier for the integration association.
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## Request Body
<a name="API_CreateUseCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_CreateUseCase_RequestSyntax) **   <a name="connect-CreateUseCase-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [UseCaseType](#API_CreateUseCase_RequestSyntax) **   <a name="connect-CreateUseCase-request-UseCaseType"></a>
The type of use case to associate to the integration association. Each integration association can have only one of each use case type.
Type: String
Valid Values: `RULES_EVALUATION | CONNECT_CAMPAIGNS`
Required: Yes

## Response Syntax
<a name="API_CreateUseCase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "UseCaseArn": "string",
   "UseCaseId": "string"
}
```

## Response Elements
<a name="API_CreateUseCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UseCaseArn](#API_CreateUseCase_ResponseSyntax) **   <a name="connect-CreateUseCase-response-UseCaseArn"></a>
The Amazon Resource Name (ARN) for the use case.
Type: String

 ** [UseCaseId](#API_CreateUseCase_ResponseSyntax) **   <a name="connect-CreateUseCase-response-UseCaseId"></a>
The identifier of the use case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.

## Errors
<a name="API_CreateUseCase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

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
<a name="API_CreateUseCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateUseCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateUseCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateUseCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateUseCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateUseCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateUseCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateUseCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateUseCase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateUseCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateUseCase)
