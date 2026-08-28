---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-flowlog-tagfieldspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FlowLog TagFieldSpecification
<a name="aws-properties-ec2-flowlog-tagfieldspecification"></a>

<a name="aws-properties-ec2-flowlog-tagfieldspecification-description"></a>The `TagFieldSpecification` property type specifies Property description not available. for an [AWS::EC2::FlowLog](aws-resource-ec2-flowlog.md).

## Syntax
<a name="aws-properties-ec2-flowlog-tagfieldspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-flowlog-tagfieldspecification-syntax.json"></a>

```
{
  "[ResourceType](#cfn-ec2-flowlog-tagfieldspecification-resourcetype)" : {{String}},
  "[TagKeys](#cfn-ec2-flowlog-tagfieldspecification-tagkeys)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-flowlog-tagfieldspecification-syntax.yaml"></a>

```
  [ResourceType](#cfn-ec2-flowlog-tagfieldspecification-resourcetype): {{String}}
  [TagKeys](#cfn-ec2-flowlog-tagfieldspecification-tagkeys): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-flowlog-tagfieldspecification-properties"></a>

`ResourceType`  <a name="cfn-ec2-flowlog-tagfieldspecification-resourcetype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TagKeys`  <a name="cfn-ec2-flowlog-tagfieldspecification-tagkeys"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
