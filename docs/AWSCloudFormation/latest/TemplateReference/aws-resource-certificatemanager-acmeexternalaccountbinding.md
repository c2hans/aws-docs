---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-certificatemanager-acmeexternalaccountbinding.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeExternalAccountBinding
<a name="aws-resource-certificatemanager-acmeexternalaccountbinding"></a>

Creates an external account binding (EAB) for an ACME endpoint. An EAB provides credentials that authorize an ACME client to register an account with the endpoint. Each EAB is associated with an IAM role that controls what certificate operations the ACME client can perform.

## Syntax
<a name="aws-resource-certificatemanager-acmeexternalaccountbinding-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-certificatemanager-acmeexternalaccountbinding-syntax.json"></a>

```
{
  "Type" : "AWS::CertificateManager::AcmeExternalAccountBinding",
  "Properties" : {
      "[AcmeEndpointArn](#cfn-certificatemanager-acmeexternalaccountbinding-acmeendpointarn)" : {{String}},
      "[Expiration](#cfn-certificatemanager-acmeexternalaccountbinding-expiration)" : {{Expiration}},
      "[RoleArn](#cfn-certificatemanager-acmeexternalaccountbinding-rolearn)" : {{String}},
      "[Tags](#cfn-certificatemanager-acmeexternalaccountbinding-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-certificatemanager-acmeexternalaccountbinding-syntax.yaml"></a>

```
Type: AWS::CertificateManager::AcmeExternalAccountBinding
Properties:
  [AcmeEndpointArn](#cfn-certificatemanager-acmeexternalaccountbinding-acmeendpointarn): {{String}}
  [Expiration](#cfn-certificatemanager-acmeexternalaccountbinding-expiration): {{
    Expiration}}
  [RoleArn](#cfn-certificatemanager-acmeexternalaccountbinding-rolearn): {{String}}
  [Tags](#cfn-certificatemanager-acmeexternalaccountbinding-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-certificatemanager-acmeexternalaccountbinding-properties"></a>

`AcmeEndpointArn`  <a name="cfn-certificatemanager-acmeexternalaccountbinding-acmeendpointarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Expiration`  <a name="cfn-certificatemanager-acmeexternalaccountbinding-expiration"></a>
Specifies an expiration configuration.
*Required*: No
*Type*: [Expiration](aws-properties-certificatemanager-acmeexternalaccountbinding-expiration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-certificatemanager-acmeexternalaccountbinding-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-certificatemanager-acmeexternalaccountbinding-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-certificatemanager-acmeexternalaccountbinding-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-certificatemanager-acmeexternalaccountbinding-return-values"></a>

### Ref
<a name="aws-resource-certificatemanager-acmeexternalaccountbinding-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-certificatemanager-acmeexternalaccountbinding-return-values-fn--getatt"></a>

####
<a name="aws-resource-certificatemanager-acmeexternalaccountbinding-return-values-fn--getatt-fn--getatt"></a>

`AcmeExternalAccountBindingArn`  <a name="AcmeExternalAccountBindingArn-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
