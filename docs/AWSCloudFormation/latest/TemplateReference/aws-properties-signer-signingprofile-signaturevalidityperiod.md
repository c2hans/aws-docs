---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-signer-signingprofile-signaturevalidityperiod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Signer::SigningProfile SignatureValidityPeriod
<a name="aws-properties-signer-signingprofile-signaturevalidityperiod"></a>

The validity period for the signing job.

## Syntax
<a name="aws-properties-signer-signingprofile-signaturevalidityperiod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-signer-signingprofile-signaturevalidityperiod-syntax.json"></a>

```
{
  "[Type](#cfn-signer-signingprofile-signaturevalidityperiod-type)" : {{String}},
  "[Value](#cfn-signer-signingprofile-signaturevalidityperiod-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-signer-signingprofile-signaturevalidityperiod-syntax.yaml"></a>

```
  [Type](#cfn-signer-signingprofile-signaturevalidityperiod-type): {{String}}
  [Value](#cfn-signer-signingprofile-signaturevalidityperiod-value): {{Integer}}
```

## Properties
<a name="aws-properties-signer-signingprofile-signaturevalidityperiod-properties"></a>

`Type`  <a name="cfn-signer-signingprofile-signaturevalidityperiod-type"></a>
The time unit for signature validity: DAYS \| MONTHS \| YEARS.
*Required*: No
*Type*: String
*Allowed values*: `DAYS | MONTHS | YEARS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-signer-signingprofile-signaturevalidityperiod-value"></a>
The numerical value of the time unit for signature validity.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
