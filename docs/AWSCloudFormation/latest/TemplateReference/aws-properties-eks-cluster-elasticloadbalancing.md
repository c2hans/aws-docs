---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-elasticloadbalancing.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ElasticLoadBalancing
<a name="aws-properties-eks-cluster-elasticloadbalancing"></a>

Indicates the current configuration of the load balancing capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. For more information, see EKS Auto Mode load balancing capability in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-cluster-elasticloadbalancing-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-elasticloadbalancing-syntax.json"></a>

```
{
  "[Enabled](#cfn-eks-cluster-elasticloadbalancing-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-eks-cluster-elasticloadbalancing-syntax.yaml"></a>

```
  [Enabled](#cfn-eks-cluster-elasticloadbalancing-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-eks-cluster-elasticloadbalancing-properties"></a>

`Enabled`  <a name="cfn-eks-cluster-elasticloadbalancing-enabled"></a>
Indicates if the load balancing capability is enabled on your EKS Auto Mode cluster. If the load balancing capability is enabled, EKS Auto Mode will create and delete load balancers in your AWS account.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
