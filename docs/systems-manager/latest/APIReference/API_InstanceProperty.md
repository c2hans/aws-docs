---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstanceProperty.html
---

# InstanceProperty
<a name="API_InstanceProperty"></a>

An object containing various properties of a managed node.

## Contents
<a name="API_InstanceProperty_Contents"></a>

 ** ActivationId **   <a name="systemsmanager-Type-InstanceProperty-ActivationId"></a>
The activation ID created by Systems Manager when the server or virtual machine (VM) was registered
Type: String
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** AgentVersion **   <a name="systemsmanager-Type-InstanceProperty-AgentVersion"></a>
The version of SSM Agent running on your managed node.
Type: String
Pattern: `^[0-9]{1,6}(\.[0-9]{1,6}){2,3}$`
Required: No

 ** Architecture **   <a name="systemsmanager-Type-InstanceProperty-Architecture"></a>
The CPU architecture of the node. For example, `x86_64`.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** AssociationOverview **   <a name="systemsmanager-Type-InstanceProperty-AssociationOverview"></a>
Status information about the aggregated associations.
Type: [InstanceAggregatedAssociationOverview](API_InstanceAggregatedAssociationOverview.md) object
Required: No

 ** AssociationStatus **   <a name="systemsmanager-Type-InstanceProperty-AssociationStatus"></a>
The status of the State Manager association applied to the managed node.
Type: String
Required: No

 ** AvailabilityZone **   <a name="systemsmanager-Type-InstanceProperty-AvailabilityZone"></a>
The Availability Zone where the managed node is located.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** ComputerName **   <a name="systemsmanager-Type-InstanceProperty-ComputerName"></a>
The fully qualified host name of the managed node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** IamRole **   <a name="systemsmanager-Type-InstanceProperty-IamRole"></a>
The IAM role used in the hybrid activation to register the node with Systems Manager.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** InstanceId **   <a name="systemsmanager-Type-InstanceProperty-InstanceId"></a>
The ID of the managed node.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** InstanceRole **   <a name="systemsmanager-Type-InstanceProperty-InstanceRole"></a>
The instance profile attached to the node. If an instance profile isn't attached to the node, this value is blank.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** InstanceState **   <a name="systemsmanager-Type-InstanceProperty-InstanceState"></a>
The current state of the node.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** InstanceType **   <a name="systemsmanager-Type-InstanceProperty-InstanceType"></a>
The instance type of the managed node. For example, t3.large.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** IPAddress **   <a name="systemsmanager-Type-InstanceProperty-IPAddress"></a>
The public IPv4 address assigned to the node. If a public IPv4 address isn't assigned to the node, this value is blank.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 46.
Required: No

 ** KeyName **   <a name="systemsmanager-Type-InstanceProperty-KeyName"></a>
The name of the key pair associated with the node. If a key pair isnt't associated with the node, this value is blank.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** LastAssociationExecutionDate **   <a name="systemsmanager-Type-InstanceProperty-LastAssociationExecutionDate"></a>
The date the association was last run.
Type: Timestamp
Required: No

 ** LastPingDateTime **   <a name="systemsmanager-Type-InstanceProperty-LastPingDateTime"></a>
The date and time when the SSM Agent last pinged the Systems Manager service.
Type: Timestamp
Required: No

 ** LastSuccessfulAssociationExecutionDate **   <a name="systemsmanager-Type-InstanceProperty-LastSuccessfulAssociationExecutionDate"></a>
The last date the association was successfully run.
Type: Timestamp
Required: No

 ** LaunchTime **   <a name="systemsmanager-Type-InstanceProperty-LaunchTime"></a>
The timestamp for when the node was launched.
Type: Timestamp
Required: No

 ** Name **   <a name="systemsmanager-Type-InstanceProperty-Name"></a>
The value of the EC2 `Name` tag associated with the node. If a `Name` tag hasn't been applied to the node, this value is blank.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** PingStatus **   <a name="systemsmanager-Type-InstanceProperty-PingStatus"></a>
Connection status of the SSM Agent on the managed node.
Type: String
Valid Values: `Online | ConnectionLost | Inactive`
Required: No

 ** PlatformName **   <a name="systemsmanager-Type-InstanceProperty-PlatformName"></a>
The name of the operating system platform running on your managed node.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** PlatformType **   <a name="systemsmanager-Type-InstanceProperty-PlatformType"></a>
The operating system platform type of the managed node. For example, Windows Server or Amazon Linux 2.
Type: String
Valid Values: `Windows | Linux | MacOS`
Required: No

 ** PlatformVersion **   <a name="systemsmanager-Type-InstanceProperty-PlatformVersion"></a>
The version of the OS platform running on your managed node.
Type: String
Length Constraints: Maximum length of 120.
Required: No

 ** RegistrationDate **   <a name="systemsmanager-Type-InstanceProperty-RegistrationDate"></a>
The date the node was registered with Systems Manager.
Type: Timestamp
Required: No

 ** ResourceType **   <a name="systemsmanager-Type-InstanceProperty-ResourceType"></a>
The type of managed node.
Type: String
Required: No

 ** SourceId **   <a name="systemsmanager-Type-InstanceProperty-SourceId"></a>
The ID of the source resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^[a-zA-Z0-9:_-]*$`
Required: No

 ** SourceLocation **   <a name="systemsmanager-Type-InstanceProperty-SourceLocation"></a>
The location of the source resource in the third-party cloud environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^.{1,128}$`
Required: No

 ** SourceType **   <a name="systemsmanager-Type-InstanceProperty-SourceType"></a>
The type of the source resource. Valid values: `AWS::EC2::Instance` \| `AWS::SSM::ManagedInstance` \| `AWS::IoT::Thing` \| `Microsoft.Compute/virtualMachines`.
Type: String
Valid Values: `AWS::EC2::Instance | AWS::IoT::Thing | AWS::SSM::ManagedInstance | Microsoft.Compute/virtualMachines`
Required: No

## See Also
<a name="API_InstanceProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstanceProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstanceProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstanceProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
