---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OidcMemberDefinition.html
---

# OidcMemberDefinition
<a name="API_OidcMemberDefinition"></a>

A list of user groups that exist in your OIDC Identity Provider (IdP). One to ten groups can be used to create a single private work team. When you add a user group to the list of `Groups`, you can add that user group to one or more private work teams. If you add a user group to a private work team, all workers in that user group are added to the work team.

## Contents
<a name="API_OidcMemberDefinition_Contents"></a>

 ** Groups **   <a name="sagemaker-Type-OidcMemberDefinition-Groups"></a>
A list of comma seperated strings that identifies user groups in your OIDC IdP. Each user group is made up of a group of private workers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

## See Also
<a name="API_OidcMemberDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OidcMemberDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OidcMemberDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OidcMemberDefinition)
