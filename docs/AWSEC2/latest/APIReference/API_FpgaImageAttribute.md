---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FpgaImageAttribute.html
---

# FpgaImageAttribute
<a name="API_FpgaImageAttribute"></a>

Describes an Amazon FPGA image (AFI) attribute.

## Contents
<a name="API_FpgaImageAttribute_Contents"></a>

 ** description **
The description of the AFI.
Type: String
Required: No

 ** fpgaImageId **
The ID of the AFI.
Type: String
Required: No

 ** LoadPermissions.N **
The load permissions.
Type: Array of [LoadPermission](API_LoadPermission.md) objects
Required: No

 ** name **
The name of the AFI.
Type: String
Required: No

 ** ProductCodes.N **
The product codes.
Type: Array of [ProductCode](API_ProductCode.md) objects
Required: No

## See Also
<a name="API_FpgaImageAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FpgaImageAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FpgaImageAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FpgaImageAttribute)
