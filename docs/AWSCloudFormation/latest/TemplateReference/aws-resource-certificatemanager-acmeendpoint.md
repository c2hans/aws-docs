---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-certificatemanager-acmeendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeEndpoint
<a name="aws-resource-certificatemanager-acmeendpoint"></a>

Contains detailed information about an ACME endpoint.

## Syntax
<a name="aws-resource-certificatemanager-acmeendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-certificatemanager-acmeendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::CertificateManager::AcmeEndpoint",
  "Properties" : {
      "[AuthorizationBehavior](#cfn-certificatemanager-acmeendpoint-authorizationbehavior)" : {{String}},
      "[CertificateAuthority](#cfn-certificatemanager-acmeendpoint-certificateauthority)" : {{CertificateAuthority}},
      "[CertificateTags](#cfn-certificatemanager-acmeendpoint-certificatetags)" : {{[ Tag, ... ]}},
      "[Contact](#cfn-certificatemanager-acmeendpoint-contact)" : {{String}},
      "[Tags](#cfn-certificatemanager-acmeendpoint-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-certificatemanager-acmeendpoint-syntax.yaml"></a>

```
Type: AWS::CertificateManager::AcmeEndpoint
Properties:
  [AuthorizationBehavior](#cfn-certificatemanager-acmeendpoint-authorizationbehavior): {{String}}
  [CertificateAuthority](#cfn-certificatemanager-acmeendpoint-certificateauthority): {{
    CertificateAuthority}}
  [CertificateTags](#cfn-certificatemanager-acmeendpoint-certificatetags): {{
    - Tag}}
  [Contact](#cfn-certificatemanager-acmeendpoint-contact): {{String}}
  [Tags](#cfn-certificatemanager-acmeendpoint-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-certificatemanager-acmeendpoint-properties"></a>

`AuthorizationBehavior`  <a name="cfn-certificatemanager-acmeendpoint-authorizationbehavior"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CertificateAuthority`  <a name="cfn-certificatemanager-acmeendpoint-certificateauthority"></a>
Defines the certificate authority to use for an ACME endpoint.
*Required*: Yes
*Type*: [CertificateAuthority](aws-properties-certificatemanager-acmeendpoint-certificateauthority.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateTags`  <a name="cfn-certificatemanager-acmeendpoint-certificatetags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-certificatemanager-acmeendpoint-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Contact`  <a name="cfn-certificatemanager-acmeendpoint-contact"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-certificatemanager-acmeendpoint-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-certificatemanager-acmeendpoint-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-certificatemanager-acmeendpoint-return-values"></a>

### Ref
<a name="aws-resource-certificatemanager-acmeendpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-certificatemanager-acmeendpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-certificatemanager-acmeendpoint-return-values-fn--getatt-fn--getatt"></a>

`AcmeEndpointArn`  <a name="AcmeEndpointArn-fn::getatt"></a>
Property description not available.

`EndpointUrl`  <a name="EndpointUrl-fn::getatt"></a>
Property description not available.
