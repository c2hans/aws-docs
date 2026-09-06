---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-session-connectionslist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Session ConnectionsList
<a name="aws-properties-glue-session-connectionslist"></a>

Specifies the connections used by a job.

## Syntax
<a name="aws-properties-glue-session-connectionslist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-session-connectionslist-syntax.json"></a>

```
{
  "[Connections](#cfn-glue-session-connectionslist-connections)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-session-connectionslist-syntax.yaml"></a>

```
  [Connections](#cfn-glue-session-connectionslist-connections): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-session-connectionslist-properties"></a>

`Connections`  <a name="cfn-glue-session-connectionslist-connections"></a>
A list of connections used by the job.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `255 | 1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
