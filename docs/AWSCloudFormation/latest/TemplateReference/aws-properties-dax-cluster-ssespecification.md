---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dax-cluster-ssespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DAX::Cluster SSESpecification
<a name="aws-properties-dax-cluster-ssespecification"></a>

Represents the settings used to enable server-side encryption.

## Syntax
<a name="aws-properties-dax-cluster-ssespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dax-cluster-ssespecification-syntax.json"></a>

```
{
  "[SSEEnabled](#cfn-dax-cluster-ssespecification-sseenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-dax-cluster-ssespecification-syntax.yaml"></a>

```
  [SSEEnabled](#cfn-dax-cluster-ssespecification-sseenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-dax-cluster-ssespecification-properties"></a>

`SSEEnabled`  <a name="cfn-dax-cluster-ssespecification-sseenabled"></a>
Indicates whether server-side encryption is enabled (true) or disabled (false) on the cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
