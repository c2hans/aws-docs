---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-qbusiness-index.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Index
<a name="aws-resource-qbusiness-index"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates an Amazon Q Business index.

To determine if index creation has completed, check the `Status` field returned from a call to `DescribeIndex`. The `Status` field is set to `ACTIVE` when the index is ready to use.

Once the index is active, you can index your documents using the [`BatchPutDocument`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html) API or the [`CreateDataSource`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API.

## Syntax
<a name="aws-resource-qbusiness-index-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-qbusiness-index-syntax.json"></a>

```
{
  "Type" : "AWS::QBusiness::Index",
  "Properties" : {
      "[ApplicationId](#cfn-qbusiness-index-applicationid)" : {{String}},
      "[CapacityConfiguration](#cfn-qbusiness-index-capacityconfiguration)" : {{IndexCapacityConfiguration}},
      "[Description](#cfn-qbusiness-index-description)" : {{String}},
      "[DisplayName](#cfn-qbusiness-index-displayname)" : {{String}},
      "[DocumentAttributeConfigurations](#cfn-qbusiness-index-documentattributeconfigurations)" : {{[ DocumentAttributeConfiguration, ... ]}},
      "[Tags](#cfn-qbusiness-index-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-qbusiness-index-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-qbusiness-index-syntax.yaml"></a>

```
Type: AWS::QBusiness::Index
Properties:
  [ApplicationId](#cfn-qbusiness-index-applicationid): {{String}}
  [CapacityConfiguration](#cfn-qbusiness-index-capacityconfiguration): {{
    IndexCapacityConfiguration}}
  [Description](#cfn-qbusiness-index-description): {{String}}
  [DisplayName](#cfn-qbusiness-index-displayname): {{String}}
  [DocumentAttributeConfigurations](#cfn-qbusiness-index-documentattributeconfigurations): {{
    - DocumentAttributeConfiguration}}
  [Tags](#cfn-qbusiness-index-tags): {{
    - Tag}}
  [Type](#cfn-qbusiness-index-type): {{String}}
```

## Properties
<a name="aws-resource-qbusiness-index-properties"></a>

`ApplicationId`  <a name="cfn-qbusiness-index-applicationid"></a>
The identifier of the Amazon Q Business application using the index.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CapacityConfiguration`  <a name="cfn-qbusiness-index-capacityconfiguration"></a>
The capacity units you want to provision for your index. You can add and remove capacity to fit your usage needs.
*Required*: No
*Type*: [IndexCapacityConfiguration](aws-properties-qbusiness-index-indexcapacityconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-qbusiness-index-description"></a>
A description for the Amazon Q Business index.
*Required*: No
*Type*: String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-qbusiness-index-displayname"></a>
The name of the index.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentAttributeConfigurations`  <a name="cfn-qbusiness-index-documentattributeconfigurations"></a>
Configuration information for document attributes. Document attributes are metadata or fields associated with your documents. For example, the company department name associated with each document.
For more information, see [Understanding document attributes](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes.html).
*Required*: No
*Type*: Array of [DocumentAttributeConfiguration](aws-properties-qbusiness-index-documentattributeconfiguration.md)
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-qbusiness-index-tags"></a>
A list of key-value pairs that identify or categorize the index. You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
*Required*: No
*Type*: Array of [Tag](aws-properties-qbusiness-index-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-qbusiness-index-type"></a>
The index type that's suitable for your needs. For more information on what's included in each type of index, see [Amazon Q Business tiers](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#index-tiers).
*Required*: No
*Type*: String
*Allowed values*: `ENTERPRISE | STARTER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-qbusiness-index-return-values"></a>

### Ref
<a name="aws-resource-qbusiness-index-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application ID and index ID. For example:

 `{"Ref": "ApplicationId|IndexId"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-qbusiness-index-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-qbusiness-index-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp when the index was created.

`IndexArn`  <a name="IndexArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of an Amazon Q Business index.

`IndexId`  <a name="IndexId-fn::getatt"></a>
The identifier for the index.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the index. When the status is `ACTIVE`, the index is ready.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The Unix timestamp when the index was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
