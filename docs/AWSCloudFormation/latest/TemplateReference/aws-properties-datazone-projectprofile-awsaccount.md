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
