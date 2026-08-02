---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FpgaImage.html
---

# FpgaImage
<a name="API_FpgaImage"></a>

Describes an Amazon FPGA image (AFI).

## Contents
<a name="API_FpgaImage_Contents"></a>

 ** createTime **
The date and time the AFI was created.
Type: Timestamp
Required: No

 ** dataRetentionSupport **
Indicates whether data retention support is enabled for the AFI.
Type: Boolean
Required: No

 ** description **
The description of the AFI.
Type: String
Required: No

 ** fpgaImageGlobalId **
The global FPGA image identifier (AGFI ID).
Type: String
Required: No

 ** fpgaImageId **
The FPGA image identifier (AFI ID).
Type: String
Required: No

 ** InstanceTypes.N **
The instance types supported by the AFI.
Type: Array of strings
Required: No

 ** name **
The name of the AFI.
Type: String
Required: No

 ** ownerAlias **
The alias of the AFI owner. Possible values include `self`, `amazon`, and `aws-marketplace`.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the AFI.
Type: String
Required: No

 ** pciId **
Information about the PCI bus.
Type: [PciId](API_PciId.md) object
Required: No

 ** ProductCodes.N **
The product codes for the AFI.
Type: Array of [ProductCode](API_ProductCode.md) objects
Required: No

 ** public **
Indicates whether the AFI is public.
Type: Boolean
Required: No

 ** shellVersion **
The version of the AWS Shell that was used to create the bitstream.
Type: String
Required: No

 ** state **
Information about the state of the AFI.
Type: [FpgaImageState](API_FpgaImageState.md) object
Required: No

 ** Tags.N **
Any tags assigned to the AFI.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** updateTime **
The time of the most recent update to the AFI.
Type: Timestamp
Required: No

## See Also
<a name="API_FpgaImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FpgaImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FpgaImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FpgaImage)
