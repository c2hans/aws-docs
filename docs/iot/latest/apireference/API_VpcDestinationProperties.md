---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_VpcDestinationProperties.html
---

# VpcDestinationProperties
<a name="API_VpcDestinationProperties"></a>

The properties of a virtual private cloud (VPC) destination.

## Contents
<a name="API_VpcDestinationProperties_Contents"></a>

 ** roleArn **   <a name="iot-Type-VpcDestinationProperties-roleArn"></a>
The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).
Type: String
Required: No

 ** securityGroups **   <a name="iot-Type-VpcDestinationProperties-securityGroups"></a>
The security groups of the VPC destination.
Type: Array of strings
Required: No

 ** subnetIds **   <a name="iot-Type-VpcDestinationProperties-subnetIds"></a>
The subnet IDs of the VPC destination.
Type: Array of strings
Required: No

 ** vpcId **   <a name="iot-Type-VpcDestinationProperties-vpcId"></a>
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_VpcDestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/VpcDestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/VpcDestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/VpcDestinationProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
