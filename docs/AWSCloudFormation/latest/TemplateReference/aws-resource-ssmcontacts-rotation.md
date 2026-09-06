---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssmcontacts-rotation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Rotation
<a name="aws-resource-ssmcontacts-rotation"></a>

Specifies a rotation in an on-call schedule.

**Note**
**Template example**: We recommend creating all Incident Manager`Contacts` resources using a single AWS CloudFormation template. For a demonstration, see the examples for [AWS::SSMContacts::Contacts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html).

## Syntax
<a name="aws-resource-ssmcontacts-rotation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssmcontacts-rotation-syntax.json"></a>

```
{
  "Type" : "AWS::SSMContacts::Rotation",
  "Properties" : {
      "[ContactIds](#cfn-ssmcontacts-rotation-contactids)" : {{[ String, ... ]}},
      "[Name](#cfn-ssmcontacts-rotation-name)" : {{String}},
      "[Recurrence](#cfn-ssmcontacts-rotation-recurrence)" : {{RecurrenceSettings}},
      "[StartTime](#cfn-ssmcontacts-rotation-starttime)" : {{String}},
      "[Tags](#cfn-ssmcontacts-rotation-tags)" : {{[ Tag, ... ]}},
      "[TimeZoneId](#cfn-ssmcontacts-rotation-timezoneid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ssmcontacts-rotation-syntax.yaml"></a>

```
Type: AWS::SSMContacts::Rotation
Properties:
  [ContactIds](#cfn-ssmcontacts-rotation-contactids): {{
    - String}}
  [Name](#cfn-ssmcontacts-rotation-name): {{String}}
  [Recurrence](#cfn-ssmcontacts-rotation-recurrence): {{
    RecurrenceSettings}}
  [StartTime](#cfn-ssmcontacts-rotation-starttime): {{String}}
  [Tags](#cfn-ssmcontacts-rotation-tags): {{
    - Tag}}
  [TimeZoneId](#cfn-ssmcontacts-rotation-timezoneid): {{String}}
```

## Properties
<a name="aws-resource-ssmcontacts-rotation-properties"></a>

`ContactIds`  <a name="cfn-ssmcontacts-rotation-contactids"></a>
The Amazon Resource Names (ARNs) of the contacts to add to the rotation.
Only the `PERSONAL` contact type is supported. The contact types `ESCALATION` and `ONCALL_SCHEDULE` are not supported for this operation.
The order in which you list the contacts is their shift order in the rotation schedule.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ssmcontacts-rotation-name"></a>
The name for the rotation.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Recurrence`  <a name="cfn-ssmcontacts-rotation-recurrence"></a>
Information about the rule that specifies when shift team members rotate.
*Required*: Yes
*Type*: [RecurrenceSettings](aws-properties-ssmcontacts-rotation-recurrencesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-ssmcontacts-rotation-starttime"></a>
The date and time the rotation goes into effect.
*Required*: Yes
*Type*: String
*Pattern*: `^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ssmcontacts-rotation-tags"></a>
Optional metadata to assign to the rotation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For more information, see [Tagging Incident Manager resources](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html) in the *Incident Manager User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-ssmcontacts-rotation-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeZoneId`  <a name="cfn-ssmcontacts-rotation-timezoneid"></a>
The time zone to base the rotation’s activity on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los\_Angeles", "UTC", or "Asia/Seoul". For more information, see the [Time Zone Database](https://www.iana.org/time-zones) on the IANA website.
Designators for time zones that don’t support Daylight Savings Time rules, such as Pacific Standard Time (PST), are not supported.
*Required*: Yes
*Type*: String
*Pattern*: `^[:a-zA-Z0-9_\-\s\.\\/]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssmcontacts-rotation-return-values"></a>

### Ref
<a name="aws-resource-ssmcontacts-rotation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssmcontacts-rotation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ssmcontacts-rotation-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the `Rotation` resource.
