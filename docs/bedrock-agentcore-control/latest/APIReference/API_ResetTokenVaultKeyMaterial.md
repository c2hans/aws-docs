---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ResetTokenVaultKeyMaterial.html
---

# ResetTokenVaultKeyMaterial
<a name="API_ResetTokenVaultKeyMaterial"></a>

Resets the key material for a token vault whose customer managed AWS KMS key has been deleted, and re-encrypts the token vault with an AWS managed key so that you can use the token vault again.

**Important**
This operation can't be undone. The reset permanently deletes the OAuth2 access tokens and refresh tokens stored in the token vault, including tokens obtained through all supported flows. After the reset, your agents must complete these flows again to get new tokens, and for user-delegated flows your users must authorize access again. The reset doesn't delete your credential providers or their configuration.

You can reset a token vault only if its customer managed key has been deleted. If the key still exists, including when it's disabled or scheduled for deletion, this operation returns a `ValidationException`. To use the token vault again, enable the key or cancel its scheduled deletion in AWS KMS. To switch to a different key, use `SetTokenVaultCMK`.

## Request Syntax
<a name="API_ResetTokenVaultKeyMaterial_RequestSyntax"></a>

```
POST /identities/reset-token-vault-key-material HTTP/1.1
Content-type: application/json

{
   "tokenVaultId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ResetTokenVaultKeyMaterial_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ResetTokenVaultKeyMaterial_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tokenVaultId](#API_ResetTokenVaultKeyMaterial_RequestSyntax) **   <a name="bedrockagentcorecontrol-ResetTokenVaultKeyMaterial-request-tokenVaultId"></a>
The unique identifier of the token vault to reset. To reset your account's default token vault, specify `default`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-_]+`
Required: Yes

## Response Syntax
<a name="API_ResetTokenVaultKeyMaterial_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "kmsConfiguration": {
      "keyType": "string",
      "kmsKeyArn": "string"
   },
   "lastModifiedDate": number,
   "tokenVaultId": "string"
}
```

## Response Elements
<a name="API_ResetTokenVaultKeyMaterial_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kmsConfiguration](#API_ResetTokenVaultKeyMaterial_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ResetTokenVaultKeyMaterial-response-kmsConfiguration"></a>
The AWS KMS configuration for the token vault after the reset. The token vault uses an AWS managed key.
Type: [KmsConfiguration](API_KmsConfiguration.md) object

 ** [lastModifiedDate](#API_ResetTokenVaultKeyMaterial_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ResetTokenVaultKeyMaterial-response-lastModifiedDate"></a>
The timestamp when the token vault was last modified.
Type: Timestamp

 ** [tokenVaultId](#API_ResetTokenVaultKeyMaterial_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ResetTokenVaultKeyMaterial-response-tokenVaultId"></a>
The ID of the token vault.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-_]+`

## Errors
<a name="API_ResetTokenVaultKeyMaterial_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This exception is thrown when a request is denied per access permissions
HTTP Status Code: 403

 ** ConflictException **
This exception is thrown when there is a conflict performing an operation
HTTP Status Code: 409

 ** InternalServerException **
This exception is thrown if there was an unexpected error during processing of request
HTTP Status Code: 500

 ** ResourceNotFoundException **
This exception is thrown when a resource referenced by the operation does not exist
HTTP Status Code: 404

 ** ThrottlingException **
This exception is thrown when the number of requests exceeds the limit
HTTP Status Code: 429

 ** UnauthorizedException **
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_ResetTokenVaultKeyMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ResetTokenVaultKeyMaterial)
