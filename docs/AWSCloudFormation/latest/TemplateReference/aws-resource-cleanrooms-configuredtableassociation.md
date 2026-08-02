---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanrooms-configuredtableassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTableAssociation
<a name="aws-resource-cleanrooms-configuredtableassociation"></a>

Creates a configured table association. A configured table association links a configured table with a collaboration.

## Syntax
<a name="aws-resource-cleanrooms-configuredtableassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanrooms-configuredtableassociation-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRooms::ConfiguredTableAssociation",
  "Properties" : {
      "[ConfiguredTableAssociationAnalysisRules](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrules)" : {{[ ConfiguredTableAssociationAnalysisRule, ... ]}},
      "[ConfiguredTableIdentifier](#cfn-cleanrooms-configuredtableassociation-configuredtableidentifier)" : {{String}},
      "[Description](#cfn-cleanrooms-configuredtableassociation-description)" : {{String}},
      "[MembershipIdentifier](#cfn-cleanrooms-configuredtableassociation-membershipidentifier)" : {{String}},
      "[Name](#cfn-cleanrooms-configuredtableassociation-name)" : {{String}},
      "[RoleArn](#cfn-cleanrooms-configuredtableassociation-rolearn)" : {{String}},
      "[Tags](#cfn-cleanrooms-configuredtableassociation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanrooms-configuredtableassociation-syntax.yaml"></a>

```
Type: AWS::CleanRooms::ConfiguredTableAssociation
Properties:
  [ConfiguredTableAssociationAnalysisRules](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrules): {{
    - ConfiguredTableAssociationAnalysisRule}}
  [ConfiguredTableIdentifier](#cfn-cleanrooms-configuredtableassociation-configuredtableidentifier): {{String}}
  [Description](#cfn-cleanrooms-configuredtableassociation-description): {{String}}
  [MembershipIdentifier](#cfn-cleanrooms-configuredtableassociation-membershipidentifier): {{String}}
  [Name](#cfn-cleanrooms-configuredtableassociation-name): {{String}}
  [RoleArn](#cfn-cleanrooms-configuredtableassociation-rolearn): {{String}}
  [Tags](#cfn-cleanrooms-configuredtableassociation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanrooms-configuredtableassociation-properties"></a>

`ConfiguredTableAssociationAnalysisRules`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrules"></a>
An analysis rule for a configured table association. This analysis rule specifies how data from the table can be used within its associated collaboration. In the console, the `ConfiguredTableAssociationAnalysisRule` is referred to as the *collaboration analysis rule*.
*Required*: No
*Type*: Array of [ConfiguredTableAssociationAnalysisRule](aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfiguredTableIdentifier`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableidentifier"></a>
A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-cleanrooms-configuredtableassociation-description"></a>
A description of the configured table association.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MembershipIdentifier`  <a name="cfn-cleanrooms-configuredtableassociation-membershipidentifier"></a>
The unique ID for the membership this configured table association belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanrooms-configuredtableassociation-name"></a>
The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-cleanrooms-configuredtableassociation-rolearn"></a>
The service will assume this role to access catalog metadata and query the table.
*Required*: Yes
*Type*: String
*Minimum*: `32`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cleanrooms-configuredtableassociation-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanrooms-configuredtableassociation-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanrooms-configuredtableassociation-return-values"></a>

### Ref
<a name="aws-resource-cleanrooms-configuredtableassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `ConfiguredTableAssociation` and the ID of the Membership. For example: `c1baf760-935e-4b2d-b36e-af8daaeb6e48|81a97460-2c40-46ce-a2fd-4ccda7398b2c`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanrooms-configuredtableassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanrooms-configuredtableassociation-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the specified configured table association.
Example: `arn:aws:cleanrooms:us-east-1:111122223333:configuredtable/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`

`ConfiguredTableAssociationIdentifier`  <a name="ConfiguredTableAssociationIdentifier-fn::getatt"></a>
Returns the unique identifier of the specified configured table association.
Example: `a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`

## Examples
<a name="aws-resource-cleanrooms-configuredtableassociation--examples"></a>

### A configured table association
<a name="aws-resource-cleanrooms-configuredtableassociation--examples--A_configured_table_association"></a>

The following is an example of a configured table association which associates a configured table to a collaboration.

#### JSON
<a name="aws-resource-cleanrooms-configuredtableassociation--examples--A_configured_table_association--json"></a>

```
"ExampleAssociation": {
  "Type" : "AWS::CleanRooms::ConfiguredTableAssociation",
  "Properties" : {
    "Name" : "Example Table",
    "Description" : "Example associated configured table",
    "ConfiguredTableIdentifier" : "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "MembershipIdentifier" : "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "RoleArn" : "arn:aws:iam::123456789012:role/service-role/cleanrooms-association-example"
  }
}
```

#### YAML
<a name="aws-resource-cleanrooms-configuredtableassociation--examples--A_configured_table_association--yaml"></a>

```
ExampleAssociation:
  Type: AWS::CleanRooms::ConfiguredTableAssociation
  Properties:
    Name: Example Table
    Description: Example associated configured table
    ConfiguredTableIdentifier: a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    MembershipIdentifier: a1b2c3d4-5678-90ab-cdef-EXAMPLE33333
    RoleArn: arn:aws:iam::123456789012:role/service-role/cleanrooms-association-example
```
