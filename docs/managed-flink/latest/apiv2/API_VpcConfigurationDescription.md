---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_VpcConfigurationDescription.html
---

# VpcConfigurationDescription
<a name="API_VpcConfigurationDescription"></a>

Describes the parameters of a VPC used by the application.

## Contents
<a name="API_VpcConfigurationDescription_Contents"></a>

 ** SecurityGroupIds **   <a name="APIReference-Type-VpcConfigurationDescription-SecurityGroupIds"></a>
The array of [SecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html) IDs used by the VPC configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** SubnetIds **   <a name="APIReference-Type-VpcConfigurationDescription-SubnetIds"></a>
The array of [Subnet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html) IDs used by the VPC configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Required: Yes

 ** VpcConfigurationId **   <a name="APIReference-Type-VpcConfigurationDescription-VpcConfigurationId"></a>
The ID of the VPC configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** VpcId **   <a name="APIReference-Type-VpcConfigurationDescription-VpcId"></a>
The ID of the associated VPC.
Type: String
Required: Yes

## See Also
<a name="API_VpcConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/VpcConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/VpcConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/VpcConfigurationDescription)
