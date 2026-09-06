---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-archiveaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet ArchiveAction
<a name="aws-properties-ses-mailmanagerruleset-archiveaction"></a>

The action to archive the email by delivering the email to an Amazon SES archive.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-archiveaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-archiveaction-syntax.json"></a>

```
{
  "[ActionFailurePolicy](#cfn-ses-mailmanagerruleset-archiveaction-actionfailurepolicy)" : {{String}},
  "[TargetArchive](#cfn-ses-mailmanagerruleset-archiveaction-targetarchive)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-archiveaction-syntax.yaml"></a>

```
  [ActionFailurePolicy](#cfn-ses-mailmanagerruleset-archiveaction-actionfailurepolicy): {{String}}
  [TargetArchive](#cfn-ses-mailmanagerruleset-archiveaction-targetarchive): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-archiveaction-properties"></a>

`ActionFailurePolicy`  <a name="cfn-ses-mailmanagerruleset-archiveaction-actionfailurepolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified archive has been deleted.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArchive`  <a name="cfn-ses-mailmanagerruleset-archiveaction-targetarchive"></a>
The identifier of the archive to send the email to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
