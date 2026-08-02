---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-targetdomain-verificationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::TargetDomain VerificationDetails
<a name="aws-properties-securityagent-targetdomain-verificationdetails"></a>

Contains the verification details for a target domain, including the verification method and provider-specific details.

## Syntax
<a name="aws-properties-securityagent-targetdomain-verificationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-targetdomain-verificationdetails-syntax.json"></a>

```
{
  "[DnsTxt](#cfn-securityagent-targetdomain-verificationdetails-dnstxt)" : {{DnsVerification}},
  "[HttpRoute](#cfn-securityagent-targetdomain-verificationdetails-httproute)" : {{HttpVerification}},
  "[Method](#cfn-securityagent-targetdomain-verificationdetails-method)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-targetdomain-verificationdetails-syntax.yaml"></a>

```
  [DnsTxt](#cfn-securityagent-targetdomain-verificationdetails-dnstxt): {{
    DnsVerification}}
  [HttpRoute](#cfn-securityagent-targetdomain-verificationdetails-httproute): {{
    HttpVerification}}
  [Method](#cfn-securityagent-targetdomain-verificationdetails-method): {{String}}
```

## Properties
<a name="aws-properties-securityagent-targetdomain-verificationdetails-properties"></a>

`DnsTxt`  <a name="cfn-securityagent-targetdomain-verificationdetails-dnstxt"></a>
The DNS TXT verification details.
*Required*: No
*Type*: [DnsVerification](aws-properties-securityagent-targetdomain-dnsverification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpRoute`  <a name="cfn-securityagent-targetdomain-verificationdetails-httproute"></a>
The HTTP route verification details.
*Required*: No
*Type*: [HttpVerification](aws-properties-securityagent-targetdomain-httpverification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Method`  <a name="cfn-securityagent-targetdomain-verificationdetails-method"></a>
The verification method used for the target domain.
*Required*: No
*Type*: String
*Allowed values*: `DNS_TXT | HTTP_ROUTE | PRIVATE_VPC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
