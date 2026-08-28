---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-ocspconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority OcspConfiguration
<a name="aws-properties-acmpca-certificateauthority-ocspconfiguration"></a>

Contains information to enable and configure Online Certificate Status Protocol (OCSP) for validating certificate revocation status.

## Syntax
<a name="aws-properties-acmpca-certificateauthority-ocspconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-ocspconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-acmpca-certificateauthority-ocspconfiguration-enabled)" : {{Boolean}},
  "[OcspCustomCname](#cfn-acmpca-certificateauthority-ocspconfiguration-ocspcustomcname)" : {{String}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-ocspconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-acmpca-certificateauthority-ocspconfiguration-enabled): {{Boolean}}
  [OcspCustomCname](#cfn-acmpca-certificateauthority-ocspconfiguration-ocspcustomcname): {{String}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-ocspconfiguration-properties"></a>

`Enabled`  <a name="cfn-acmpca-certificateauthority-ocspconfiguration-enabled"></a>
Flag enabling use of the Online Certificate Status Protocol (OCSP) for validating certificate revocation status.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OcspCustomCname`  <a name="cfn-acmpca-certificateauthority-ocspconfiguration-ocspcustomcname"></a>
By default, AWS Private CA injects an Amazon domain into certificates being validated by the Online Certificate Status Protocol (OCSP). A customer can alternatively use this object to define a CNAME specifying a customized OCSP domain.
The content of a Canonical Name (CNAME) record must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".
*Required*: No
*Type*: String
*Pattern*: `[-a-zA-Z0-9;/?:@&=+$,%_.!~*()']*`
*Minimum*: `0`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
