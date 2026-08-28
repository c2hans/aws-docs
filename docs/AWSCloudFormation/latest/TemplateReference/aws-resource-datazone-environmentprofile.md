---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-environmentprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::EnvironmentProfile
<a name="aws-resource-datazone-environmentprofile"></a>

The details of an environment profile.

## Syntax
<a name="aws-resource-datazone-environmentprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-environmentprofile-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::EnvironmentProfile",
  "Properties" : {
      "[AwsAccountId](#cfn-datazone-environmentprofile-awsaccountid)" : {{String}},
      "[AwsAccountRegion](#cfn-datazone-environmentprofile-awsaccountregion)" : {{String}},
      "[Description](#cfn-datazone-environmentprofile-description)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-environmentprofile-domainidentifier)" : {{String}},
      "[EnvironmentBlueprintIdentifier](#cfn-datazone-environmentprofile-environmentblueprintidentifier)" : {{String}},
      "[Name](#cfn-datazone-environmentprofile-name)" : {{String}},
      "[ProjectIdentifier](#cfn-datazone-environmentprofile-projectidentifier)" : {{String}},
      "[UserParameters](#cfn-datazone-environmentprofile-userparameters)" : {{[ EnvironmentParameter, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datazone-environmentprofile-syntax.yaml"></a>

```
Type: AWS::DataZone::EnvironmentProfile
Properties:
  [AwsAccountId](#cfn-datazone-environmentprofile-awsaccountid): {{String}}
  [AwsAccountRegion](#cfn-datazone-environmentprofile-awsaccountregion): {{String}}
  [Description](#cfn-datazone-environmentprofile-description): {{String}}
  [DomainIdentifier](#cfn-datazone-environmentprofile-domainidentifier): {{String}}
  [EnvironmentBlueprintIdentifier](#cfn-datazone-environmentprofile-environmentblueprintidentifier): {{String}}
  [Name](#cfn-datazone-environmentprofile-name): {{String}}
  [ProjectIdentifier](#cfn-datazone-environmentprofile-projectidentifier): {{String}}
  [UserParameters](#cfn-datazone-environmentprofile-userparameters): {{
    - EnvironmentParameter}}
```

## Properties
<a name="aws-resource-datazone-environmentprofile-properties"></a>

`AwsAccountId`  <a name="cfn-datazone-environmentprofile-awsaccountid"></a>
The identifier of an AWS account in which an environment profile exists.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsAccountRegion`  <a name="cfn-datazone-environmentprofile-awsaccountregion"></a>
The AWS Region in which an environment profile exists.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z]{2}-[a-z]{4,10}-\d$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-datazone-environmentprofile-description"></a>
The description of the environment profile.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-environmentprofile-domainidentifier"></a>
The identifier of the Amazon DataZone domain in which the environment profile exists.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentBlueprintIdentifier`  <a name="cfn-datazone-environmentprofile-environmentblueprintidentifier"></a>
The identifier of a blueprint with which an environment profile is created.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-datazone-environmentprofile-name"></a>
The name of the environment profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w -]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectIdentifier`  <a name="cfn-datazone-environmentprofile-projectidentifier"></a>
The identifier of a project in which an environment profile exists.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserParameters`  <a name="cfn-datazone-environmentprofile-userparameters"></a>
The user parameters of this Amazon DataZone environment profile.
*Required*: No
*Type*: Array of [EnvironmentParameter](aws-properties-datazone-environmentprofile-environmentparameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datazone-environmentprofile-return-values"></a>

### Ref
<a name="aws-resource-datazone-environmentprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and the `EnvironmentProfileId`, which uniquely identifies the environment profile. For example: `{ "Ref": "MyEnvironmentProfile" }` for the resource with the logical `ID MyEnvironmentProfile`, `Ref` returns `DomainId|EnvironmentProfileId`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-environmentprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-environmentprofile-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when an environment profile was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The Amazon DataZone user who created the environment profile.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The identifier of the Amazon DataZone domain in which the environment profile exists.

`EnvironmentBlueprintId`  <a name="EnvironmentBlueprintId-fn::getatt"></a>
The identifier of a blueprint with which an environment profile is created.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the environment profile.

`ProjectId`  <a name="ProjectId-fn::getatt"></a>
The identifier of a project in which an environment profile exists.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp of when the environment profile was updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
