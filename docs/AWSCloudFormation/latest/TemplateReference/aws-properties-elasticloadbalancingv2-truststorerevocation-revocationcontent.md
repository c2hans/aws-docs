---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-truststorerevocation-revocationcontent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::TrustStoreRevocation RevocationContent
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-revocationcontent"></a>

Information about a revocation file. You must specify `S3Bucket` and `S3Key`.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-revocationcontent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-revocationcontent-syntax.json"></a>

```
{
  "[RevocationType](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-revocationtype)" : {{String}},
  "[S3Bucket](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-s3bucket)" : {{String}},
  "[S3Key](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-s3key)" : {{String}},
  "[S3ObjectVersion](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-s3objectversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-revocationcontent-syntax.yaml"></a>

```
  [RevocationType](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-revocationtype): {{String}}
  [S3Bucket](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-s3bucket): {{String}}
  [S3Key](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-s3key): {{String}}
  [S3ObjectVersion](#cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-s3objectversion): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-truststorerevocation-revocationcontent-properties"></a>

`RevocationType`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-revocationtype"></a>
The type of revocation file.
*Required*: No
*Type*: String
*Allowed values*: `CRL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Bucket`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-s3bucket"></a>
The Amazon S3 bucket for the revocation file.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Key`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-s3key"></a>
The Amazon S3 path for the revocation file.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3ObjectVersion`  <a name="cfn-elasticloadbalancingv2-truststorerevocation-revocationcontent-s3objectversion"></a>
The Amazon S3 object version of the revocation file.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
