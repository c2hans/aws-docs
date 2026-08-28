---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteRemediationConfiguration.html
---

# DeleteRemediationConfiguration
<a name="API_DeleteRemediationConfiguration"></a>

Deletes the remediation configuration.

## Request Syntax
<a name="API_DeleteRemediationConfiguration_RequestSyntax"></a>

```
{
   "ConfigRuleName": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRemediationConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleName](#API_DeleteRemediationConfiguration_RequestSyntax) **   <a name="config-DeleteRemediationConfiguration-request-ConfigRuleName"></a>
The name of the AWS Config rule for which you want to delete remediation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** [ResourceType](#API_DeleteRemediationConfiguration_RequestSyntax) **   <a name="config-DeleteRemediationConfiguration-request-ResourceType"></a>
The type of a resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Elements
<a name="API_DeleteRemediationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteRemediationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPermissionsException **
Indicates one of the following errors:
+ For [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html), the rule cannot be created because the IAM role assigned to AWS Config lacks permissions to perform the config:Put\* action.
+ For [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html), the AWS Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.
+ For [PutOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html), organization AWS Config rule cannot be created because you do not have permissions to call IAM `GetRole` action or create a service-linked role.
+ For [PutConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html) and [PutOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html), a conformance pack cannot be created because you do not have the following permissions:
  + You do not have permission to call IAM `GetRole` action or create a service-linked role.
  + You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.
+ For [PutServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html), a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM `CreateServiceLinkedRole`.
+ For [PutConnector](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html), a connector cannot be created because you do not have the following permissions: IAM `CreateServiceLinkedRole`.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** NoSuchRemediationConfigurationException **
You specified an AWS Config rule without a remediation configuration.
HTTP Status Code: 400

 ** RemediationInProgressException **
Remediation action is in progress. You can either cancel execution in AWS Systems Manager or wait and try again later.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRemediationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DeleteRemediationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DeleteRemediationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeleteRemediationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DeleteRemediationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeleteRemediationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DeleteRemediationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DeleteRemediationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DeleteRemediationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DeleteRemediationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeleteRemediationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
