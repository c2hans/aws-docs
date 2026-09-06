---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3outposts-endpoint-failedreason.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Outposts::Endpoint FailedReason
<a name="aws-properties-s3outposts-endpoint-failedreason"></a>

The failure reason, if any, for a create or delete endpoint operation.

## Syntax
<a name="aws-properties-s3outposts-endpoint-failedreason-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3outposts-endpoint-failedreason-syntax.json"></a>

```
{
  "[ErrorCode](#cfn-s3outposts-endpoint-failedreason-errorcode)" : {{String}},
  "[Message](#cfn-s3outposts-endpoint-failedreason-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3outposts-endpoint-failedreason-syntax.yaml"></a>

```
  [ErrorCode](#cfn-s3outposts-endpoint-failedreason-errorcode): {{String}}
  [Message](#cfn-s3outposts-endpoint-failedreason-message): {{String}}
```

## Properties
<a name="aws-properties-s3outposts-endpoint-failedreason-properties"></a>

`ErrorCode`  <a name="cfn-s3outposts-endpoint-failedreason-errorcode"></a>
The failure code, if any, for a create or delete endpoint operation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-s3outposts-endpoint-failedreason-message"></a>
Additional error details describing the endpoint failure and recommended action.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
