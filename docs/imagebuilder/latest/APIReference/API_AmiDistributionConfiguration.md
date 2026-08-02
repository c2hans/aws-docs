---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_AmiDistributionConfiguration.html
---

# AmiDistributionConfiguration
<a name="API_AmiDistributionConfiguration"></a>

Define and configure the output AMIs of the pipeline.

## Contents
<a name="API_AmiDistributionConfiguration_Contents"></a>

 ** amiTags **   <a name="imagebuilder-Type-AmiDistributionConfiguration-amiTags"></a>
The tags to apply to AMIs distributed to this Region.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** description **   <a name="imagebuilder-Type-AmiDistributionConfiguration-description"></a>
The description of the AMI distribution configuration. Minimum and maximum length are in characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** kmsKeyId **   <a name="imagebuilder-Type-AmiDistributionConfiguration-kmsKeyId"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt the distributed image. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** launchPermission **   <a name="imagebuilder-Type-AmiDistributionConfiguration-launchPermission"></a>
Launch permissions can be used to configure which AWS accounts can use the AMI to launch instances.
Type: [LaunchPermissionConfiguration](API_LaunchPermissionConfiguration.md) object
Required: No

 ** name **   <a name="imagebuilder-Type-AmiDistributionConfiguration-name"></a>
The name of the output AMI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[-_A-Za-z0-9{][-_A-Za-z0-9\s:{}\.]+[-_A-Za-z0-9}]$`
Required: No

 ** targetAccountIds **   <a name="imagebuilder-Type-AmiDistributionConfiguration-targetAccountIds"></a>
The ID of an account to which you want to distribute an image.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1536 items.
Pattern: `^[0-9]{12}$`
Required: No

## See Also
<a name="API_AmiDistributionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/AmiDistributionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/AmiDistributionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/AmiDistributionConfiguration)
