---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcs-queue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Queue
<a name="aws-resource-pcs-queue"></a>

Creates an AWS PCS queue resource. For more information, see [Creating a queue in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_queues_create.html) in the *AWS PCS User Guide*.

## Syntax
<a name="aws-resource-pcs-queue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pcs-queue-syntax.json"></a>

```
{
  "Type" : "AWS::PCS::Queue",
  "Properties" : {
      "[ClusterId](#cfn-pcs-queue-clusterid)" : {{String}},
      "[ComputeNodeGroupConfigurations](#cfn-pcs-queue-computenodegroupconfigurations)" : {{[ ComputeNodeGroupConfiguration, ... ]}},
      "[Name](#cfn-pcs-queue-name)" : {{String}},
      "[SlurmConfiguration](#cfn-pcs-queue-slurmconfiguration)" : {{SlurmConfiguration}},
      "[Tags](#cfn-pcs-queue-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-pcs-queue-syntax.yaml"></a>

```
Type: AWS::PCS::Queue
Properties:
  [ClusterId](#cfn-pcs-queue-clusterid): {{String}}
  [ComputeNodeGroupConfigurations](#cfn-pcs-queue-computenodegroupconfigurations): {{
    - ComputeNodeGroupConfiguration}}
  [Name](#cfn-pcs-queue-name): {{String}}
  [SlurmConfiguration](#cfn-pcs-queue-slurmconfiguration): {{
    SlurmConfiguration}}
  [Tags](#cfn-pcs-queue-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-pcs-queue-properties"></a>

`ClusterId`  <a name="cfn-pcs-queue-clusterid"></a>
The ID of the cluster of the queue.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComputeNodeGroupConfigurations`  <a name="cfn-pcs-queue-computenodegroupconfigurations"></a>
The list of compute node group configurations associated with the queue. Queues assign jobs to associated compute node groups.
*Required*: No
*Type*: Array of [ComputeNodeGroupConfiguration](aws-properties-pcs-queue-computenodegroupconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-pcs-queue-name"></a>
The name that identifies the queue.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SlurmConfiguration`  <a name="cfn-pcs-queue-slurmconfiguration"></a>
Additional options related to the Slurm scheduler.
*Required*: No
*Type*: [SlurmConfiguration](aws-properties-pcs-queue-slurmconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-pcs-queue-tags"></a>
1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pcs-queue-return-values"></a>

### Ref
<a name="aws-resource-pcs-queue-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-pcs-queue-return-values-fn--getatt"></a>

####
<a name="aws-resource-pcs-queue-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The unique Amazon Resource Name (ARN) of the queue.

`ErrorInfo`  <a name="ErrorInfo-fn::getatt"></a>
The list of errors that occurred during queue provisioning.

`Id`  <a name="Id-fn::getatt"></a>
The generated unique ID of the queue.

`Status`  <a name="Status-fn::getatt"></a>
The provisioning status of the queue.
The provisioning status doesn't indicate the overall health of the queue.
The resource enters the `SUSPENDING` and `SUSPENDED` states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is `SUSPENDED`. For more information, see [Frequently asked questions about Slurm versions in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html) in the *AWS PCS User Guide*.
