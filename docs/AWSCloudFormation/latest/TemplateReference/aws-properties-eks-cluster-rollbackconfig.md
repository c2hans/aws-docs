---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-rollbackconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster RollbackConfig
<a name="aws-properties-eks-cluster-rollbackconfig"></a>

The rollback configuration for the cluster version rollback.

## Syntax
<a name="aws-properties-eks-cluster-rollbackconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-rollbackconfig-syntax.json"></a>

```
{
  "[TimeoutMinutes](#cfn-eks-cluster-rollbackconfig-timeoutminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-eks-cluster-rollbackconfig-syntax.yaml"></a>

```
  [TimeoutMinutes](#cfn-eks-cluster-rollbackconfig-timeoutminutes): {{Integer}}
```

## Properties
<a name="aws-properties-eks-cluster-rollbackconfig-properties"></a>

`TimeoutMinutes`  <a name="cfn-eks-cluster-rollbackconfig-timeoutminutes"></a>
The length of time in minutes to wait before cancelling the update. Timeout is a minimum-bound property, meaning the timeout occurs no sooner than the time you specify, but can occur shortly thereafter. This value can be between 120 (2 hours) and 10080 (7 days). Default: `720` (12 hours) if not specified.
*Required*: No
*Type*: Integer
*Minimum*: `120`
*Maximum*: `10080`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
