---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_RegisterImageOptions.html
---

# RegisterImageOptions
<a name="API_RegisterImageOptions"></a>

Controls Secure Boot and UEFI data settings for the resulting image during ISO imports. For more information, see [UEFI Secure Boot for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html) in the * *Amazon EC2 User Guide* *.

## Contents
<a name="API_RegisterImageOptions_Contents"></a>

 ** secureBootEnabled **   <a name="imagebuilder-Type-RegisterImageOptions-secureBootEnabled"></a>
Specifies whether Secure Boot is enabled for the output AMI. The default value is `true`. To disable Secure Boot for custom unsigned drivers, set this value to `false`.
Type: Boolean
Required: No

 ** uefiData **   <a name="imagebuilder-Type-RegisterImageOptions-uefiData"></a>
A Base64-encoded representation of the non-volatile UEFI variable store. You can specify this parameter only when `secureBootEnabled` is `true` or unspecified. You can inspect and modify the UEFI data by using the [python-uefivars tool on GitHub](https://github.com/awslabs/python-uefivars).
For more information, see [UEFI variables for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-variables.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64000.
Required: No

## See Also
<a name="API_RegisterImageOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/RegisterImageOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/RegisterImageOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/RegisterImageOptions)
