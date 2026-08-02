---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3tables-namespace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Namespace
<a name="aws-resource-s3tables-namespace"></a>

Creates a namespace. A namespace is a logical grouping of tables within your table bucket, which you can use to organize tables. For more information, see [Create a namespace](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-create.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:CreateNamespace` permission to use this operation.

 AWS Cloud Development Kit (AWS CDK)
To use S3 Tables AWS CDK constructs, add the `@aws-cdk/aws-s3tables-alpha` dependency with one of the following options:
+ NPM: `npm i @aws-cdk/aws-s3tables-alpha`
+ Yarn:`yarn add @aws-cdk/aws-s3tables-alpha`

## Syntax
<a name="aws-resource-s3tables-namespace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3tables-namespace-syntax.json"></a>

```
{
  "Type" : "AWS::S3Tables::Namespace",
  "Properties" : {
      "[Namespace](#cfn-s3tables-namespace-namespace)" : {{String}},
      "[TableBucketARN](#cfn-s3tables-namespace-tablebucketarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-s3tables-namespace-syntax.yaml"></a>

```
Type: AWS::S3Tables::Namespace
Properties:
  [Namespace](#cfn-s3tables-namespace-namespace): {{String}}
  [TableBucketARN](#cfn-s3tables-namespace-tablebucketarn): {{String}}
```

## Properties
<a name="aws-resource-s3tables-namespace-properties"></a>

`Namespace`  <a name="cfn-s3tables-namespace-namespace"></a>
The name of the namespace.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableBucketARN`  <a name="cfn-s3tables-namespace-tablebucketarn"></a>
The Amazon Resource Name (ARN) of the table bucket to create the namespace in.
*Required*: Yes
*Type*: String
*Pattern*: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3tables-namespace-return-values"></a>

### Ref
<a name="aws-resource-s3tables-namespace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the namespace name.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
