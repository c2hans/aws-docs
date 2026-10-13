---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionrevision.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionRevision
<a name="aws-resource-lambda-webfunctionrevision"></a>

The `AWS::Lambda::WebFunctionRevision` resource creates an immutable revision for a Lambda web function. A revision represents a specific version of the function's code and configuration. You can't modify a revision after you create it. You also can't delete a revision that is currently serving traffic on an endpoint. To route traffic to a revision, reference it from the `RevisionWeights` property of an `AWS::Lambda::WebFunctionEndpoint` resource.

## Syntax
<a name="aws-resource-lambda-webfunctionrevision-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-webfunctionrevision-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::WebFunctionRevision",
  "Properties" : {
      "[BuildConfig](#cfn-lambda-webfunctionrevision-buildconfig)" : {{BuildConfig}},
      "[Description](#cfn-lambda-webfunctionrevision-description)" : {{String}},
      "[FunctionName](#cfn-lambda-webfunctionrevision-functionname)" : {{String}},
      "[KmsKeyArn](#cfn-lambda-webfunctionrevision-kmskeyarn)" : {{String}},
      "[ServiceConfig](#cfn-lambda-webfunctionrevision-serviceconfig)" : {{ServiceConfig}}
    }
}
```

### YAML
<a name="aws-resource-lambda-webfunctionrevision-syntax.yaml"></a>

```
Type: AWS::Lambda::WebFunctionRevision
Properties:
  [BuildConfig](#cfn-lambda-webfunctionrevision-buildconfig): {{
    BuildConfig}}
  [Description](#cfn-lambda-webfunctionrevision-description): {{String}}
  [FunctionName](#cfn-lambda-webfunctionrevision-functionname): {{String}}
  [KmsKeyArn](#cfn-lambda-webfunctionrevision-kmskeyarn): {{String}}
  [ServiceConfig](#cfn-lambda-webfunctionrevision-serviceconfig): {{
    ServiceConfig}}
```

## Properties
<a name="aws-resource-lambda-webfunctionrevision-properties"></a>

`BuildConfig`  <a name="cfn-lambda-webfunctionrevision-buildconfig"></a>
The build configuration for the revision, including code location and runtime settings.
*Required*: Yes
*Type*: [BuildConfig](aws-properties-lambda-webfunctionrevision-buildconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-lambda-webfunctionrevision-description"></a>
A description of the revision.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionName`  <a name="cfn-lambda-webfunctionrevision-functionname"></a>
The web function.
You can specify either of the following:
+ The function name, for example `my-function`.
+ The function ARN, for example `arn:aws:lambda:us-east-1:111122223333:web-function/my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyArn`  <a name="cfn-lambda-webfunctionrevision-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used to encrypt the revision's code and environment variables.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-z-]*){1}:kms:[a-z0-9-]+:[0-9]{12}:key/.*$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceConfig`  <a name="cfn-lambda-webfunctionrevision-serviceconfig"></a>
The service configuration for the revision, including execution role, timeout, and concurrency settings.
*Required*: Yes
*Type*: [ServiceConfig](aws-properties-lambda-webfunctionrevision-serviceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lambda-webfunctionrevision-return-values"></a>

### Ref
<a name="aws-resource-lambda-webfunctionrevision-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the revision.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-webfunctionrevision-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lambda-webfunctionrevision-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time the revision was created.

`FunctionArn`  <a name="FunctionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the web function.

`RevisionArn`  <a name="RevisionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the revision.

`RevisionId`  <a name="RevisionId-fn::getatt"></a>
The identifier of the revision.

`State`  <a name="State-fn::getatt"></a>
The current state of the revision.

`StateReason`  <a name="StateReason-fn::getatt"></a>
The reason for the current state of the revision.

## Examples
<a name="aws-resource-lambda-webfunctionrevision--examples"></a>

### Web function revision
<a name="aws-resource-lambda-webfunctionrevision--examples--Web_function_revision"></a>

Create a revision for the web function `my-web-function` from a deployment package in Amazon S3.

#### JSON
<a name="aws-resource-lambda-webfunctionrevision--examples--Web_function_revision--json"></a>

```
"MyRevision": {
    "Type": "AWS::Lambda::WebFunctionRevision",
    "Properties": {
        "FunctionName": "my-web-function",
        "Description": "First revision",
        "BuildConfig": {
            "CodeConfig": {
                "S3Object": {
                    "Bucket": "amzn-s3-demo-bucket",
                    "Key": "app.zip"
                }
            },
            "RuntimeConfig": {
                "Runtime": "nodejs24.x"
            }
        },
        "ServiceConfig": {
            "ExecutionRoleArn": {
                "Fn::GetAtt": [
                    "MyExecutionRole",
                    "Arn"
                ]
            },
            "TimeoutSeconds": 30
        }
    }
}
```

#### YAML
<a name="aws-resource-lambda-webfunctionrevision--examples--Web_function_revision--yaml"></a>

```
MyRevision:
  Type: AWS::Lambda::WebFunctionRevision
  Properties:
    FunctionName: my-web-function
    Description: First revision
    BuildConfig:
      CodeConfig:
        S3Object:
          Bucket: amzn-s3-demo-bucket
          Key: app.zip
      RuntimeConfig:
        Runtime: nodejs24.x
    ServiceConfig:
      ExecutionRoleArn: !GetAtt MyExecutionRole.Arn
      TimeoutSeconds: 30
```
