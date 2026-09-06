---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateStaticPolicyDefinition.html
---

# UpdateStaticPolicyDefinition
<a name="API_UpdateStaticPolicyDefinition"></a>

Contains information about an update to a static policy.

## Contents
<a name="API_UpdateStaticPolicyDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** statement **   <a name="verifiedpermissions-Type-UpdateStaticPolicyDefinition-statement"></a>
Specifies the Cedar policy language text to be added to or replaced on the static policy.
You can change only the following elements from the original content:
+ The `action` referenced by the policy.
+ Any conditional clauses, such as `when` or `unless` clauses.
You **can't** change the following elements:
+ Changing from `StaticPolicy` to `TemplateLinkedPolicy`.
+ The effect (`permit` or `forbid`) of the policy.
+ The `principal` referenced by the policy.
+ The `resource` referenced by the policy.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** description **   <a name="verifiedpermissions-Type-UpdateStaticPolicyDefinition-description"></a>
Specifies the description to be added to or replaced on the static policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Required: No

## See Also
<a name="API_UpdateStaticPolicyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/UpdateStaticPolicyDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/UpdateStaticPolicyDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/UpdateStaticPolicyDefinition)
