---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-project.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Project
<a name="aws-resource-datazone-project"></a>

The `AWS::DataZone::Project`resource specifies an Amazon DataZone project. Projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data in the Amazon DataZone catalog. Project members consume assets from the Amazon DataZone catalog and produce new assets using one or more analytical workflows.

## Syntax
<a name="aws-resource-datazone-project-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-project-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::Project",
  "Properties" : {
      "[Description](#cfn-datazone-project-description)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-project-domainidentifier)" : {{String}},
      "[DomainUnitId](#cfn-datazone-project-domainunitid)" : {{String}},
      "[GlossaryTerms](#cfn-datazone-project-glossaryterms)" : {{[ String, ... ]}},
      "[MembershipAssignments](#cfn-datazone-project-membershipassignments)" : {{[ ProjectMembershipAssignment, ... ]}},
      "[Name](#cfn-datazone-project-name)" : {{String}},
      "[ProjectCategory](#cfn-datazone-project-projectcategory)" : {{String}},
      "[ProjectExecutionRole](#cfn-datazone-project-projectexecutionrole)" : {{String}},
      "[ProjectProfileId](#cfn-datazone-project-projectprofileid)" : {{String}},
      "[ProjectProfileVersion](#cfn-datazone-project-projectprofileversion)" : {{String}},
      "[ResourceTags](#cfn-datazone-project-resourcetags)" : {{[ ResourceTag, ... ]}},
      "[UserParameters](#cfn-datazone-project-userparameters)" : {{[ EnvironmentConfigurationUserParameter, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datazone-project-syntax.yaml"></a>

```
Type: AWS::DataZone::Project
Properties:
  [Description](#cfn-datazone-project-description): {{String}}
  [DomainIdentifier](#cfn-datazone-project-domainidentifier): {{String}}
  [DomainUnitId](#cfn-datazone-project-domainunitid): {{String}}
  [GlossaryTerms](#cfn-datazone-project-glossaryterms): {{
    - String}}
  [MembershipAssignments](#cfn-datazone-project-membershipassignments): {{
    - ProjectMembershipAssignment}}
  [Name](#cfn-datazone-project-name): {{String}}
  [ProjectCategory](#cfn-datazone-project-projectcategory): {{String}}
  [ProjectExecutionRole](#cfn-datazone-project-projectexecutionrole): {{String}}
  [ProjectProfileId](#cfn-datazone-project-projectprofileid): {{String}}
  [ProjectProfileVersion](#cfn-datazone-project-projectprofileversion): {{String}}
  [ResourceTags](#cfn-datazone-project-resourcetags): {{
    - ResourceTag}}
  [UserParameters](#cfn-datazone-project-userparameters): {{
    - EnvironmentConfigurationUserParameter}}
```

## Properties
<a name="aws-resource-datazone-project-properties"></a>

`Description`  <a name="cfn-datazone-project-description"></a>
The description of a project.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-project-domainidentifier"></a>
The identifier of a Amazon DataZone domain where the project exists.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainUnitId`  <a name="cfn-datazone-project-domainunitid"></a>
The ID of the domain unit. This parameter is not required and if it is not specified, then the project is created at the root domain unit level.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9_\-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlossaryTerms`  <a name="cfn-datazone-project-glossaryterms"></a>
The glossary terms that can be used in this Amazon DataZone project.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MembershipAssignments`  <a name="cfn-datazone-project-membershipassignments"></a>
Property description not available.
*Required*: No
*Type*: Array of [ProjectMembershipAssignment](aws-properties-datazone-project-projectmembershipassignment.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-datazone-project-name"></a>
The name of a project.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w -]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectCategory`  <a name="cfn-datazone-project-projectcategory"></a>
The category of the project.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectExecutionRole`  <a name="cfn-datazone-project-projectexecutionrole"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role/[\w+=,.@/-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectProfileId`  <a name="cfn-datazone-project-projectprofileid"></a>
The ID of the project profile.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectProfileVersion`  <a name="cfn-datazone-project-projectprofileversion"></a>
The project profile version to which the project should be updated. You can only specify the following string for this parameter: `latest`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTags`  <a name="cfn-datazone-project-resourcetags"></a>
The resource tags of the project.
*Required*: No
*Type*: Array of [ResourceTag](aws-properties-datazone-project-resourcetag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserParameters`  <a name="cfn-datazone-project-userparameters"></a>
The user parameters of the project.
*Required*: No
*Type*: Array of [EnvironmentConfigurationUserParameter](aws-properties-datazone-project-environmentconfigurationuserparameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datazone-project-return-values"></a>

### Ref
<a name="aws-resource-datazone-project-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and the `ProjectId` that uniquely identify the project. For example: `{ "Ref": "MyProject" }` for the resource with the logical ID `MyProject`, `Ref` returns `DomainId|ProjectId`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-project-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-project-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when a project was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The Amazon DataZone user who created the project.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The identifier of a Amazon DataZone domain where the project exists.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of a project.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp of when the project was last updated.

`ProjectStatus`  <a name="ProjectStatus-fn::getatt"></a>
The status of the project.
