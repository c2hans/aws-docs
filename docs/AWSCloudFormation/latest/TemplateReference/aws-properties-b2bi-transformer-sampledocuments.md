---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-sampledocuments.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer SampleDocuments
<a name="aws-properties-b2bi-transformer-sampledocuments"></a>

Describes a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.

## Syntax
<a name="aws-properties-b2bi-transformer-sampledocuments-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-sampledocuments-syntax.json"></a>

```
{
  "[BucketName](#cfn-b2bi-transformer-sampledocuments-bucketname)" : {{String}},
  "[Keys](#cfn-b2bi-transformer-sampledocuments-keys)" : {{[ SampleDocumentKeys, ... ]}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-sampledocuments-syntax.yaml"></a>

```
  [BucketName](#cfn-b2bi-transformer-sampledocuments-bucketname): {{String}}
  [Keys](#cfn-b2bi-transformer-sampledocuments-keys): {{
    - SampleDocumentKeys}}
```

## Properties
<a name="aws-properties-b2bi-transformer-sampledocuments-properties"></a>

`BucketName`  <a name="cfn-b2bi-transformer-sampledocuments-bucketname"></a>
Contains the Amazon S3 bucket that is used to hold your sample documents.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Keys`  <a name="cfn-b2bi-transformer-sampledocuments-keys"></a>
Contains an array of the Amazon S3 keys used to identify the location for your sample documents.
*Required*: Yes
*Type*: Array of [SampleDocumentKeys](aws-properties-b2bi-transformer-sampledocumentkeys.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
