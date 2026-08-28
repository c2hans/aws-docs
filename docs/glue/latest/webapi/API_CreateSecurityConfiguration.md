---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateSecurityConfiguration.html
---

# CreateSecurityConfiguration
<a name="API_CreateSecurityConfiguration"></a>

Creates a new security configuration. A security configuration is a set of security properties that can be used by AWS Glue. You can use a security configuration to encrypt data at rest. For information about using security configurations in AWS Glue, see [Encrypting Data Written by Crawlers, Jobs, and Development Endpoints](https://docs.aws.amazon.com/glue/latest/dg/encryption-security-configuration.html).

## Request Syntax
<a name="API_CreateSecurityConfiguration_RequestSyntax"></a>

```
{
   "EncryptionConfiguration": {
      "CloudWatchEncryption": {
         "CloudWatchEncryptionMode": "{{string}}",
         "KmsKeyArn": "{{string}}"
      },
      "DataQualityEncryption": {
         "DataQualityEncryptionMode": "{{string}}",
         "KmsKeyArn": "{{string}}"
      },
      "JobBookmarksEncryption": {
         "JobBookmarksEncryptionMode": "{{string}}",
         "KmsKeyArn": "{{string}}"
      },
      "S3Encryption": [
         {
            "KmsKeyArn": "{{string}}",
            "S3EncryptionMode": "{{string}}"
         }
      ]
   },
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateSecurityConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EncryptionConfiguration](#API_CreateSecurityConfiguration_RequestSyntax) **   <a name="Glue-CreateSecurityConfiguration-request-EncryptionConfiguration"></a>
The encryption configuration for the new security configuration.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: Yes

 ** [Name](#API_CreateSecurityConfiguration_RequestSyntax) **   <a name="Glue-CreateSecurityConfiguration-request-Name"></a>
The name for the new security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_CreateSecurityConfiguration_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateSecurityConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_CreateSecurityConfiguration_ResponseSyntax) **   <a name="Glue-CreateSecurityConfiguration-response-CreatedTimestamp"></a>
The time at which the new security configuration was created.
Type: Timestamp

 ** [Name](#API_CreateSecurityConfiguration_ResponseSyntax) **   <a name="Glue-CreateSecurityConfiguration-response-Name"></a>
The name assigned to the new security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_CreateSecurityConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateSecurityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateSecurityConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateSecurityConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateSecurityConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateSecurityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateSecurityConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateSecurityConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateSecurityConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateSecurityConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateSecurityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateSecurityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
