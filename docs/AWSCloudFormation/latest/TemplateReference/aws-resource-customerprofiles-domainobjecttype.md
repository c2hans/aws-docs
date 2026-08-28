---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-domainobjecttype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::DomainObjectType
<a name="aws-resource-customerprofiles-domainobjecttype"></a>

<a name="aws-resource-customerprofiles-domainobjecttype-description"></a>The `AWS::CustomerProfiles::DomainObjectType` resource Property description not available. for CustomerProfiles.

## Syntax
<a name="aws-resource-customerprofiles-domainobjecttype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-domainobjecttype-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::DomainObjectType",
  "Properties" : {
      "[Description](#cfn-customerprofiles-domainobjecttype-description)" : {{String}},
      "[DomainName](#cfn-customerprofiles-domainobjecttype-domainname)" : {{String}},
      "[EncryptionKey](#cfn-customerprofiles-domainobjecttype-encryptionkey)" : {{String}},
      "[Fields](#cfn-customerprofiles-domainobjecttype-fields)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ObjectTypeName](#cfn-customerprofiles-domainobjecttype-objecttypename)" : {{String}},
      "[Tags](#cfn-customerprofiles-domainobjecttype-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-domainobjecttype-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::DomainObjectType
Properties:
  [Description](#cfn-customerprofiles-domainobjecttype-description): {{String}}
  [DomainName](#cfn-customerprofiles-domainobjecttype-domainname): {{String}}
  [EncryptionKey](#cfn-customerprofiles-domainobjecttype-encryptionkey): {{String}}
  [Fields](#cfn-customerprofiles-domainobjecttype-fields): {{
    {{Key}}: {{Value}}}}
  [ObjectTypeName](#cfn-customerprofiles-domainobjecttype-objecttypename): {{String}}
  [Tags](#cfn-customerprofiles-domainobjecttype-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-customerprofiles-domainobjecttype-properties"></a>

`Description`  <a name="cfn-customerprofiles-domainobjecttype-description"></a>
A description explaining the purpose and characteristics of this object type.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-customerprofiles-domainobjecttype-domainname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionKey`  <a name="cfn-customerprofiles-domainobjecttype-encryptionkey"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Fields`  <a name="cfn-customerprofiles-domainobjecttype-fields"></a>
Property description not available.
*Required*: Yes
*Type*: Object of [DomainObjectTypeField](aws-properties-customerprofiles-domainobjecttype-domainobjecttypefield.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ObjectTypeName`  <a name="cfn-customerprofiles-domainobjecttype-objecttypename"></a>
The name that identifies the object type within the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-customerprofiles-domainobjecttype-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-customerprofiles-domainobjecttype-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-customerprofiles-domainobjecttype-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-domainobjecttype-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-customerprofiles-domainobjecttype-return-values-fn--getatt"></a>

####
<a name="aws-resource-customerprofiles-domainobjecttype-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the domain object type was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp of when the domain object type was most recently edited.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
