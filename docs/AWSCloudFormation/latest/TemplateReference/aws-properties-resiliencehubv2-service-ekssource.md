---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-ekssource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service EksSource
<a name="aws-properties-resiliencehubv2-service-ekssource"></a>

Defines an Amazon EKS cluster and its namespaces as an input source for resource discovery.

## Syntax
<a name="aws-properties-resiliencehubv2-service-ekssource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-ekssource-syntax.json"></a>

```
{
  "[ClusterArn](#cfn-resiliencehubv2-service-ekssource-clusterarn)" : {{String}},
  "[Namespaces](#cfn-resiliencehubv2-service-ekssource-namespaces)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-ekssource-syntax.yaml"></a>

```
  [ClusterArn](#cfn-resiliencehubv2-service-ekssource-clusterarn): {{String}}
  [Namespaces](#cfn-resiliencehubv2-service-ekssource-namespaces): {{
    - String}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-ekssource-properties"></a>

`ClusterArn`  <a name="cfn-resiliencehubv2-service-ekssource-clusterarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespaces`  <a name="cfn-resiliencehubv2-service-ekssource-namespaces"></a>
The list of Kubernetes namespaces within the EKS cluster.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
