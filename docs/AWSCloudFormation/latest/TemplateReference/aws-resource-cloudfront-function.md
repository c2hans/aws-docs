---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-function.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Function
<a name="aws-resource-cloudfront-function"></a>

Creates a CloudFront function.

To create a function, you provide the function code and some configuration information about the function. The response contains an Amazon Resource Name (ARN) that uniquely identifies the function, and the function’s stage.

By default, when you create a function, it’s in the `DEVELOPMENT` stage. In this stage, you can [test the function](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/test-function.html) in the CloudFront console (or with `TestFunction` in the CloudFront API).

When you’re ready to use your function with a CloudFront distribution, publish the function to the `LIVE` stage. You can do this in the CloudFront console, with `PublishFunction` in the CloudFront API, or by updating the `AWS::CloudFront::Function` resource with the `AutoPublish` property set to `true`. When the function is published to the `LIVE` stage, you can attach it to a distribution’s cache behavior, using the function’s ARN.

To automatically publish the function to the `LIVE` stage when it’s created, set the `AutoPublish` property to `true`.

## Syntax
<a name="aws-resource-cloudfront-function-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-function-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::Function",
  "Properties" : {
      "[AutoPublish](#cfn-cloudfront-function-autopublish)" : {{Boolean}},
      "[FunctionCode](#cfn-cloudfront-function-functioncode)" : {{String}},
      "[FunctionConfig](#cfn-cloudfront-function-functionconfig)" : {{FunctionConfig}},
      "[FunctionMetadata](#cfn-cloudfront-function-functionmetadata)" : {{FunctionMetadata}},
      "[Name](#cfn-cloudfront-function-name)" : {{String}},
      "[Tags](#cfn-cloudfront-function-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-function-syntax.yaml"></a>

```
Type: AWS::CloudFront::Function
Properties:
  [AutoPublish](#cfn-cloudfront-function-autopublish): {{Boolean}}
  [FunctionCode](#cfn-cloudfront-function-functioncode): {{String}}
  [FunctionConfig](#cfn-cloudfront-function-functionconfig): {{
    FunctionConfig}}
  [FunctionMetadata](#cfn-cloudfront-function-functionmetadata): {{
    FunctionMetadata}}
  [Name](#cfn-cloudfront-function-name): {{String}}
  [Tags](#cfn-cloudfront-function-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudfront-function-properties"></a>

`AutoPublish`  <a name="cfn-cloudfront-function-autopublish"></a>
A flag that determines whether to automatically publish the function to the `LIVE` stage when it’s created. To automatically publish to the `LIVE` stage, set this property to `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionCode`  <a name="cfn-cloudfront-function-functioncode"></a>
The function code. For more information about writing a CloudFront function, see [Writing function code for CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/writing-function-code.html) in the *Amazon CloudFront Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionConfig`  <a name="cfn-cloudfront-function-functionconfig"></a>
Contains configuration information about a CloudFront function.
*Required*: Yes
*Type*: [FunctionConfig](aws-properties-cloudfront-function-functionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionMetadata`  <a name="cfn-cloudfront-function-functionmetadata"></a>
Contains metadata about a CloudFront function.
*Required*: No
*Type*: [FunctionMetadata](aws-properties-cloudfront-function-functionmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudfront-function-name"></a>
A name to identify the function.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9-_]{1,64}`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudfront-function-tags"></a>
A complex type that contains zero or more `Tag` elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudfront-function-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-function-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-cloudfront-function-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudfront-function-return-values-fn--getatt-fn--getatt"></a>

`FunctionARN`  <a name="FunctionARN-fn::getatt"></a>
The ARN of the function. For example:
`arn:aws:cloudfront::123456789012:function/ExampleFunction`.
To get the function ARN, use the following syntax:
 `!GetAtt Function_Logical_ID.FunctionMetadata.FunctionARN`

`FunctionMetadata.FunctionARN`  <a name="FunctionMetadata.FunctionARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of the function. The ARN uniquely identifies the function.

## Examples
<a name="aws-resource-cloudfront-function--examples"></a>

### Create a CloudFront function
<a name="aws-resource-cloudfront-function--examples--Create_a_CloudFront_function"></a>

The following examples show how to create a basic CloudFront function.

#### YAML
<a name="aws-resource-cloudfront-function--examples--Create_a_CloudFront_function--yaml"></a>

```
Resources:
  CloudFrontFunction:
    Type: AWS::CloudFront::Function
    Properties:
      Name: MyFunctionName
      FunctionConfig:
        Comment: A basic CloudFront function
        Runtime: cloudfront-js-2.0
      FunctionCode: |
        function handler(event) {
            // NOTE: This example function is for a viewer request event trigger.
            // Choose viewer request for the event trigger when you associate this function with a distribution.
            var response = {
                statusCode: 200,
                statusDescription: 'OK',
                headers: {
                    'cloudfront-functions': { value: 'generated-by-CloudFront-Functions' }
                }
            };
            return response;
        }
      AutoPublish: true
```

#### JSON
<a name="aws-resource-cloudfront-function--examples--Create_a_CloudFront_function--json"></a>

```
{
    "Resources": {
        "CloudFrontFunction": {
            "Type": "AWS::CloudFront::Function",
            "Properties": {
                "Name": "MyFunctionNameJSON",
                "FunctionConfig": {
                    "Comment": "A basic CloudFront function",
                    "Runtime": "cloudfront-js-2.0"
                },
                "FunctionCode": "function handler(event) {\n    // NOTE: This example function is for a viewer request event trigger.\n    // Choose viewer request for the event trigger when you associate this function with a distribution.\n    var response = {\n        statusCode: 200,\n        statusDescription: 'OK',\n        headers: {\n            'cloudfront-functions': { value: 'generated-by-CloudFront-Functions' }\n        }\n    };\n    return response;\n}\n",
                "AutoPublish": true
            }
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
