---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-s3configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget S3Configuration
<a name="aws-properties-bedrockagentcore-gatewaytarget-s3configuration"></a>

The Amazon S3 configuration for a gateway. This structure defines how the gateway accesses files in Amazon S3.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-s3configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-s3configuration-syntax.json"></a>

```
{
  "[BucketOwnerAccountId](#cfn-bedrockagentcore-gatewaytarget-s3configuration-bucketowneraccountid)" : {{String}},
  "[Uri](#cfn-bedrockagentcore-gatewaytarget-s3configuration-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-s3configuration-syntax.yaml"></a>

```
  [BucketOwnerAccountId](#cfn-bedrockagentcore-gatewaytarget-s3configuration-bucketowneraccountid): {{String}}
  [Uri](#cfn-bedrockagentcore-gatewaytarget-s3configuration-uri): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-s3configuration-properties"></a>

`BucketOwnerAccountId`  <a name="cfn-bedrockagentcore-gatewaytarget-s3configuration-bucketowneraccountid"></a>
The account ID of the Amazon S3 bucket owner. This ID is used for cross-account access to the bucket.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uri`  <a name="cfn-bedrockagentcore-gatewaytarget-s3configuration-uri"></a>
The URI of the Amazon S3 object. This URI specifies the location of the object in Amazon S3.
*Required*: No
*Type*: String
*Pattern*: `^s3://.{1,2043}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
