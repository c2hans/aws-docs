---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssetAttributes.html
---

# AssetAttributes
<a name="API_AssetAttributes"></a>

A collection of attributes of the host from which the finding is generated.

## Contents
<a name="API_AssetAttributes_Contents"></a>

 ** schemaVersion **   <a name="Inspector-Type-AssetAttributes-schemaVersion"></a>
The schema version of this data type.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** agentId **   <a name="Inspector-Type-AssetAttributes-agentId"></a>
The ID of the agent that is installed on the EC2 instance where the finding is generated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** amiId **   <a name="Inspector-Type-AssetAttributes-amiId"></a>
The ID of the Amazon Machine Image (AMI) that is installed on the EC2 instance where the finding is generated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** autoScalingGroup **   <a name="Inspector-Type-AssetAttributes-autoScalingGroup"></a>
The Auto Scaling group of the EC2 instance where the finding is generated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** hostname **   <a name="Inspector-Type-AssetAttributes-hostname"></a>
The hostname of the EC2 instance where the finding is generated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** ipv4Addresses **   <a name="Inspector-Type-AssetAttributes-ipv4Addresses"></a>
The list of IP v4 addresses of the EC2 instance where the finding is generated.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 7. Maximum length of 15.
Required: No

 ** networkInterfaces **   <a name="Inspector-Type-AssetAttributes-networkInterfaces"></a>
An array of the network interfaces interacting with the EC2 instance where the finding is generated.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Required: No

 ** tags **   <a name="Inspector-Type-AssetAttributes-tags"></a>
The tags related to the EC2 instance where the finding is generated.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_AssetAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssetAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssetAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssetAttributes)
