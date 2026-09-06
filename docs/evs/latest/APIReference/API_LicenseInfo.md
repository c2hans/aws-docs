---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_LicenseInfo.html
---

# LicenseInfo
<a name="API_LicenseInfo"></a>

 The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key.

## Contents
<a name="API_LicenseInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** solutionKey **   <a name="evs-Type-LicenseInfo-solutionKey"></a>
 The VCF solution key. This license unlocks VMware VCF product features, including vSphere, NSX, SDDC Manager, and vCenter Server. The VCF solution key must meet the instance-type-specific minimum core requirements.
Type: String
Pattern: `[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}`
Required: Yes

 ** vsanKey **   <a name="evs-Type-LicenseInfo-vsanKey"></a>
 The VSAN license key. This license unlocks vSAN features. The vSAN license key must meet the instance-type-specific minimum capacity requirements.
Type: String
Pattern: `[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}`
Required: Yes

## See Also
<a name="API_LicenseInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/LicenseInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/LicenseInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/LicenseInfo)
