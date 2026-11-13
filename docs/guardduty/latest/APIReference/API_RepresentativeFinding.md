---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RepresentativeFinding.html
---

# RepresentativeFinding
<a name="API_RepresentativeFinding"></a>

Contains a representative finding for an affected resource. GuardDuty selects one finding for each affected resource, based on severity.

## Contents
<a name="API_RepresentativeFinding_Contents"></a>

 ** findingCount **   <a name="guardduty-Type-RepresentativeFinding-findingCount"></a>
The number of findings for the resource.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** findingId **   <a name="guardduty-Type-RepresentativeFinding-findingId"></a>
The ID of the representative finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** identifier **   <a name="guardduty-Type-RepresentativeFinding-identifier"></a>
The identifier of the affected resource.
Type: String
Required: No

 ** resourceType **   <a name="guardduty-Type-RepresentativeFinding-resourceType"></a>
The type of the affected resource.
Type: String
Required: No

 ** riskLevel **   <a name="guardduty-Type-RepresentativeFinding-riskLevel"></a>
The assessed risk level of the resource. Possible values are `Info`, `Low`, `Medium`, `High`, and `Critical`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `Info | Low | Medium | High | Critical`
Required: No

 ** riskRationale **   <a name="guardduty-Type-RepresentativeFinding-riskRationale"></a>
The reason for the assessed risk level.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_RepresentativeFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RepresentativeFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RepresentativeFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RepresentativeFinding)
