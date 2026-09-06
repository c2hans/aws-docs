---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ArchiveRuleSummary.html
---

# ArchiveRuleSummary
<a name="API_ArchiveRuleSummary"></a>

Contains information about an archive rule. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.

## Contents
<a name="API_ArchiveRuleSummary_Contents"></a>

 ** createdAt **   <a name="accessanalyzer-Type-ArchiveRuleSummary-createdAt"></a>
The time at which the archive rule was created.
Type: Timestamp
Required: Yes

 ** filter **   <a name="accessanalyzer-Type-ArchiveRuleSummary-filter"></a>
A filter used to define the archive rule.
Type: String to [Criterion](API_Criterion.md) object map
Required: Yes

 ** ruleName **   <a name="accessanalyzer-Type-ArchiveRuleSummary-ruleName"></a>
The name of the archive rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

 ** updatedAt **   <a name="accessanalyzer-Type-ArchiveRuleSummary-updatedAt"></a>
The time at which the archive rule was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_ArchiveRuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ArchiveRuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ArchiveRuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ArchiveRuleSummary)
