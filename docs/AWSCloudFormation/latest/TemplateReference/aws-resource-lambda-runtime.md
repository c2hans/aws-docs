---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-runtime.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Runtime

The `AWS::Lambda::Runtime` resource creates a customer-managed runtime. A customer-managed runtime provides a centrally managed execution environment for your Lambda functions. It is the parent of runtime versions and runtime aliases. To publish a container image as a runtime version, use the `AWS::Lambda::RuntimeVersion` resource. To give functions a named pointer to a version, use the `AWS::Lambda::RuntimeAlias` resource.

When you delete this resource, Lambda schedules it for deletion after a 30-day recovery window, and CloudFormation treats it as deleted. Until the window ends, the name stays reserved: you can't create a runtime with the same name, so use a new name if you re-create it.

## Syntax
<a name="aws-resource-lambda-runtime-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-runtime-syntax.json"></a>

```json
{
  "Type" : "AWS::Lambda::Runtime",
  "Properties" : {
      "[Description](#cfn-lambda-runtime-description)" : {{String}},
      "[LicenseInfo](#cfn-lambda-runtime-licenseinfo)" : {{String}},
      "[Name](#cfn-lambda-runtime-name)" : {{String}},
      "[ReleaseLifecycle](#cfn-lambda-runtime-releaselifecycle)" : {{ReleaseLifecycle}},
      "[Tags](#cfn-lambda-runtime-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lambda-runtime-syntax.yaml"></a>

```yaml
Type: AWS::Lambda::Runtime
Properties:
  [Description](#cfn-lambda-runtime-description): {{String}}
  [LicenseInfo](#cfn-lambda-runtime-licenseinfo): {{String}}
  [Name](#cfn-lambda-runtime-name): {{String}}
  [ReleaseLifecycle](#cfn-lambda-runtime-releaselifecycle): {{
    ReleaseLifecycle}}
  [Tags](#cfn-lambda-runtime-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lambda-runtime-properties"></a>

`Description`  <a name="cfn-lambda-runtime-description"></a>
A description of the runtime. If you remove this property from the template, the description is cleared.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseInfo`  <a name="cfn-lambda-runtime-licenseinfo"></a>
The license information for the runtime. If you remove this property from the template, the license information is cleared.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lambda-runtime-name"></a>
The name of the runtime to create.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]$`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseLifecycle`  <a name="cfn-lambda-runtime-releaselifecycle"></a>
The runtime lifecycle for the runtime (optional). Use this to schedule runtime deprecation.
*Required*: No
*Type*: [ReleaseLifecycle](aws-properties-lambda-runtime-releaselifecycle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-lambda-runtime-tags"></a>
A list of [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) to apply to the runtime.
You must have the `lambda:TagResource`, `lambda:UntagResource`, and `lambda:ListTags` permissions for your [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) to manage the CloudFormation stack. If you don't have these permissions, there might be unexpected behavior with stack-level tags propagating to the resource during resource creation and update.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-runtime-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-runtime-return-values"></a>

### Ref
<a name="aws-resource-lambda-runtime-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the runtime.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-runtime-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lambda-runtime-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the runtime.

`Created`  <a name="Created-fn::getatt"></a>
The date and time when the runtime was created.

`LastModified`  <a name="LastModified-fn::getatt"></a>
The date and time when the runtime was last modified.

`State`  <a name="State-fn::getatt"></a>
The current state of the runtime.

## Examples
<a name="aws-resource-lambda-runtime--examples"></a>

### Customer-managed runtime
<a name="aws-resource-lambda-runtime--examples--Customer-managed_runtime"></a>

Create a runtime named `my-runtime` that is generally available and scheduled for deprecation.

#### JSON
<a name="aws-resource-lambda-runtime--examples--Customer-managed_runtime--json"></a>

```json
"MyRuntime": {
    "Type": "AWS::Lambda::Runtime",
    "Properties": {
        "Name": "my-runtime",
        "Description": "Runtime for my functions",
        "LicenseInfo": "MIT",
        "ReleaseLifecycle": {
            "ReleaseState": "GA",
            "DeprecationDate": "2027-12-31"
        },
        "Tags": [
            {
                "Key": "Environment",
                "Value": "Production"
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-lambda-runtime--examples--Customer-managed_runtime--yaml"></a>

```yaml
MyRuntime:
  Type: AWS::Lambda::Runtime
  Properties:
    Name: my-runtime
    Description: Runtime for my functions
    LicenseInfo: MIT
    ReleaseLifecycle:
      ReleaseState: GA
      DeprecationDate: "2027-12-31"
    Tags:
      - Key: Environment
        Value: Production
```
