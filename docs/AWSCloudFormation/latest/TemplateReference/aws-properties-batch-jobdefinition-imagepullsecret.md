---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-imagepullsecret.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition ImagePullSecret
<a name="aws-properties-batch-jobdefinition-imagepullsecret"></a>

References a Kubernetes secret resource. This name of the secret must start and end with an alphanumeric character, is required to be lowercase, can include periods (.) and hyphens (-), and can't contain more than 253 characters.

## Syntax
<a name="aws-properties-batch-jobdefinition-imagepullsecret-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-imagepullsecret-syntax.json"></a>

```
{
  "[Name](#cfn-batch-jobdefinition-imagepullsecret-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-imagepullsecret-syntax.yaml"></a>

```
  [Name](#cfn-batch-jobdefinition-imagepullsecret-name): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-imagepullsecret-properties"></a>

`Name`  <a name="cfn-batch-jobdefinition-imagepullsecret-name"></a>
Provides a unique identifier for the `ImagePullSecret`. This object is required when `EksPodProperties$imagePullSecrets` is used.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
