---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-s3vectorsengine.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain S3VectorsEngine
<a name="aws-properties-opensearchservice-domain-s3vectorsengine"></a>

Options for enabling S3 vectors engine features on the specified domain.

## Syntax
<a name="aws-properties-opensearchservice-domain-s3vectorsengine-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-s3vectorsengine-syntax.json"></a>

```
{
  "[Enabled](#cfn-opensearchservice-domain-s3vectorsengine-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-s3vectorsengine-syntax.yaml"></a>

```
  [Enabled](#cfn-opensearchservice-domain-s3vectorsengine-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-s3vectorsengine-properties"></a>

`Enabled`  <a name="cfn-opensearchservice-domain-s3vectorsengine-enabled"></a>
Enables S3 vectors engine features.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
