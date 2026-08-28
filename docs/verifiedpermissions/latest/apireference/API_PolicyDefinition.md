---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinition.html
---

# PolicyDefinition
<a name="API_PolicyDefinition"></a>

A structure that contains the details for a Cedar policy definition. It includes the policy type, a description, and a policy body. This is a top level data type used to create a policy.

This data type is used as a request parameter for the [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html) operation. This structure must always have either an `static` or a `templateLinked` element.

## Contents
<a name="API_PolicyDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** static **   <a name="verifiedpermissions-Type-PolicyDefinition-static"></a>
A structure that describes a static policy. An static policy doesn't use a template or allow placeholders for entities.
Type: [StaticPolicyDefinition](API_StaticPolicyDefinition.md) object
Required: No

 ** templateLinked **   <a name="verifiedpermissions-Type-PolicyDefinition-templateLinked"></a>
A structure that describes a policy that was instantiated from a template. The template can specify placeholders for `principal` and `resource`. When you use [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html) to create a policy from a template, you specify the exact principal and resource to use for the instantiated policy.
Type: [TemplateLinkedPolicyDefinition](API_TemplateLinkedPolicyDefinition.md) object
Required: No

## See Also
<a name="API_PolicyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/PolicyDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/PolicyDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/PolicyDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
