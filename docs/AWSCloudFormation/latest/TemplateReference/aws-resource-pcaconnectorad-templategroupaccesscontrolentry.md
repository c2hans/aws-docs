---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorAD::TemplateGroupAccessControlEntry
<a name="aws-resource-pcaconnectorad-templategroupaccesscontrolentry"></a>

Create a group access control entry. Allow or deny Active Directory groups from enrolling and/or autoenrolling with the template based on the group security identifiers (SIDs).

## Syntax
<a name="aws-resource-pcaconnectorad-templategroupaccesscontrolentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pcaconnectorad-templategroupaccesscontrolentry-syntax.json"></a>

```
{
  "Type" : "AWS::PCAConnectorAD::TemplateGroupAccessControlEntry",
  "Properties" : {
      "[AccessRights](#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights)" : {{AccessRights}},
      "[GroupDisplayName](#cfn-pcaconnectorad-templategroupaccesscontrolentry-groupdisplayname)" : {{String}},
      "[GroupSecurityIdentifier](#cfn-pcaconnectorad-templategroupaccesscontrolentry-groupsecurityidentifier)" : {{String}},
      "[TemplateArn](#cfn-pcaconnectorad-templategroupaccesscontrolentry-templatearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pcaconnectorad-templategroupaccesscontrolentry-syntax.yaml"></a>

```
Type: AWS::PCAConnectorAD::TemplateGroupAccessControlEntry
Properties:
  [AccessRights](#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights): {{
    AccessRights}}
  [GroupDisplayName](#cfn-pcaconnectorad-templategroupaccesscontrolentry-groupdisplayname): {{String}}
  [GroupSecurityIdentifier](#cfn-pcaconnectorad-templategroupaccesscontrolentry-groupsecurityidentifier): {{String}}
  [TemplateArn](#cfn-pcaconnectorad-templategroupaccesscontrolentry-templatearn): {{String}}
```

## Properties
<a name="aws-resource-pcaconnectorad-templategroupaccesscontrolentry-properties"></a>

`AccessRights`  <a name="cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights"></a>
Permissions to allow or deny an Active Directory group to enroll or autoenroll certificates issued against a template.
*Required*: Yes
*Type*: [AccessRights](aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupDisplayName`  <a name="cfn-pcaconnectorad-templategroupaccesscontrolentry-groupdisplayname"></a>
Name of the Active Directory group. This name does not need to match the group name in Active Directory.
*Required*: Yes
*Type*: String
*Pattern*: `^[\x20-\x7E]+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupSecurityIdentifier`  <a name="cfn-pcaconnectorad-templategroupaccesscontrolentry-groupsecurityidentifier"></a>
Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".
*Required*: Yes
*Type*: String
*Pattern*: `^S-[0-9]-([0-9]+-){1,14}[0-9]+$`
*Minimum*: `7`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TemplateArn`  <a name="cfn-pcaconnectorad-templategroupaccesscontrolentry-templatearn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector(\/[\w-]+)\/template(\/[\w-]+)$`
*Minimum*: `5`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
