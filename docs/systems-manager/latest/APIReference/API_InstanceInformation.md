---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstanceInformation.html
---

# InstanceInformation
<a name="API_InstanceInformation"></a>

Describes a filter for a specific list of managed nodes.

## Contents
<a name="API_InstanceInformation_Contents"></a>

 ** ActivationId **   <a name="systemsmanager-Type-InstanceInformation-ActivationId"></a>
The activation ID created by AWS Systems Manager when the server or virtual machine (VM) was registered.
Type: String
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** AgentVersion **   <a name="systemsmanager-Type-InstanceInformation-AgentVersion"></a>
The version of SSM Agent running on your Linux managed node.
Type: String
Pattern: `^[0-9]{1,6}(\.[0-9]{1,6}){2,3}$`
Required: No

 ** AssociationOverview **   <a name="systemsmanager-Type-InstanceInformation-AssociationOverview"></a>
Information about the association.
Type: [InstanceAggregatedAssociationOverview](API_InstanceAggregatedAssociationOverview.md) object
Required: No

 ** AssociationStatus **   <a name="systemsmanager-Type-InstanceInformation-AssociationStatus"></a>
The status of the association.
Type: String
Required: No

 ** ComputerName **   <a name="systemsmanager-Type-InstanceInformation-ComputerName"></a>
The fully qualified host name of the managed node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** IamRole **   <a name="systemsmanager-Type-InstanceInformation-IamRole"></a>
The role assigned to an Amazon EC2 instance configured with a Systems Manager Quick Setup host management configuration or the role assigned to an on-premises managed node.
 This call doesn't return the IAM role for *unmanaged* Amazon EC2 instances (instances not configured for Systems Manager). To retrieve the role for an unmanaged instance, use the Amazon EC2 `DescribeInstances` operation. For information, see [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) in the *Amazon EC2 API Reference* or [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) in the * AWS CLI Command Reference*.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** InstanceId **   <a name="systemsmanager-Type-InstanceInformation-InstanceId"></a>
The managed node ID.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** IPAddress **   <a name="systemsmanager-Type-InstanceInformation-IPAddress"></a>
The IP address of the managed node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 46.
Required: No

 ** IsLatestVersion **   <a name="systemsmanager-Type-InstanceInformation-IsLatestVersion"></a>
Indicates whether the latest version of SSM Agent is running on your Linux managed node. This field doesn't indicate whether or not the latest version is installed on Windows managed nodes, because some older versions of Windows Server use the EC2Config service to process Systems Manager requests.
Type: Boolean
Required: No

 ** LastAssociationExecutionDate **   <a name="systemsmanager-Type-InstanceInformation-LastAssociationExecutionDate"></a>
The date the association was last run.
Type: Timestamp
Required: No

 ** LastPingDateTime **   <a name="systemsmanager-Type-InstanceInformation-LastPingDateTime"></a>
The date and time when the agent last pinged the Systems Manager service.
Type: Timestamp
Required: No

 ** LastSuccessfulAssociationExecutionDate **   <a name="systemsmanager-Type-InstanceInformation-LastSuccessfulAssociationExecutionDate"></a>
The last date the association was successfully run.
Type: Timestamp
Required: No

 ** Name **   <a name="systemsmanager-Type-InstanceInformation-Name"></a>
The name assigned to an on-premises server, edge device, or virtual machine (VM) when it is activated as a Systems Manager managed node. The name is specified as the `DefaultInstanceName` property using the [CreateActivation](API_CreateActivation.md) command. It is applied to the managed node by specifying the Activation Code and Activation ID when you install SSM Agent on the node, as explained in [How to install SSM Agent on hybrid Linux nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-ssm-agent-install-linux.html) and [How to install SSM Agent on hybrid Windows Server nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-ssm-agent-install-windows.html). To retrieve the `Name` tag of an EC2 instance, use the Amazon EC2 `DescribeInstances` operation. For information, see [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) in the *Amazon EC2 API Reference* or [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) in the * AWS CLI Command Reference*.
Type: String
Required: No

 ** PingStatus **   <a name="systemsmanager-Type-InstanceInformation-PingStatus"></a>
Connection status of SSM Agent.
The status `Inactive` has been deprecated and is no longer in use.
Type: String
Valid Values: `Online | ConnectionLost | Inactive`
Required: No

 ** PlatformName **   <a name="systemsmanager-Type-InstanceInformation-PlatformName"></a>
The name of the operating system platform running on your managed node.
Type: String
Required: No

 ** PlatformType **   <a name="systemsmanager-Type-InstanceInformation-PlatformType"></a>
The operating system platform type.
Type: String
Valid Values: `Windows | Linux | MacOS`
Required: No

 ** PlatformVersion **   <a name="systemsmanager-Type-InstanceInformation-PlatformVersion"></a>
The version of the OS platform running on your managed node.
Type: String
Required: No

 ** RegistrationDate **   <a name="systemsmanager-Type-InstanceInformation-RegistrationDate"></a>
The date the server or VM was registered with AWS as a managed node.
Type: Timestamp
Required: No

 ** ResourceType **   <a name="systemsmanager-Type-InstanceInformation-ResourceType"></a>
The type of instance. Instances are either EC2 instances or managed instances.
Type: String
Valid Values: `ManagedInstance | EC2Instance`
Required: No

 ** SourceId **   <a name="systemsmanager-Type-InstanceInformation-SourceId"></a>
The ID of the source resource. For AWS IoT Greengrass devices, `SourceId` is the Thing name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^[a-zA-Z0-9:_-]*$`
Required: No

 ** SourceLocation **   <a name="systemsmanager-Type-InstanceInformation-SourceLocation"></a>
The location of the source resource in the third-party cloud environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^.{1,128}$`
Required: No

 ** SourceType **   <a name="systemsmanager-Type-InstanceInformation-SourceType"></a>
The type of the source resource. For AWS IoT Greengrass devices, `SourceType` is `AWS::IoT::Thing`. For Azure Virtual Machines, `SourceType` is `Microsoft.Compute/virtualMachines`.
Type: String
Valid Values: `AWS::EC2::Instance | AWS::IoT::Thing | AWS::SSM::ManagedInstance | Microsoft.Compute/virtualMachines`
Required: No

## See Also
<a name="API_InstanceInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstanceInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstanceInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstanceInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
