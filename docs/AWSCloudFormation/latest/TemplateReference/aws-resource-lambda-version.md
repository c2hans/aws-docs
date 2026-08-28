---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-version.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Version
<a name="aws-resource-lambda-version"></a>

The `AWS::Lambda::Version` resource creates a [version](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html) from the current code and configuration of a function. Use versions to create a snapshot of your function code and configuration that doesn't change.

## Syntax
<a name="aws-resource-lambda-version-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-version-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::Version",
  "Properties" : {
      "[CodeSha256](#cfn-lambda-version-codesha256)" : {{String}},
      "[Description](#cfn-lambda-version-description)" : {{String}},
      "[FunctionName](#cfn-lambda-version-functionname)" : {{String}},
      "[FunctionScalingConfig](#cfn-lambda-version-functionscalingconfig)" : {{FunctionScalingConfig}},
      "[ProvisionedConcurrencyConfig](#cfn-lambda-version-provisionedconcurrencyconfig)" : {{ProvisionedConcurrencyConfiguration}},
      "[RuntimePolicy](#cfn-lambda-version-runtimepolicy)" : {{RuntimePolicy}}
    }
}
```

### YAML
<a name="aws-resource-lambda-version-syntax.yaml"></a>

```
Type: AWS::Lambda::Version
Properties:
  [CodeSha256](#cfn-lambda-version-codesha256): {{String}}
  [Description](#cfn-lambda-version-description): {{String}}
  [FunctionName](#cfn-lambda-version-functionname): {{String}}
  [FunctionScalingConfig](#cfn-lambda-version-functionscalingconfig): {{
    FunctionScalingConfig}}
  [ProvisionedConcurrencyConfig](#cfn-lambda-version-provisionedconcurrencyconfig): {{
    ProvisionedConcurrencyConfiguration}}
  [RuntimePolicy](#cfn-lambda-version-runtimepolicy): {{
    RuntimePolicy}}
```

## Properties
<a name="aws-resource-lambda-version-properties"></a>

`CodeSha256`  <a name="cfn-lambda-version-codesha256"></a>
Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. Updates are not supported for this property.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-lambda-version-description"></a>
A description for the version to override the description in the function configuration. Updates are not supported for this property.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionName`  <a name="cfn-lambda-version-functionname"></a>
The name or ARN of the Lambda function.

**Name formats**
+ **Function name** - `MyFunction`.
+ **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
+ **Partial ARN** - `123456789012:function:MyFunction`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:lambda:)?((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionScalingConfig`  <a name="cfn-lambda-version-functionscalingconfig"></a>
Configuration that defines the scaling behavior for a Lambda Managed Instances function, including the minimum and maximum number of execution environments that can be provisioned.
*Required*: No
*Type*: [FunctionScalingConfig](aws-properties-lambda-version-functionscalingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProvisionedConcurrencyConfig`  <a name="cfn-lambda-version-provisionedconcurrencyconfig"></a>
Specifies a provisioned concurrency configuration for a function's version. Updates are not supported for this property.
*Required*: No
*Type*: [ProvisionedConcurrencyConfiguration](aws-properties-lambda-version-provisionedconcurrencyconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuntimePolicy`  <a name="cfn-lambda-version-runtimepolicy"></a>
The runtime management configuration for the version. Use the runtime policy to control the management mode and runtime version that Lambda uses to run the version.
*Required*: No
*Type*: [RuntimePolicy](aws-properties-lambda-version-runtimepolicy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lambda-version-return-values"></a>

### Ref
<a name="aws-resource-lambda-version-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the version, such as `arn:aws:lambda:us-east-2:123456789012:function:helloworld:1`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-version-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lambda-version-return-values-fn--getatt-fn--getatt"></a>

`FunctionArn`  <a name="FunctionArn-fn::getatt"></a>
The ARN of the function.

`Version`  <a name="Version-fn::getatt"></a>
The version number.

## Examples
<a name="aws-resource-lambda-version--examples"></a>

### Function Version
<a name="aws-resource-lambda-version--examples--Function_Version"></a>

Publish a version with provisioned concurrency.

#### YAML
<a name="aws-resource-lambda-version--examples--Function_Version--yaml"></a>

```
Resources:
  function:
    Type: AWS::Lambda::Function
    Properties:
      Handler: index.handler
      Role: arn:aws:iam::123456789012:role/lambda-role
      Code:
        ZipFile: |
          exports.handler = async (event) => {
              console.log(JSON.stringify(event, null, 2));
              const response = {
                  statusCode: 200,
                  body: JSON.stringify('Hello from Lambda!'),
              };
              return response;
          };
      Runtime: nodejs18.x
      TracingConfig:
        Mode: Active
  version:
    Type: AWS::Lambda::Version
    Properties:
      FunctionName: !Ref function
      Description: v1
      ProvisionedConcurrencyConfig:
        ProvisionedConcurrentExecutions: 20
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
