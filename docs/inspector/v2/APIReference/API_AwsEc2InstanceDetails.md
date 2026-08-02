---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEc2InstanceDetails.html
---

# AwsEc2InstanceDetails
<a name="API_AwsEc2InstanceDetails"></a>

Details of the Amazon EC2 instance involved in a finding.

## Contents
<a name="API_AwsEc2InstanceDetails_Contents"></a>

 ** iamInstanceProfileArn **   <a name="inspector2-Type-AwsEc2InstanceDetails-iamInstanceProfileArn"></a>
The IAM instance profile ARN of the Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** imageId **   <a name="inspector2-Type-AwsEc2InstanceDetails-imageId"></a>
The image ID of the Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ipV4Addresses **   <a name="inspector2-Type-AwsEc2InstanceDetails-ipV4Addresses"></a>
The IPv4 addresses of the Amazon EC2 instance.
Type: Array of strings
Length Constraints: Minimum length of 7. Maximum length of 15.
Pattern: `(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])`
Required: No

 ** ipV6Addresses **   <a name="inspector2-Type-AwsEc2InstanceDetails-ipV6Addresses"></a>
The IPv6 addresses of the Amazon EC2 instance.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 47.
Required: No

 ** keyName **   <a name="inspector2-Type-AwsEc2InstanceDetails-keyName"></a>
The name of the key pair used to launch the Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** launchedAt **   <a name="inspector2-Type-AwsEc2InstanceDetails-launchedAt"></a>
The date and time the Amazon EC2 instance was launched at.
Type: Timestamp
Required: No

 ** platform **   <a name="inspector2-Type-AwsEc2InstanceDetails-platform"></a>
The platform of the Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** subnetId **   <a name="inspector2-Type-AwsEc2InstanceDetails-subnetId"></a>
The subnet ID of the Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** type **   <a name="inspector2-Type-AwsEc2InstanceDetails-type"></a>
The type of the Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** vpcId **   <a name="inspector2-Type-AwsEc2InstanceDetails-vpcId"></a>
The VPC ID of the Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_AwsEc2InstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AwsEc2InstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AwsEc2InstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AwsEc2InstanceDetails)
