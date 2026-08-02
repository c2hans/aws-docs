---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_Policy.html
---

# Policy
<a name="API_Policy"></a>

Contains rules to be applied to the affected accounts. Policies can be attached directly to accounts, or to roots and OUs to affect all accounts in those hierarchies.

## Contents
<a name="API_Policy_Contents"></a>

 ** Content **   <a name="organizations-Type-Policy-Content"></a>
The text content of the policy.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\s\S]*`
Required: No

 ** PolicySummary **   <a name="organizations-Type-Policy-PolicySummary"></a>
A structure that contains additional details about the policy.
Type: [PolicySummary](API_PolicySummary.md) object
Required: No

## See Also
<a name="API_Policy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/Policy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/Policy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/Policy)
