---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Cvss.html
---

# Cvss
<a name="API_Cvss"></a>

CVSS scores from the advisory related to the vulnerability.

## Contents
<a name="API_Cvss_Contents"></a>

 ** Adjustments **   <a name="securityhub-Type-Cvss-Adjustments"></a>
Adjustments to the CVSS metrics.
Type: Array of [Adjustment](API_Adjustment.md) objects
Required: No

 ** BaseScore **   <a name="securityhub-Type-Cvss-BaseScore"></a>
The base CVSS score.
Type: Double
Required: No

 ** BaseVector **   <a name="securityhub-Type-Cvss-BaseVector"></a>
The base scoring vector for the CVSS score.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Source **   <a name="securityhub-Type-Cvss-Source"></a>
The origin of the original CVSS score and vector.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Version **   <a name="securityhub-Type-Cvss-Version"></a>
The version of CVSS for the CVSS score.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Cvss_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Cvss)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Cvss)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Cvss)
