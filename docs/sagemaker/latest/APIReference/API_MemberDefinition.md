---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MemberDefinition.html
---

# MemberDefinition
<a name="API_MemberDefinition"></a>

Defines an Amazon Cognito or your own OIDC IdP user group that is part of a work team.

## Contents
<a name="API_MemberDefinition_Contents"></a>

 ** CognitoMemberDefinition **   <a name="sagemaker-Type-MemberDefinition-CognitoMemberDefinition"></a>
The Amazon Cognito user group that is part of the work team.
Type: [CognitoMemberDefinition](API_CognitoMemberDefinition.md) object
Required: No

 ** OidcMemberDefinition **   <a name="sagemaker-Type-MemberDefinition-OidcMemberDefinition"></a>
A list user groups that exist in your OIDC Identity Provider (IdP). One to ten groups can be used to create a single private work team. When you add a user group to the list of `Groups`, you can add that user group to one or more private work teams. If you add a user group to a private work team, all workers in that user group are added to the work team.
Type: [OidcMemberDefinition](API_OidcMemberDefinition.md) object
Required: No

## See Also
<a name="API_MemberDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MemberDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MemberDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MemberDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
