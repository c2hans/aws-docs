---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-refactorspaces-environment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RefactorSpaces::Environment
<a name="aws-resource-refactorspaces-environment"></a>

**Note**
AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Creates an AWS Migration Hub Refactor Spaces environment. The caller owns the environment resource, and all Refactor Spaces applications, services, and routes created within the environment. They are referred to as the *environment owner*. The environment owner has cross-account visibility and control of Refactor Spaces resources that are added to the environment by other accounts that the environment is shared with.

When creating an environment with a [CreateEnvironment:NetworkFabricType](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType) of `TRANSIT_GATEWAY`, Refactor Spaces provisions a transit gateway to enable services in VPCs to communicate directly across accounts. If [CreateEnvironment:NetworkFabricType](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType) is `NONE`, Refactor Spaces does not create a transit gateway and you must use your network infrastructure to route traffic to services with private URL endpoints.

## Syntax
<a name="aws-resource-refactorspaces-environment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-refactorspaces-environment-syntax.json"></a>

```
{
  "Type" : "AWS::RefactorSpaces::Environment",
  "Properties" : {
      "[Description](#cfn-refactorspaces-environment-description)" : {{String}},
      "[Name](#cfn-refactorspaces-environment-name)" : {{String}},
      "[NetworkFabricType](#cfn-refactorspaces-environment-networkfabrictype)" : {{String}},
      "[Tags](#cfn-refactorspaces-environment-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-refactorspaces-environment-syntax.yaml"></a>

```
Type: AWS::RefactorSpaces::Environment
Properties:
  [Description](#cfn-refactorspaces-environment-description): {{String}}
  [Name](#cfn-refactorspaces-environment-name): {{String}}
  [NetworkFabricType](#cfn-refactorspaces-environment-networkfabrictype): {{String}}
  [Tags](#cfn-refactorspaces-environment-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-refactorspaces-environment-properties"></a>

`Description`  <a name="cfn-refactorspaces-environment-description"></a>
A description of the environment.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_\s\.\!\*\#\@\']+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-refactorspaces-environment-name"></a>
The name of the environment.
*Required*: No
*Type*: String
*Pattern*: `^(?!env-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkFabricType`  <a name="cfn-refactorspaces-environment-networkfabrictype"></a>
The network fabric type of the environment.
*Required*: No
*Type*: String
*Allowed values*: `TRANSIT_GATEWAY | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-refactorspaces-environment-tags"></a>
The tags assigned to the environment.
*Required*: No
*Type*: Array of [Tag](aws-properties-refactorspaces-environment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-refactorspaces-environment-return-values"></a>

### Ref
<a name="aws-resource-refactorspaces-environment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the environment, for example, `env-1234654123`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-refactorspaces-environment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-refactorspaces-environment-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the environment.

`EnvironmentIdentifier`  <a name="EnvironmentIdentifier-fn::getatt"></a>
The unique identifier of the environment.

`TransitGatewayId`  <a name="TransitGatewayId-fn::getatt"></a>
The ID of the AWS Transit Gateway set up by the environment.
