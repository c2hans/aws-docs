---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_StaticPolicyDefinitionDetail.html
---

# StaticPolicyDefinitionDetail
<a name="API_StaticPolicyDefinitionDetail"></a>

A structure that contains details about a static policy. It includes the description and policy body.

This data type is used within a [PolicyDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinition.html) structure as part of a request parameter for the [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html) operation.

## Contents
<a name="API_StaticPolicyDefinitionDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** statement **   <a name="verifiedpermissions-Type-StaticPolicyDefinitionDetail-statement"></a>
The content of the static policy written in the Cedar policy language.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** description **   <a name="verifiedpermissions-Type-StaticPolicyDefinitionDetail-description"></a>
A description of the static policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Required: No

## See Also
<a name="API_StaticPolicyDefinitionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/StaticPolicyDefinitionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/StaticPolicyDefinitionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/StaticPolicyDefinitionDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
