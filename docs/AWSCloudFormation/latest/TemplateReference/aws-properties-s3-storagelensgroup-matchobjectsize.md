---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelensgroup-matchobjectsize.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLensGroup MatchObjectSize
<a name="aws-properties-s3-storagelensgroup-matchobjectsize"></a>

This resource filters objects that match the specified object size range.

## Syntax
<a name="aws-properties-s3-storagelensgroup-matchobjectsize-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelensgroup-matchobjectsize-syntax.json"></a>

```
{
  "[BytesGreaterThan](#cfn-s3-storagelensgroup-matchobjectsize-bytesgreaterthan)" : {{Integer}},
  "[BytesLessThan](#cfn-s3-storagelensgroup-matchobjectsize-byteslessthan)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3-storagelensgroup-matchobjectsize-syntax.yaml"></a>

```
  [BytesGreaterThan](#cfn-s3-storagelensgroup-matchobjectsize-bytesgreaterthan): {{Integer}}
  [BytesLessThan](#cfn-s3-storagelensgroup-matchobjectsize-byteslessthan): {{Integer}}
```

## Properties
<a name="aws-properties-s3-storagelensgroup-matchobjectsize-properties"></a>

`BytesGreaterThan`  <a name="cfn-s3-storagelensgroup-matchobjectsize-bytesgreaterthan"></a>
This property specifies the minimum object size in bytes. The value must be a positive number, greater than 0 and less than 5 TB.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BytesLessThan`  <a name="cfn-s3-storagelensgroup-matchobjectsize-byteslessthan"></a>
This property specifies the maximum object size in bytes. The value must be a positive number, greater than the minimum object size and less than 5 TB.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
