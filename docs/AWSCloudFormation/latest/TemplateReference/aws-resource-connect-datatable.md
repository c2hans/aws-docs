---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-datatable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::DataTable
<a name="aws-resource-connect-datatable"></a>

Represents a data table in Amazon Connect. A data table is a JSON-like data structure where attributes and values are dynamically set by customers. Customers can reference table values within call flows, applications, views, and workspaces to pinpoint dynamic configuration that changes their contact center's behavior in a predetermined and safe way.

## Syntax
<a name="aws-resource-connect-datatable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-datatable-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::DataTable",
  "Properties" : {
      "[Description](#cfn-connect-datatable-description)" : {{String}},
      "[InstanceArn](#cfn-connect-datatable-instancearn)" : {{String}},
      "[Name](#cfn-connect-datatable-name)" : {{String}},
      "[Status](#cfn-connect-datatable-status)" : {{String}},
      "[Tags](#cfn-connect-datatable-tags)" : {{[ Tag, ... ]}},
      "[TimeZone](#cfn-connect-datatable-timezone)" : {{String}},
      "[ValueLockLevel](#cfn-connect-datatable-valuelocklevel)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-datatable-syntax.yaml"></a>

```
Type: AWS::Connect::DataTable
Properties:
  [Description](#cfn-connect-datatable-description): {{String}}
  [InstanceArn](#cfn-connect-datatable-instancearn): {{String}}
  [Name](#cfn-connect-datatable-name): {{String}}
  [Status](#cfn-connect-datatable-status): {{String}}
  [Tags](#cfn-connect-datatable-tags): {{
    - Tag}}
  [TimeZone](#cfn-connect-datatable-timezone): {{String}}
  [ValueLockLevel](#cfn-connect-datatable-valuelocklevel): {{String}}
```

## Properties
<a name="aws-resource-connect-datatable-properties"></a>

`Description`  <a name="cfn-connect-datatable-description"></a>
An optional description of the data table's purpose and contents.
*Required*: No
*Type*: String
*Pattern*: `^[\P{C} ]+$`
*Minimum*: `0`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-datatable-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-connect-datatable-name"></a>
The human-readable name of the data table. Must be unique within the instance and conform to Connect naming standards.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-connect-datatable-status"></a>
The current status of the data table. One of PUBLISHED or SAVED.
*Required*: Yes
*Type*: String
*Allowed values*: `PUBLISHED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-connect-datatable-tags"></a>
Key-value pairs for attribute based access control (TBAC or ABAC) and organization.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-datatable-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeZone`  <a name="cfn-connect-datatable-timezone"></a>
The IANA timezone identifier used when resolving time based dynamic values. Required even if no time slices are specified.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueLockLevel`  <a name="cfn-connect-datatable-valuelocklevel"></a>
The data level that concurrent value edits are locked on. One of DATA\_TABLE, PRIMARY\_VALUE, ATTRIBUTE, VALUE, and NONE. Determines how concurrent edits are handled when multiple users attempt to modify values simultaneously.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | DATA_TABLE | PRIMARY_VALUE | ATTRIBUTE | VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-datatable-return-values"></a>

### Ref
<a name="aws-resource-connect-datatable-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-datatable-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-datatable-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the data table. Does not include version aliases.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The timestamp when the data table was created.

`LastModifiedRegion`  <a name="LastModifiedRegion-fn::getatt"></a>
The AWS Region where the data table was last modified, used for region replication.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The timestamp when the data table or any of its properties were last modified.
