---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-projectmembership.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::ProjectMembership
<a name="aws-resource-datazone-projectmembership"></a>

The `AWS::DataZone::ProjectMembership` resource adds a member to an Amazon DataZone project. Project members consume assets from the Amazon DataZone catalog and produce new assets using one or more analytical workflows.

## Syntax
<a name="aws-resource-datazone-projectmembership-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-projectmembership-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::ProjectMembership",
  "Properties" : {
      "[Designation](#cfn-datazone-projectmembership-designation)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-projectmembership-domainidentifier)" : {{String}},
      "[Member](#cfn-datazone-projectmembership-member)" : {{Member}},
      "[ProjectIdentifier](#cfn-datazone-projectmembership-projectidentifier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datazone-projectmembership-syntax.yaml"></a>

```
Type: AWS::DataZone::ProjectMembership
Properties:
  [Designation](#cfn-datazone-projectmembership-designation): {{String}}
  [DomainIdentifier](#cfn-datazone-projectmembership-domainidentifier): {{String}}
  [Member](#cfn-datazone-projectmembership-member): {{
    Member}}
  [ProjectIdentifier](#cfn-datazone-projectmembership-projectidentifier): {{String}}
```

## Properties
<a name="aws-resource-datazone-projectmembership-properties"></a>

`Designation`  <a name="cfn-datazone-projectmembership-designation"></a>
The designated role of a project member.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-projectmembership-domainidentifier"></a>
The ID of the Amazon DataZone domain in which project membership is created.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Member`  <a name="cfn-datazone-projectmembership-member"></a>
The details about a project member.
*Required*: Yes
*Type*: [Member](aws-properties-datazone-projectmembership-member.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectIdentifier`  <a name="cfn-datazone-projectmembership-projectidentifier"></a>
The ID of the project for which this project membership was created.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-projectmembership-return-values"></a>

### Ref
<a name="aws-resource-datazone-projectmembership-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId`, `MemberId`, `MemberType`, and `ProjectId` that uniquely identify the project membership. For example: `{ "Ref": "MyProjectMembership" }` for the resource with the logical ID `MyProjectMembership`, `Ref` returns `DomainId|MemberId|MemberType|ProjectId`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-projectmembership-return-values-fn--getatt"></a>

####
<a name="aws-resource-datazone-projectmembership-return-values-fn--getatt-fn--getatt"></a>

`MemberIdentifier`  <a name="MemberIdentifier-fn::getatt"></a>
The identifier of the project member.

`MemberIdentifierType`  <a name="MemberIdentifierType-fn::getatt"></a>
The type of the project member identifier.
