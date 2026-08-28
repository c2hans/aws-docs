---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-environmentactions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::EnvironmentActions
<a name="aws-resource-datazone-environmentactions"></a>

The details about the specified action configured for an environment. For example, the details of the specified console links for an analytics tool that is available in this environment.

## Syntax
<a name="aws-resource-datazone-environmentactions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-environmentactions-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::EnvironmentActions",
  "Properties" : {
      "[Description](#cfn-datazone-environmentactions-description)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-environmentactions-domainidentifier)" : {{String}},
      "[EnvironmentIdentifier](#cfn-datazone-environmentactions-environmentidentifier)" : {{String}},
      "[Identifier](#cfn-datazone-environmentactions-identifier)" : {{String}},
      "[Name](#cfn-datazone-environmentactions-name)" : {{String}},
      "[Parameters](#cfn-datazone-environmentactions-parameters)" : {{AwsConsoleLinkParameters}}
    }
}
```

### YAML
<a name="aws-resource-datazone-environmentactions-syntax.yaml"></a>

```
Type: AWS::DataZone::EnvironmentActions
Properties:
  [Description](#cfn-datazone-environmentactions-description): {{String}}
  [DomainIdentifier](#cfn-datazone-environmentactions-domainidentifier): {{String}}
  [EnvironmentIdentifier](#cfn-datazone-environmentactions-environmentidentifier): {{String}}
  [Identifier](#cfn-datazone-environmentactions-identifier): {{String}}
  [Name](#cfn-datazone-environmentactions-name): {{String}}
  [Parameters](#cfn-datazone-environmentactions-parameters): {{
    AwsConsoleLinkParameters}}
```

## Properties
<a name="aws-resource-datazone-environmentactions-properties"></a>

`Description`  <a name="cfn-datazone-environmentactions-description"></a>
The environment action description.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-environmentactions-domainidentifier"></a>
The Amazon DataZone domain ID of the environment action.
*Required*: No
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentIdentifier`  <a name="cfn-datazone-environmentactions-environmentidentifier"></a>
The environment ID of the environment action.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_-]{1,36}$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Identifier`  <a name="cfn-datazone-environmentactions-identifier"></a>
The ID of the environment action.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-datazone-environmentactions-name"></a>
The name of the environment action.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w -]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-datazone-environmentactions-parameters"></a>
The parameters of the environment action.
*Required*: No
*Type*: [AwsConsoleLinkParameters](aws-properties-datazone-environmentactions-awsconsolelinkparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datazone-environmentactions-return-values"></a>

### Ref
<a name="aws-resource-datazone-environmentactions-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and `EnvironmentActionId`, which uniquely identifies the environment action. For example: `{ "Ref": "MyEnvironmentAction" }` for the resource with the logical ID `MyEnvironmentAction`, `Ref` returns `DomainId|EnvironmentActionId`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-environmentactions-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-environmentactions-return-values-fn--getatt-fn--getatt"></a>

`DomainId`  <a name="DomainId-fn::getatt"></a>
The Amazon DataZone domain ID of the environment action.

`EnvironmentId`  <a name="EnvironmentId-fn::getatt"></a>
The environment ID of the environment action.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the environment action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
