---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-recordexpiration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket RecordExpiration
<a name="aws-properties-s3-bucket-recordexpiration"></a>

 The journal table record expiration settings for a journal table in an S3 Metadata configuration.

## Syntax
<a name="aws-properties-s3-bucket-recordexpiration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-recordexpiration-syntax.json"></a>

```
{
  "[Days](#cfn-s3-bucket-recordexpiration-days)" : {{Integer}},
  "[Expiration](#cfn-s3-bucket-recordexpiration-expiration)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-recordexpiration-syntax.yaml"></a>

```
  [Days](#cfn-s3-bucket-recordexpiration-days): {{Integer}}
  [Expiration](#cfn-s3-bucket-recordexpiration-expiration): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-recordexpiration-properties"></a>

`Days`  <a name="cfn-s3-bucket-recordexpiration-days"></a>
 If you enable journal table record expiration, you can set the number of days to retain your journal table records. Journal table records must be retained for a minimum of 7 days. To set this value, specify any whole number from `7` to `2147483647`. For example, to retain your journal table records for one year, set this value to `365`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expiration`  <a name="cfn-s3-bucket-recordexpiration-expiration"></a>
 Specifies whether journal table record expiration is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
