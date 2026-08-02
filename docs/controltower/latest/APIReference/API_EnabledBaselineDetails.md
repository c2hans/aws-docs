---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineDetails.html
---

# EnabledBaselineDetails
<a name="API_EnabledBaselineDetails"></a>

Details of the `EnabledBaseline` resource.

## Contents
<a name="API_EnabledBaselineDetails_Contents"></a>

 ** arn **   <a name="controltower-Type-EnabledBaselineDetails-arn"></a>
The ARN of the `EnabledBaseline` resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: Yes

 ** baselineIdentifier **   <a name="controltower-Type-EnabledBaselineDetails-baselineIdentifier"></a>
The specific `Baseline` enabled as part of the `EnabledBaseline` resource.
Type: String
Required: Yes

 ** statusSummary **   <a name="controltower-Type-EnabledBaselineDetails-statusSummary"></a>
The deployment summary of an `EnabledControl` or `EnabledBaseline` resource.
Type: [EnablementStatusSummary](API_EnablementStatusSummary.md) object
Required: Yes

 ** targetIdentifier **   <a name="controltower-Type-EnabledBaselineDetails-targetIdentifier"></a>
The target on which to enable the `Baseline`.
Type: String
Required: Yes

 ** baselineVersion **   <a name="controltower-Type-EnabledBaselineDetails-baselineVersion"></a>
The enabled version of the `Baseline`.
Type: String
Required: No

 ** driftStatusSummary **   <a name="controltower-Type-EnabledBaselineDetails-driftStatusSummary"></a>
The drift status of the enabled baseline.
Type: [EnabledBaselineDriftStatusSummary](API_EnabledBaselineDriftStatusSummary.md) object
Required: No

 ** parameters **   <a name="controltower-Type-EnabledBaselineDetails-parameters"></a>
Shows the parameters that are applied when enabling this `Baseline`.
Type: Array of [EnabledBaselineParameterSummary](API_EnabledBaselineParameterSummary.md) objects
Required: No

 ** parentIdentifier **   <a name="controltower-Type-EnabledBaselineDetails-parentIdentifier"></a>
An ARN that represents the parent `EnabledBaseline` at the Organizational Unit (OU) level, from which the child `EnabledBaseline` inherits its configuration. The value is returned by `GetEnabledBaseline`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

## See Also
<a name="API_EnabledBaselineDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnabledBaselineDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnabledBaselineDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnabledBaselineDetails)
