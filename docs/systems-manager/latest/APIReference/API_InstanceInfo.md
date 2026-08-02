---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstanceInfo.html
---

# InstanceInfo
<a name="API_InstanceInfo"></a>

Details about a specific managed node.

## Contents
<a name="API_InstanceInfo_Contents"></a>

 ** AgentType **   <a name="systemsmanager-Type-InstanceInfo-AgentType"></a>
The type of agent installed on the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** AgentVersion **   <a name="systemsmanager-Type-InstanceInfo-AgentVersion"></a>
The version number of the agent installed on the node.
Type: String
Pattern: `^[0-9]{1,6}(\.[0-9]{1,6}){2,3}$`
Required: No

 ** AvailabilityZone **   <a name="systemsmanager-Type-InstanceInfo-AvailabilityZone"></a>
The Availability Zone where the managed node is located.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** AvailabilityZoneId **   <a name="systemsmanager-Type-InstanceInfo-AvailabilityZoneId"></a>
The Availability Zone ID where the managed node is located.
Type: String
Length Constraints: Maximum length of 50.
Required: No

 ** ComputerName **   <a name="systemsmanager-Type-InstanceInfo-ComputerName"></a>
The fully qualified host name of the managed node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** InstanceStatus **   <a name="systemsmanager-Type-InstanceInfo-InstanceStatus"></a>
The current status of the managed node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** IpAddress **   <a name="systemsmanager-Type-InstanceInfo-IpAddress"></a>
The IP address of the managed node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 46.
Required: No

 ** ManagedStatus **   <a name="systemsmanager-Type-InstanceInfo-ManagedStatus"></a>
Indicates whether the node is managed by Systems Manager.
Type: String
Valid Values: `All | Managed | Unmanaged`
Required: No

 ** Name **   <a name="systemsmanager-Type-InstanceInfo-Name"></a>
The name assigned to the managed node.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** PlatformName **   <a name="systemsmanager-Type-InstanceInfo-PlatformName"></a>
The name of the operating system platform running on your managed node.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** PlatformType **   <a name="systemsmanager-Type-InstanceInfo-PlatformType"></a>
The operating system platform type of the managed node.
Type: String
Valid Values: `Windows | Linux | MacOS`
Required: No

 ** PlatformVersion **   <a name="systemsmanager-Type-InstanceInfo-PlatformVersion"></a>
The version of the OS platform running on your managed node.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** ResourceType **   <a name="systemsmanager-Type-InstanceInfo-ResourceType"></a>
The type of instance, either an EC2 instance or another supported machine type in a hybrid fleet.
Type: String
Valid Values: `ManagedInstance | EC2Instance`
Required: No

 ** SourceId **   <a name="systemsmanager-Type-InstanceInfo-SourceId"></a>
The ID of the source resource. For AWS IoT Greengrass devices, `SourceId` is the Thing name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^[a-zA-Z0-9:_-]*$`
Required: No

 ** SourceLocation **   <a name="systemsmanager-Type-InstanceInfo-SourceLocation"></a>
The location of the source resource in the third-party cloud environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^.{1,128}$`
Required: No

 ** SourceType **   <a name="systemsmanager-Type-InstanceInfo-SourceType"></a>
The type of the source resource. For AWS IoT Greengrass devices, `SourceType` is `AWS::IoT::Thing`.
Type: String
Valid Values: `AWS::EC2::Instance | AWS::IoT::Thing | AWS::SSM::ManagedInstance | Microsoft.Compute/virtualMachines`
Required: No

## See Also
<a name="API_InstanceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstanceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstanceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstanceInfo)
