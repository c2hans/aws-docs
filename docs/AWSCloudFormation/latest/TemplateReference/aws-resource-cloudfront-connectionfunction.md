---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-connectionfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ConnectionFunction
<a name="aws-resource-cloudfront-connectionfunction"></a>

A connection function.

## Syntax
<a name="aws-resource-cloudfront-connectionfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-connectionfunction-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::ConnectionFunction",
  "Properties" : {
      "[AutoPublish](#cfn-cloudfront-connectionfunction-autopublish)" : {{Boolean}},
      "[ConnectionFunctionCode](#cfn-cloudfront-connectionfunction-connectionfunctioncode)" : {{String}},
      "[ConnectionFunctionConfig](#cfn-cloudfront-connectionfunction-connectionfunctionconfig)" : {{ConnectionFunctionConfig}},
      "[Name](#cfn-cloudfront-connectionfunction-name)" : {{String}},
      "[Tags](#cfn-cloudfront-connectionfunction-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-connectionfunction-syntax.yaml"></a>

```
Type: AWS::CloudFront::ConnectionFunction
Properties:
  [AutoPublish](#cfn-cloudfront-connectionfunction-autopublish): {{Boolean}}
  [ConnectionFunctionCode](#cfn-cloudfront-connectionfunction-connectionfunctioncode): {{String}}
  [ConnectionFunctionConfig](#cfn-cloudfront-connectionfunction-connectionfunctionconfig): {{
    ConnectionFunctionConfig}}
  [Name](#cfn-cloudfront-connectionfunction-name): {{String}}
  [Tags](#cfn-cloudfront-connectionfunction-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudfront-connectionfunction-properties"></a>

`AutoPublish`  <a name="cfn-cloudfront-connectionfunction-autopublish"></a>
A flag that determines whether to automatically publish the function to the `LIVE` stage when it’s created. To automatically publish to the `LIVE` stage, set this property to `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionFunctionCode`  <a name="cfn-cloudfront-connectionfunction-connectionfunctioncode"></a>
The code for the connection function.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionFunctionConfig`  <a name="cfn-cloudfront-connectionfunction-connectionfunctionconfig"></a>
Contains configuration information about a CloudFront function.
*Required*: Yes
*Type*: [ConnectionFunctionConfig](aws-properties-cloudfront-connectionfunction-connectionfunctionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudfront-connectionfunction-name"></a>
The connection function name.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9-_]{1,64}`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudfront-connectionfunction-tags"></a>
A complex type that contains zero or more `Tag` elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudfront-connectionfunction-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-connectionfunction-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-connectionfunction-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudfront-connectionfunction-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudfront-connectionfunction-return-values-fn--getatt-fn--getatt"></a>

`ConnectionFunctionArn`  <a name="ConnectionFunctionArn-fn::getatt"></a>
The connection function Amazon Resource Name (ARN).

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The connection function created time.

`ETag`  <a name="ETag-fn::getatt"></a>
A complex type that contains `Tag` key and `Tag` value.

`Id`  <a name="Id-fn::getatt"></a>
The connection function ID.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The connection function last modified time.

`Stage`  <a name="Stage-fn::getatt"></a>
The connection function stage.

`Status`  <a name="Status-fn::getatt"></a>
The connection function status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
