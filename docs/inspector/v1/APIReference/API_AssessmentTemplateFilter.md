---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentTemplateFilter.html
---

# AssessmentTemplateFilter
<a name="API_AssessmentTemplateFilter"></a>

Used as the request parameter in the [ListAssessmentTemplates](API_ListAssessmentTemplates.md) action.

## Contents
<a name="API_AssessmentTemplateFilter_Contents"></a>

 ** durationRange **   <a name="Inspector-Type-AssessmentTemplateFilter-durationRange"></a>
For a record to match a filter, the value specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **durationInSeconds** property of the [AssessmentTemplate](API_AssessmentTemplate.md) data type.
Type: [DurationRange](API_DurationRange.md) object
Required: No

 ** namePattern **   <a name="Inspector-Type-AssessmentTemplateFilter-namePattern"></a>
For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the **assessmentTemplateName** property of the [AssessmentTemplate](API_AssessmentTemplate.md) data type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Required: No

 ** rulesPackageArns **   <a name="Inspector-Type-AssessmentTemplateFilter-rulesPackageArns"></a>
For a record to match a filter, the values that are specified for this data type property must be contained in the list of values of the **rulesPackageArns** property of the [AssessmentTemplate](API_AssessmentTemplate.md) data type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## See Also
<a name="API_AssessmentTemplateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssessmentTemplateFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssessmentTemplateFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssessmentTemplateFilter)
