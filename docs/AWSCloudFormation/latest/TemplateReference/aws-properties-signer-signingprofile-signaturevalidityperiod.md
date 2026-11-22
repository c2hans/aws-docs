---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-signer-signingprofile-signaturevalidityperiod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Signer::SigningProfile SignatureValidityPeriod

The validity period for the signing job.

## Syntax
<a name="aws-properties-signer-signingprofile-signaturevalidityperiod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-signer-signingprofile-signaturevalidityperiod-syntax.json"></a>

```json
{
  "[Type](#cfn-signer-signingprofile-signaturevalidityperiod-type)" : {{String}},
  "[Value](#cfn-signer-signingprofile-signaturevalidityperiod-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-signer-signingprofile-signaturevalidityperiod-syntax.yaml"></a>

```yaml
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
