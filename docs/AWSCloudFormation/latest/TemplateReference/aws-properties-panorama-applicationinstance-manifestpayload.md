---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-panorama-applicationinstance-manifestpayload.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Panorama::ApplicationInstance ManifestPayload
<a name="aws-properties-panorama-applicationinstance-manifestpayload"></a>

A application verion's manifest file. This is a JSON document that has a single key (`PayloadData`) where the value is an escaped string representation of the application manifest (`graph.json`). This file is located in the `graphs` folder in your application source.

## Syntax
<a name="aws-properties-panorama-applicationinstance-manifestpayload-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-panorama-applicationinstance-manifestpayload-syntax.json"></a>

```
{
  "[PayloadData](#cfn-panorama-applicationinstance-manifestpayload-payloaddata)" : {{String}}
}
```

### YAML
<a name="aws-properties-panorama-applicationinstance-manifestpayload-syntax.yaml"></a>

```
  [PayloadData](#cfn-panorama-applicationinstance-manifestpayload-payloaddata): {{String}}
```

## Properties
<a name="aws-properties-panorama-applicationinstance-manifestpayload-properties"></a>

`PayloadData`  <a name="cfn-panorama-applicationinstance-manifestpayload-payloaddata"></a>
The application manifest.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `51200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
