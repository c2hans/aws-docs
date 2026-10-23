---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_SignalImpactDimensions.html
---

# SignalImpactDimensions
<a name="API_SignalImpactDimensions"></a>

The three impact dimensions an impact signal assessed. The computed impact band is derived from attackerGains and blastRadius, then shifted by targetValue.

## Contents
<a name="API_SignalImpactDimensions_Contents"></a>

 ** attackerGains **   <a name="continuum-Type-SignalImpactDimensions-attackerGains"></a>
The assessed attacker-gains dimension with the basis behind it.
Type: [SignalAttackerGainsDimension](API_SignalAttackerGainsDimension.md) object
Required: No

 ** blastRadius **   <a name="continuum-Type-SignalImpactDimensions-blastRadius"></a>
The assessed blast-radius dimension with the basis behind it.
Type: [SignalBlastRadiusDimension](API_SignalBlastRadiusDimension.md) object
Required: No

 ** targetValue **   <a name="continuum-Type-SignalImpactDimensions-targetValue"></a>
The assessed target-value dimension with the basis behind it.
Type: [SignalTargetValueDimension](API_SignalTargetValueDimension.md) object
Required: No

## See Also
<a name="API_SignalImpactDimensions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/SignalImpactDimensions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/SignalImpactDimensions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/SignalImpactDimensions)
