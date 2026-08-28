---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanageringresspoint-truststore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerIngressPoint TrustStore
<a name="aws-properties-ses-mailmanageringresspoint-truststore"></a>

The trust store used for mutual TLS authentication. It contains the certificate authority (CA) certificates and optional certificate revocation list (CRL).

## Syntax
<a name="aws-properties-ses-mailmanageringresspoint-truststore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanageringresspoint-truststore-syntax.json"></a>

```
{
  "[CAContent](#cfn-ses-mailmanageringresspoint-truststore-cacontent)" : {{String}},
  "[CrlContent](#cfn-ses-mailmanageringresspoint-truststore-crlcontent)" : {{String}},
  "[KmsKeyArn](#cfn-ses-mailmanageringresspoint-truststore-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanageringresspoint-truststore-syntax.yaml"></a>

```
  [CAContent](#cfn-ses-mailmanageringresspoint-truststore-cacontent): {{String}}
  [CrlContent](#cfn-ses-mailmanageringresspoint-truststore-crlcontent): {{String}}
  [KmsKeyArn](#cfn-ses-mailmanageringresspoint-truststore-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanageringresspoint-truststore-properties"></a>

`CAContent`  <a name="cfn-ses-mailmanageringresspoint-truststore-cacontent"></a>
The PEM-encoded certificate authority (CA) certificates bundle for the trust store.
*Required*: Yes
*Type*: String
*Pattern*: `^[\P{C}\s]*$`
*Minimum*: `1`
*Maximum*: `500000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrlContent`  <a name="cfn-ses-mailmanageringresspoint-truststore-crlcontent"></a>
The PEM-encoded certificate revocation lists (CRLs) for the trust store. There can be one CRL per certificate authority (CA) in the trust store.
*Required*: No
*Type*: String
*Pattern*: `^[\P{C}\s]*$`
*Minimum*: `1`
*Maximum*: `500000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-ses-mailmanageringresspoint-truststore-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the trust store contents.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc):kms:[a-z0-9-]+:\d{12}:(key|alias)/[a-zA-Z0-9/_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
