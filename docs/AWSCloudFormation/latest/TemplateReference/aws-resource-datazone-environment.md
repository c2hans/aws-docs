---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-environment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Environment
<a name="aws-resource-datazone-environment"></a>

The `AWS::DataZone::Environment`resource specifies an Amazon DataZone environment, which is a collection of zero or more configured resources with a given set of IAM principals who can operate on those resources.

## Syntax
<a name="aws-resource-datazone-environment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-environment-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::Environment",
  "Properties" : {
      "[DeploymentOrder](#cfn-datazone-environment-deploymentorder)" : {{Integer}},
      "[Description](#cfn-datazone-environment-description)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-environment-domainidentifier)" : {{String}},
      "[EnvironmentAccountIdentifier](#cfn-datazone-environment-environmentaccountidentifier)" : {{String}},
      "[EnvironmentAccountRegion](#cfn-datazone-environment-environmentaccountregion)" : {{String}},
      "[EnvironmentBlueprintIdentifier](#cfn-datazone-environment-environmentblueprintidentifier)" : {{String}},
      "[EnvironmentConfigurationId](#cfn-datazone-environment-environmentconfigurationid)" : {{String}},
      "[EnvironmentProfileIdentifier](#cfn-datazone-environment-environmentprofileidentifier)" : {{String}},
      "[EnvironmentRoleArn](#cfn-datazone-environment-environmentrolearn)" : {{String}},
      "[GlossaryTerms](#cfn-datazone-environment-glossaryterms)" : {{[ String, ... ]}},
      "[Name](#cfn-datazone-environment-name)" : {{String}},
      "[ProjectIdentifier](#cfn-datazone-environment-projectidentifier)" : {{String}},
      "[UserParameters](#cfn-datazone-environment-userparameters)" : {{[ EnvironmentParameter, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datazone-environment-syntax.yaml"></a>

```
Type: AWS::DataZone::Environment
Properties:
  [DeploymentOrder](#cfn-datazone-environment-deploymentorder): {{Integer}}
  [Description](#cfn-datazone-environment-description): {{String}}
  [DomainIdentifier](#cfn-datazone-environment-domainidentifier): {{String}}
  [EnvironmentAccountIdentifier](#cfn-datazone-environment-environmentaccountidentifier): {{String}}
  [EnvironmentAccountRegion](#cfn-datazone-environment-environmentaccountregion): {{String}}
  [EnvironmentBlueprintIdentifier](#cfn-datazone-environment-environmentblueprintidentifier): {{String}}
  [EnvironmentConfigurationId](#cfn-datazone-environment-environmentconfigurationid): {{String}}
  [EnvironmentProfileIdentifier](#cfn-datazone-environment-environmentprofileidentifier): {{String}}
  [EnvironmentRoleArn](#cfn-datazone-environment-environmentrolearn): {{String}}
  [GlossaryTerms](#cfn-datazone-environment-glossaryterms): {{
    - String}}
  [Name](#cfn-datazone-environment-name): {{String}}
  [ProjectIdentifier](#cfn-datazone-environment-projectidentifier): {{String}}
  [UserParameters](#cfn-datazone-environment-userparameters): {{
    - EnvironmentParameter}}
```

## Properties
<a name="aws-resource-datazone-environment-properties"></a>

`DeploymentOrder`  <a name="cfn-datazone-environment-deploymentorder"></a>
The deployment order of the environment.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-datazone-environment-description"></a>
The description of the environment.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-environment-domainidentifier"></a>
The identifier of the Amazon DataZone domain in which the environment is created.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentAccountIdentifier`  <a name="cfn-datazone-environment-environmentaccountidentifier"></a>
The identifier of the AWS account in which an environment exists.
*Required*: No
*Type*: String
*Pattern*: `^\d{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentAccountRegion`  <a name="cfn-datazone-environment-environmentaccountregion"></a>
The AWS Region in which an environment exists.
*Required*: No
*Type*: String
*Pattern*: `^[a-z]{2}-[a-z]{4,10}-\d$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentBlueprintIdentifier`  <a name="cfn-datazone-environment-environmentblueprintidentifier"></a>
The ID of the blueprint with which the environment is being created.
This parameter is only valid for V1 domains. If provided for a V2 domain, the service returns a ValidationException.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentConfigurationId`  <a name="cfn-datazone-environment-environmentconfigurationid"></a>
The configuration ID with which the environment is created.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentProfileIdentifier`  <a name="cfn-datazone-environment-environmentprofileidentifier"></a>
The identifier of the environment profile that is used to create this Amazon DataZone environment.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{0,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentRoleArn`  <a name="cfn-datazone-environment-environmentrolearn"></a>
The ARN of the environment role.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlossaryTerms`  <a name="cfn-datazone-environment-glossaryterms"></a>
The glossary terms that can be used in this Amazon DataZone environment.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-datazone-environment-name"></a>
The name of the Amazon DataZone environment.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectIdentifier`  <a name="cfn-datazone-environment-projectidentifier"></a>
The identifier of the Amazon DataZone project in which this environment is created.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserParameters`  <a name="cfn-datazone-environment-userparameters"></a>
The user parameters of this Amazon DataZone environment.
*Required*: No
*Type*: Array of [EnvironmentParameter](aws-properties-datazone-environment-environmentparameter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-environment-return-values"></a>

### Ref
<a name="aws-resource-datazone-environment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and `EnvironmentId`, which uniquely identifies the environment. For example: `{ "Ref": "MyEnvironment" }` for the resource with the logical ID `MyEnvironment`, `Ref` returns `DomainId|EnvironmentId`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-environment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-environment-return-values-fn--getatt-fn--getatt"></a>

`AwsAccountId`  <a name="AwsAccountId-fn::getatt"></a>
The identifier of the AWS account in which an environment exists.

`AwsAccountRegion`  <a name="AwsAccountRegion-fn::getatt"></a>
The AWS Region in which an environment exists.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the environment was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The Amazon DataZone user who created the environment.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The identifier of the Amazon DataZone domain in which the environment exists.

`EnvironmentBlueprintId`  <a name="EnvironmentBlueprintId-fn::getatt"></a>
The identifier of a blueprint with which an environment profile is created.

`EnvironmentProfileId`  <a name="EnvironmentProfileId-fn::getatt"></a>
The identifier of the environment profile with which the environment was created.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the environment.

`ProjectId`  <a name="ProjectId-fn::getatt"></a>
The identifier of the project in which the environment exists.

`Provider`  <a name="Provider-fn::getatt"></a>
The provider of the environment.

`Status`  <a name="Status-fn::getatt"></a>
The status of the environment.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp of when the environment was updated.
