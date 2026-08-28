---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_IdentitySourceParametersForList.html
---

# IdentitySourceParametersForList
<a name="API_IdentitySourceParametersForList"></a>

Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance. For more information, see [Identity source](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Contents
<a name="API_IdentitySourceParametersForList_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** IamIdentityCenter **   <a name="mpa-Type-IdentitySourceParametersForList-IamIdentityCenter"></a>
 AWS IAM Identity Center credentials.
Type: [IamIdentityCenterForList](API_IamIdentityCenterForList.md) object
Required: No

## See Also
<a name="API_IdentitySourceParametersForList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/IdentitySourceParametersForList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/IdentitySourceParametersForList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/IdentitySourceParametersForList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
