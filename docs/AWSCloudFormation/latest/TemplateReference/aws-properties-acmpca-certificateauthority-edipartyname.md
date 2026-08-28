---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-edipartyname.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority EdiPartyName
<a name="aws-properties-acmpca-certificateauthority-edipartyname"></a>

Describes an Electronic Data Interchange (EDI) entity as described in as defined in [Subject Alternative Name](https://datatracker.ietf.org/doc/html/rfc5280) in RFC 5280.

## Syntax
<a name="aws-properties-acmpca-certificateauthority-edipartyname-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-edipartyname-syntax.json"></a>

```
{
  "[NameAssigner](#cfn-acmpca-certificateauthority-edipartyname-nameassigner)" : {{String}},
  "[PartyName](#cfn-acmpca-certificateauthority-edipartyname-partyname)" : {{String}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-edipartyname-syntax.yaml"></a>

```
  [NameAssigner](#cfn-acmpca-certificateauthority-edipartyname-nameassigner): {{String}}
  [PartyName](#cfn-acmpca-certificateauthority-edipartyname-partyname): {{String}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-edipartyname-properties"></a>

`NameAssigner`  <a name="cfn-acmpca-certificateauthority-edipartyname-nameassigner"></a>
Specifies the name assigner.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PartyName`  <a name="cfn-acmpca-certificateauthority-edipartyname-partyname"></a>
Specifies the party name.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
