---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3outposts-bucket-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Outposts::Bucket Rule
<a name="aws-properties-s3outposts-bucket-rule"></a>

A container for an Amazon S3 on Outposts bucket lifecycle rule.

## Syntax
<a name="aws-properties-s3outposts-bucket-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3outposts-bucket-rule-syntax.json"></a>

```
{
  "[AbortIncompleteMultipartUpload](#cfn-s3outposts-bucket-rule-abortincompletemultipartupload)" : {{AbortIncompleteMultipartUpload}},
  "[ExpirationDate](#cfn-s3outposts-bucket-rule-expirationdate)" : {{String}},
  "[ExpirationInDays](#cfn-s3outposts-bucket-rule-expirationindays)" : {{Integer}},
  "[Filter](#cfn-s3outposts-bucket-rule-filter)" : {{Filter}},
  "[Id](#cfn-s3outposts-bucket-rule-id)" : {{String}},
  "[Status](#cfn-s3outposts-bucket-rule-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3outposts-bucket-rule-syntax.yaml"></a>

```
  [AbortIncompleteMultipartUpload](#cfn-s3outposts-bucket-rule-abortincompletemultipartupload): {{
    AbortIncompleteMultipartUpload}}
  [ExpirationDate](#cfn-s3outposts-bucket-rule-expirationdate): {{String}}
  [ExpirationInDays](#cfn-s3outposts-bucket-rule-expirationindays): {{Integer}}
  [Filter](#cfn-s3outposts-bucket-rule-filter): {{
    Filter}}
  [Id](#cfn-s3outposts-bucket-rule-id): {{String}}
  [Status](#cfn-s3outposts-bucket-rule-status): {{String}}
```

## Properties
<a name="aws-properties-s3outposts-bucket-rule-properties"></a>

`AbortIncompleteMultipartUpload`  <a name="cfn-s3outposts-bucket-rule-abortincompletemultipartupload"></a>
The container for the abort incomplete multipart upload rule.
*Required*: No
*Type*: [AbortIncompleteMultipartUpload](aws-properties-s3outposts-bucket-abortincompletemultipartupload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExpirationDate`  <a name="cfn-s3outposts-bucket-rule-expirationdate"></a>
Specifies the expiration for the lifecycle of the object by specifying an expiry date.
*Required*: No
*Type*: String
*Pattern*: `^([0-2]\d{3})-(0[0-9]|1[0-2])-([0-2]\d|3[01])T([01]\d|2[0-4]):([0-5]\d):([0-6]\d)((\.\d{3})?)Z$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExpirationInDays`  <a name="cfn-s3outposts-bucket-rule-expirationindays"></a>
Specifies the expiration for the lifecycle of the object in the form of days that the object has been in the S3 on Outposts bucket.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Filter`  <a name="cfn-s3outposts-bucket-rule-filter"></a>
The container for the filter of the lifecycle rule.
*Required*: No
*Type*: [Filter](aws-properties-s3outposts-bucket-filter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-s3outposts-bucket-rule-id"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-s3outposts-bucket-rule-status"></a>
If `Enabled`, the rule is currently being applied. If `Disabled`, the rule is not currently being applied.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
