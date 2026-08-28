---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BGW_ImportHypervisorConfiguration.html
---

# ImportHypervisorConfiguration
<a name="API_BGW_ImportHypervisorConfiguration"></a>

Connect to a hypervisor by importing its configuration.

## Request Syntax
<a name="API_BGW_ImportHypervisorConfiguration_RequestSyntax"></a>

```
{
   "Host": "{{string}}",
   "KmsKeyArn": "{{string}}",
   "Name": "{{string}}",
   "Password": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Username": "{{string}}"
}
```

## Request Parameters
<a name="API_BGW_ImportHypervisorConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Host](#API_BGW_ImportHypervisorConfiguration_RequestSyntax) **   <a name="Backup-BGW_ImportHypervisorConfiguration-request-Host"></a>
The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `.+`
Required: Yes

 ** [KmsKeyArn](#API_BGW_ImportHypervisorConfiguration_RequestSyntax) **   <a name="Backup-BGW_ImportHypervisorConfiguration-request-KmsKeyArn"></a>
The AWS Key Management Service for the hypervisor.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `(^arn:(aws|aws-cn|aws-us-gov):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`
Required: No

 ** [Name](#API_BGW_ImportHypervisorConfiguration_RequestSyntax) **   <a name="Backup-BGW_ImportHypervisorConfiguration-request-Name"></a>
The name of the hypervisor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: Yes

 ** [Password](#API_BGW_ImportHypervisorConfiguration_RequestSyntax) **   <a name="Backup-BGW_ImportHypervisorConfiguration-request-Password"></a>
The password for the hypervisor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[ -~]+`
Required: No

 ** [Tags](#API_BGW_ImportHypervisorConfiguration_RequestSyntax) **   <a name="Backup-BGW_ImportHypervisorConfiguration-request-Tags"></a>
The tags of the hypervisor configuration to import.
Type: Array of [Tag](API_BGW_Tag.md) objects
Required: No

 ** [Username](#API_BGW_ImportHypervisorConfiguration_RequestSyntax) **   <a name="Backup-BGW_ImportHypervisorConfiguration-request-Username"></a>
The username for the hypervisor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*`
Required: No

## Response Syntax
<a name="API_BGW_ImportHypervisorConfiguration_ResponseSyntax"></a>

```
{
   "HypervisorArn": "string"
}
```

## Response Elements
<a name="API_BGW_ImportHypervisorConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HypervisorArn](#API_BGW_ImportHypervisorConfiguration_ResponseSyntax) **   <a name="Backup-BGW_ImportHypervisorConfiguration-response-HypervisorArn"></a>
The Amazon Resource Name (ARN) of the hypervisor you disassociated.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

## Errors
<a name="API_BGW_ImportHypervisorConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The operation cannot proceed because you have insufficient permissions.
 ** ErrorCode **
A description of why you have insufficient permissions.
HTTP Status Code: 400

 ** ConflictException **
The operation cannot proceed because it is not supported.
 ** ErrorCode **
A description of why the operation is not supported.
HTTP Status Code: 400

 ** InternalServerException **
The operation did not succeed because an internal error occurred. Try again later.
 ** ErrorCode **
A description of which internal error occured.
HTTP Status Code: 500

 ** ThrottlingException **
TPS has been limited to protect against intentional or unintentional high request volumes.
 ** ErrorCode **
Error: TPS has been limited to protect against intentional or unintentional high request volumes.
HTTP Status Code: 400

 ** ValidationException **
The operation did not succeed because a validation error occurred.
 ** ErrorCode **
A description of what caused the validation error.
HTTP Status Code: 400

## See Also
<a name="API_BGW_ImportHypervisorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/ImportHypervisorConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/ImportHypervisorConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/ImportHypervisorConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/ImportHypervisorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/ImportHypervisorConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/ImportHypervisorConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/ImportHypervisorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
