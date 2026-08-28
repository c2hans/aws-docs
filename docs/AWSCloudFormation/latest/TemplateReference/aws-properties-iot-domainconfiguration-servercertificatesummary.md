---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-domainconfiguration-servercertificatesummary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::DomainConfiguration ServerCertificateSummary
<a name="aws-properties-iot-domainconfiguration-servercertificatesummary"></a>

An object that contains information about a server certificate.

## Syntax
<a name="aws-properties-iot-domainconfiguration-servercertificatesummary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-domainconfiguration-servercertificatesummary-syntax.json"></a>

```
{
  "[ServerCertificateArn](#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatearn)" : {{String}},
  "[ServerCertificateStatus](#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatus)" : {{String}},
  "[ServerCertificateStatusDetail](#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatusdetail)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-domainconfiguration-servercertificatesummary-syntax.yaml"></a>

```
  [ServerCertificateArn](#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatearn): {{String}}
  [ServerCertificateStatus](#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatus): {{String}}
  [ServerCertificateStatusDetail](#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatusdetail): {{String}}
```

## Properties
<a name="aws-properties-iot-domainconfiguration-servercertificatesummary-properties"></a>

`ServerCertificateArn`  <a name="cfn-iot-domainconfiguration-servercertificatesummary-servercertificatearn"></a>
The ARN of the server certificate.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\d{1}:\d{12}:certificate/[a-zA-Z0-9/-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerCertificateStatus`  <a name="cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatus"></a>
The status of the server certificate.
*Required*: No
*Type*: String
*Allowed values*: `INVALID | VALID`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerCertificateStatusDetail`  <a name="cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatusdetail"></a>
Details that explain the status of the server certificate.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
