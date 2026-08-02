---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-truststorerevocation-truststorerevocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::TrustStoreRevocation TrustStoreRevocation
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-truststorerevocation"></a>

Information about a revocation file in use by a trust store.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-truststorerevocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-truststorerevocation-syntax.json"></a>

```
{
  "[NumberOfRevokedEntries](#cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-numberofrevokedentries)" : {{Integer}},
  "[RevocationId](#cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-revocationid)" : {{String}},
  "[RevocationType](#cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-revocationtype)" : {{String}},
  "[TrustStoreArn](#cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-truststorearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-truststorerevocation-syntax.yaml"></a>

```
  [NumberOfRevokedEntries](#cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-numberofrevokedentries): {{Integer}}
  [RevocationId](#cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-revocationid): {{String}}
  [RevocationType](#cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-revocationtype): {{String}}
  [TrustStoreArn](#cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-truststorearn): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-truststorerevocation-properties"></a>

`NumberOfRevokedEntries`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-numberofrevokedentries"></a>
The number of revoked certificates.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RevocationId`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-revocationid"></a>
The revocation ID of the revocation file.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RevocationType`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-revocationtype"></a>
The type of revocation file.
*Required*: No
*Type*: String
*Allowed values*: `CRL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrustStoreArn`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-truststorerevocation-truststorearn"></a>
The Amazon Resource Name (ARN) of the trust store.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
