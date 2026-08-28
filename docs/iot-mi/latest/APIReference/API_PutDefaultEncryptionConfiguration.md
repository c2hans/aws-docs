---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_PutDefaultEncryptionConfiguration.html
---

# PutDefaultEncryptionConfiguration
<a name="API_PutDefaultEncryptionConfiguration"></a>

Sets the default encryption configuration for the AWS account. For more information, see [Key management](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html) in the AWS IoT SiteWise User Guide.

## Request Syntax
<a name="API_PutDefaultEncryptionConfiguration_RequestSyntax"></a>

```
POST /configuration/account/encryption HTTP/1.1
Content-type: application/json

{
   "encryptionType": "{{string}}",
   "kmsKeyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutDefaultEncryptionConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutDefaultEncryptionConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encryptionType](#API_PutDefaultEncryptionConfiguration_RequestSyntax) **   <a name="managedintegrations-PutDefaultEncryptionConfiguration-request-encryptionType"></a>
The type of encryption used for the encryption configuration.
Type: String
Valid Values: `MANAGED_INTEGRATIONS_DEFAULT_ENCRYPTION | CUSTOMER_KEY_ENCRYPTION`
Required: Yes

 ** [kmsKeyArn](#API_PutDefaultEncryptionConfiguration_RequestSyntax) **   <a name="managedintegrations-PutDefaultEncryptionConfiguration-request-kmsKeyArn"></a>
The Key Amazon Resource Name (ARN) of the AWS AWS KMS key used for AWS KMS encryption if you use `KMS_BASED_ENCRYPTION`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws:kms:[0-9a-zA-Z-]+:[0-9]+:key/[0-9a-zA-Z-]+`
Required: No

## Response Syntax
<a name="API_PutDefaultEncryptionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "configurationStatus": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   },
   "encryptionType": "string",
   "kmsKeyArn": "string"
}
```

## Response Elements
<a name="API_PutDefaultEncryptionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [configurationStatus](#API_PutDefaultEncryptionConfiguration_ResponseSyntax) **   <a name="managedintegrations-PutDefaultEncryptionConfiguration-response-configurationStatus"></a>
Provides the status of the default encryption configuration for an AWS account.
Type: [ConfigurationStatus](API_ConfigurationStatus.md) object

 ** [encryptionType](#API_PutDefaultEncryptionConfiguration_ResponseSyntax) **   <a name="managedintegrations-PutDefaultEncryptionConfiguration-response-encryptionType"></a>
The type of encryption used for the encryption configuration.
Type: String
Valid Values: `MANAGED_INTEGRATIONS_DEFAULT_ENCRYPTION | CUSTOMER_KEY_ENCRYPTION`

 ** [kmsKeyArn](#API_PutDefaultEncryptionConfiguration_ResponseSyntax) **   <a name="managedintegrations-PutDefaultEncryptionConfiguration-response-kmsKeyArn"></a>
The Key Amazon Resource Name (ARN) of the AWS AWS KMS key used for AWS KMS encryption if you use `KMS_BASED_ENCRYPTION`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws:kms:[0-9a-zA-Z-]+:[0-9]+:key/[0-9a-zA-Z-]+`

## Errors
<a name="API_PutDefaultEncryptionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalFailureException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
HTTP Status Code: 401

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_PutDefaultEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/PutDefaultEncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
