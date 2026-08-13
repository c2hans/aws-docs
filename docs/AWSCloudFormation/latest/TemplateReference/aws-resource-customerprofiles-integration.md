---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration
<a name="aws-resource-customerprofiles-integration"></a>

Specifies an Amazon Connect Customer Profiles Integration.

## Syntax
<a name="aws-resource-customerprofiles-integration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-integration-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::Integration",
  "Properties" : {
      "[DomainName](#cfn-customerprofiles-integration-domainname)" : {{String}},
      "[EventTriggerNames](#cfn-customerprofiles-integration-eventtriggernames)" : {{[ String, ... ]}},
      "[FlowDefinition](#cfn-customerprofiles-integration-flowdefinition)" : {{FlowDefinition}},
      "[ObjectTypeName](#cfn-customerprofiles-integration-objecttypename)" : {{String}},
      "[ObjectTypeNames](#cfn-customerprofiles-integration-objecttypenames)" : {{[ ObjectTypeMapping, ... ]}},
      "[Scope](#cfn-customerprofiles-integration-scope)" : {{String}},
      "[Tags](#cfn-customerprofiles-integration-tags)" : {{[ Tag, ... ]}},
      "[Uri](#cfn-customerprofiles-integration-uri)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-integration-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::Integration
Properties:
  [DomainName](#cfn-customerprofiles-integration-domainname): {{String}}
  [EventTriggerNames](#cfn-customerprofiles-integration-eventtriggernames): {{
    - String}}
  [FlowDefinition](#cfn-customerprofiles-integration-flowdefinition): {{
    FlowDefinition}}
  [ObjectTypeName](#cfn-customerprofiles-integration-objecttypename): {{String}}
  [ObjectTypeNames](#cfn-customerprofiles-integration-objecttypenames): {{
    - ObjectTypeMapping}}
  [Scope](#cfn-customerprofiles-integration-scope): {{String}}
  [Tags](#cfn-customerprofiles-integration-tags): {{
    - Tag}}
  [Uri](#cfn-customerprofiles-integration-uri): {{String}}
```

## Properties
<a name="aws-resource-customerprofiles-integration-properties"></a>

`DomainName`  <a name="cfn-customerprofiles-integration-domainname"></a>
The unique name of the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventTriggerNames`  <a name="cfn-customerprofiles-integration-eventtriggernames"></a>
A list of unique names for active event triggers associated with the integration.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `64 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowDefinition`  <a name="cfn-customerprofiles-integration-flowdefinition"></a>
The configuration that controls how Customer Profiles retrieves data from the source.
*Required*: No
*Type*: [FlowDefinition](aws-properties-customerprofiles-integration-flowdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectTypeName`  <a name="cfn-customerprofiles-integration-objecttypename"></a>
The name of the profile object type mapping to use.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectTypeNames`  <a name="cfn-customerprofiles-integration-objecttypenames"></a>
The object type mapping.
*Required*: No
*Type*: Array of [ObjectTypeMapping](aws-properties-customerprofiles-integration-objecttypemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-customerprofiles-integration-scope"></a>
The scope or boundary of the integration item's applicability.
*Required*: No
*Type*: String
*Allowed values*: `PROFILE | DOMAIN`
*Pattern*: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-customerprofiles-integration-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-customerprofiles-integration-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uri`  <a name="cfn-customerprofiles-integration-uri"></a>
The URI of the S3 bucket or any other type of data source.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-customerprofiles-integration-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-integration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the DomainName and the Uri of the integration.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-customerprofiles-integration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-customerprofiles-integration-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the integration was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp of when the integration was most recently edited.

## Examples
<a name="aws-resource-customerprofiles-integration--examples"></a>

The following example creates an integration if Domain existed.

###
<a name="aws-resource-customerprofiles-integration--examples--"></a>

#### YAML
<a name="aws-resource-customerprofiles-integration--examples----yaml"></a>

```
Type: "AWS::CustomerProfiles::Integration"
Properties:
    DomainName: "ExampleDomain"
    ObjectTypeName: "CTR"
    Uri: "arn:aws:connect:us-east-1:123456789012:instance/11111111-1111-1111-1111-111111111111"
```

#### JSON
<a name="aws-resource-customerprofiles-integration--examples----json"></a>

```
"Type": "AWS::CustomerProfiles::Integration",
"Properties": {
    "DomainName": "ExampleDomain",
    "ObjectTypeName": "CTR",
    "Uri": "arn:aws:connect:us-east-1:123456789012:instance/11111111-1111-1111-1111-111111111111" } } }
}
```
