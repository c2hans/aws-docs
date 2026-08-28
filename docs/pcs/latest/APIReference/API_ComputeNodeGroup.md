---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ComputeNodeGroup.html
---

# ComputeNodeGroup
<a name="API_ComputeNodeGroup"></a>

A compute node group associated with a cluster.

## Contents
<a name="API_ComputeNodeGroup_Contents"></a>

 ** arn **   <a name="PCS-Type-ComputeNodeGroup-arn"></a>
The unique Amazon Resource Name (ARN) of the compute node group.
Type: String
Required: Yes

 ** clusterId **   <a name="PCS-Type-ComputeNodeGroup-clusterId"></a>
The ID of the cluster of the compute node group.
Type: String
Required: Yes

 ** createdAt **   <a name="PCS-Type-ComputeNodeGroup-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** customLaunchTemplate **   <a name="PCS-Type-ComputeNodeGroup-customLaunchTemplate"></a>
An Amazon EC2 launch template AWS PCS uses to launch compute nodes.
Type: [CustomLaunchTemplate](API_CustomLaunchTemplate.md) object
Required: Yes

 ** iamInstanceProfileArn **   <a name="PCS-Type-ComputeNodeGroup-iamInstanceProfileArn"></a>
The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have the `pcs:RegisterComputeNodeGroupInstance` permission and the role name must start with `AWSPCS` or must have the path `/aws-pcs/`. For more information, see [IAM instance profiles for AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles.html) in the * AWS PCS User Guide*.
Type: String
Pattern: `arn:aws([a-zA-Z-]{0,10})?:iam::[0-9]{12}:instance-profile/([!-~]{1,510}/)?([\w+=,.@-]{1,128})`
Required: Yes

 ** id **   <a name="PCS-Type-ComputeNodeGroup-id"></a>
The generated unique ID of the compute node group.
Type: String
Required: Yes

 ** instanceConfigs **   <a name="PCS-Type-ComputeNodeGroup-instanceConfigs"></a>
A list of EC2 instance configurations that AWS PCS can provision in the compute node group.
Type: Array of [InstanceConfig](API_InstanceConfig.md) objects
Required: Yes

 ** modifiedAt **   <a name="PCS-Type-ComputeNodeGroup-modifiedAt"></a>
The date and time the resource was modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="PCS-Type-ComputeNodeGroup-name"></a>
The name that identifies the compute node group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 25.
Pattern: `(?!pcs_)^[A-Za-z][A-Za-z0-9-]+`
Required: Yes

 ** scalingConfiguration **   <a name="PCS-Type-ComputeNodeGroup-scalingConfiguration"></a>
Specifies the boundaries of the compute node group auto scaling.
Type: [ScalingConfiguration](API_ScalingConfiguration.md) object
Required: Yes

 ** status **   <a name="PCS-Type-ComputeNodeGroup-status"></a>
The provisioning status of the compute node group.
The provisioning status doesn't indicate the overall health of the compute node group.
The resource enters the `SUSPENDING` and `SUSPENDED` states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is `SUSPENDED`. For more information, see [Frequently asked questions about Slurm versions in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html) in the * AWS PCS User Guide*.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | DELETE_FAILED | UPDATE_FAILED | DELETED | SUSPENDING | SUSPENDED | RESUMING`
Required: Yes

 ** subnetIds **   <a name="PCS-Type-ComputeNodeGroup-subnetIds"></a>
The list of subnet IDs where instances are provisioned by the compute node group. The subnets must be in the same VPC as the cluster.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `subnet-\w{8,17}`
Required: Yes

 ** amiId **   <a name="PCS-Type-ComputeNodeGroup-amiId"></a>
The ID of the Amazon Machine Image (AMI) that AWS PCS uses to launch instances. If not provided, AWS PCS uses the AMI ID specified in the custom launch template.
Type: String
Pattern: `ami-[a-z0-9]+`
Required: No

 ** errorInfo **   <a name="PCS-Type-ComputeNodeGroup-errorInfo"></a>
The list of errors that occurred during compute node group provisioning.
Type: Array of [ErrorInfo](API_ErrorInfo.md) objects
Required: No

 ** nodeLifecycleActions **   <a name="PCS-Type-ComputeNodeGroup-nodeLifecycleActions"></a>
The lifecycle actions to run on compute nodes in the compute node group. Use lifecycle actions to run custom scripts at defined stages of a compute node's lifecycle, such as when a compute node finishes bootstrapping or becomes ready to accept jobs.
Type: [NodeLifecycleActions](API_NodeLifecycleActions.md) object
Required: No

 ** purchaseOption **   <a name="PCS-Type-ComputeNodeGroup-purchaseOption"></a>
Specifies how EC2 instances are purchased on your behalf. AWS PCS supports On-Demand Instances, Spot Instances, Interruptible Capacity Reservations, On-Demand Capacity Reservations, and Amazon EC2 Capacity Blocks for ML. For more information, see [Amazon EC2 billing and purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html) in the *Amazon Elastic Compute Cloud User Guide*. For more information about AWS PCS support for Capacity Blocks, see [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html) in the * AWS PCS User Guide*. For more information about AWS PCS support for interruptible capacity reservations, see [Using I-ODCRs with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-iodcr.html) in the * AWS PCS User Guide*. Choose On-Demand if you plan to use an On-Demand Capacity Reservation (ODCR). For more information, see [Using ODCRs with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html). If you don't provide this option, it defaults to On-Demand.
Type: String
Valid Values: `ONDEMAND | SPOT | CAPACITY_BLOCK | INTERRUPTIBLE_CAPACITY_RESERVATION`
Required: No

 ** slurmConfiguration **   <a name="PCS-Type-ComputeNodeGroup-slurmConfiguration"></a>
Additional options related to the Slurm scheduler.
Type: [ComputeNodeGroupSlurmConfiguration](API_ComputeNodeGroupSlurmConfiguration.md) object
Required: No

 ** spotOptions **   <a name="PCS-Type-ComputeNodeGroup-spotOptions"></a>
Additional configuration when you specify `SPOT` as the `purchaseOption` for the `CreateComputeNodeGroup` API action.
Type: [SpotOptions](API_SpotOptions.md) object
Required: No

## See Also
<a name="API_ComputeNodeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ComputeNodeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ComputeNodeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ComputeNodeGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
