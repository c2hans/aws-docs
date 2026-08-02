---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeExternalAccountBinding.html
---

# CreateAcmeExternalAccountBinding
<a name="API_CreateAcmeExternalAccountBinding"></a>

Creates an external account binding (EAB) for an ACME endpoint. An EAB provides credentials that authorize an ACME client to register an account with the endpoint. Each EAB is associated with an IAM role that controls what certificate operations the ACME client can perform.

## Request Syntax
<a name="API_CreateAcmeExternalAccountBinding_RequestSyntax"></a>

```
{
   "AcmeEndpointArn": "{{string}}",
   "Expiration": {
      "Type": "{{string}}",
      "Value": {{number}}
   },
   "IdempotencyToken": "{{string}}",
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAcmeExternalAccountBinding_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AcmeEndpointArn](#API_CreateAcmeExternalAccountBinding_RequestSyntax) **   <a name="ACM-CreateAcmeExternalAccountBinding-request-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the ACME endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`
Required: Yes

 ** [RoleArn](#API_CreateAcmeExternalAccountBinding_RequestSyntax) **   <a name="ACM-CreateAcmeExternalAccountBinding-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to associate with the external account binding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [Expiration](#API_CreateAcmeExternalAccountBinding_RequestSyntax) **   <a name="ACM-CreateAcmeExternalAccountBinding-request-Expiration"></a>
The expiration configuration for the external account binding.
Type: [Expiration](API_Expiration.md) object
Required: No

 ** [IdempotencyToken](#API_CreateAcmeExternalAccountBinding_RequestSyntax) **   <a name="ACM-CreateAcmeExternalAccountBinding-request-IdempotencyToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Required: No

 ** [Tags](#API_CreateAcmeExternalAccountBinding_RequestSyntax) **   <a name="ACM-CreateAcmeExternalAccountBinding-request-Tags"></a>
One or more tags to associate with the external account binding.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAcmeExternalAccountBinding_ResponseSyntax"></a>

```
{
   "ExternalAccountBinding": {
      "AcmeEndpointArn": "string",
      "AcmeExternalAccountBindingArn": "string",
      "CreatedAt": number,
      "ExpiresAt": number,
      "LastUsedAt": number,
      "RevokedAt": number,
      "RoleArn": "string",
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateAcmeExternalAccountBinding_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExternalAccountBinding](#API_CreateAcmeExternalAccountBinding_ResponseSyntax) **   <a name="ACM-CreateAcmeExternalAccountBinding-response-ExternalAccountBinding"></a>
The created external account binding.
Type: [AcmeExternalAccountBinding](API_AcmeExternalAccountBinding.md) object

## Errors
<a name="API_CreateAcmeExternalAccountBinding_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have access required to perform this action.
HTTP Status Code: 400

 ** ConflictException **
You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
A service quota has been exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded a quota.
 ** throttlingReasons **
One or more reasons why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **
The supplied input failed to satisfy constraints of an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateAcmeExternalAccountBinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/CreateAcmeExternalAccountBinding)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/CreateAcmeExternalAccountBinding)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CreateAcmeExternalAccountBinding)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/CreateAcmeExternalAccountBinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CreateAcmeExternalAccountBinding)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/CreateAcmeExternalAccountBinding)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/CreateAcmeExternalAccountBinding)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/CreateAcmeExternalAccountBinding)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/CreateAcmeExternalAccountBinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CreateAcmeExternalAccountBinding)
