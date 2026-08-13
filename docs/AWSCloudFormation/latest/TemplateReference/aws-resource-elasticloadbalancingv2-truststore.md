---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-truststore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::TrustStore
<a name="aws-resource-elasticloadbalancingv2-truststore"></a>

Creates a trust store. You must specify `CaCertificatesBundleS3Bucket` and `CaCertificatesBundleS3Key`. When you create a trust store, you must specify `Name`.

## Syntax
<a name="aws-resource-elasticloadbalancingv2-truststore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticloadbalancingv2-truststore-syntax.json"></a>

```
{
  "Type" : "AWS::ElasticLoadBalancingV2::TrustStore",
  "Properties" : {
      "[CaCertificatesBundleS3Bucket](#cfn-elasticloadbalancingv2-truststore-cacertificatesbundles3bucket)" : {{String}},
      "[CaCertificatesBundleS3Key](#cfn-elasticloadbalancingv2-truststore-cacertificatesbundles3key)" : {{String}},
      "[CaCertificatesBundleS3ObjectVersion](#cfn-elasticloadbalancingv2-truststore-cacertificatesbundles3objectversion)" : {{String}},
      "[Name](#cfn-elasticloadbalancingv2-truststore-name)" : {{String}},
      "[Tags](#cfn-elasticloadbalancingv2-truststore-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticloadbalancingv2-truststore-syntax.yaml"></a>

```
Type: AWS::ElasticLoadBalancingV2::TrustStore
Properties:
  [CaCertificatesBundleS3Bucket](#cfn-elasticloadbalancingv2-truststore-cacertificatesbundles3bucket): {{String}}
  [CaCertificatesBundleS3Key](#cfn-elasticloadbalancingv2-truststore-cacertificatesbundles3key): {{String}}
  [CaCertificatesBundleS3ObjectVersion](#cfn-elasticloadbalancingv2-truststore-cacertificatesbundles3objectversion): {{String}}
  [Name](#cfn-elasticloadbalancingv2-truststore-name): {{String}}
  [Tags](#cfn-elasticloadbalancingv2-truststore-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-elasticloadbalancingv2-truststore-properties"></a>

`CaCertificatesBundleS3Bucket`  <a name="cfn-elasticloadbalancingv2-truststore-cacertificatesbundles3bucket"></a>
The Amazon S3 bucket for the ca certificates bundle.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CaCertificatesBundleS3Key`  <a name="cfn-elasticloadbalancingv2-truststore-cacertificatesbundles3key"></a>
The Amazon S3 path for the ca certificates bundle.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CaCertificatesBundleS3ObjectVersion`  <a name="cfn-elasticloadbalancingv2-truststore-cacertificatesbundles3objectversion"></a>
The Amazon S3 object version for the ca certificates bundle. If undefined the current version is used.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-elasticloadbalancingv2-truststore-name"></a>
The name of the trust store.
*Required*: No
*Type*: String
*Pattern*: `^([a-zA-Z0-9]+-)*[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-elasticloadbalancingv2-truststore-tags"></a>
The tags to assign to the trust store.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticloadbalancingv2-truststore-tag.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticloadbalancingv2-truststore-return-values"></a>

### Ref
<a name="aws-resource-elasticloadbalancingv2-truststore-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the trust store.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticloadbalancingv2-truststore-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticloadbalancingv2-truststore-return-values-fn--getatt-fn--getatt"></a>

`NumberOfCaCertificates`  <a name="NumberOfCaCertificates-fn::getatt"></a>
The number of ca certificates in the trust store.

`Status`  <a name="Status-fn::getatt"></a>
The status of the trust store. The possible values are `CREATING` and `ACTIVE`.

`TrustStoreArn`  <a name="TrustStoreArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the trust store.

## Examples
<a name="aws-resource-elasticloadbalancingv2-truststore--examples"></a>

###
<a name="aws-resource-elasticloadbalancingv2-truststore--examples--"></a>

The following example creates a trust store.

#### YAML
<a name="aws-resource-elasticloadbalancingv2-truststore--examples----yaml"></a>

```
myTrustStore:
  Type: 'AWS::ElasticLoadBalancingV2::TrustStore'
  Properties:
    Name: my-trust-store
    CaCertificatesBundleS3Bucket: amzn-s3-demo-bucket
    CaCertificatesBundleS3Key: certificates/ca-bundle.pem
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-truststore--examples----json"></a>

```
{
  "myTrustStore": {
    "Type": "AWS::ElasticLoadBalancingV2::TrustStore",
    "Properties": {
      "Name": "my-trust-store",
      "CaCertificatesBundleS3Bucket": "amzn-s3-demo-bucket",
      "CaCertificatesBundleS3Key": "certificates/ca-bundle.pem"
    }
  }
}
```
