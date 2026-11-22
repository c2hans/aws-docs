---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-runtimealias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::RuntimeAlias

The `AWS::Lambda::RuntimeAlias` resource creates a runtime alias for a customer-managed runtime. A runtime alias is a named pointer to a runtime version. Functions use a customer-managed runtime through a runtime alias, so updating the alias's `RuntimeVersion` releases a new version to those functions, and pointing it back rolls the release back.

When you delete this resource, Lambda schedules it for deletion after a 30-day recovery window, and CloudFormation treats it as deleted. Until the window ends, the name stays reserved: you can't create a runtime alias with the same name, so use a new name if you re-create it.

## Syntax
<a name="aws-resource-lambda-runtimealias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-runtimealias-syntax.json"></a>

```json
{
  "Type" : "AWS::Lambda::RuntimeAlias",
  "Properties" : {
      "[Description](#cfn-lambda-runtimealias-description)" : {{String}},
      "[Name](#cfn-lambda-runtimealias-name)" : {{String}},
      "[ReleaseLifecycle](#cfn-lambda-runtimealias-releaselifecycle)" : {{ReleaseLifecycle}},
      "[RuntimeName](#cfn-lambda-runtimealias-runtimename)" : {{String}},
      "[RuntimeVersion](#cfn-lambda-runtimealias-runtimeversion)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lambda-runtimealias-syntax.yaml"></a>

```yaml
Type: AWS::Lambda::RuntimeAlias
Properties:
  [Description](#cfn-lambda-runtimealias-description): {{String}}
  [Name](#cfn-lambda-runtimealias-name): {{String}}
  [ReleaseLifecycle](#cfn-lambda-runtimealias-releaselifecycle): {{
    ReleaseLifecycle}}
  [RuntimeName](#cfn-lambda-runtimealias-runtimename): {{String}}
  [RuntimeVersion](#cfn-lambda-runtimealias-runtimeversion): {{String}}
```

## Properties
<a name="aws-resource-lambda-runtimealias-properties"></a>

`Description`  <a name="cfn-lambda-runtimealias-description"></a>
A description of the runtime alias. If you remove this property from the template, the description is cleared.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lambda-runtimealias-name"></a>
The name to assign to the new runtime alias.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseLifecycle`  <a name="cfn-lambda-runtimealias-releaselifecycle"></a>
The runtime lifecycle for the alias. By default, this is inherited from the runtime lifecycle. Optionally, you can override the lifecycle information at the alias level, if required.
*Required*: No
*Type*: [ReleaseLifecycle](aws-properties-lambda-runtimealias-releaselifecycle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeName`  <a name="cfn-lambda-runtimealias-runtimename"></a>
The name of the runtime that the alias belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]$`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuntimeVersion`  <a name="cfn-lambda-runtimealias-runtimeversion"></a>
The name of the runtime version the alias points to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-runtimealias-return-values"></a>

### Ref
<a name="aws-resource-lambda-runtimealias-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the runtime alias.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-runtimealias-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

 `Compatibility`
The compatibility of the runtime version that the alias points to: the integration models and architectures it supports, and whether it supports Lambda Managed Instances. The value is a [Compatibility](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-runtimealias-compatibility.html) object.

####
<a name="aws-resource-lambda-runtimealias-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the runtime alias.

`Created`  <a name="Created-fn::getatt"></a>
The date and time when the runtime alias was created.

`LastModified`  <a name="LastModified-fn::getatt"></a>
The date and time when the runtime alias was last modified.

`RuntimeVersionArn`  <a name="RuntimeVersionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the runtime version the alias points to.

`State`  <a name="State-fn::getatt"></a>
The current state of the runtime alias.

## Examples
<a name="aws-resource-lambda-runtimealias--examples"></a>

### Runtime alias
<a name="aws-resource-lambda-runtimealias--examples--Runtime_alias"></a>

Create a runtime alias named `stable` that points to version `v1` of the runtime.

#### JSON
<a name="aws-resource-lambda-runtimealias--examples--Runtime_alias--json"></a>

```json
"MyRuntimeAlias": {
    "Type": "AWS::Lambda::RuntimeAlias",
    "Properties": {
        "RuntimeName": {
            "Ref": "MyRuntimeName"
        },
        "Name": "stable",
        "RuntimeVersion": "v1",
        "Description": "Version used by production functions"
    }
}
```

#### YAML
<a name="aws-resource-lambda-runtimealias--examples--Runtime_alias--yaml"></a>

```yaml
MyRuntimeAlias:
  Type: AWS::Lambda::RuntimeAlias
  Properties:
    RuntimeName:
      Ref: MyRuntimeName
    Name: stable
    RuntimeVersion: v1
    Description: Version used by production functions
```
