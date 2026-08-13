---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cassandra-type.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Type
<a name="aws-resource-cassandra-type"></a>

 The `CreateType` operation creates a new user-defined type in the specified keyspace.

To configure the required permissions, see [Permissions to create a UDT](https://docs.aws.amazon.com/keyspaces/latest/devguide/configure-udt-permissions.html#udt-permissions-create) in the *Amazon Keyspaces Developer Guide*.

For more information, see [User-defined types (UDTs)](https://docs.aws.amazon.com/keyspaces/latest/devguide/udts.html) in the *Amazon Keyspaces Developer Guide*.

## Syntax
<a name="aws-resource-cassandra-type-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cassandra-type-syntax.json"></a>

```
{
  "Type" : "AWS::Cassandra::Type",
  "Properties" : {
      "[Fields](#cfn-cassandra-type-fields)" : {{[ Field, ... ]}},
      "[KeyspaceName](#cfn-cassandra-type-keyspacename)" : {{String}},
      "[TypeName](#cfn-cassandra-type-typename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cassandra-type-syntax.yaml"></a>

```
Type: AWS::Cassandra::Type
Properties:
  [Fields](#cfn-cassandra-type-fields): {{
    - Field}}
  [KeyspaceName](#cfn-cassandra-type-keyspacename): {{String}}
  [TypeName](#cfn-cassandra-type-typename): {{String}}
```

## Properties
<a name="aws-resource-cassandra-type-properties"></a>

`Fields`  <a name="cfn-cassandra-type-fields"></a>
A list of fields that define this type.
*Required*: Yes
*Type*: Array of [Field](aws-properties-cassandra-type-field.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KeyspaceName`  <a name="cfn-cassandra-type-keyspacename"></a>
The name of the keyspace to create the type in. The keyspace must already exist.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TypeName`  <a name="cfn-cassandra-type-typename"></a>
The name of the user-defined type. UDT names must contain 48 characters or less, must begin with an alphabetic character, and can only contain alpha-numeric characters and underscores. Amazon Keyspaces converts upper case characters automatically into lower case characters. For more information, see [Create a user-defined type (UDT) in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-create-udt.html) in the *Amazon Keyspaces Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cassandra-type-return-values"></a>

### Ref
<a name="aws-resource-cassandra-type-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the type and the keyspace where the type exists (delimited by '\|'). For example:

 `{ "Ref": "myKeyspace|myType" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cassandra-type-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cassandra-type-return-values-fn--getatt-fn--getatt"></a>

`DirectParentTypes`  <a name="DirectParentTypes-fn::getatt"></a>
A list of user-defined types that use this type.

`DirectReferringTables`  <a name="DirectReferringTables-fn::getatt"></a>
A list of tables that use this type.

`KeyspaceArn`  <a name="KeyspaceArn-fn::getatt"></a>
The unique identifier of the keyspace that contains this type in the format of Amazon Resource Name (ARN)

`LastModifiedTimestamp`  <a name="LastModifiedTimestamp-fn::getatt"></a>
The last time this type was modified.

`MaxNestingDepth`  <a name="MaxNestingDepth-fn::getatt"></a>
The maximum nesting depth of this type. For more information, see [Amazon Keyspaces UDT quotas and default values](https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html#quotas-udts) in the *Amazon Keyspaces Developer Guide*.

## Examples
<a name="aws-resource-cassandra-type--examples"></a>

This section includes code examples that demonstrate how to create and use user-defined types (UDTs).

**Topics**
+ [Create a new UDT](#aws-resource-cassandra-type--examples--Create_a_new_UDT)
+ [Create a new UDT with a nested UDT](#aws-resource-cassandra-type--examples--Create_a_new_UDT_with_a_nested_UDT)
+ [Create a new table that uses UDTs](#aws-resource-cassandra-type--examples--Create_a_new_table_that_uses_UDTs)

### Create a new UDT
<a name="aws-resource-cassandra-type--examples--Create_a_new_UDT"></a>

The following example creates a new type named `my_udt`.

#### JSON
<a name="aws-resource-cassandra-type--examples--Create_a_new_UDT--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyNewKeyspaceResource": {
      "Type": "AWS::Cassandra::Keyspace",
      "Properties": {
        "KeyspaceName": "my_keyspace"
      }
    },
    "MyNewTypeResource": {
      "Type": "AWS::Cassandra::Type",
      "Properties": {
        "KeyspaceName": "my_keyspace",
        "TypeName": "my_udt",
        "Fields": [
          {
            "FieldName": "field_1",
            "FieldType": "int"
          }
        ]
      },
      "DependsOn": "MyNewKeyspaceResource"
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-type--examples--Create_a_new_UDT--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyNewKeyspaceResource:
    Type: 'AWS::Cassandra::Keyspace'
    Properties:
      KeyspaceName: my_keyspace
  MyNewTypeResource:
    Type: 'AWS::Cassandra::Type'
    Properties:
      KeyspaceName: my_keyspace
      TypeName: my_udt
      Fields:
        - FieldName: field_1
          FieldType: int
    DependsOn: "MyNewKeyspaceResource"
```

### Create a new UDT with a nested UDT
<a name="aws-resource-cassandra-type--examples--Create_a_new_UDT_with_a_nested_UDT"></a>

The following example creates a new UDT named `parent_udt` that uses the nested type `child_udt`.

#### JSON
<a name="aws-resource-cassandra-type--examples--Create_a_new_UDT_with_a_nested_UDT--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyNewKeyspaceResource": {
      "Type": "AWS::Cassandra::Keyspace",
      "Properties": {
        "KeyspaceName": "my_ks"
      }
    },
    "MyNewChildTypeResource": {
      "Type": "AWS::Cassandra::Type",
      "Properties": {
        "KeyspaceName": "my_ks",
        "TypeName": "child_udt",
        "Fields": [
          {
            "FieldName": "field_a",
            "FieldType": "int"
          }
        ]
      },
      "DependsOn": "MyNewKeyspaceResource"
    },
    "MyNewParentTypeResource": {
      "Type": "AWS::Cassandra::Type",
      "Properties": {
        "KeyspaceName": "my_ks",
        "TypeName": "parent_udt",
        "Fields": [
          {
            "FieldName": "child_type_field",
            "FieldType": "frozen<child_udt>"
          },
          {
            "FieldName": "int_field",
            "FieldType": "int"
          }
        ]
      },
      "DependsOn": ["MyNewChildTypeResource", "MyNewKeyspaceResource"]
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-type--examples--Create_a_new_UDT_with_a_nested_UDT--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyNewKeyspaceResource:
    Type: 'AWS::Cassandra::Keyspace'
    Properties:
      KeyspaceName: my_ks
  MyNewChildTypeResource:
    Type: 'AWS::Cassandra::Type'
    Properties:
      KeyspaceName: my_ks
      TypeName: child_udt
      Fields:
        - FieldName: field_a
          FieldType: int
    DependsOn: "MyNewKeyspaceResource"
  MyNewParentTypeResource:
    Type: 'AWS::Cassandra::Type'
    Properties:
      KeyspaceName: my_ks
      TypeName: parent_udt
      Fields:
        - FieldName: child_type_field
          FieldType: frozen<child_udt>
        - FieldName: int_field
          FieldType: int
    DependsOn: ["MyNewChildTypeResource", "MyNewKeyspaceResource"]
```

### Create a new table that uses UDTs
<a name="aws-resource-cassandra-type--examples--Create_a_new_table_that_uses_UDTs"></a>

The following example creates a new table called `my_table` that uses a UDT named `my_udt`.

#### JSON
<a name="aws-resource-cassandra-type--examples--Create_a_new_table_that_uses_UDTs--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyNewKeyspaceResource": {
      "Type": "AWS::Cassandra::Keyspace",
      "Properties": {
        "KeyspaceName": "my_ks"
      }
    },
    "MyNewTypeResource": {
      "Type": "AWS::Cassandra::Type",
      "Properties": {
        "KeyspaceName": "my_ks",
        "TypeName": "my_udt",
        "Fields": [
          {
            "FieldName": "field_1",
            "FieldType": "int"
          }
        ]
      },
      "DependsOn": "MyNewKeyspaceResource"
    },
    "MyNewTableResource": {
      "Type": "AWS::Cassandra::Table",
      "Properties": {
        "KeyspaceName": "my_ks",
        "TableName": "my_table",
        "PartitionKeyColumns": [
          {
            "ColumnName": "frozen_udt",
            "ColumnType": "frozen<my_udt>"
          }
        ],
        "RegularColumns": [
          {
            "ColumnName": "udt_field",
            "ColumnType": "my_udt"
          },
          {
            "ColumnName": "other_field",
            "ColumnType": "int"
          }
        ]
      },
      "DependsOn": ["MyNewTypeResource", "MyNewKeyspaceResource"]
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-type--examples--Create_a_new_table_that_uses_UDTs--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyNewKeyspaceResource:
    Type: 'AWS::Cassandra::Keyspace'
    Properties:
      KeyspaceName: my_ks
  MyNewTypeResource:
    Type: 'AWS::Cassandra::Type'
    Properties:
      KeyspaceName: my_ks
      TypeName: my_udt
      Fields:
        - FieldName: field_1
          FieldType: int
    DependsOn: "MyNewKeyspaceResource"
  MyNewTableResource:
    Type: 'AWS::Cassandra::Table'
    Properties:
      KeyspaceName: my_ks
      TableName: my_table
      PartitionKeyColumns:
        - ColumnName: frozen_udt
          ColumnType: frozen<my_udt>
      RegularColumns:
        - ColumnName: udt_field
          ColumnType: my_udt
        - ColumnName: other_field
          ColumnType: int
    DependsOn: ["MyNewTypeResource", "MyNewKeyspaceResource"]
```
