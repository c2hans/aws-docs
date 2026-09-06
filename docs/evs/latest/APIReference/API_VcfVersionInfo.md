---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_VcfVersionInfo.html
---

# VcfVersionInfo
<a name="API_VcfVersionInfo"></a>

Information about a VCF versions provided by Amazon EVS, including its status, default ESX version, and EC2 instance types.

## Contents
<a name="API_VcfVersionInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** defaultEsxVersion **   <a name="evs-Type-VcfVersionInfo-defaultEsxVersion"></a>
The default ESX version for this VCF version. It is based on Broadcom's Bill Of Materials (BOM).
Type: String
Required: Yes

 ** instanceTypes **   <a name="evs-Type-VcfVersionInfo-instanceTypes"></a>
EC2 instance types provided by Amazon EVS for this VCF version for creating environments.
Type: Array of strings
Valid Values: `i4i.metal | i7i.metal-24xl | i7i.metal-48xl`
Required: Yes

 ** status **   <a name="evs-Type-VcfVersionInfo-status"></a>
The status for this VCF version. Valid values are:
+  `AVAILABLE` - This VCF version is available to you.
+  `RESTRICTED` - This VCF version has limited availability.
 If the version you need shows RESTRICTED, and you require, check out [VCF versions and EC2 instance types provided by Amazon EVS](https://docs.aws.amazon.com/evs/latest/userguide/versions-provided.html) for more information.
Type: String
Required: Yes

 ** vcfVersion **   <a name="evs-Type-VcfVersionInfo-vcfVersion"></a>
The VCF version number.
Type: String
Valid Values: `VCF-5.2.1 | VCF-5.2.2 | SELF_DEPLOYED`
Required: Yes

## See Also
<a name="API_VcfVersionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/VcfVersionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/VcfVersionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/VcfVersionInfo)
