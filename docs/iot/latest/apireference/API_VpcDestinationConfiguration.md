---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_VpcDestinationConfiguration.html
---

# VpcDestinationConfiguration
<a name="API_VpcDestinationConfiguration"></a>

The configuration information for a virtual private cloud (VPC) destination.

## Contents
<a name="API_VpcDestinationConfiguration_Contents"></a>

 ** roleArn **   <a name="iot-Type-VpcDestinationConfiguration-roleArn"></a>
The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).
Type: String
Required: Yes

 ** subnetIds **   <a name="iot-Type-VpcDestinationConfiguration-subnetIds"></a>
The subnet IDs of the VPC destination.
Type: Array of strings
Required: Yes

 ** vpcId **   <a name="iot-Type-VpcDestinationConfiguration-vpcId"></a>
The ID of the VPC.
Type: String
Required: Yes

 ** securityGroups **   <a name="iot-Type-VpcDestinationConfiguration-securityGroups"></a>
The security groups of the VPC destination.
Type: Array of strings
Required: No

## See Also
<a name="API_VpcDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/VpcDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/VpcDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/VpcDestinationConfiguration)
