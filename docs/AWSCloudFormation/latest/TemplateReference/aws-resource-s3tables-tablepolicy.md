---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3tables-tablepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TablePolicy
<a name="aws-resource-s3tables-tablepolicy"></a>

Creates a new maintenance configuration or replaces an existing table policy for a table. For more information, see [Adding a table policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-policy.html#table-policy-add) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:PutTablePolicy` permission to use this operation.

 AWS Cloud Development Kit (AWS CDK)
To use S3 Tables AWS CDK constructs, add the `@aws-cdk/aws-s3tables-alpha` dependency with one of the following options:
+ NPM: `npm i @aws-cdk/aws-s3tables-alpha`
+ Yarn:`yarn add @aws-cdk/aws-s3tables-alpha`

## Syntax
<a name="aws-resource-s3tables-tablepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3tables-tablepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::S3Tables::TablePolicy",
  "Properties" : {
      "[ResourcePolicy](#cfn-s3tables-tablepolicy-resourcepolicy)" : {{Json}},
      "[TableARN](#cfn-s3tables-tablepolicy-tablearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-s3tables-tablepolicy-syntax.yaml"></a>

```
Type: AWS::S3Tables::TablePolicy
Properties:
  [ResourcePolicy](#cfn-s3tables-tablepolicy-resourcepolicy): {{Json}}
  [TableARN](#cfn-s3tables-tablepolicy-tablearn): {{String}}
```

## Properties
<a name="aws-resource-s3tables-tablepolicy-properties"></a>

`ResourcePolicy`  <a name="cfn-s3tables-tablepolicy-resourcepolicy"></a>
The `JSON` that defines the policy.
*Required*: Yes
*Type*: Json
*Minimum*: `1`
*Maximum*: `20480`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableARN`  <a name="cfn-s3tables-tablepolicy-tablearn"></a>
The Amazon Resource Name (ARN) of the table.
*Required*: Yes
*Type*: String
*Pattern*: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3tables-tablepolicy-return-values"></a>

### Ref
<a name="aws-resource-s3tables-tablepolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns some information about your table policy.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3tables-tablepolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3tables-tablepolicy-return-values-fn--getatt-fn--getatt"></a>

`Namespace`  <a name="Namespace-fn::getatt"></a>
The namespace to associated with the table.

`TableBucketARN`  <a name="TableBucketARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of the table bucket that contains the table.

`TableName`  <a name="TableName-fn::getatt"></a>
The name of the table.
