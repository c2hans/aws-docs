---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentTargetFilter.html
---

# AssessmentTargetFilter
<a name="API_AssessmentTargetFilter"></a>

Used as the request parameter in the [ListAssessmentTargets](API_ListAssessmentTargets.md) action.

## Contents
<a name="API_AssessmentTargetFilter_Contents"></a>

 ** assessmentTargetNamePattern **   <a name="Inspector-Type-AssessmentTargetFilter-assessmentTargetNamePattern"></a>
For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the **assessmentTargetName** property of the [AssessmentTarget](API_AssessmentTarget.md) data type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Required: No

## See Also
<a name="API_AssessmentTargetFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssessmentTargetFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssessmentTargetFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssessmentTargetFilter)
