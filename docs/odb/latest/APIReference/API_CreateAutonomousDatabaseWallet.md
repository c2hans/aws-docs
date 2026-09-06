---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateAutonomousDatabaseWallet.html
---

# CreateAutonomousDatabaseWallet
<a name="API_CreateAutonomousDatabaseWallet"></a>

Creates a new wallet for the specified Autonomous Database.

## Request Syntax
<a name="API_CreateAutonomousDatabaseWallet_RequestSyntax"></a>

```
{
   "autonomousDatabaseId": "{{string}}",
   "clientToken": "{{string}}",
   "password": "{{string}}",
   "passwordSource": "{{string}}",
   "passwordSourceConfiguration": { ... },
   "walletType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateAutonomousDatabaseWallet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autonomousDatabaseId](#API_CreateAutonomousDatabaseWallet_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseWallet-request-autonomousDatabaseId"></a>
The unique identifier of the Autonomous Database to create a wallet for.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [clientToken](#API_CreateAutonomousDatabaseWallet_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseWallet-request-clientToken"></a>
A client-provided token to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [password](#API_CreateAutonomousDatabaseWallet_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseWallet-request-password"></a>
The password to encrypt the keys inside the wallet.
Type: String
Length Constraints: Minimum length of 8.
Required: No

 ** [passwordSource](#API_CreateAutonomousDatabaseWallet_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseWallet-request-passwordSource"></a>
The source of the password for encrypting the wallet. When set to `CUSTOMER_MANAGED_AWS_SECRET`, the password is retrieved from an AWS Secrets Manager secret.
Type: String
Valid Values: `CUSTOMER_MANAGED_AWS_SECRET | API_REQUEST_PARAMETER`
Required: No

 ** [passwordSourceConfiguration](#API_CreateAutonomousDatabaseWallet_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseWallet-request-passwordSourceConfiguration"></a>
The configuration of the password source for the Autonomous Database wallet.
Type: [WalletPasswordSourceConfigurationInput](API_WalletPasswordSourceConfigurationInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [walletType](#API_CreateAutonomousDatabaseWallet_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseWallet-request-walletType"></a>
The type of wallet to create, either a regional wallet or an instance wallet.
Type: String
Valid Values: `REGIONAL | INSTANCE`
Required: No

## Response Syntax
<a name="API_CreateAutonomousDatabaseWallet_ResponseSyntax"></a>

```
{
   "autonomousDatabaseWalletFile": blob
}
```

## Response Elements
<a name="API_CreateAutonomousDatabaseWallet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseWalletFile](#API_CreateAutonomousDatabaseWallet_ResponseSyntax) **   <a name="odb-CreateAutonomousDatabaseWallet-response-autonomousDatabaseWalletFile"></a>
The generated wallet file for the Autonomous Database, returned as a compressed archive.
Type: Base64-encoded binary data object

## Errors
<a name="API_CreateAutonomousDatabaseWallet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateAutonomousDatabaseWallet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateAutonomousDatabaseWallet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateAutonomousDatabaseWallet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateAutonomousDatabaseWallet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateAutonomousDatabaseWallet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateAutonomousDatabaseWallet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateAutonomousDatabaseWallet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateAutonomousDatabaseWallet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateAutonomousDatabaseWallet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateAutonomousDatabaseWallet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateAutonomousDatabaseWallet)
