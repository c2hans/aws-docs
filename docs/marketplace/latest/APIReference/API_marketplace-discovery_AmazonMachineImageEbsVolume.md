---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_AmazonMachineImageEbsVolume.html
---

# AmazonMachineImageEbsVolume
<a name="API_marketplace-discovery_AmazonMachineImageEbsVolume"></a>

Contains supported Amazon EBS volume information for an AMI fulfillment option.

## Contents
<a name="API_marketplace-discovery_AmazonMachineImageEbsVolume_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** volumeTypes **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageEbsVolume-volumeTypes"></a>
The supported Amazon EBS volume types.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** iops **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageEbsVolume-iops"></a>
The total number of provisioned IOPS supported.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_marketplace-discovery_AmazonMachineImageEbsVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/AmazonMachineImageEbsVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/AmazonMachineImageEbsVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/AmazonMachineImageEbsVolume)
