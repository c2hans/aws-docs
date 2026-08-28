---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CognitoMemberDefinition.html
---

# CognitoMemberDefinition
<a name="API_CognitoMemberDefinition"></a>

Identifies a Amazon Cognito user group. A user group can be used in on or more work teams.

## Contents
<a name="API_CognitoMemberDefinition_Contents"></a>

 ** ClientId **   <a name="sagemaker-Type-CognitoMemberDefinition-ClientId"></a>
An identifier for an application client. You must create the app client ID using Amazon Cognito.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[ -~]+`
Required: Yes

 ** UserGroup **   <a name="sagemaker-Type-CognitoMemberDefinition-UserGroup"></a>
An identifier for a user group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** UserPool **   <a name="sagemaker-Type-CognitoMemberDefinition-UserPool"></a>
An identifier for a user pool. The user pool must be in the same region as the service that you are calling.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_CognitoMemberDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CognitoMemberDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CognitoMemberDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CognitoMemberDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
