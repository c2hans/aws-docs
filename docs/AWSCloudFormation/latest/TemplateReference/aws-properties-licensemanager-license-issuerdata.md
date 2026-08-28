---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-license-issuerdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::License IssuerData
<a name="aws-properties-licensemanager-license-issuerdata"></a>

Details associated with the issuer of a license.

## Syntax
<a name="aws-properties-licensemanager-license-issuerdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-license-issuerdata-syntax.json"></a>

```
{
  "[Name](#cfn-licensemanager-license-issuerdata-name)" : {{String}},
  "[SignKey](#cfn-licensemanager-license-issuerdata-signkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-licensemanager-license-issuerdata-syntax.yaml"></a>

```
  [Name](#cfn-licensemanager-license-issuerdata-name): {{String}}
  [SignKey](#cfn-licensemanager-license-issuerdata-signkey): {{String}}
```

## Properties
<a name="aws-properties-licensemanager-license-issuerdata-properties"></a>

`Name`  <a name="cfn-licensemanager-license-issuerdata-name"></a>
Issuer name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SignKey`  <a name="cfn-licensemanager-license-issuerdata-signkey"></a>
Asymmetric KMS key from AWS Key Management Service. The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
