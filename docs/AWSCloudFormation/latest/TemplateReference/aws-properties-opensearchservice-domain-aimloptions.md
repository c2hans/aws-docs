---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-aimloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain AIMLOptions
<a name="aws-properties-opensearchservice-domain-aimloptions"></a>

<a name="aws-properties-opensearchservice-domain-aimloptions-description"></a>The `AIMLOptions` property type specifies Property description not available. for an [AWS::OpenSearchService::Domain](aws-resource-opensearchservice-domain.md).

## Syntax
<a name="aws-properties-opensearchservice-domain-aimloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-aimloptions-syntax.json"></a>

```
{
  "[S3VectorsEngine](#cfn-opensearchservice-domain-aimloptions-s3vectorsengine)" : {{S3VectorsEngine}},
  "[ServerlessVectorAcceleration](#cfn-opensearchservice-domain-aimloptions-serverlessvectoracceleration)" : {{ServerlessVectorAcceleration}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-aimloptions-syntax.yaml"></a>

```
  [S3VectorsEngine](#cfn-opensearchservice-domain-aimloptions-s3vectorsengine): {{
    S3VectorsEngine}}
  [ServerlessVectorAcceleration](#cfn-opensearchservice-domain-aimloptions-serverlessvectoracceleration): {{
    ServerlessVectorAcceleration}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-aimloptions-properties"></a>

`S3VectorsEngine`  <a name="cfn-opensearchservice-domain-aimloptions-s3vectorsengine"></a>
Property description not available.
*Required*: No
*Type*: [S3VectorsEngine](aws-properties-opensearchservice-domain-s3vectorsengine.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerlessVectorAcceleration`  <a name="cfn-opensearchservice-domain-aimloptions-serverlessvectoracceleration"></a>
Property description not available.
*Required*: No
*Type*: [ServerlessVectorAcceleration](aws-properties-opensearchservice-domain-serverlessvectoracceleration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
