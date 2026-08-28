---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-resourceretentionpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition ResourceRetentionPolicy
<a name="aws-properties-batch-jobdefinition-resourceretentionpolicy"></a>

Specifies the resource retention policy settings for a job definition.

## Syntax
<a name="aws-properties-batch-jobdefinition-resourceretentionpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-resourceretentionpolicy-syntax.json"></a>

```
{
  "[SkipDeregisterOnUpdate](#cfn-batch-jobdefinition-resourceretentionpolicy-skipderegisteronupdate)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-resourceretentionpolicy-syntax.yaml"></a>

```
  [SkipDeregisterOnUpdate](#cfn-batch-jobdefinition-resourceretentionpolicy-skipderegisteronupdate): {{Boolean}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-resourceretentionpolicy-properties"></a>

`SkipDeregisterOnUpdate`  <a name="cfn-batch-jobdefinition-resourceretentionpolicy-skipderegisteronupdate"></a>
Specifies whether the previous revision of the job definition is retained in an active status after UPDATE events for the resource. The default value is `false`. When the property is set to `false`, the previous revision of the job definition is de-registered after a new revision is created. When the property is set to `true`, the previous revision of the job definition is not de-registered.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
