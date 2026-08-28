---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-s3datasourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource S3DataSourceConfiguration
<a name="aws-properties-bedrock-datasource-s3datasourceconfiguration"></a>

The configuration information to connect to Amazon S3 as your data source for self-managed knowledge bases. To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html).

## Syntax
<a name="aws-properties-bedrock-datasource-s3datasourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-s3datasourceconfiguration-syntax.json"></a>

```
{
  "[BucketArn](#cfn-bedrock-datasource-s3datasourceconfiguration-bucketarn)" : {{String}},
  "[BucketOwnerAccountId](#cfn-bedrock-datasource-s3datasourceconfiguration-bucketowneraccountid)" : {{String}},
  "[InclusionPrefixes](#cfn-bedrock-datasource-s3datasourceconfiguration-inclusionprefixes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-s3datasourceconfiguration-syntax.yaml"></a>

```
  [BucketArn](#cfn-bedrock-datasource-s3datasourceconfiguration-bucketarn): {{String}}
  [BucketOwnerAccountId](#cfn-bedrock-datasource-s3datasourceconfiguration-bucketowneraccountid): {{String}}
  [InclusionPrefixes](#cfn-bedrock-datasource-s3datasourceconfiguration-inclusionprefixes): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-s3datasourceconfiguration-properties"></a>

`BucketArn`  <a name="cfn-bedrock-datasource-s3datasourceconfiguration-bucketarn"></a>
The Amazon Resource Name (ARN) of the S3 bucket that contains your data.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:s3:::[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketOwnerAccountId`  <a name="cfn-bedrock-datasource-s3datasourceconfiguration-bucketowneraccountid"></a>
The account ID for the owner of the S3 bucket.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InclusionPrefixes`  <a name="cfn-bedrock-datasource-s3datasourceconfiguration-inclusionprefixes"></a>
A list of S3 prefixes to include certain files or content. This field is an array with a maximum of one item, which can contain a string that has a maximum length of 300 characters. For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html).
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `300 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
