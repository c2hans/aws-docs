---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-delivertoqbusinessaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet DeliverToQBusinessAction
<a name="aws-properties-ses-mailmanagerruleset-delivertoqbusinessaction"></a>

The action to deliver incoming emails to an Amazon Q Business application for indexing.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-delivertoqbusinessaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-delivertoqbusinessaction-syntax.json"></a>

```
{
  "[ActionFailurePolicy](#cfn-ses-mailmanagerruleset-delivertoqbusinessaction-actionfailurepolicy)" : {{String}},
  "[ApplicationId](#cfn-ses-mailmanagerruleset-delivertoqbusinessaction-applicationid)" : {{String}},
  "[IndexId](#cfn-ses-mailmanagerruleset-delivertoqbusinessaction-indexid)" : {{String}},
  "[RoleArn](#cfn-ses-mailmanagerruleset-delivertoqbusinessaction-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-delivertoqbusinessaction-syntax.yaml"></a>

```
  [ActionFailurePolicy](#cfn-ses-mailmanagerruleset-delivertoqbusinessaction-actionfailurepolicy): {{String}}
  [ApplicationId](#cfn-ses-mailmanagerruleset-delivertoqbusinessaction-applicationid): {{String}}
  [IndexId](#cfn-ses-mailmanagerruleset-delivertoqbusinessaction-indexid): {{String}}
  [RoleArn](#cfn-ses-mailmanagerruleset-delivertoqbusinessaction-rolearn): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-delivertoqbusinessaction-properties"></a>

`ActionFailurePolicy`  <a name="cfn-ses-mailmanagerruleset-delivertoqbusinessaction-actionfailurepolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified application has been deleted or the role lacks necessary permissions to call the `qbusiness:BatchPutDocument` API.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationId`  <a name="cfn-ses-mailmanagerruleset-delivertoqbusinessaction-applicationid"></a>
The unique identifier of the Amazon Q Business application instance where the email content will be delivered.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexId`  <a name="cfn-ses-mailmanagerruleset-delivertoqbusinessaction-indexid"></a>
The identifier of the knowledge base index within the Amazon Q Business application where the email content will be stored and indexed.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ses-mailmanagerruleset-delivertoqbusinessaction-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM Role to use while delivering to Amazon Q Business. This role must have access to the `qbusiness:BatchPutDocument` API for the given application and index.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
