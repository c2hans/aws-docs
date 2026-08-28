---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GeneralLabelsSettings.html
---

# GeneralLabelsSettings
<a name="API_GeneralLabelsSettings"></a>

Contains filters for the object labels returned by DetectLabels. Filters can be inclusive, exclusive, or a combination of both and can be applied to individual labels or entire label categories. To see a list of label categories, see [Detecting Labels](https://docs.aws.amazon.com/rekognition/latest/dg/labels.html).

## Contents
<a name="API_GeneralLabelsSettings_Contents"></a>

 ** LabelCategoryExclusionFilters **   <a name="rekognition-Type-GeneralLabelsSettings-LabelCategoryExclusionFilters"></a>
The label categories that should be excluded from the return from DetectLabels.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[A-Za-z0-9àâèçñó'-_(). ]*`
Required: No

 ** LabelCategoryInclusionFilters **   <a name="rekognition-Type-GeneralLabelsSettings-LabelCategoryInclusionFilters"></a>
The label categories that should be included in the return from DetectLabels.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[A-Za-z0-9àâèçñó'-_(). ]*`
Required: No

 ** LabelExclusionFilters **   <a name="rekognition-Type-GeneralLabelsSettings-LabelExclusionFilters"></a>
The labels that should be excluded from the return from DetectLabels.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[A-Za-z0-9àâèçñó'-_(). ]*`
Required: No

 ** LabelInclusionFilters **   <a name="rekognition-Type-GeneralLabelsSettings-LabelInclusionFilters"></a>
The labels that should be included in the return from DetectLabels.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[A-Za-z0-9àâèçñó'-_(). ]*`
Required: No

## See Also
<a name="API_GeneralLabelsSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GeneralLabelsSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GeneralLabelsSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GeneralLabelsSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
