---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcs-computenodegroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup
<a name="aws-resource-pcs-computenodegroup"></a>

Creates an AWS PCS compute node group resource. For more information, see [Creating a compute node group in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_cng_create.html) in the *AWS PCS User Guide*.

## Syntax
<a name="aws-resource-pcs-computenodegroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pcs-computenodegroup-syntax.json"></a>

```
{
  "Type" : "AWS::PCS::ComputeNodeGroup",
  "Properties" : {
      "[AmiId](#cfn-pcs-computenodegroup-amiid)" : {{String}},
      "[ClusterId](#cfn-pcs-computenodegroup-clusterid)" : {{String}},
      "[CustomLaunchTemplate](#cfn-pcs-computenodegroup-customlaunchtemplate)" : {{CustomLaunchTemplate}},
      "[IamInstanceProfileArn](#cfn-pcs-computenodegroup-iaminstanceprofilearn)" : {{String}},
      "[InstanceConfigs](#cfn-pcs-computenodegroup-instanceconfigs)" : {{[ InstanceConfig, ... ]}},
      "[Name](#cfn-pcs-computenodegroup-name)" : {{String}},
      "[NodeLifecycleActions](#cfn-pcs-computenodegroup-nodelifecycleactions)" : {{NodeLifecycleActions}},
      "[PurchaseOption](#cfn-pcs-computenodegroup-purchaseoption)" : {{String}},
      "[ScalingConfiguration](#cfn-pcs-computenodegroup-scalingconfiguration)" : {{ScalingConfiguration}},
      "[SlurmConfiguration](#cfn-pcs-computenodegroup-slurmconfiguration)" : {{SlurmConfiguration}},
      "[SpotOptions](#cfn-pcs-computenodegroup-spotoptions)" : {{SpotOptions}},
      "[SubnetIds](#cfn-pcs-computenodegroup-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-pcs-computenodegroup-tags)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pcs-computenodegroup-syntax.yaml"></a>

```
Type: AWS::PCS::ComputeNodeGroup
Properties:
  [AmiId](#cfn-pcs-computenodegroup-amiid): {{String}}
  [ClusterId](#cfn-pcs-computenodegroup-clusterid): {{String}}
  [CustomLaunchTemplate](#cfn-pcs-computenodegroup-customlaunchtemplate): {{
    CustomLaunchTemplate}}
  [IamInstanceProfileArn](#cfn-pcs-computenodegroup-iaminstanceprofilearn): {{String}}
  [InstanceConfigs](#cfn-pcs-computenodegroup-instanceconfigs): {{
    - InstanceConfig}}
  [Name](#cfn-pcs-computenodegroup-name): {{String}}
  [NodeLifecycleActions](#cfn-pcs-computenodegroup-nodelifecycleactions): {{
    NodeLifecycleActions}}
  [PurchaseOption](#cfn-pcs-computenodegroup-purchaseoption): {{String}}
  [ScalingConfiguration](#cfn-pcs-computenodegroup-scalingconfiguration): {{
    ScalingConfiguration}}
  [SlurmConfiguration](#cfn-pcs-computenodegroup-slurmconfiguration): {{
    SlurmConfiguration}}
  [SpotOptions](#cfn-pcs-computenodegroup-spotoptions): {{
    SpotOptions}}
  [SubnetIds](#cfn-pcs-computenodegroup-subnetids): {{
    - String}}
  [Tags](#cfn-pcs-computenodegroup-tags): {{String}}
```

## Properties
<a name="aws-resource-pcs-computenodegroup-properties"></a>

`AmiId`  <a name="cfn-pcs-computenodegroup-amiid"></a>
The ID of the Amazon Machine Image (AMI) that AWS PCS uses to launch instances. If not provided, AWS PCS uses the AMI ID specified in the custom launch template.
*Required*: No
*Type*: String
*Pattern*: `^ami-[a-z0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterId`  <a name="cfn-pcs-computenodegroup-clusterid"></a>
The ID of the cluster of the compute node group.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomLaunchTemplate`  <a name="cfn-pcs-computenodegroup-customlaunchtemplate"></a>
An Amazon EC2 launch template AWS PCS uses to launch compute nodes.
*Required*: No
*Type*: [CustomLaunchTemplate](aws-properties-pcs-computenodegroup-customlaunchtemplate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamInstanceProfileArn`  <a name="cfn-pcs-computenodegroup-iaminstanceprofilearn"></a>
The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have the `pcs:RegisterComputeNodeGroupInstance` permission and the role name must start with `AWSPCS` or must have the path `/aws-pcs/`. For more information, see [IAM instance profiles for AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles.html) in the *AWS PCS User Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws([a-zA-Z-]{0,10})?:iam::[0-9]{12}:instance-profile/.{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceConfigs`  <a name="cfn-pcs-computenodegroup-instanceconfigs"></a>
A list of EC2 instance configurations that AWS PCS can provision in the compute node group.
*Required*: Yes
*Type*: Array of [InstanceConfig](aws-properties-pcs-computenodegroup-instanceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-pcs-computenodegroup-name"></a>
The name that identifies the compute node group.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NodeLifecycleActions`  <a name="cfn-pcs-computenodegroup-nodelifecycleactions"></a>
The lifecycle actions to run on compute nodes in the compute node group. Use lifecycle actions to run custom scripts at defined stages of a compute node's lifecycle, such as when a compute node finishes bootstrapping or becomes ready to accept jobs.
*Required*: No
*Type*: [NodeLifecycleActions](aws-properties-pcs-computenodegroup-nodelifecycleactions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PurchaseOption`  <a name="cfn-pcs-computenodegroup-purchaseoption"></a>
Specifies how EC2 instances are purchased on your behalf. AWS PCS supports On-Demand Instances, Spot Instances, Interruptible Capacity Reservations, On-Demand Capacity Reservations, and Amazon EC2 Capacity Blocks for ML. For more information, see [Amazon EC2 billing and purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html) in the *Amazon Elastic Compute Cloud User Guide*. For more information about AWS PCS support for Capacity Blocks, see [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html) in the *AWS PCS User Guide*. For more information about AWS PCS support for interruptible capacity reservations, see [Using I-ODCRs with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-iodcr.html) in the *AWS PCS User Guide*. Choose On-Demand if you plan to use an On-Demand Capacity Reservation (ODCR). For more information, see [Using ODCRs with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html). If you don't provide this option, it defaults to On-Demand.
*Required*: No
*Type*: String
*Allowed values*: `ONDEMAND | SPOT | CAPACITY_BLOCK | INTERRUPTIBLE_CAPACITY_RESERVATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingConfiguration`  <a name="cfn-pcs-computenodegroup-scalingconfiguration"></a>
Specifies the boundaries of the compute node group auto scaling.
*Required*: Yes
*Type*: [ScalingConfiguration](aws-properties-pcs-computenodegroup-scalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlurmConfiguration`  <a name="cfn-pcs-computenodegroup-slurmconfiguration"></a>
Additional options related to the Slurm scheduler.
*Required*: No
*Type*: [SlurmConfiguration](aws-properties-pcs-computenodegroup-slurmconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpotOptions`  <a name="cfn-pcs-computenodegroup-spotoptions"></a>
Additional configuration when you specify `SPOT` as the `purchaseOption` for the `CreateComputeNodeGroup` API action.
*Required*: No
*Type*: [SpotOptions](aws-properties-pcs-computenodegroup-spotoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-pcs-computenodegroup-subnetids"></a>
The list of subnet IDs where instances are provisioned by the compute node group. The subnets must be in the same VPC as the cluster.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-pcs-computenodegroup-tags"></a>
1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pcs-computenodegroup-return-values"></a>

### Ref
<a name="aws-resource-pcs-computenodegroup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-pcs-computenodegroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-pcs-computenodegroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The unique Amazon Resource Name (ARN) of the compute node group.

`ErrorInfo`  <a name="ErrorInfo-fn::getatt"></a>
The list of errors that occurred during compute node group provisioning.

`Id`  <a name="Id-fn::getatt"></a>
The generated unique ID of the compute node group.

`Status`  <a name="Status-fn::getatt"></a>
The provisioning status of the compute node group.
The provisioning status doesn't indicate the overall health of the compute node group.
The resource enters the `SUSPENDING` and `SUSPENDED` states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is `SUSPENDED`. For more information, see [Frequently asked questions about Slurm versions in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html) in the *AWS PCS User Guide*.
