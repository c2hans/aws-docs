---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-registration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::Registration
<a name="aws-resource-smsvoice-registration"></a>

Creates a new registration based on the **RegistrationType** field.

## Syntax
<a name="aws-resource-smsvoice-registration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-registration-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::Registration",
  "Properties" : {
      "[RegistrationType](#cfn-smsvoice-registration-registrationtype)" : {{String}},
      "[Tags](#cfn-smsvoice-registration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-registration-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::Registration
Properties:
  [RegistrationType](#cfn-smsvoice-registration-registrationtype): {{String}}
  [Tags](#cfn-smsvoice-registration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-smsvoice-registration-properties"></a>

`RegistrationType`  <a name="cfn-smsvoice-registration-registrationtype"></a>
The type of registration form. The list of **RegistrationTypes** can be found using the DescribeRegistrationTypeDefinitions action.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-smsvoice-registration-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-registration-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-registration-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-registration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-smsvoice-registration-return-values-fn--getatt"></a>

####
<a name="aws-resource-smsvoice-registration-return-values-fn--getatt-fn--getatt"></a>

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
The time when the registration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.

`CurrentVersionNumber`  <a name="CurrentVersionNumber-fn::getatt"></a>
The current version number of the registration.

`RegistrationArn`  <a name="RegistrationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the registration.

`RegistrationId`  <a name="RegistrationId-fn::getatt"></a>
The unique identifier for the registration.

`RegistrationStatus`  <a name="RegistrationStatus-fn::getatt"></a>
The status of the registration.
+ `CLOSED`: The phone number or sender ID has been deleted and you must also delete the registration for the number.
+ `CREATED`: Your registration is created but not submitted.
+ `COMPLETE`: Your registration has been approved and your origination identity has been created.
+ `DELETED`: The registration has been deleted.
+ `PROVISIONING`: Your registration has been approved and your origination identity is being created.
+ `REQUIRES_AUTHENTICATION`: You need to complete email authentication.
+ `REQUIRES_UPDATES`: You must fix your registration and resubmit it.
+ `REVIEWING`: Your registration has been accepted and is being reviewed.
+ `SUBMITTED`: Your registration has been submitted and is awaiting review.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
