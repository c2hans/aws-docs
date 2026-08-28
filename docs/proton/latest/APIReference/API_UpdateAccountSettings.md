---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateAccountSettings.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# UpdateAccountSettings
<a name="API_UpdateAccountSettings"></a>

Update AWS Proton settings that are used for multiple services in the AWS account.

## Request Syntax
<a name="API_UpdateAccountSettings_RequestSyntax"></a>

```
{
   "deletePipelineProvisioningRepository": {{boolean}},
   "pipelineCodebuildRoleArn": "{{string}}",
   "pipelineProvisioningRepository": {
      "branch": "{{string}}",
      "name": "{{string}}",
      "provider": "{{string}}"
   },
   "pipelineServiceRoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAccountSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deletePipelineProvisioningRepository](#API_UpdateAccountSettings_RequestSyntax) **   <a name="proton-UpdateAccountSettings-request-deletePipelineProvisioningRepository"></a>
Set to `true` to remove a configured pipeline repository from the account settings. Don't set this field if you are updating the configured pipeline repository.
Type: Boolean
Required: No

 ** [pipelineCodebuildRoleArn](#API_UpdateAccountSettings_RequestSyntax) **   <a name="proton-UpdateAccountSettings-request-pipelineCodebuildRoleArn"></a>
The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. AWS Proton assumes this role for CodeBuild-based provisioning.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*(^$)|(^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})$).*`
Required: No

 ** [pipelineProvisioningRepository](#API_UpdateAccountSettings_RequestSyntax) **   <a name="proton-UpdateAccountSettings-request-pipelineProvisioningRepository"></a>
A linked repository for pipeline provisioning. Specify it if you have environments configured for self-managed provisioning with services that include pipelines. A linked repository is a repository that has been registered with AWS Proton. For more information, see [CreateRepository](API_CreateRepository.md).
To remove a previously configured repository, set `deletePipelineProvisioningRepository` to `true`, and don't set `pipelineProvisioningRepository`.
Type: [RepositoryBranchInput](API_RepositoryBranchInput.md) object
Required: No

 ** [pipelineServiceRoleArn](#API_UpdateAccountSettings_RequestSyntax) **   <a name="proton-UpdateAccountSettings-request-pipelineServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Assumed by AWS Proton for AWS-managed provisioning, and by customer-owned automation for self-managed provisioning.
To remove a previously configured ARN, specify an empty string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*(^$)|(^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})$).*`
Required: No

## Response Syntax
<a name="API_UpdateAccountSettings_ResponseSyntax"></a>

```
{
   "accountSettings": {
      "pipelineCodebuildRoleArn": "string",
      "pipelineProvisioningRepository": {
         "arn": "string",
         "branch": "string",
         "name": "string",
         "provider": "string"
      },
      "pipelineServiceRoleArn": "string"
   }
}
```

## Response Elements
<a name="API_UpdateAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountSettings](#API_UpdateAccountSettings_ResponseSyntax) **   <a name="proton-UpdateAccountSettings-response-accountSettings"></a>
The AWS Proton pipeline service role and repository data shared across the AWS account.
Type: [AccountSettings](API_AccountSettings.md) object

## Errors
<a name="API_UpdateAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** ConflictException **
The request *couldn't* be made due to a conflicting operation or resource.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/UpdateAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/UpdateAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/UpdateAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/UpdateAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/UpdateAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/UpdateAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/UpdateAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/UpdateAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/UpdateAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/UpdateAccountSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
