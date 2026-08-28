---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateEncryptionConfiguration.html
---

# UpdateEncryptionConfiguration
<a name="API_UpdateEncryptionConfiguration"></a>

Updates the encryption configuration. By default, AWS IoT Core encrypts your data at rest using AWS owned keys. AWS IoT Core also supports symmetric customer managed keys from AWS Key Management Service (AWS KMS). With customer managed keys, you create, own, and manage the KMS keys in your AWS account.

Before using this API, you must set up permissions for AWS IoT Core to access AWS KMS. For more information, see [Data encryption at rest](https://docs.aws.amazon.com/iot/latest/developerguide/encryption-at-rest.html) in the * AWS IoT Core Developer Guide*.

## Request Syntax
<a name="API_UpdateEncryptionConfiguration_RequestSyntax"></a>

```
PATCH /encryption-configuration HTTP/1.1
Content-type: application/json

{
   "encryptionType": "{{string}}",
   "kmsAccessRoleArn": "{{string}}",
   "kmsKeyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEncryptionConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateEncryptionConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encryptionType](#API_UpdateEncryptionConfiguration_RequestSyntax) **   <a name="iot-UpdateEncryptionConfiguration-request-encryptionType"></a>
The type of the KMS key.
Type: String
Valid Values: `CUSTOMER_MANAGED_KMS_KEY | AWS_OWNED_KMS_KEY`
Required: Yes

 ** [kmsAccessRoleArn](#API_UpdateEncryptionConfiguration_RequestSyntax) **   <a name="iot-UpdateEncryptionConfiguration-request-kmsAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role assumed by AWS IoT Core to call AWS KMS on behalf of the customer.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [kmsKeyArn](#API_UpdateEncryptionConfiguration_RequestSyntax) **   <a name="iot-UpdateEncryptionConfiguration-request-kmsKeyArn"></a>
The ARN of the customer managedKMS key.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_UpdateEncryptionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateEncryptionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateEncryptionConfiguration_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_UpdateEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateEncryptionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateEncryptionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateEncryptionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateEncryptionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateEncryptionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateEncryptionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateEncryptionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateEncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
