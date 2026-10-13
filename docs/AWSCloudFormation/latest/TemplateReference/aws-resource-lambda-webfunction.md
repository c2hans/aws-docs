---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunction
<a name="aws-resource-lambda-webfunction"></a>

The `AWS::Lambda::WebFunction` resource creates a Lambda web function. A web function is a container for revisions and endpoints. This resource creates the web function only, with no revisions and no endpoints. The web function serves no traffic until you add revisions and endpoints. To add them, use the `AWS::Lambda::WebFunctionRevision` and `AWS::Lambda::WebFunctionEndpoint` resources. In this resource's template, you can set only `FunctionName` and `Tags`.

## Syntax
<a name="aws-resource-lambda-webfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-webfunction-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::WebFunction",
  "Properties" : {
      "[FunctionName](#cfn-lambda-webfunction-functionname)" : {{String}},
      "[Tags](#cfn-lambda-webfunction-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lambda-webfunction-syntax.yaml"></a>

```
Type: AWS::Lambda::WebFunction
Properties:
  [FunctionName](#cfn-lambda-webfunction-functionname): {{String}}
  [Tags](#cfn-lambda-webfunction-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lambda-webfunction-properties"></a>

`FunctionName`  <a name="cfn-lambda-webfunction-functionname"></a>
The name of the web function. The name can contain letters, numbers, hyphens (-), and underscores (\_), and can't begin or end with a hyphen or an underscore. The name is limited to 64 characters in length.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-lambda-webfunction-tags"></a>
A list of tag key-value pairs to apply to the web function. If a tag key already exists, the new value overwrites the existing value.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-webfunction-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-webfunction-return-values"></a>

### Ref
<a name="aws-resource-lambda-webfunction-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the web function.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-webfunction-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lambda-webfunction-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time the web function was created.

`FunctionArn`  <a name="FunctionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the web function.

`State`  <a name="State-fn::getatt"></a>
The current state of the web function.

`StateReason`  <a name="StateReason-fn::getatt"></a>
The reason for the current state of the web function.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time the web function was last updated.

## Examples
<a name="aws-resource-lambda-webfunction--examples"></a>

### Web function
<a name="aws-resource-lambda-webfunction--examples--Web_function"></a>

Create a web function named `my-web-function`.

#### JSON
<a name="aws-resource-lambda-webfunction--examples--Web_function--json"></a>

```
"MyWebFunction": {
    "Type": "AWS::Lambda::WebFunction",
    "Properties": {
        "FunctionName": "my-web-function",
        "Tags": [
            {
                "Key": "Environment",
                "Value": "Production"
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-lambda-webfunction--examples--Web_function--yaml"></a>

```
MyWebFunction:
  Type: AWS::Lambda::WebFunction
  Properties:
    FunctionName: my-web-function
    Tags:
      - Key: Environment
        Value: Production
```
