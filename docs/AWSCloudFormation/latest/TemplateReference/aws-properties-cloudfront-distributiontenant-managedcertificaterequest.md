---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distributiontenant-managedcertificaterequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::DistributionTenant ManagedCertificateRequest
<a name="aws-properties-cloudfront-distributiontenant-managedcertificaterequest"></a>

An object that represents the request for the Amazon CloudFront managed ACM certificate.

## Syntax
<a name="aws-properties-cloudfront-distributiontenant-managedcertificaterequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distributiontenant-managedcertificaterequest-syntax.json"></a>

```
{
  "[CertificateTransparencyLoggingPreference](#cfn-cloudfront-distributiontenant-managedcertificaterequest-certificatetransparencyloggingpreference)" : {{String}},
  "[PrimaryDomainName](#cfn-cloudfront-distributiontenant-managedcertificaterequest-primarydomainname)" : {{String}},
  "[ValidationTokenHost](#cfn-cloudfront-distributiontenant-managedcertificaterequest-validationtokenhost)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distributiontenant-managedcertificaterequest-syntax.yaml"></a>

```
  [CertificateTransparencyLoggingPreference](#cfn-cloudfront-distributiontenant-managedcertificaterequest-certificatetransparencyloggingpreference): {{String}}
  [PrimaryDomainName](#cfn-cloudfront-distributiontenant-managedcertificaterequest-primarydomainname): {{String}}
  [ValidationTokenHost](#cfn-cloudfront-distributiontenant-managedcertificaterequest-validationtokenhost): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distributiontenant-managedcertificaterequest-properties"></a>

`CertificateTransparencyLoggingPreference`  <a name="cfn-cloudfront-distributiontenant-managedcertificaterequest-certificatetransparencyloggingpreference"></a>
You can opt out of certificate transparency logging by specifying the `disabled` option. Opt in by specifying `enabled`. For more information, see [Certificate Transparency Logging ](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency) in the *AWS Certificate Manager User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `enabled | disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryDomainName`  <a name="cfn-cloudfront-distributiontenant-managedcertificaterequest-primarydomainname"></a>
The primary domain name associated with the CloudFront managed ACM certificate.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidationTokenHost`  <a name="cfn-cloudfront-distributiontenant-managedcertificaterequest-validationtokenhost"></a>
Specify how the HTTP validation token will be served when requesting the CloudFront managed ACM certificate.
+ For `cloudfront`, CloudFront will automatically serve the validation token. Choose this mode if you can point the domain's DNS to CloudFront immediately.
+ For `self-hosted`, you serve the validation token from your existing infrastructure. Choose this mode when you need to maintain current traffic flow while your certificate is being issued. You can place the validation token at the well-known path on your existing web server, wait for ACM to validate and issue the certificate, and then update your DNS to point to CloudFront.
*Required*: No
*Type*: String
*Allowed values*: `cloudfront | self-hosted`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
