---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-truststorerevocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::TrustStoreRevocation
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation"></a>

Adds the specified revocation contents to the specified trust store. You must specify `TrustStoreArn`.

## Syntax
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation-syntax.json"></a>

```
{
  "Type" : "AWS::ElasticLoadBalancingV2::TrustStoreRevocation",
  "Properties" : {
      "[RevocationContents](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontents)" : {{[ RevocationContent, ... ]}},
      "[TrustStoreArn](#cfn-elasticloadbalancingv2-truststorerevocation-truststorearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation-syntax.yaml"></a>

```
Type: AWS::ElasticLoadBalancingV2::TrustStoreRevocation
Properties:
  [RevocationContents](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontents): {{
    - RevocationContent}}
  [TrustStoreArn](#cfn-elasticloadbalancingv2-truststorerevocation-truststorearn): {{String}}
```

## Properties
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation-properties"></a>

`RevocationContents`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-revocationcontents"></a>
The revocation file to add.
*Required*: No
*Type*: Array of [RevocationContent](aws-properties-elasticloadbalancingv2-truststorerevocation-revocationcontent.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrustStoreArn`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-truststorearn"></a>
The Amazon Resource Name (ARN) of the trust store.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation-return-values"></a>

### Ref
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the trust store.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation-return-values-fn--getatt-fn--getatt"></a>

`RevocationId`  <a name="RevocationId-fn::getatt"></a>
The revocation ID of the revocation file.

`TrustStoreRevocations`  <a name="TrustStoreRevocations-fn::getatt"></a>
Information about the revocation file in the trust store. For more information, see [TrustStoreRevocation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-truststorerevocation-truststorerevocation.html).

## Examples
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation--examples"></a>

###
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation--examples--"></a>

The following example creates a revocation list.

#### YAML
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation--examples----yaml"></a>

```
myRevocationList:
  Type: 'AWS::ElasticLoadBalancingV2::TrustStoreRevocation'
  Properties:
    TrustStoreArn: !Ref myTrustStore
    RevocationContents:
        - RevocationType: CRL
          S3Bucket: amzn-s3-demo-bucket
          S3Key: crl/revoked-list.crl
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-truststorerevocation--examples----json"></a>

```
{
    "myRevocationList": {
        "Type": "AWS::ElasticLoadBalancingV2::TrustStoreRevocation",
        "Properties": {
            "TrustStoreArn": {
                "Ref": "myTrustStore"
            },
            "RevocationContents": [
                {
                    "RevocationType": "CRL",
                    "S3Bucket": "amzn-s3-demo-bucket",
                    "S3Key": "crl/revoked-list.crl"
                }
            ]
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
