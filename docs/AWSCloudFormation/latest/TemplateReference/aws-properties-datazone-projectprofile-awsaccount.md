---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-projectprofile-awsaccount.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::ProjectProfile AwsAccount
<a name="aws-properties-datazone-projectprofile-awsaccount"></a>

The AWS account of the environment.

## Syntax
<a name="aws-properties-datazone-projectprofile-awsaccount-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-projectprofile-awsaccount-syntax.json"></a>

```
{
  "[AwsAccountId](#cfn-datazone-projectprofile-awsaccount-awsaccountid)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-projectprofile-awsaccount-syntax.yaml"></a>

```
  [AwsAccountId](#cfn-datazone-projectprofile-awsaccount-awsaccountid): {{String}}
```

## Properties
<a name="aws-properties-datazone-projectprofile-awsaccount-properties"></a>

`AwsAccountId`  <a name="cfn-datazone-projectprofile-awsaccount-awsaccountid"></a>
The account ID of a project.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
