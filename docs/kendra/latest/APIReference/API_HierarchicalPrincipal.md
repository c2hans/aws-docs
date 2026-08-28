---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_HierarchicalPrincipal.html
---

# HierarchicalPrincipal
<a name="API_HierarchicalPrincipal"></a>

 Information to define the hierarchy for which documents users should have access to.

## Contents
<a name="API_HierarchicalPrincipal_Contents"></a>

 ** PrincipalList **   <a name="kendra-Type-HierarchicalPrincipal-PrincipalList"></a>
A list of [principal](https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html) lists that define the hierarchy for which documents users should have access to. Each hierarchical list specifies which user or group has allow or deny access for each document.
Type: Array of [Principal](API_Principal.md) objects
Required: Yes

## See Also
<a name="API_HierarchicalPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/HierarchicalPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/HierarchicalPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/HierarchicalPrincipal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
