---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_ResourcePolicySummary.html
---

# ResourcePolicySummary
<a name="API_ResourcePolicySummary"></a>

Summary of a policy attached to a resource: its name and revision ID.

## Contents
<a name="API_ResourcePolicySummary_Contents"></a>

 ** PolicyName **   <a name="eventbridgev2-Type-ResourcePolicySummary-PolicyName"></a>
Name of a policy attached to a resource. Valid values: "default" (the customer-managed policy) and "AWS\_RAM" (managed exclusively by AWS Resource Access Manager). Any other value is rejected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** RevisionId **   <a name="eventbridgev2-Type-ResourcePolicySummary-RevisionId"></a>
Revision ID of a resource policy. A new revision ID is generated on every successful write.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_ResourcePolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/ResourcePolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/ResourcePolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/ResourcePolicySummary)
