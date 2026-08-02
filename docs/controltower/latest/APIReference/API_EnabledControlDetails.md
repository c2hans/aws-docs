---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlDetails.html
---

# EnabledControlDetails
<a name="API_EnabledControlDetails"></a>

Information about the enabled control.

## Contents
<a name="API_EnabledControlDetails_Contents"></a>

 ** arn **   <a name="controltower-Type-EnabledControlDetails-arn"></a>
The ARN of the enabled control.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** controlIdentifier **   <a name="controltower-Type-EnabledControlDetails-controlIdentifier"></a>
The control identifier of the enabled control. For information on how to find the `controlIdentifier`, see [the overview page](https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** driftStatusSummary **   <a name="controltower-Type-EnabledControlDetails-driftStatusSummary"></a>
The drift status of the enabled control.
Type: [DriftStatusSummary](API_DriftStatusSummary.md) object
Required: No

 ** parameters **   <a name="controltower-Type-EnabledControlDetails-parameters"></a>
Array of `EnabledControlParameter` objects.
Type: Array of [EnabledControlParameterSummary](API_EnabledControlParameterSummary.md) objects
Required: No

 ** parentIdentifier **   <a name="controltower-Type-EnabledControlDetails-parentIdentifier"></a>
The ARN of the parent enabled control from which this control inherits its configuration, if applicable.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** statusSummary **   <a name="controltower-Type-EnabledControlDetails-statusSummary"></a>
The deployment summary of the enabled control.
Type: [EnablementStatusSummary](API_EnablementStatusSummary.md) object
Required: No

 ** targetIdentifier **   <a name="controltower-Type-EnabledControlDetails-targetIdentifier"></a>
The ARN of the organizational unit. For information on how to find the `targetIdentifier`, see [the overview page](https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** targetRegions **   <a name="controltower-Type-EnabledControlDetails-targetRegions"></a>
Target AWS Regions for the enabled control.
Type: Array of [Region](API_Region.md) objects
Required: No

## See Also
<a name="API_EnabledControlDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnabledControlDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnabledControlDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnabledControlDetails)
