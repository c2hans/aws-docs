---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_VpcDestinationSummary.html
---

# VpcDestinationSummary
<a name="API_VpcDestinationSummary"></a>

The summary of a virtual private cloud (VPC) destination.

## Contents
<a name="API_VpcDestinationSummary_Contents"></a>

 ** roleArn **   <a name="iot-Type-VpcDestinationSummary-roleArn"></a>
The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).
Type: String
Required: No

 ** securityGroups **   <a name="iot-Type-VpcDestinationSummary-securityGroups"></a>
The security groups of the VPC destination.
Type: Array of strings
Required: No

 ** subnetIds **   <a name="iot-Type-VpcDestinationSummary-subnetIds"></a>
The subnet IDs of the VPC destination.
Type: Array of strings
Required: No

 ** vpcId **   <a name="iot-Type-VpcDestinationSummary-vpcId"></a>
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_VpcDestinationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/VpcDestinationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/VpcDestinationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/VpcDestinationSummary)
