---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-zonalshiftconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ZonalShiftConfig
<a name="aws-properties-eks-cluster-zonalshiftconfig"></a>

The configuration for zonal shift for the cluster.

## Syntax
<a name="aws-properties-eks-cluster-zonalshiftconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-zonalshiftconfig-syntax.json"></a>

```
{
  "[Enabled](#cfn-eks-cluster-zonalshiftconfig-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-eks-cluster-zonalshiftconfig-syntax.yaml"></a>

```
  [Enabled](#cfn-eks-cluster-zonalshiftconfig-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-eks-cluster-zonalshiftconfig-properties"></a>

`Enabled`  <a name="cfn-eks-cluster-zonalshiftconfig-enabled"></a>
If zonal shift is enabled, AWS configures zonal autoshift for the cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
