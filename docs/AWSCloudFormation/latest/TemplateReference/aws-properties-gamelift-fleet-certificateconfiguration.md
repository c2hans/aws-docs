---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-fleet-certificateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Fleet CertificateConfiguration
<a name="aws-properties-gamelift-fleet-certificateconfiguration"></a>

Determines whether a TLS/SSL certificate is generated for a fleet. This feature must be enabled when creating the fleet. All instances in a fleet share the same certificate. The certificate can be retrieved by calling the [GameLift Server SDK](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html) operation `GetInstanceCertificate`.

## Syntax
<a name="aws-properties-gamelift-fleet-certificateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-fleet-certificateconfiguration-syntax.json"></a>

```
{
  "[CertificateType](#cfn-gamelift-fleet-certificateconfiguration-certificatetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-fleet-certificateconfiguration-syntax.yaml"></a>

```
  [CertificateType](#cfn-gamelift-fleet-certificateconfiguration-certificatetype): {{String}}
```

## Properties
<a name="aws-properties-gamelift-fleet-certificateconfiguration-properties"></a>

`CertificateType`  <a name="cfn-gamelift-fleet-certificateconfiguration-certificatetype"></a>
Indicates whether a TLS/SSL certificate is generated for a fleet.
Valid values include:
+ **GENERATED** - Generate a TLS/SSL certificate for this fleet.
+ **DISABLED** - (default) Do not generate a TLS/SSL certificate for this fleet.
*Required*: Yes
*Type*: String
*Allowed values*: `DISABLED | GENERATED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-gamelift-fleet-certificateconfiguration--seealso"></a>
+ [ Create GameLift resources using Amazon CloudFront](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Developer Guide*
+ [Deploy a GameLift fleet for a custom game build](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating.html) in the *Amazon GameLift Developer Guide*
+ [Deploy a Realtime Servers fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-fleets-creating.html) in the *Amazon GameLift Developer Guide*
+ [CertificateConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CertificateConfiguration.html) in the *Amazon GameLift API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
