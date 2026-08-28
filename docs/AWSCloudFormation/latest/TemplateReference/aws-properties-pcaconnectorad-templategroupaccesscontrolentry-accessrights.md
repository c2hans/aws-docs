---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorAD::TemplateGroupAccessControlEntry AccessRights
<a name="aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights"></a>

 Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.

## Syntax
<a name="aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights-syntax.json"></a>

```
{
  "[AutoEnroll](#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-autoenroll)" : {{String}},
  "[Enroll](#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-enroll)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights-syntax.yaml"></a>

```
  [AutoEnroll](#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-autoenroll): {{String}}
  [Enroll](#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-enroll): {{String}}
```

## Properties
<a name="aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights-properties"></a>

`AutoEnroll`  <a name="cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-autoenroll"></a>
Allow or deny an Active Directory group from autoenrolling certificates issued against a template. The Active Directory group must be allowed to enroll to allow autoenrollment
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enroll`  <a name="cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-enroll"></a>
Allow or deny an Active Directory group from enrolling certificates issued against a template.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
