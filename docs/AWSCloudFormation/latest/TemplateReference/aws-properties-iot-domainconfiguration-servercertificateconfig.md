---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-domainconfiguration-servercertificateconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::DomainConfiguration ServerCertificateConfig
<a name="aws-properties-iot-domainconfiguration-servercertificateconfig"></a>

The server certificate configuration.

For more information, see [Configurable endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable.html) from the AWS IoT Core Developer Guide.

## Syntax
<a name="aws-properties-iot-domainconfiguration-servercertificateconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-domainconfiguration-servercertificateconfig-syntax.json"></a>

```
{
  "[EnableOCSPCheck](#cfn-iot-domainconfiguration-servercertificateconfig-enableocspcheck)" : {{Boolean}},
  "[OcspAuthorizedResponderArn](#cfn-iot-domainconfiguration-servercertificateconfig-ocspauthorizedresponderarn)" : {{String}},
  "[OcspLambdaArn](#cfn-iot-domainconfiguration-servercertificateconfig-ocsplambdaarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-domainconfiguration-servercertificateconfig-syntax.yaml"></a>

```
  [EnableOCSPCheck](#cfn-iot-domainconfiguration-servercertificateconfig-enableocspcheck): {{Boolean}}
  [OcspAuthorizedResponderArn](#cfn-iot-domainconfiguration-servercertificateconfig-ocspauthorizedresponderarn): {{String}}
  [OcspLambdaArn](#cfn-iot-domainconfiguration-servercertificateconfig-ocsplambdaarn): {{String}}
```

## Properties
<a name="aws-properties-iot-domainconfiguration-servercertificateconfig-properties"></a>

`EnableOCSPCheck`  <a name="cfn-iot-domainconfiguration-servercertificateconfig-enableocspcheck"></a>
A Boolean value that indicates whether Online Certificate Status Protocol (OCSP) server certificate check is enabled or not. For more information, see [Configurable endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable.html) from the AWS IoT Core Developer Guide.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OcspAuthorizedResponderArn`  <a name="cfn-iot-domainconfiguration-servercertificateconfig-ocspauthorizedresponderarn"></a>
The Amazon Resource Name (ARN) for an X.509 certificate stored in ACM. If provided, AWS IoT Core will use this certificate to validate the signature of the received OCSP response. The OCSP responder must sign responses using either this authorized responder certificate or the issuing certificate, depending on whether the ARN is provided or not. The certificate must be in the same account and region as the domain configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\d{1}:\d{12}:certificate/[a-zA-Z0-9/-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OcspLambdaArn`  <a name="cfn-iot-domainconfiguration-servercertificateconfig-ocsplambdaarn"></a>
The Amazon Resource Name (ARN) for a Lambda function that acts as a Request for Comments (RFC) 6960-compliant Online Certificate Status Protocol (OCSP) responder, supporting basic OCSP responses. The Lambda function accepts a base64-encoding of the OCSP request in the Distinguished Encoding Rules (DER) format. The Lambda function's response is also a base64-encoded OCSP response in the DER format. The response size must not exceed 4 kilobytes (KiB). The Lambda function must be in the same account and region as the domain configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
