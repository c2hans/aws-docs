---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rolesanywhere-trustanchor-sourcedata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RolesAnywhere::TrustAnchor SourceData
<a name="aws-properties-rolesanywhere-trustanchor-sourcedata"></a>

 A union object representing the data field of the TrustAnchor depending on its type

## Syntax
<a name="aws-properties-rolesanywhere-trustanchor-sourcedata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rolesanywhere-trustanchor-sourcedata-syntax.json"></a>

```
{
  "[AcmPcaArn](#cfn-rolesanywhere-trustanchor-sourcedata-acmpcaarn)" : {{String}},
  "[X509CertificateData](#cfn-rolesanywhere-trustanchor-sourcedata-x509certificatedata)" : {{String}}
}
```

### YAML
<a name="aws-properties-rolesanywhere-trustanchor-sourcedata-syntax.yaml"></a>

```
  [AcmPcaArn](#cfn-rolesanywhere-trustanchor-sourcedata-acmpcaarn): {{String}}
  [X509CertificateData](#cfn-rolesanywhere-trustanchor-sourcedata-x509certificatedata): {{String}}
```

## Properties
<a name="aws-properties-rolesanywhere-trustanchor-sourcedata-properties"></a>

`AcmPcaArn`  <a name="cfn-rolesanywhere-trustanchor-sourcedata-acmpcaarn"></a>
 The root certificate of the AWS Private Certificate Authority specified by this ARN is used in trust validation for temporary credential requests. Included for trust anchors of type `AWS_ACM_PCA`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`X509CertificateData`  <a name="cfn-rolesanywhere-trustanchor-sourcedata-x509certificatedata"></a>
The PEM-encoded data for the certificate anchor. Included for trust anchors of type `CERTIFICATE_BUNDLE`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `8000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
