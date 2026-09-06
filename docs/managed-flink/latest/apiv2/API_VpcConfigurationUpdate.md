---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_VpcConfigurationUpdate.html
---

# VpcConfigurationUpdate
<a name="API_VpcConfigurationUpdate"></a>

Describes updates to the VPC configuration used by the application.

## Contents
<a name="API_VpcConfigurationUpdate_Contents"></a>

 ** VpcConfigurationId **   <a name="APIReference-Type-VpcConfigurationUpdate-VpcConfigurationId"></a>
Describes an update to the ID of the VPC configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** SecurityGroupIdUpdates **   <a name="APIReference-Type-VpcConfigurationUpdate-SecurityGroupIdUpdates"></a>
Describes updates to the array of [SecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html) IDs used by the VPC configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** SubnetIdUpdates **   <a name="APIReference-Type-VpcConfigurationUpdate-SubnetIdUpdates"></a>
Describes updates to the array of [Subnet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html) IDs used by the VPC configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Required: No

## See Also
<a name="API_VpcConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/VpcConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/VpcConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/VpcConfigurationUpdate)
