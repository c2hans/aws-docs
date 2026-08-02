---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-qbusiness-retriever.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Retriever
<a name="aws-resource-qbusiness-retriever"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Adds a retriever to your Amazon Q Business application.

## Syntax
<a name="aws-resource-qbusiness-retriever-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-qbusiness-retriever-syntax.json"></a>

```
{
  "Type" : "AWS::QBusiness::Retriever",
  "Properties" : {
      "[ApplicationId](#cfn-qbusiness-retriever-applicationid)" : {{String}},
      "[Configuration](#cfn-qbusiness-retriever-configuration)" : {{RetrieverConfiguration}},
      "[DisplayName](#cfn-qbusiness-retriever-displayname)" : {{String}},
      "[RoleArn](#cfn-qbusiness-retriever-rolearn)" : {{String}},
      "[Tags](#cfn-qbusiness-retriever-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-qbusiness-retriever-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-qbusiness-retriever-syntax.yaml"></a>

```
Type: AWS::QBusiness::Retriever
Properties:
  [ApplicationId](#cfn-qbusiness-retriever-applicationid): {{String}}
  [Configuration](#cfn-qbusiness-retriever-configuration): {{
    RetrieverConfiguration}}
  [DisplayName](#cfn-qbusiness-retriever-displayname): {{String}}
  [RoleArn](#cfn-qbusiness-retriever-rolearn): {{String}}
  [Tags](#cfn-qbusiness-retriever-tags): {{
    - Tag}}
  [Type](#cfn-qbusiness-retriever-type): {{String}}
```

## Properties
<a name="aws-resource-qbusiness-retriever-properties"></a>

`ApplicationId`  <a name="cfn-qbusiness-retriever-applicationid"></a>
The identifier of the Amazon Q Business application using the retriever.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-qbusiness-retriever-configuration"></a>
Provides information on how the retriever used for your Amazon Q Business application is configured.
*Required*: Yes
*Type*: [RetrieverConfiguration](aws-properties-qbusiness-retriever-retrieverconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-qbusiness-retriever-displayname"></a>
The name of your retriever.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-qbusiness-retriever-rolearn"></a>
The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-qbusiness-retriever-tags"></a>
A list of key-value pairs that identify or categorize the retriever. You can also use tags to help control access to the retriever. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
*Required*: No
*Type*: Array of [Tag](aws-properties-qbusiness-retriever-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-qbusiness-retriever-type"></a>
The type of your retriever.
*Required*: Yes
*Type*: String
*Allowed values*: `NATIVE_INDEX | KENDRA_INDEX`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-qbusiness-retriever-return-values"></a>

### Ref
<a name="aws-resource-qbusiness-retriever-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application ID and retriever ID. For example:

 `{"Ref": "ApplicationId|RetrieverId"}`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-qbusiness-retriever-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-qbusiness-retriever-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp when the retriever was created.

`RetrieverArn`  <a name="RetrieverArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the retriever.

`RetrieverId`  <a name="RetrieverId-fn::getatt"></a>
The identifier of the retriever used by your Amazon Q Business application.

`Status`  <a name="Status-fn::getatt"></a>
The status of your retriever.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The Unix timestamp when the retriever was last updated.
