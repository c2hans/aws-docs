---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpointpolicy-cdnauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpointPolicy CdnAuthConfiguration
<a name="aws-properties-mediapackagev2-originendpointpolicy-cdnauthconfiguration"></a>

The settings to enable CDN authorization headers in MediaPackage.

## Syntax
<a name="aws-properties-mediapackagev2-originendpointpolicy-cdnauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpointpolicy-cdnauthconfiguration-syntax.json"></a>

```
{
  "[CdnIdentifierSecretArns](#cfn-mediapackagev2-originendpointpolicy-cdnauthconfiguration-cdnidentifiersecretarns)" : {{[ String, ... ]}},
  "[SecretsRoleArn](#cfn-mediapackagev2-originendpointpolicy-cdnauthconfiguration-secretsrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpointpolicy-cdnauthconfiguration-syntax.yaml"></a>

```
  [CdnIdentifierSecretArns](#cfn-mediapackagev2-originendpointpolicy-cdnauthconfiguration-cdnidentifiersecretarns): {{
    - String}}
  [SecretsRoleArn](#cfn-mediapackagev2-originendpointpolicy-cdnauthconfiguration-secretsrolearn): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpointpolicy-cdnauthconfiguration-properties"></a>

`CdnIdentifierSecretArns`  <a name="cfn-mediapackagev2-originendpointpolicy-cdnauthconfiguration-cdnidentifiersecretarns"></a>
The ARN for the secret in Secrets Manager that your CDN uses for authorization to access the endpoint.
*Required*: Yes
*Type*: Array of String
*Minimum*: `20 | 1`
*Maximum*: `2048 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsRoleArn`  <a name="cfn-mediapackagev2-originendpointpolicy-cdnauthconfiguration-secretsrolearn"></a>
The ARN for the IAM role that gives MediaPackage read access to Secrets Manager and AWS KMS for CDN authorization.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
