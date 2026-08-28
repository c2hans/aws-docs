---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-ssespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table SSESpecification
<a name="aws-properties-dynamodb-table-ssespecification"></a>

Represents the settings used to enable server-side encryption.

## Syntax
<a name="aws-properties-dynamodb-table-ssespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-ssespecification-syntax.json"></a>

```
{
  "[KMSMasterKeyId](#cfn-dynamodb-table-ssespecification-kmsmasterkeyid)" : {{String}},
  "[SSEEnabled](#cfn-dynamodb-table-ssespecification-sseenabled)" : {{Boolean}},
  "[SSEType](#cfn-dynamodb-table-ssespecification-ssetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-ssespecification-syntax.yaml"></a>

```
  [KMSMasterKeyId](#cfn-dynamodb-table-ssespecification-kmsmasterkeyid): {{String}}
  [SSEEnabled](#cfn-dynamodb-table-ssespecification-sseenabled): {{Boolean}}
  [SSEType](#cfn-dynamodb-table-ssespecification-ssetype): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-table-ssespecification-properties"></a>

`KMSMasterKeyId`  <a name="cfn-dynamodb-table-ssespecification-kmsmasterkeyid"></a>
The AWS KMS key that should be used for the AWS KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB key `alias/aws/dynamodb`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SSEEnabled`  <a name="cfn-dynamodb-table-ssespecification-sseenabled"></a>
Indicates whether server-side encryption is done using an AWS managed key or an AWS owned key. If enabled (true), server-side encryption type is set to `KMS` and an AWS managed key is used (AWS KMS charges apply). If disabled (false) or not specified, server-side encryption is set to AWS owned key.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SSEType`  <a name="cfn-dynamodb-table-ssespecification-ssetype"></a>
Server-side encryption type. The only supported value is:
+ `KMS` - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
