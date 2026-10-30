---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-integration-integrationcredential.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Integration IntegrationCredential
<a name="aws-properties-cloudwatch-integration-integrationcredential"></a>

Write-only API-key credential material for the integration. Stored encrypted and never returned on read.

## Syntax
<a name="aws-properties-cloudwatch-integration-integrationcredential-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-integration-integrationcredential-syntax.json"></a>

```
{
  "[ApiKeyCredential](#cfn-cloudwatch-integration-integrationcredential-apikeycredential)" : {{ApiKeyCredential}}
}
```

### YAML
<a name="aws-properties-cloudwatch-integration-integrationcredential-syntax.yaml"></a>

```
  [ApiKeyCredential](#cfn-cloudwatch-integration-integrationcredential-apikeycredential): {{
    ApiKeyCredential}}
```

## Properties
<a name="aws-properties-cloudwatch-integration-integrationcredential-properties"></a>

`ApiKeyCredential`  <a name="cfn-cloudwatch-integration-integrationcredential-apikeycredential"></a>
API-key credential material that can be rotated in place on update.
*Required*: Yes
*Type*: [ApiKeyCredential](aws-properties-cloudwatch-integration-apikeycredential.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
