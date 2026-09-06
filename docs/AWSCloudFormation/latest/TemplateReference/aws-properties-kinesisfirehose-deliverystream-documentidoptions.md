---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-documentidoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream DocumentIdOptions
<a name="aws-properties-kinesisfirehose-deliverystream-documentidoptions"></a>

Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-documentidoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-documentidoptions-syntax.json"></a>

```
{
  "[DefaultDocumentIdFormat](#cfn-kinesisfirehose-deliverystream-documentidoptions-defaultdocumentidformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-documentidoptions-syntax.yaml"></a>

```
  [DefaultDocumentIdFormat](#cfn-kinesisfirehose-deliverystream-documentidoptions-defaultdocumentidformat): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-documentidoptions-properties"></a>

`DefaultDocumentIdFormat`  <a name="cfn-kinesisfirehose-deliverystream-documentidoptions-defaultdocumentidformat"></a>
When the `FIREHOSE_DEFAULT` option is chosen, Firehose generates a unique document ID for each record based on a unique internal identifier. The generated document ID is stable across multiple delivery attempts, which helps prevent the same record from being indexed multiple times with different document IDs.
When the `NO_DOCUMENT_ID` option is chosen, Firehose does not include any document IDs in the requests it sends to the Amazon OpenSearch Service. This causes the Amazon OpenSearch Service domain to generate document IDs. In case of multiple delivery attempts, this may cause the same record to be indexed more than once with different document IDs. This option enables write-heavy operations, such as the ingestion of logs and observability data, to consume less resources in the Amazon OpenSearch Service domain, resulting in improved performance.
*Required*: Yes
*Type*: String
*Allowed values*: `FIREHOSE_DEFAULT | NO_DOCUMENT_ID`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
