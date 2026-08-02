---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Ec2Instance.html
---

# Ec2Instance
<a name="API_Ec2Instance"></a>

Details about the potentially impacted Amazon EC2 instance resource.

## Contents
<a name="API_Ec2Instance_Contents"></a>

 ** availabilityZone **   <a name="guardduty-Type-Ec2Instance-availabilityZone"></a>
The availability zone of the Amazon EC2 instance. For more information, see [Availability zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** ec2NetworkInterfaceUids **   <a name="guardduty-Type-Ec2Instance-ec2NetworkInterfaceUids"></a>
The ID of the network interface.
Type: Array of strings
Required: No

 ** IamInstanceProfile **   <a name="guardduty-Type-Ec2Instance-IamInstanceProfile"></a>
Contains information about the EC2 instance profile.
Type: [IamInstanceProfile](API_IamInstanceProfile.md) object
Required: No

 ** imageDescription **   <a name="guardduty-Type-Ec2Instance-imageDescription"></a>
The image description of the Amazon EC2 instance.
Type: String
Required: No

 ** instanceState **   <a name="guardduty-Type-Ec2Instance-instanceState"></a>
The state of the Amazon EC2 instance. For more information, see [Amazon EC2 instance state changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** instanceType **   <a name="guardduty-Type-Ec2Instance-instanceType"></a>
Type of the Amazon EC2 instance.
Type: String
Required: No

 ** outpostArn **   <a name="guardduty-Type-Ec2Instance-outpostArn"></a>
The Amazon Resource Name (ARN) of the AWS Outpost. This shows applicable AWS Outposts instances.
Type: String
Required: No

 ** platform **   <a name="guardduty-Type-Ec2Instance-platform"></a>
The platform of the Amazon EC2 instance.
Type: String
Required: No

 ** productCodes **   <a name="guardduty-Type-Ec2Instance-productCodes"></a>
The product code of the Amazon EC2 instance.
Type: Array of [ProductCode](API_ProductCode.md) objects
Required: No

## See Also
<a name="API_Ec2Instance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Ec2Instance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Ec2Instance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Ec2Instance)
