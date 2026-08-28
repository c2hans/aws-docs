---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PinpointEmail::ConfigurationSetEventDestination PinpointDestination
<a name="aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination"></a>

An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.

## Syntax
<a name="aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination-syntax.json"></a>

```
{
  "[ApplicationArn](#cfn-pinpointemail-configurationseteventdestination-pinpointdestination-applicationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination-syntax.yaml"></a>

```
  [ApplicationArn](#cfn-pinpointemail-configurationseteventdestination-pinpointdestination-applicationarn): {{String}}
```

## Properties
<a name="aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination-properties"></a>

`ApplicationArn`  <a name="cfn-pinpointemail-configurationseteventdestination-pinpointdestination-applicationarn"></a>
The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
