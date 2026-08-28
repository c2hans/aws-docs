---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint CertificateAuthenticationRequest
<a name="aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest"></a>

Information about the client certificate to be used for authentication.

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest-syntax.json"></a>

```
{
  "[ClientRootCertificateChainArn](#cfn-ec2-clientvpnendpoint-certificateauthenticationrequest-clientrootcertificatechainarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest-syntax.yaml"></a>

```
  [ClientRootCertificateChainArn](#cfn-ec2-clientvpnendpoint-certificateauthenticationrequest-clientrootcertificatechainarn): {{String}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest-properties"></a>

`ClientRootCertificateChainArn`  <a name="cfn-ec2-clientvpnendpoint-certificateauthenticationrequest-clientrootcertificatechainarn"></a>
The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in AWS Certificate Manager (ACM).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
