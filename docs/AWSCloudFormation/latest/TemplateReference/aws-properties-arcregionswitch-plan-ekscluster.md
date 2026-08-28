---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-ekscluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan EksCluster
<a name="aws-properties-arcregionswitch-plan-ekscluster"></a>

The AWS EKS cluster execution block configuration.

## Syntax
<a name="aws-properties-arcregionswitch-plan-ekscluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-ekscluster-syntax.json"></a>

```
{
  "[ClusterArn](#cfn-arcregionswitch-plan-ekscluster-clusterarn)" : {{String}},
  "[CrossAccountRole](#cfn-arcregionswitch-plan-ekscluster-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-ekscluster-externalid)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-ekscluster-syntax.yaml"></a>

```
  [ClusterArn](#cfn-arcregionswitch-plan-ekscluster-clusterarn): {{String}}
  [CrossAccountRole](#cfn-arcregionswitch-plan-ekscluster-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-ekscluster-externalid): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-ekscluster-properties"></a>

`ClusterArn`  <a name="cfn-arcregionswitch-plan-ekscluster-clusterarn"></a>
The Amazon Resource Name (ARN) of an AWS EKS cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:eks:[a-z0-9-]+:\d{12}:cluster/[a-zA-Z0-9][a-zA-Z0-9-_]{0,99}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-ekscluster-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-ekscluster-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
