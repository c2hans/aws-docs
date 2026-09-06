---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InstanceDetails.html
---

# InstanceDetails
<a name="API_InstanceDetails"></a>

Contains information about the details of an instance.

## Contents
<a name="API_InstanceDetails_Contents"></a>

 ** availabilityZone **   <a name="guardduty-Type-InstanceDetails-availabilityZone"></a>
The Availability Zone of the EC2 instance.
Type: String
Required: No

 ** iamInstanceProfile **   <a name="guardduty-Type-InstanceDetails-iamInstanceProfile"></a>
The profile information of the EC2 instance.
Type: [IamInstanceProfile](API_IamInstanceProfile.md) object
Required: No

 ** imageDescription **   <a name="guardduty-Type-InstanceDetails-imageDescription"></a>
The image description of the EC2 instance.
Type: String
Required: No

 ** imageId **   <a name="guardduty-Type-InstanceDetails-imageId"></a>
The image ID of the EC2 instance.
Type: String
Required: No

 ** instanceId **   <a name="guardduty-Type-InstanceDetails-instanceId"></a>
The ID of the EC2 instance.
Type: String
Required: No

 ** instanceState **   <a name="guardduty-Type-InstanceDetails-instanceState"></a>
The state of the EC2 instance.
Type: String
Required: No

 ** instanceType **   <a name="guardduty-Type-InstanceDetails-instanceType"></a>
The type of the EC2 instance.
Type: String
Required: No

 ** launchTime **   <a name="guardduty-Type-InstanceDetails-launchTime"></a>
The launch time of the EC2 instance.
Type: String
Required: No

 ** networkInterfaces **   <a name="guardduty-Type-InstanceDetails-networkInterfaces"></a>
The elastic network interface information of the EC2 instance.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Required: No

 ** outpostArn **   <a name="guardduty-Type-InstanceDetails-outpostArn"></a>
The Amazon Resource Name (ARN) of the AWS Outpost. Only applicable to AWS Outposts instances.
Type: String
Required: No

 ** platform **   <a name="guardduty-Type-InstanceDetails-platform"></a>
The platform of the EC2 instance.
Type: String
Required: No

 ** productCodes **   <a name="guardduty-Type-InstanceDetails-productCodes"></a>
The product code of the EC2 instance.
Type: Array of [ProductCode](API_ProductCode.md) objects
Required: No

 ** tags **   <a name="guardduty-Type-InstanceDetails-tags"></a>
The tags of the EC2 instance.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_InstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InstanceDetails)
