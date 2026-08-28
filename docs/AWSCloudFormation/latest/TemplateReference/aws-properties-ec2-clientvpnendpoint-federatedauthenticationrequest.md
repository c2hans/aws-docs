---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint FederatedAuthenticationRequest
<a name="aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest"></a>

The IAM SAML identity provider used for federated authentication.

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest-syntax.json"></a>

```
{
  "[SAMLProviderArn](#cfn-ec2-clientvpnendpoint-federatedauthenticationrequest-samlproviderarn)" : {{String}},
  "[SelfServiceSAMLProviderArn](#cfn-ec2-clientvpnendpoint-federatedauthenticationrequest-selfservicesamlproviderarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest-syntax.yaml"></a>

```
  [SAMLProviderArn](#cfn-ec2-clientvpnendpoint-federatedauthenticationrequest-samlproviderarn): {{String}}
  [SelfServiceSAMLProviderArn](#cfn-ec2-clientvpnendpoint-federatedauthenticationrequest-selfservicesamlproviderarn): {{String}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest-properties"></a>

`SAMLProviderArn`  <a name="cfn-ec2-clientvpnendpoint-federatedauthenticationrequest-samlproviderarn"></a>
The Amazon Resource Name (ARN) of the IAM SAML identity provider.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SelfServiceSAMLProviderArn`  <a name="cfn-ec2-clientvpnendpoint-federatedauthenticationrequest-selfservicesamlproviderarn"></a>
The Amazon Resource Name (ARN) of the IAM SAML identity provider for the self-service portal.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
