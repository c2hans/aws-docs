---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentTarget.html
---

# AssessmentTarget
<a name="API_AssessmentTarget"></a>

Contains information about an Amazon Inspector Classic application. This data type is used as the response element in the [DescribeAssessmentTargets](API_DescribeAssessmentTargets.md) action.

## Contents
<a name="API_AssessmentTarget_Contents"></a>

 ** arn **   <a name="Inspector-Type-AssessmentTarget-arn"></a>
The ARN that specifies the Amazon Inspector Classic assessment target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** createdAt **   <a name="Inspector-Type-AssessmentTarget-createdAt"></a>
The time at which the assessment target is created.
Type: Timestamp
Required: Yes

 ** name **   <a name="Inspector-Type-AssessmentTarget-name"></a>
The name of the Amazon Inspector Classic assessment target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Required: Yes

 ** updatedAt **   <a name="Inspector-Type-AssessmentTarget-updatedAt"></a>
The time at which [UpdateAssessmentTarget](API_UpdateAssessmentTarget.md) is called.
Type: Timestamp
Required: Yes

 ** resourceGroupArn **   <a name="Inspector-Type-AssessmentTarget-resourceGroupArn"></a>
The ARN that specifies the resource group that is associated with the assessment target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## See Also
<a name="API_AssessmentTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssessmentTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssessmentTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssessmentTarget)
