---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-mqbrokeraccesscredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe MQBrokerAccessCredentials
<a name="aws-properties-pipes-pipe-mqbrokeraccesscredentials"></a>

The AWS Secrets Manager secret that stores your broker credentials.

## Syntax
<a name="aws-properties-pipes-pipe-mqbrokeraccesscredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-mqbrokeraccesscredentials-syntax.json"></a>

```
{
  "[BasicAuth](#cfn-pipes-pipe-mqbrokeraccesscredentials-basicauth)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-mqbrokeraccesscredentials-syntax.yaml"></a>

```
  [BasicAuth](#cfn-pipes-pipe-mqbrokeraccesscredentials-basicauth): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-mqbrokeraccesscredentials-properties"></a>

`BasicAuth`  <a name="cfn-pipes-pipe-mqbrokeraccesscredentials-basicauth"></a>
The ARN of the Secrets Manager secret.
*Required*: Yes
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):secret:.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
