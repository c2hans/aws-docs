---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_AssessmentTargetFilter.html
---

# AssessmentTargetFilter
<a name="API_AssessmentTargetFilter"></a>

Filters assessment list results by the resource that was assessed. Provide an entity identifier, a change set identifier, or both.

## Contents
<a name="API_AssessmentTargetFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ChangeSetId **   <a name="AWSMarketplaceService-Type-AssessmentTargetFilter-ChangeSetId"></a>
The unique ID of the change set that triggered the assessments you want to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: No

 ** EntityId **   <a name="AWSMarketplaceService-Type-AssessmentTargetFilter-EntityId"></a>
The unique ID of the entity whose assessments you want to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: No

## See Also
<a name="API_AssessmentTargetFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/AssessmentTargetFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/AssessmentTargetFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/AssessmentTargetFilter)
