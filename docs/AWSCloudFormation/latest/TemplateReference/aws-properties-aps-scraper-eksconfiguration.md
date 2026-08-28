---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-eksconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper EksConfiguration
<a name="aws-properties-aps-scraper-eksconfiguration"></a>

The `EksConfiguration` structure describes the connection to the Amazon EKS cluster from which a scraper collects metrics.

## Syntax
<a name="aws-properties-aps-scraper-eksconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-eksconfiguration-syntax.json"></a>

```
{
  "[ClusterArn](#cfn-aps-scraper-eksconfiguration-clusterarn)" : {{String}},
  "[SecurityGroupIds](#cfn-aps-scraper-eksconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-aps-scraper-eksconfiguration-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-aps-scraper-eksconfiguration-syntax.yaml"></a>

```
  [ClusterArn](#cfn-aps-scraper-eksconfiguration-clusterarn): {{String}}
  [SecurityGroupIds](#cfn-aps-scraper-eksconfiguration-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-aps-scraper-eksconfiguration-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-aps-scraper-eksconfiguration-properties"></a>

`ClusterArn`  <a name="cfn-aps-scraper-eksconfiguration-clusterarn"></a>
ARN of the Amazon EKS cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:eks:[-a-z0-9]+:[0-9]{12}:cluster/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-aps-scraper-eksconfiguration-securitygroupids"></a>
A list of the security group IDs for the Amazon EKS cluster VPC configuration.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-aps-scraper-eksconfiguration-subnetids"></a>
A list of subnet IDs for the Amazon EKS cluster VPC configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
