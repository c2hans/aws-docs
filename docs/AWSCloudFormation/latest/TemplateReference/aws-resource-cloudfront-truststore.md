---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-truststore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::TrustStore
<a name="aws-resource-cloudfront-truststore"></a>

A trust store.

## Syntax
<a name="aws-resource-cloudfront-truststore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-truststore-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::TrustStore",
  "Properties" : {
      "[CaCertificatesBundleSource](#cfn-cloudfront-truststore-cacertificatesbundlesource)" : {{CaCertificatesBundleSource}},
      "[Name](#cfn-cloudfront-truststore-name)" : {{String}},
      "[Tags](#cfn-cloudfront-truststore-tags)" : {{[ Tag, ... ]}},
      "[UseClientCertificateOCSPEndpoint](#cfn-cloudfront-truststore-useclientcertificateocspendpoint)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-truststore-syntax.yaml"></a>

```
Type: AWS::CloudFront::TrustStore
Properties:
  [CaCertificatesBundleSource](#cfn-cloudfront-truststore-cacertificatesbundlesource): {{
    CaCertificatesBundleSource}}
  [Name](#cfn-cloudfront-truststore-name): {{String}}
  [Tags](#cfn-cloudfront-truststore-tags): {{
    - Tag}}
  [UseClientCertificateOCSPEndpoint](#cfn-cloudfront-truststore-useclientcertificateocspendpoint): {{Boolean}}
```

## Properties
<a name="aws-resource-cloudfront-truststore-properties"></a>

`CaCertificatesBundleSource`  <a name="cfn-cloudfront-truststore-cacertificatesbundlesource"></a>
A CA certificates bundle source.
*Required*: No
*Type*: [CaCertificatesBundleSource](aws-properties-cloudfront-truststore-cacertificatesbundlesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudfront-truststore-name"></a>
The trust store's name.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudfront-truststore-tags"></a>
A complex type that contains zero or more `Tag` elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudfront-truststore-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseClientCertificateOCSPEndpoint`  <a name="cfn-cloudfront-truststore-useclientcertificateocspendpoint"></a>
A boolean. When true, performs real-time certificate revocation checks by querying the OCSP endpoint specified within the client certificate.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-truststore-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-truststore-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudfront-truststore-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudfront-truststore-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The trust store's Amazon Resource Name (ARN).

`ETag`  <a name="ETag-fn::getatt"></a>
The version identifier for the current version of the trust store.

`Id`  <a name="Id-fn::getatt"></a>
The trust store's ID.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The trust store's last modified time.

`NumberOfCaCertificates`  <a name="NumberOfCaCertificates-fn::getatt"></a>
The trust store's number of CA certificates.

`Status`  <a name="Status-fn::getatt"></a>
The trust store's status.
