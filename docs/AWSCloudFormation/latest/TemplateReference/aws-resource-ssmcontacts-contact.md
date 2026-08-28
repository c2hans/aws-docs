---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssmcontacts-contact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Contact
<a name="aws-resource-ssmcontacts-contact"></a>

The `AWS::SSMContacts::Contact` resource specifies a contact or escalation plan. Incident Manager contacts are a subset of actions and data types that you can use for managing responder engagement and interaction.

## Syntax
<a name="aws-resource-ssmcontacts-contact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssmcontacts-contact-syntax.json"></a>

```
{
  "Type" : "AWS::SSMContacts::Contact",
  "Properties" : {
      "[Alias](#cfn-ssmcontacts-contact-alias)" : {{String}},
      "[DisplayName](#cfn-ssmcontacts-contact-displayname)" : {{String}},
      "[Plan](#cfn-ssmcontacts-contact-plan)" : {{[ Stage, ... ]}},
      "[Tags](#cfn-ssmcontacts-contact-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-ssmcontacts-contact-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ssmcontacts-contact-syntax.yaml"></a>

```
Type: AWS::SSMContacts::Contact
Properties:
  [Alias](#cfn-ssmcontacts-contact-alias): {{String}}
  [DisplayName](#cfn-ssmcontacts-contact-displayname): {{String}}
  [Plan](#cfn-ssmcontacts-contact-plan): {{
    - Stage}}
  [Tags](#cfn-ssmcontacts-contact-tags): {{
    - Tag}}
  [Type](#cfn-ssmcontacts-contact-type): {{String}}
```

## Properties
<a name="aws-resource-ssmcontacts-contact-properties"></a>

`Alias`  <a name="cfn-ssmcontacts-contact-alias"></a>
The unique and identifiable alias of the contact or escalation plan.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9_\-\.]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DisplayName`  <a name="cfn-ssmcontacts-contact-displayname"></a>
The full name of the contact or escalation plan.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\s]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Plan`  <a name="cfn-ssmcontacts-contact-plan"></a>
A list of stages. A contact has an engagement plan with stages that contact specified contact channels. An escalation plan uses stages that contact specified contacts.
*Required*: No
*Type*: Array of [Stage](aws-properties-ssmcontacts-contact-stage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ssmcontacts-contact-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ssmcontacts-contact-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-ssmcontacts-contact-type"></a>
The type of contact.
+ `PERSONAL`: A single, individual contact.
+ `ESCALATION`: An escalation plan.
+ `ONCALL_SCHEDULE`: An on-call schedule.
*Required*: Yes
*Type*: String
*Allowed values*: `PERSONAL | ESCALATION | ONCALL_SCHEDULE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ssmcontacts-contact-return-values"></a>

### Ref
<a name="aws-resource-ssmcontacts-contact-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the resource.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ssmcontacts-contact-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ssmcontacts-contact-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the `Contact` resource, such as `arn:aws:ssm-contacts:us-west-2:123456789012:contact/contactalias`.

## Examples
<a name="aws-resource-ssmcontacts-contact--examples"></a>

### Create Incident Manager resources
<a name="aws-resource-ssmcontacts-contact--examples--Create_resources"></a>

The following example demonstrates the creation of not only contacts, but also a contact channel, a contact plan, and on-call rotation schedules. We recommend creating all Incident Manager`Contacts` resources using a single AWS CloudFormation template.

