---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-authkey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster AuthKey
<a name="aws-properties-pcs-cluster-authkey"></a>

The shared Slurm key for authentication, also known as the **cluster secret**.

## Syntax
<a name="aws-properties-pcs-cluster-authkey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-authkey-syntax.json"></a>

```
{
  "[SecretArn](#cfn-pcs-cluster-authkey-secretarn)" : {{String}},
  "[SecretVersion](#cfn-pcs-cluster-authkey-secretversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-authkey-syntax.yaml"></a>

```
  [SecretArn](#cfn-pcs-cluster-authkey-secretarn): {{String}}
  [SecretVersion](#cfn-pcs-cluster-authkey-secretversion): {{String}}
```

## Properties
<a name="aws-properties-pcs-cluster-authkey-properties"></a>

`SecretArn`  <a name="cfn-pcs-cluster-authkey-secretarn"></a>
The Amazon Resource Name (ARN) of the shared Slurm key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretVersion`  <a name="cfn-pcs-cluster-authkey-secretversion"></a>
The version of the shared Slurm key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
