---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_EntryViolation.html
---

# EntryViolation
<a name="API_EntryViolation"></a>

Detailed information about an entry violation in a network ACL. The violation is against the network ACL specification inside the Firewall Manager network ACL policy. This data object is part of `InvalidNetworkAclEntriesViolation`.

## Contents
<a name="API_EntryViolation_Contents"></a>

 ** ActualEvaluationOrder **   <a name="fms-Type-EntryViolation-ActualEvaluationOrder"></a>
The evaluation location within the ordered list of entries where the `ExpectedEntry` is currently located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** EntriesWithConflicts **   <a name="fms-Type-EntryViolation-EntriesWithConflicts"></a>
The list of entries that are in conflict with `ExpectedEntry`.
Type: Array of [EntryDescription](API_EntryDescription.md) objects
Required: No

 ** EntryAtExpectedEvaluationOrder **   <a name="fms-Type-EntryViolation-EntryAtExpectedEvaluationOrder"></a>
The entry that's currently in the `ExpectedEvaluationOrder` location, in place of the expected entry.
Type: [EntryDescription](API_EntryDescription.md) object
Required: No

 ** EntryViolationReasons **   <a name="fms-Type-EntryViolation-EntryViolationReasons"></a>
Descriptions of the violations that Firewall Manager found for these entries.
Type: Array of strings
Valid Values: `MISSING_EXPECTED_ENTRY | INCORRECT_ENTRY_ORDER | ENTRY_CONFLICT`
Required: No

 ** ExpectedEntry **   <a name="fms-Type-EntryViolation-ExpectedEntry"></a>
The Firewall Manager-managed network ACL entry that is involved in the entry violation.
Type: [EntryDescription](API_EntryDescription.md) object
Required: No

 ** ExpectedEvaluationOrder **   <a name="fms-Type-EntryViolation-ExpectedEvaluationOrder"></a>
The evaluation location within the ordered list of entries where the `ExpectedEntry` should be, according to the network ACL policy specifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_EntryViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/EntryViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/EntryViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/EntryViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
