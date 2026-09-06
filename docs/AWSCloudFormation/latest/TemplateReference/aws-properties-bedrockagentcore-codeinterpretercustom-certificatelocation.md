---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-codeinterpretercustom-certificatelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CodeInterpreterCustom CertificateLocation
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-certificatelocation"></a>

The location from which to retrieve a certificate.

## Syntax
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-certificatelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-certificatelocation-syntax.json"></a>

```
{
  "[SecretArn](#cfn-bedrockagentcore-codeinterpretercustom-certificatelocation-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-certificatelocation-syntax.yaml"></a>

```
  [SecretArn](#cfn-bedrockagentcore-codeinterpretercustom-certificatelocation-secretarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-certificatelocation-properties"></a>

`SecretArn`  <a name="cfn-bedrockagentcore-codeinterpretercustom-certificatelocation-secretarn"></a>
The AWS Secrets Manager location of the certificate.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws(?:-cn|-us-gov|-iso(?:-[bef])?)?):secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=.@-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
