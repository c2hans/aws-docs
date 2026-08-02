---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlSummary.html
---

# EnabledControlSummary
<a name="API_EnabledControlSummary"></a>

Returns a summary of information about an enabled control.

## Contents
<a name="API_EnabledControlSummary_Contents"></a>

 ** arn **   <a name="controltower-Type-EnabledControlSummary-arn"></a>
The ARN of the enabled control.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** controlIdentifier **   <a name="controltower-Type-EnabledControlSummary-controlIdentifier"></a>
The `controlIdentifier` of the enabled control.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** driftStatusSummary **   <a name="controltower-Type-EnabledControlSummary-driftStatusSummary"></a>
The drift status of the enabled control.
Type: [DriftStatusSummary](API_DriftStatusSummary.md) object
Required: No

 ** parentIdentifier **   <a name="controltower-Type-EnabledControlSummary-parentIdentifier"></a>
The ARN of the parent enabled control from which this control inherits its configuration, if applicable.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** statusSummary **   <a name="controltower-Type-EnabledControlSummary-statusSummary"></a>
A short description of the status of the enabled control.
Type: [EnablementStatusSummary](API_EnablementStatusSummary.md) object
Required: No

 ** targetIdentifier **   <a name="controltower-Type-EnabledControlSummary-targetIdentifier"></a>
The ARN of the organizational unit.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

## See Also
<a name="API_EnabledControlSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnabledControlSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnabledControlSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnabledControlSummary)
