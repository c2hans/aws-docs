---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-job-connectionslist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Job ConnectionsList
<a name="aws-properties-glue-job-connectionslist"></a>

Specifies the connections used by a job.

## Syntax
<a name="aws-properties-glue-job-connectionslist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-job-connectionslist-syntax.json"></a>

```
{
  "[Connections](#cfn-glue-job-connectionslist-connections)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-job-connectionslist-syntax.yaml"></a>

```
  [Connections](#cfn-glue-job-connectionslist-connections): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-job-connectionslist-properties"></a>

`Connections`  <a name="cfn-glue-job-connectionslist-connections"></a>
A list of connections used by the job.
*Required*: No
*Type*: Array of String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