#### JSON
<a name="aws-resource-ssmcontacts-contact--examples--Create_resources--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "MySSMContact": {
            "Type": "AWS::SSMContacts::Contact",
            "Properties": {
                "Alias": "my-ssm-contact",
                "DisplayName": "My_SSM_contact",
                "Type": "PERSONAL"
            }
        },
        "MyEscalationPlan": {
            "Type": "AWS::SSMContacts::Contact",
            "Properties": {
                "Alias": "my-escalation-plan",
                "DisplayName": "My_escalation_plan",
                "Type": "ESCALATION"
            }
        },
        "MyOncallScheduleContact": {
            "Type": "AWS::SSMContacts::Contact",
            "Properties": {
                "Alias": "my-oncall-schedule",
                "DisplayName": "My_on-call_schedule",
                "Type": "ONCALL_SCHEDULE"
            }
        },
        "MyContactChannelEmail": {
            "Type": "AWS::SSMContacts::ContactChannel",
            "Properties": {
                "ContactId": {"Ref": "MySSMContact"},
                "ChannelName": "MyEmailChannel",
                "ChannelType": "EMAIL",
                "ChannelAddress": "contact-email-channel@example.com"
            }
        },
        "MySSMContactEngagementPlan": {
            "Type": "AWS::SSMContacts::Plan",
            "Properties": {
                "ContactId": {"Ref": "MySSMContact"},
                "Stages": [
                    {
                        "DurationInMinutes": 10,
                        "Targets": [
                            {
                                "ChannelTargetInfo": {
                                    "ChannelId": {"Ref": "MyContactChannelEmail"},
                                    "RetryIntervalInMinutes": 3
                                }
                            }
                        ]
                    }
                ]
            }
        },
        "MySSMContactEscalationPlan": {
            "Type": "AWS::SSMContacts::Plan",
            "Properties": {
                "ContactId": {"Ref": "MyEscalationPlan"},
                "Stages": [
                    {
                        "DurationInMinutes": 0,
                        "Targets": [
                            {
                                "ContactTargetInfo": {
                                    "ContactId": {"Ref": "MySSMContact"},
                                    "IsEssential": true
                                }
                            }
                        ]
                    }
                ]
            }
        },
        "MyDailyRotation": {
            "Type": "AWS::SSMContacts::Rotation",
            "Properties": {
                "Name": "My_daily_rotation",
                "ContactIds": [
                    {"Ref": "MySSMContact"}
                ],
                "StartTime": "2025-03-03T20:20:39",
                "TimeZoneId": "America/Los_Angeles",
                "Recurrence": {
                    "NumberOfOnCalls": 1,
                    "RecurrenceMultiplier": 1,
                    "DailySettings": ["13:00"]
                }
            }
        },
        "MyWeeklyRotation": {
            "Type": "AWS::SSMContacts::Rotation",
            "Properties": {
                "Name": "My_weekly_rotation",
                "ContactIds": [
                    {"Ref": "MySSMContact"}
                ],
                "StartTime": "2025-03-03T20:20:39",
                "TimeZoneId": "America/Los_Angeles",
                "Recurrence": {
                    "NumberOfOnCalls": 1,
                    "RecurrenceMultiplier": 1,
                    "WeeklySettings": [
                        {
                            "DayOfWeek": "MON",
                            "HandOffTime": "13:00"
                        }
                    ]
                }
            }
        },
        "MyMonthlyRotation": {
            "Type": "AWS::SSMContacts::Rotation",
            "Properties": {
                "Name": "My_monthly_rotation",
                "ContactIds": [
                    {"Ref": "MySSMContact"}
                ],
                "StartTime": "2025-03-03T20:20:39",
                "TimeZoneId": "America/Los_Angeles",
                "Recurrence": {
                    "ShiftCoverages": [
                        {
                            "DayOfWeek": "MON",
                            "CoverageTimes": [
                                {
                                    "StartTime": "10:00",
                                    "EndTime": "18:00"
                                }
                            ]
                        }
                    ],
                    "NumberOfOnCalls": 1,
                    "RecurrenceMultiplier": 1,
                    "MonthlySettings": [
                        {
                            "DayOfMonth": 10,
                            "HandOffTime": "13:00"
                        }
                    ]
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ssmcontacts-contact--examples--Create_resources--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MySSMContact:
    Type: 'AWS::SSMContacts::Contact'
    Properties:
      Alias: my-ssm-contact
      DisplayName: My_SSM_contact
      Type: PERSONAL
  MyEscalationPlan:
    Type: 'AWS::SSMContacts::Contact'
    Properties:
      Alias: my-escalation-plan
      DisplayName: My_escalation_plan
      Type: ESCALATION
  MyOncallScheduleContact:
    Type: 'AWS::SSMContacts::Contact'
    Properties:
      Alias: my-oncall-schedule
      DisplayName: My_on-call_schedule
      Type: ONCALL_SCHEDULE
  MyContactChannelEmail:
    Type: 'AWS::SSMContacts::ContactChannel'
    Properties:
      ContactId:
        Ref: MySSMContact
      ChannelName: MyEmailChannel
      ChannelType: EMAIL
      ChannelAddress: contact-email-channel@example.com
  MySSMContactEngagementPlan:
    Type: 'AWS::SSMContacts::Plan'
    Properties:
      ContactId:
        Ref: MySSMContact
      Stages:
        - DurationInMinutes: 10
          Targets:
            - ChannelTargetInfo:
                ChannelId:
                  Ref: MyContactChannelEmail
                RetryIntervalInMinutes: 3
  MySSMContactEscalationPlan:
    Type: 'AWS::SSMContacts::Plan'
    Properties:
      ContactId:
        Ref: MyEscalationPlan
      Stages:
        - DurationInMinutes: 0
          Targets:
            - ContactTargetInfo:
                ContactId:
                  Ref: MySSMContact
                IsEssential: true
  MyDailyRotation:
    Type: 'AWS::SSMContacts::Rotation'
    Properties:
      Name: My_daily_rotation
      ContactIds:
        - Ref: MySSMContact
      StartTime: '2025-03-03T20:20:39'
      TimeZoneId: America/Los_Angeles
      Recurrence:
        NumberOfOnCalls: 1
        RecurrenceMultiplier: 1
        DailySettings:
          - '13:00'
  MyWeeklyRotation:
    Type: 'AWS::SSMContacts::Rotation'
    Properties:
      Name: My_weekly_rotation
      ContactIds:
        - Ref: MySSMContact
      StartTime: '2025-03-03T20:20:39'
      TimeZoneId: America/Los_Angeles
      Recurrence:
        NumberOfOnCalls: 1
        RecurrenceMultiplier: 1
        WeeklySettings:
          - DayOfWeek: MON
            HandOffTime: '13:00'
  MyMonthlyRotation:
    Type: 'AWS::SSMContacts::Rotation'
    Properties:
      Name: My_monthly_rotation
      ContactIds:
        - Ref: MySSMContact
      StartTime: '2025-03-03T20:20:39'
      TimeZoneId: America/Los_Angeles
      Recurrence:
        ShiftCoverages:
          - DayOfWeek: MON
            CoverageTimes:
              - StartTime: '10:00'
                EndTime: '18:00'
        NumberOfOnCalls: 1
        RecurrenceMultiplier: 1
        MonthlySettings:
          - DayOfMonth: 10
            HandOffTime: '13:00'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
