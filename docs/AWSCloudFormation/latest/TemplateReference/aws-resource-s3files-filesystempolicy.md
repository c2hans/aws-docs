---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3files-filesystempolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::FileSystemPolicy
<a name="aws-resource-s3files-filesystempolicy"></a>

The `AWS::S3Files::FileSystemPolicy` resource specifies a resource-based policy for an Amazon S3 Files file system. Use this resource to control access permissions for the file system.

## Syntax
<a name="aws-resource-s3files-filesystempolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3files-filesystempolicy-syntax.json"></a>

```
{
  "Type" : "AWS::S3Files::FileSystemPolicy",
  "Properties" : {
      "[FileSystemId](#cfn-s3files-filesystempolicy-filesystemid)" : {{String}},
      "[Policy](#cfn-s3files-filesystempolicy-policy)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-s3files-filesystempolicy-syntax.yaml"></a>

```
Type: AWS::S3Files::FileSystemPolicy
Properties:
  [FileSystemId](#cfn-s3files-filesystempolicy-filesystemid): {{String}}
  [Policy](#cfn-s3files-filesystempolicy-policy): {{Json}}
```

## Properties
<a name="aws-resource-s3files-filesystempolicy-properties"></a>

`FileSystemId`  <a name="cfn-s3files-filesystempolicy-filesystemid"></a>
The ID of the S3 Files file system to which the policy applies.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-s3files-filesystempolicy-policy"></a>
The JSON formatted resource-based policy for the file system.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-s3files-filesystempolicy-return-values"></a>

### Ref
<a name="aws-resource-s3files-filesystempolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the file system ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
