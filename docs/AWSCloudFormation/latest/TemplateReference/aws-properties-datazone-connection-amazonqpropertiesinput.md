---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-amazonqpropertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection AmazonQPropertiesInput
<a name="aws-properties-datazone-connection-amazonqpropertiesinput"></a>

The Amazon Q properties of the connection.

## Syntax
<a name="aws-properties-datazone-connection-amazonqpropertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-amazonqpropertiesinput-syntax.json"></a>

```
{
  "[AuthMode](#cfn-datazone-connection-amazonqpropertiesinput-authmode)" : {{String}},
  "[IsEnabled](#cfn-datazone-connection-amazonqpropertiesinput-isenabled)" : {{Boolean}},
  "[ProfileArn](#cfn-datazone-connection-amazonqpropertiesinput-profilearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-amazonqpropertiesinput-syntax.yaml"></a>

```
  [AuthMode](#cfn-datazone-connection-amazonqpropertiesinput-authmode): {{String}}
  [IsEnabled](#cfn-datazone-connection-amazonqpropertiesinput-isenabled): {{Boolean}}
  [ProfileArn](#cfn-datazone-connection-amazonqpropertiesinput-profilearn): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-amazonqpropertiesinput-properties"></a>

`AuthMode`  <a name="cfn-datazone-connection-amazonqpropertiesinput-authmode"></a>
The authentication mode of the connection's Amazon Q properties.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsEnabled`  <a name="cfn-datazone-connection-amazonqpropertiesinput-isenabled"></a>
Specifies whether Amazon Q is enabled for the connection.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileArn`  <a name="cfn-datazone-connection-amazonqpropertiesinput-profilearn"></a>
The profile ARN of the connection's Amazon Q properties.
*Required*: No
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:[a-z0-9\-]+:[a-z0-9\-]*:[0-9]*:.*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
