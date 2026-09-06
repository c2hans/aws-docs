---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspacesweb-truststore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::TrustStore
<a name="aws-resource-workspacesweb-truststore"></a>

This resource specifies a trust store that can be associated with a web portal. A trust store contains certificate authority (CA) certificates. Once associated with a web portal, the browser in a streaming session will recognize certificates that have been issued using any of the CAs in the trust store. If your organization has internal websites that use certificates issued by private CAs, you should add the private CA certificate to the trust store.

## Syntax
<a name="aws-resource-workspacesweb-truststore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspacesweb-truststore-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpacesWeb::TrustStore",
  "Properties" : {
      "[CertificateList](#cfn-workspacesweb-truststore-certificatelist)" : {{[ String, ... ]}},
      "[Tags](#cfn-workspacesweb-truststore-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-workspacesweb-truststore-syntax.yaml"></a>

```
Type: AWS::WorkSpacesWeb::TrustStore
Properties:
  [CertificateList](#cfn-workspacesweb-truststore-certificatelist): {{
    - String}}
  [Tags](#cfn-workspacesweb-truststore-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-workspacesweb-truststore-properties"></a>

`CertificateList`  <a name="cfn-workspacesweb-truststore-certificatelist"></a>
A list of CA certificates to be added to the trust store.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-workspacesweb-truststore-tags"></a>
The tags to add to the trust store. A tag is a key-value pair.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspacesweb-truststore-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspacesweb-truststore-return-values"></a>

### Ref
<a name="aws-resource-workspacesweb-truststore-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource's Amazon Resource Name (ARN).

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-workspacesweb-truststore-return-values-fn--getatt"></a>

####
<a name="aws-resource-workspacesweb-truststore-return-values-fn--getatt-fn--getatt"></a>

`AssociatedPortalArns`  <a name="AssociatedPortalArns-fn::getatt"></a>
A list of web portal ARNs that this trust store is associated with.

`TrustStoreArn`  <a name="TrustStoreArn-fn::getatt"></a>
The ARN of the trust store.
