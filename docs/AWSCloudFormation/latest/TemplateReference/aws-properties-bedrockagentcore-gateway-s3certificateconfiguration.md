---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-s3certificateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway S3CertificateConfiguration

<a name="aws-properties-bedrockagentcore-gateway-s3certificateconfiguration-description"></a>The `S3CertificateConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Gateway](aws-resource-bedrockagentcore-gateway.md).

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-s3certificateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-s3certificateconfiguration-syntax.json"></a>

```json
{
  "[BucketOwnerAccountId](#cfn-bedrockagentcore-gateway-s3certificateconfiguration-bucketowneraccountid)" : {{String}},
  "[Uri](#cfn-bedrockagentcore-gateway-s3certificateconfiguration-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-s3certificateconfiguration-syntax.yaml"></a>

```yaml
  [BucketOwnerAccountId](#cfn-bedrockagentcore-gateway-s3certificateconfiguration-bucketowneraccountid): {{String}}
  [Uri](#cfn-bedrockagentcore-gateway-s3certificateconfiguration-uri): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-s3certificateconfiguration-properties"></a>

`BucketOwnerAccountId`  <a name="cfn-bedrockagentcore-gateway-s3certificateconfiguration-bucketowneraccountid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uri`  <a name="cfn-bedrockagentcore-gateway-s3certificateconfiguration-uri"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://.{1,2043}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
