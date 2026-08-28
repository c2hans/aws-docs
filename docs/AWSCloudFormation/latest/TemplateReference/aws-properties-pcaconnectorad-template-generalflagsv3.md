---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcaconnectorad-template-generalflagsv3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorAD::Template GeneralFlagsV3
<a name="aws-properties-pcaconnectorad-template-generalflagsv3"></a>

General flags for v3 template schema that defines if the template is for a machine or a user and if the template can be issued using autoenrollment.

## Syntax
<a name="aws-properties-pcaconnectorad-template-generalflagsv3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcaconnectorad-template-generalflagsv3-syntax.json"></a>

```
{
  "[AutoEnrollment](#cfn-pcaconnectorad-template-generalflagsv3-autoenrollment)" : {{Boolean}},
  "[MachineType](#cfn-pcaconnectorad-template-generalflagsv3-machinetype)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-pcaconnectorad-template-generalflagsv3-syntax.yaml"></a>

```
  [AutoEnrollment](#cfn-pcaconnectorad-template-generalflagsv3-autoenrollment): {{Boolean}}
  [MachineType](#cfn-pcaconnectorad-template-generalflagsv3-machinetype): {{Boolean}}
```

## Properties
<a name="aws-properties-pcaconnectorad-template-generalflagsv3-properties"></a>

`AutoEnrollment`  <a name="cfn-pcaconnectorad-template-generalflagsv3-autoenrollment"></a>
Allows certificate issuance using autoenrollment. Set to TRUE to allow autoenrollment.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MachineType`  <a name="cfn-pcaconnectorad-template-generalflagsv3-machinetype"></a>
Defines if the template is for machines or users. Set to TRUE if the template is for machines. Set to FALSE if the template is for users
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
