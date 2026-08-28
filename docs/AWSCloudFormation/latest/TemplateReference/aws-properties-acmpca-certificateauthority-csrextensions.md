---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-csrextensions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority CsrExtensions
<a name="aws-properties-acmpca-certificateauthority-csrextensions"></a>

Describes the certificate extensions to be added to the certificate signing request (CSR).

## Syntax
<a name="aws-properties-acmpca-certificateauthority-csrextensions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-csrextensions-syntax.json"></a>

```
{
  "[KeyUsage](#cfn-acmpca-certificateauthority-csrextensions-keyusage)" : {{KeyUsage}},
  "[SubjectInformationAccess](#cfn-acmpca-certificateauthority-csrextensions-subjectinformationaccess)" : {{[ AccessDescription, ... ]}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-csrextensions-syntax.yaml"></a>

```
  [KeyUsage](#cfn-acmpca-certificateauthority-csrextensions-keyusage): {{
    KeyUsage}}
  [SubjectInformationAccess](#cfn-acmpca-certificateauthority-csrextensions-subjectinformationaccess): {{
    - AccessDescription}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-csrextensions-properties"></a>

`KeyUsage`  <a name="cfn-acmpca-certificateauthority-csrextensions-keyusage"></a>
Indicates the purpose of the certificate and of the key contained in the certificate.
*Required*: No
*Type*: [KeyUsage](aws-properties-acmpca-certificateauthority-keyusage.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubjectInformationAccess`  <a name="cfn-acmpca-certificateauthority-csrextensions-subjectinformationaccess"></a>
For CA certificates, provides a path to additional information pertaining to the CA, such as revocation and policy. For more information, see [Subject Information Access](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.2) in RFC 5280.
*Required*: No
*Type*: Array of [AccessDescription](aws-properties-acmpca-certificateauthority-accessdescription.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
