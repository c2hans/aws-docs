---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_AccountAggregation.html
---

# AccountAggregation
<a name="API_AccountAggregation"></a>

Contains counts of vulnerability findings from image scans that run when you create new Image Builder images, or build new versions of existing images. The vulnerability counts are grouped by severity level. The counts are aggregated across resources to create the final tally for the account that owns them.

## Contents
<a name="API_AccountAggregation_Contents"></a>

 ** accountId **   <a name="imagebuilder-Type-AccountAggregation-accountId"></a>
Identifies the account that owns the aggregated resource findings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** severityCounts **   <a name="imagebuilder-Type-AccountAggregation-severityCounts"></a>
Counts by severity level for medium severity and higher level findings, plus a total for all of the findings.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_AccountAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/AccountAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/AccountAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/AccountAggregation)
