---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-publicaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster PublicAccess
<a name="aws-properties-msk-cluster-publicaccess"></a>

Broker access controls

## Syntax
<a name="aws-properties-msk-cluster-publicaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-publicaccess-syntax.json"></a>

```
{
  "[Type](#cfn-msk-cluster-publicaccess-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-cluster-publicaccess-syntax.yaml"></a>

```
  [Type](#cfn-msk-cluster-publicaccess-type): {{String}}
```

## Properties
<a name="aws-properties-msk-cluster-publicaccess-properties"></a>

`Type`  <a name="cfn-msk-cluster-publicaccess-type"></a>
DISABLED means that public access is turned off. SERVICE\_PROVIDED\_EIPS means that public access is turned on.
*Required*: No
*Type*: String
*Minimum*: `7`
*Maximum*: `23`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
