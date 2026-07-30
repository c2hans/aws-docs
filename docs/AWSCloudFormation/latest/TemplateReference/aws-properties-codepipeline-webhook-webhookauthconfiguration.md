---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-webhook-webhookauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Webhook WebhookAuthConfiguration
<a name="aws-properties-codepipeline-webhook-webhookauthconfiguration"></a>

The authentication applied to incoming webhook trigger requests.

## Syntax
<a name="aws-properties-codepipeline-webhook-webhookauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-webhook-webhookauthconfiguration-syntax.json"></a>

```
{
  "[AllowedIPRange](#cfn-codepipeline-webhook-webhookauthconfiguration-allowediprange)" : {{String}},
  "[SecretToken](#cfn-codepipeline-webhook-webhookauthconfiguration-secrettoken)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-webhook-webhookauthconfiguration-syntax.yaml"></a>

```
  [AllowedIPRange](#cfn-codepipeline-webhook-webhookauthconfiguration-allowediprange): {{String}}
  [SecretToken](#cfn-codepipeline-webhook-webhookauthconfiguration-secrettoken): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-webhook-webhookauthconfiguration-properties"></a>

`AllowedIPRange`  <a name="cfn-codepipeline-webhook-webhookauthconfiguration-allowediprange"></a>
The property used to configure acceptance of webhooks in an IP address range. For IP, only the `AllowedIPRange` property must be set. This property must be set to a valid CIDR range.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretToken`  <a name="cfn-codepipeline-webhook-webhookauthconfiguration-secrettoken"></a>
The property used to configure GitHub authentication. For GITHUB\_HMAC, only the `SecretToken` property must be set.
When creating CodePipeline webhooks, do not use your own credentials or reuse the same secret token across multiple webhooks. For optimal security, generate a unique secret token for each webhook you create. The secret token is an arbitrary string that you provide, which GitHub uses to compute and sign the webhook payloads sent to CodePipeline, for protecting the integrity and authenticity of the webhook payloads. Using your own credentials or reusing the same token across multiple webhooks can lead to security vulnerabilities.
If a secret token was provided, it will be redacted in the response.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
