---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-httpauthorization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule HttpAuthorization
<a name="aws-properties-iot-topicrule-httpauthorization"></a>

The authorization method used to send messages.

## Syntax
<a name="aws-properties-iot-topicrule-httpauthorization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-httpauthorization-syntax.json"></a>

```
{
  "[Sigv4](#cfn-iot-topicrule-httpauthorization-sigv4)" : {{SigV4Authorization}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-httpauthorization-syntax.yaml"></a>

```
  [Sigv4](#cfn-iot-topicrule-httpauthorization-sigv4): {{
    SigV4Authorization}}
```

## Properties
<a name="aws-properties-iot-topicrule-httpauthorization-properties"></a>

`Sigv4`  <a name="cfn-iot-topicrule-httpauthorization-sigv4"></a>
Use Sig V4 authorization. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).
*Required*: No
*Type*: [SigV4Authorization](aws-properties-iot-topicrule-sigv4authorization.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
