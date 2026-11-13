---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingDetail.html
---

# FindingDetail
<a name="API_FindingDetail"></a>

Contains details about a GuardDuty finding.

## Contents
<a name="API_FindingDetail_Contents"></a>

 ** accountId **   <a name="guardduty-Type-FindingDetail-accountId"></a>
The ID of the AWS account in which the finding was generated.
Type: String
Required: No

 ** activityWindow **   <a name="guardduty-Type-FindingDetail-activityWindow"></a>
The time range of the activity that the finding describes.
Type: [ActivityWindow](API_ActivityWindow.md) object
Required: No

 ** findingId **   <a name="guardduty-Type-FindingDetail-findingId"></a>
The ID of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** findingType **   <a name="guardduty-Type-FindingDetail-findingType"></a>
The type of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** region **   <a name="guardduty-Type-FindingDetail-region"></a>
The AWS Region in which the finding was generated.
Type: String
Required: No

 ** severity **   <a name="guardduty-Type-FindingDetail-severity"></a>
The severity of the finding.
Type: String
Required: No

## See Also
<a name="API_FindingDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FindingDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FindingDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FindingDetail)
