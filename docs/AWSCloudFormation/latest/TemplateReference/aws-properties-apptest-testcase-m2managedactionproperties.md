---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-m2managedactionproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase M2ManagedActionProperties
<a name="aws-properties-apptest-testcase-m2managedactionproperties"></a>

Specifies the AWS Mainframe Modernization managed action properties.

## Syntax
<a name="aws-properties-apptest-testcase-m2managedactionproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-m2managedactionproperties-syntax.json"></a>

```
{
  "[ForceStop](#cfn-apptest-testcase-m2managedactionproperties-forcestop)" : {{Boolean}},
  "[ImportDataSetLocation](#cfn-apptest-testcase-m2managedactionproperties-importdatasetlocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-m2managedactionproperties-syntax.yaml"></a>

```
  [ForceStop](#cfn-apptest-testcase-m2managedactionproperties-forcestop): {{Boolean}}
  [ImportDataSetLocation](#cfn-apptest-testcase-m2managedactionproperties-importdatasetlocation): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-m2managedactionproperties-properties"></a>

`ForceStop`  <a name="cfn-apptest-testcase-m2managedactionproperties-forcestop"></a>
Force stops the AWS Mainframe Modernization managed action properties.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImportDataSetLocation`  <a name="cfn-apptest-testcase-m2managedactionproperties-importdatasetlocation"></a>
The import data set location of the AWS Mainframe Modernization managed action properties.
*Required*: No
*Type*: String
*Pattern*: `^\S{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
