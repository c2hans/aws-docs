---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Ami.html
---

# Ami
<a name="API_Ami"></a>

Details of an Amazon EC2 AMI.

## Contents
<a name="API_Ami_Contents"></a>

 ** accountId **   <a name="imagebuilder-Type-Ami-accountId"></a>
The account ID of the owner of the AMI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** description **   <a name="imagebuilder-Type-Ami-description"></a>
The description of the Amazon EC2 AMI. Minimum and maximum length are in characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** image **   <a name="imagebuilder-Type-Ami-image"></a>
The AMI ID of the Amazon EC2 AMI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-Ami-name"></a>
The name of the Amazon EC2 AMI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** region **   <a name="imagebuilder-Type-Ami-region"></a>
The AWS Region of the Amazon EC2 AMI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** state **   <a name="imagebuilder-Type-Ami-state"></a>
The state of the AMI, which includes the status and, if applicable, the reason for that status.
Type: [ImageState](API_ImageState.md) object
Required: No

## See Also
<a name="API_Ami_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/Ami)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/Ami)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/Ami)
