---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-sigv4authorization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule SigV4Authorization
<a name="aws-properties-iot-topicrule-sigv4authorization"></a>

For more information, see [Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Syntax
<a name="aws-properties-iot-topicrule-sigv4authorization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-sigv4authorization-syntax.json"></a>

```
{
  "[RoleArn](#cfn-iot-topicrule-sigv4authorization-rolearn)" : {{String}},
  "[ServiceName](#cfn-iot-topicrule-sigv4authorization-servicename)" : {{String}},
  "[SigningRegion](#cfn-iot-topicrule-sigv4authorization-signingregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-sigv4authorization-syntax.yaml"></a>

```
  [RoleArn](#cfn-iot-topicrule-sigv4authorization-rolearn): {{String}}
  [ServiceName](#cfn-iot-topicrule-sigv4authorization-servicename): {{String}}
  [SigningRegion](#cfn-iot-topicrule-sigv4authorization-signingregion): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-sigv4authorization-properties"></a>

`RoleArn`  <a name="cfn-iot-topicrule-sigv4authorization-rolearn"></a>
The ARN of the signing role.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceName`  <a name="cfn-iot-topicrule-sigv4authorization-servicename"></a>
The service name to use while signing with Sig V4.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SigningRegion`  <a name="cfn-iot-topicrule-sigv4authorization-signingregion"></a>
The signing region.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
