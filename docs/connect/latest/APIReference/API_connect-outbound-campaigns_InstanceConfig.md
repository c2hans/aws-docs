---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_InstanceConfig.html
---

# InstanceConfig
<a name="API_connect-outbound-campaigns_InstanceConfig"></a>

Contains configuration information about the Connect Customer instance.

## Contents
<a name="API_connect-outbound-campaigns_InstanceConfig_Contents"></a>

 ** connectInstanceId **   <a name="connect-Type-connect-outbound-campaigns_InstanceConfig-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

 ** encryptionConfig **   <a name="connect-Type-connect-outbound-campaigns_InstanceConfig-encryptionConfig"></a>
Encryption information.
Type: [EncryptionConfig](API_connect-outbound-campaigns_EncryptionConfig.md) object
Required: Yes

 ** serviceLinkedRoleArn **   <a name="connect-Type-connect-outbound-campaigns_InstanceConfig-serviceLinkedRoleArn"></a>
The The Amazon Resource Name (ARN) of the service linked role.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_connect-outbound-campaigns_InstanceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/InstanceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/InstanceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/InstanceConfig)
