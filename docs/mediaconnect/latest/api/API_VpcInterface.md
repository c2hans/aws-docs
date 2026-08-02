---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_VpcInterface.html
---

# VpcInterface
<a name="API_VpcInterface"></a>

 The settings for a VPC source.

## Contents
<a name="API_VpcInterface_Contents"></a>

 ** name **   <a name="mediaconnect-Type-VpcInterface-name"></a>
 Immutable and has to be a unique against other VpcInterfaces in this Flow.
Type: String
Required: Yes

 ** networkInterfaceIds **   <a name="mediaconnect-Type-VpcInterface-networkInterfaceIds"></a>
 IDs of the network interfaces created in customer's account by MediaConnect.
Type: Array of strings
Required: Yes

 ** networkInterfaceType **   <a name="mediaconnect-Type-VpcInterface-networkInterfaceType"></a>
 The type of network interface.
Type: String
Valid Values: `ena | efa`
Required: Yes

 ** roleArn **   <a name="mediaconnect-Type-VpcInterface-roleArn"></a>
 A role Arn MediaConnect can assume to create ENIs in your account.
Type: String
Required: Yes

 ** securityGroupIds **   <a name="mediaconnect-Type-VpcInterface-securityGroupIds"></a>
 Security Group IDs to be used on ENI.
Type: Array of strings
Required: Yes

 ** subnetId **   <a name="mediaconnect-Type-VpcInterface-subnetId"></a>
 Subnet must be in the AZ of the Flow.
Type: String
Required: Yes

## See Also
<a name="API_VpcInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/VpcInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/VpcInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/VpcInterface)
