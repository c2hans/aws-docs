---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcs-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster
<a name="aws-resource-pcs-cluster"></a>

Creates an AWS PCS cluster resource. For more information, see [Creating a cluster in AWS Parallel Computing Service](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_create.html) in the *AWS PCS User Guide*.

## Syntax
<a name="aws-resource-pcs-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pcs-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::PCS::Cluster",
  "Properties" : {
      "[Name](#cfn-pcs-cluster-name)" : {{String}},
      "[Networking](#cfn-pcs-cluster-networking)" : {{Networking}},
      "[Scheduler](#cfn-pcs-cluster-scheduler)" : {{Scheduler}},
      "[Size](#cfn-pcs-cluster-size)" : {{String}},
      "[SlurmConfiguration](#cfn-pcs-cluster-slurmconfiguration)" : {{SlurmConfiguration}},
      "[Tags](#cfn-pcs-cluster-tags)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pcs-cluster-syntax.yaml"></a>

```
Type: AWS::PCS::Cluster
Properties:
  [Name](#cfn-pcs-cluster-name): {{String}}
  [Networking](#cfn-pcs-cluster-networking): {{
    Networking}}
  [Scheduler](#cfn-pcs-cluster-scheduler): {{
    Scheduler}}
  [Size](#cfn-pcs-cluster-size): {{String}}
  [SlurmConfiguration](#cfn-pcs-cluster-slurmconfiguration): {{
    SlurmConfiguration}}
  [Tags](#cfn-pcs-cluster-tags): {{String}}
```

## Properties
<a name="aws-resource-pcs-cluster-properties"></a>

`Name`  <a name="cfn-pcs-cluster-name"></a>
The name that identifies the cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Networking`  <a name="cfn-pcs-cluster-networking"></a>
The networking configuration for the cluster's control plane.
*Required*: Yes
*Type*: [Networking](aws-properties-pcs-cluster-networking.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scheduler`  <a name="cfn-pcs-cluster-scheduler"></a>
The cluster management and job scheduling software associated with the cluster.
*Required*: Yes
*Type*: [Scheduler](aws-properties-pcs-cluster-scheduler.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Size`  <a name="cfn-pcs-cluster-size"></a>
The size of the cluster.
+ `SMALL`: 32 compute nodes and 256 jobs
+ `MEDIUM`: 512 compute nodes and 8192 jobs
+ `LARGE`: 2048 compute nodes and 16,384 jobs
*Required*: Yes
*Type*: String
*Allowed values*: `SMALL | MEDIUM | LARGE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SlurmConfiguration`  <a name="cfn-pcs-cluster-slurmconfiguration"></a>
Additional options related to the Slurm scheduler.
*Required*: No
*Type*: [SlurmConfiguration](aws-properties-pcs-cluster-slurmconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-pcs-cluster-tags"></a>
1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-pcs-cluster-return-values"></a>

### Ref
<a name="aws-resource-pcs-cluster-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-pcs-cluster-return-values-fn--getatt"></a>

####
<a name="aws-resource-pcs-cluster-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The unique Amazon Resource Name (ARN) of the cluster.

`Endpoints`  <a name="Endpoints-fn::getatt"></a>
The list of endpoints available for interaction with the scheduler.

`ErrorInfo`  <a name="ErrorInfo-fn::getatt"></a>
The list of errors that occurred during cluster provisioning.

`Id`  <a name="Id-fn::getatt"></a>
The generated unique ID of the cluster.

`Status`  <a name="Status-fn::getatt"></a>
The provisioning status of the cluster.
The provisioning status doesn't indicate the overall health of the cluster.
The resource enters the `SUSPENDING` and `SUSPENDED` states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is `SUSPENDED`. For more information, see [Frequently asked questions about Slurm versions in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html) in the *AWS PCS User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
