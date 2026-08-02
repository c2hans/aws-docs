---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sso-applicationprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::ApplicationProvider
<a name="aws-resource-sso-applicationprovider"></a>

A structure that describes a provider that can be used to connect an AWS managed application or customer managed application to IAM Identity Center.

## Syntax
<a name="aws-resource-sso-applicationprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sso-applicationprovider-syntax.json"></a>

```
{
  "Type" : "AWS::SSO::ApplicationProvider"
}
```

### YAML
<a name="aws-resource-sso-applicationprovider-syntax.yaml"></a>

```
Type: AWS::SSO::ApplicationProvider
```

## Return values
<a name="aws-resource-sso-applicationprovider-return-values"></a>

### Ref
<a name="aws-resource-sso-applicationprovider-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sso-applicationprovider-return-values-fn--getatt"></a>

####
<a name="aws-resource-sso-applicationprovider-return-values-fn--getatt-fn--getatt"></a>

`ApplicationProviderArn`  <a name="ApplicationProviderArn-fn::getatt"></a>
The ARN of the application provider.

`FederationProtocol`  <a name="FederationProtocol-fn::getatt"></a>
The protocol that the application provider uses to perform federation.
