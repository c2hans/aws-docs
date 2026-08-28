---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-accessdescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority AccessDescription
<a name="aws-properties-acmpca-certificateauthority-accessdescription"></a>

Provides access information used by the `authorityInfoAccess` and `subjectInfoAccess` extensions described in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280).

## Syntax
<a name="aws-properties-acmpca-certificateauthority-accessdescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-accessdescription-syntax.json"></a>

```
{
  "[AccessLocation](#cfn-acmpca-certificateauthority-accessdescription-accesslocation)" : {{GeneralName}},
  "[AccessMethod](#cfn-acmpca-certificateauthority-accessdescription-accessmethod)" : {{AccessMethod}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-accessdescription-syntax.yaml"></a>

```
  [AccessLocation](#cfn-acmpca-certificateauthority-accessdescription-accesslocation): {{
    GeneralName}}
  [AccessMethod](#cfn-acmpca-certificateauthority-accessdescription-accessmethod): {{
    AccessMethod}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-accessdescription-properties"></a>

`AccessLocation`  <a name="cfn-acmpca-certificateauthority-accessdescription-accesslocation"></a>
The location of `AccessDescription` information.
*Required*: Yes
*Type*: [GeneralName](aws-properties-acmpca-certificateauthority-generalname.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AccessMethod`  <a name="cfn-acmpca-certificateauthority-accessdescription-accessmethod"></a>
The type and format of `AccessDescription` information.
*Required*: Yes
*Type*: [AccessMethod](aws-properties-acmpca-certificateauthority-accessmethod.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
