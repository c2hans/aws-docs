---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationEc2Instance.html
---

# InvestigationEc2Instance
<a name="API_InvestigationEc2Instance"></a>

Contains details about an Amazon EC2 instance.

## Contents
<a name="API_InvestigationEc2Instance_Contents"></a>

 ** availabilityZone **   <a name="guardduty-Type-InvestigationEc2Instance-availabilityZone"></a>
The Availability Zone of the instance.
Type: String
Required: No

 ** imageId **   <a name="guardduty-Type-InvestigationEc2Instance-imageId"></a>
The ID of the Amazon Machine Image (AMI) that was used to launch the instance.
Type: String
Required: No

 ** instanceId **   <a name="guardduty-Type-InvestigationEc2Instance-instanceId"></a>
The ID of the instance.
Type: String
Required: No

 ** instanceState **   <a name="guardduty-Type-InvestigationEc2Instance-instanceState"></a>
The state of the instance.
Type: String
Required: No

 ** instanceType **   <a name="guardduty-Type-InvestigationEc2Instance-instanceType"></a>
The instance type.
Type: String
Required: No

 ** launchedAt **   <a name="guardduty-Type-InvestigationEc2Instance-launchedAt"></a>
The timestamp at which the instance was launched.
Type: Timestamp
Required: No

 ** privateIpAddress **   <a name="guardduty-Type-InvestigationEc2Instance-privateIpAddress"></a>
The private IP address of the instance.
Type: String
Required: No

 ** publicIp **   <a name="guardduty-Type-InvestigationEc2Instance-publicIp"></a>
The public IP address of the instance.
Type: String
Required: No

 ** subnetId **   <a name="guardduty-Type-InvestigationEc2Instance-subnetId"></a>
The ID of the subnet in which the instance runs.
Type: String
Required: No

 ** vpcId **   <a name="guardduty-Type-InvestigationEc2Instance-vpcId"></a>
The ID of the VPC in which the instance runs.
Type: String
Required: No

## See Also
<a name="API_InvestigationEc2Instance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationEc2Instance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationEc2Instance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationEc2Instance)
