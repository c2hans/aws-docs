---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-serverlessvectoracceleration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain ServerlessVectorAcceleration
<a name="aws-properties-opensearchservice-domain-serverlessvectoracceleration"></a>

Configuration for serverless vector acceleration, which provides [GPU-accelerated](https://docs.aws.amazon.com//opensearch-service/latest/developerguide/gpu-acceleration-vector-index.html) vector search capabilities for improved performance on vector workloads.

## Syntax
<a name="aws-properties-opensearchservice-domain-serverlessvectoracceleration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-serverlessvectoracceleration-syntax.json"></a>

```
{
  "[Enabled](#cfn-opensearchservice-domain-serverlessvectoracceleration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-serverlessvectoracceleration-syntax.yaml"></a>

```
  [Enabled](#cfn-opensearchservice-domain-serverlessvectoracceleration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-serverlessvectoracceleration-properties"></a>

`Enabled`  <a name="cfn-opensearchservice-domain-serverlessvectoracceleration-enabled"></a>
Specifies whether serverless vector acceleration is enabled for the domain.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
