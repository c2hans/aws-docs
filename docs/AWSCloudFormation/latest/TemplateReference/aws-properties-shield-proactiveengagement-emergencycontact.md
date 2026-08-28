---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-shield-proactiveengagement-emergencycontact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Shield::ProactiveEngagement EmergencyContact
<a name="aws-properties-shield-proactiveengagement-emergencycontact"></a>

Contact information that the SRT can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.

## Syntax
<a name="aws-properties-shield-proactiveengagement-emergencycontact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-shield-proactiveengagement-emergencycontact-syntax.json"></a>

```
{
  "[ContactNotes](#cfn-shield-proactiveengagement-emergencycontact-contactnotes)" : {{String}},
  "[EmailAddress](#cfn-shield-proactiveengagement-emergencycontact-emailaddress)" : {{String}},
  "[PhoneNumber](#cfn-shield-proactiveengagement-emergencycontact-phonenumber)" : {{String}}
}
```

### YAML
<a name="aws-properties-shield-proactiveengagement-emergencycontact-syntax.yaml"></a>

```
  [ContactNotes](#cfn-shield-proactiveengagement-emergencycontact-contactnotes): {{String}}
  [EmailAddress](#cfn-shield-proactiveengagement-emergencycontact-emailaddress): {{String}}
  [PhoneNumber](#cfn-shield-proactiveengagement-emergencycontact-phonenumber): {{String}}
```

## Properties
<a name="aws-properties-shield-proactiveengagement-emergencycontact-properties"></a>

`ContactNotes`  <a name="cfn-shield-proactiveengagement-emergencycontact-contactnotes"></a>
Additional notes regarding the contact.
*Required*: No
*Type*: String
*Pattern*: `^[\w\s\.\-,:/()+@]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailAddress`  <a name="cfn-shield-proactiveengagement-emergencycontact-emailaddress"></a>
The email address for the contact.
*Required*: Yes
*Type*: String
*Pattern*: `^\S+@\S+\.\S+$`
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhoneNumber`  <a name="cfn-shield-proactiveengagement-emergencycontact-phonenumber"></a>
The phone number for the contact.
*Required*: No
*Type*: String
*Pattern*: `^\+[1-9]\d{1,14}$`
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
