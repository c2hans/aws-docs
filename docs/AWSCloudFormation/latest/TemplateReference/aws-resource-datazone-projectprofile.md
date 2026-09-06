---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-projectprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::ProjectProfile
<a name="aws-resource-datazone-projectprofile"></a>

The summary of a project profile.

## Syntax
<a name="aws-resource-datazone-projectprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-projectprofile-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::ProjectProfile",
  "Properties" : {
      "[AllowCustomProjectResourceTags](#cfn-datazone-projectprofile-allowcustomprojectresourcetags)" : {{Boolean}},
      "[Description](#cfn-datazone-projectprofile-description)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-projectprofile-domainidentifier)" : {{String}},
      "[DomainUnitIdentifier](#cfn-datazone-projectprofile-domainunitidentifier)" : {{String}},
      "[EnvironmentConfigurations](#cfn-datazone-projectprofile-environmentconfigurations)" : {{[ EnvironmentConfiguration, ... ]}},
      "[Name](#cfn-datazone-projectprofile-name)" : {{String}},
      "[ProjectResourceTags](#cfn-datazone-projectprofile-projectresourcetags)" : {{[ ResourceTagParameter, ... ]}},
      "[ProjectResourceTagsDescription](#cfn-datazone-projectprofile-projectresourcetagsdescription)" : {{String}},
      "[Status](#cfn-datazone-projectprofile-status)" : {{String}},
      "[UseDefaultConfigurations](#cfn-datazone-projectprofile-usedefaultconfigurations)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-datazone-projectprofile-syntax.yaml"></a>

```
Type: AWS::DataZone::ProjectProfile
Properties:
  [AllowCustomProjectResourceTags](#cfn-datazone-projectprofile-allowcustomprojectresourcetags): {{Boolean}}
  [Description](#cfn-datazone-projectprofile-description): {{String}}
  [DomainIdentifier](#cfn-datazone-projectprofile-domainidentifier): {{String}}
  [DomainUnitIdentifier](#cfn-datazone-projectprofile-domainunitidentifier): {{String}}
  [EnvironmentConfigurations](#cfn-datazone-projectprofile-environmentconfigurations): {{
    - EnvironmentConfiguration}}
  [Name](#cfn-datazone-projectprofile-name): {{String}}
  [ProjectResourceTags](#cfn-datazone-projectprofile-projectresourcetags): {{
    - ResourceTagParameter}}
  [ProjectResourceTagsDescription](#cfn-datazone-projectprofile-projectresourcetagsdescription): {{String}}
  [Status](#cfn-datazone-projectprofile-status): {{String}}
  [UseDefaultConfigurations](#cfn-datazone-projectprofile-usedefaultconfigurations): {{Boolean}}
```

## Properties
<a name="aws-resource-datazone-projectprofile-properties"></a>

`AllowCustomProjectResourceTags`  <a name="cfn-datazone-projectprofile-allowcustomprojectresourcetags"></a>
Specifies whether custom project resource tags are supported.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-datazone-projectprofile-description"></a>
The description of the project profile.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-projectprofile-domainidentifier"></a>
A domain ID of the project profile.
*Required*: No
*Type*: String
*Pattern*: `^dzd[_-][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainUnitIdentifier`  <a name="cfn-datazone-projectprofile-domainunitidentifier"></a>
A domain unit ID of the project profile.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9_\-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentConfigurations`  <a name="cfn-datazone-projectprofile-environmentconfigurations"></a>
Environment configurations of a project profile.
*Required*: No
*Type*: Array of [EnvironmentConfiguration](aws-properties-datazone-projectprofile-environmentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-datazone-projectprofile-name"></a>
The name of a project profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w -]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectResourceTags`  <a name="cfn-datazone-projectprofile-projectresourcetags"></a>
The resource tag of the project.
*Required*: No
*Type*: Array of [ResourceTagParameter](aws-properties-datazone-projectprofile-resourcetagparameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectResourceTagsDescription`  <a name="cfn-datazone-projectprofile-projectresourcetagsdescription"></a>
Field viewable through the UI that provides a project user with the allowed resource tag specifications.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-datazone-projectprofile-status"></a>
The status of a project profile.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseDefaultConfigurations`  <a name="cfn-datazone-projectprofile-usedefaultconfigurations"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-projectprofile-return-values"></a>

### Ref
<a name="aws-resource-datazone-projectprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and `DomainUnitId`, which uniquely identifies a domain unit. For example: { `"Ref": "MyDomainUnit"` } for the resource with the logical ID MyDomainUnit, Ref returns `DomainId|DomainUnitId`.

### Fn::GetAtt
<a name="aws-resource-datazone-projectprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-projectprofile-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the project profile was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The user who created the project profile.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The domain ID of the project profile.

`DomainUnitId`  <a name="DomainUnitId-fn::getatt"></a>
The domain unit ID of the project profile.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the project profile.

`Identifier`  <a name="Identifier-fn::getatt"></a>
Project profile ID.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp at which a project profile was last updated.
