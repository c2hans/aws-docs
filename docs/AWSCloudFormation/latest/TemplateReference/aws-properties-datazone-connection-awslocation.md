---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-awslocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection AwsLocation
<a name="aws-properties-datazone-connection-awslocation"></a>

The location of a project.

## Syntax
<a name="aws-properties-datazone-connection-awslocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-awslocation-syntax.json"></a>

```
{
  "[AccessRole](#cfn-datazone-connection-awslocation-accessrole)" : {{String}},
  "[AwsAccountId](#cfn-datazone-connection-awslocation-awsaccountid)" : {{String}},
  "[AwsRegion](#cfn-datazone-connection-awslocation-awsregion)" : {{String}},
  "[IamConnectionId](#cfn-datazone-connection-awslocation-iamconnectionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-awslocation-syntax.yaml"></a>

```
  [AccessRole](#cfn-datazone-connection-awslocation-accessrole): {{String}}
  [AwsAccountId](#cfn-datazone-connection-awslocation-awsaccountid): {{String}}
  [AwsRegion](#cfn-datazone-connection-awslocation-awsregion): {{String}}
  [IamConnectionId](#cfn-datazone-connection-awslocation-iamconnectionid): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-awslocation-properties"></a>

`AccessRole`  <a name="cfn-datazone-connection-awslocation-accessrole"></a>
The access role of a connection.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsAccountId`  <a name="cfn-datazone-connection-awslocation-awsaccountid"></a>
The account ID of a connection.
*Required*: No
*Type*: String
*Pattern*: `^\d{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsRegion`  <a name="cfn-datazone-connection-awslocation-awsregion"></a>
The Region of a connection.
*Required*: No
*Type*: String
*Pattern*: `^[a-z]{2}-[a-z]{4,10}-\d$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamConnectionId`  <a name="cfn-datazone-connection-awslocation-iamconnectionid"></a>
The IAM connection ID of a connection.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
