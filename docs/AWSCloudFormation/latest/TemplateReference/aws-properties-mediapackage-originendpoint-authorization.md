---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackage-originendpoint-authorization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::OriginEndpoint Authorization
<a name="aws-properties-mediapackage-originendpoint-authorization"></a>

Parameters for enabling CDN authorization on the endpoint.

## Syntax
<a name="aws-properties-mediapackage-originendpoint-authorization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackage-originendpoint-authorization-syntax.json"></a>

```
{
  "[CdnIdentifierSecret](#cfn-mediapackage-originendpoint-authorization-cdnidentifiersecret)" : {{String}},
  "[SecretsRoleArn](#cfn-mediapackage-originendpoint-authorization-secretsrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackage-originendpoint-authorization-syntax.yaml"></a>

```
  [CdnIdentifierSecret](#cfn-mediapackage-originendpoint-authorization-cdnidentifiersecret): {{String}}
  [SecretsRoleArn](#cfn-mediapackage-originendpoint-authorization-secretsrolearn): {{String}}
```

## Properties
<a name="aws-properties-mediapackage-originendpoint-authorization-properties"></a>

`CdnIdentifierSecret`  <a name="cfn-mediapackage-originendpoint-authorization-cdnidentifiersecret"></a>
The Amazon Resource Name (ARN) for the secret in AWS Secrets Manager that your Content Delivery Network (CDN) uses for authorization to access your endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsRoleArn`  <a name="cfn-mediapackage-originendpoint-authorization-secretsrolearn"></a>
The Amazon Resource Name (ARN) for the IAM role that allows AWS Elemental MediaPackage to communicate with AWS Secrets Manager.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
