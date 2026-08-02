---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-configurationseteventdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSetEventDestination
<a name="aws-resource-ses-configurationseteventdestination"></a>

Specifies a configuration set event destination. *Events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

A single configuration set can include more than one event destination.

## Syntax
<a name="aws-resource-ses-configurationseteventdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-configurationseteventdestination-syntax.json"></a>

```
{
  "Type" : "AWS::SES::ConfigurationSetEventDestination",
  "Properties" : {
      "[ConfigurationSetName](#cfn-ses-configurationseteventdestination-configurationsetname)" : {{String}},
      "[EventDestination](#cfn-ses-configurationseteventdestination-eventdestination)" : {{EventDestination}}
    }
}
```

### YAML
<a name="aws-resource-ses-configurationseteventdestination-syntax.yaml"></a>

```
Type: AWS::SES::ConfigurationSetEventDestination
Properties:
  [ConfigurationSetName](#cfn-ses-configurationseteventdestination-configurationsetname): {{String}}
  [EventDestination](#cfn-ses-configurationseteventdestination-eventdestination): {{
    EventDestination}}
```

## Properties
<a name="aws-resource-ses-configurationseteventdestination-properties"></a>

`ConfigurationSetName`  <a name="cfn-ses-configurationseteventdestination-configurationsetname"></a>
The name of the configuration set that contains the event destination.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventDestination`  <a name="cfn-ses-configurationseteventdestination-eventdestination"></a>
An object that defines the event destination.
*Required*: Yes
*Type*: [EventDestination](aws-properties-ses-configurationseteventdestination-eventdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-configurationseteventdestination-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-ses-configurationseteventdestination-return-values-fn--getatt"></a>

## Examples
<a name="aws-resource-ses-configurationseteventdestination--examples"></a>

Specifies an event destination for a configuration set.

###
<a name="aws-resource-ses-configurationseteventdestination--examples--"></a>

#### JSON
<a name="aws-resource-ses-configurationseteventdestination--examples----json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS SES ConfigurationSetEventDestination Sample Template",
    "Parameters": {
        "ConfigSetName": {
            "Type": "String"
        },
        "EventDestinationName": {
            "Type": "String"
        },
        "EventType1": {
            "Type": "String"
        },
        "EventType2": {
            "Type": "String"
        },
        "EventType3": {
            "Type": "String"
        },
        "DimensionName1": {
            "Type": "String"
        },
        "DimensionValueSource1": {
            "Type": "String"
        },
        "DefaultDimensionValue1": {
            "Type": "String"
        },
        "DimensionName2": {
            "Type": "String"
        },
        "DimensionValueSource2": {
            "Type": "String"
        },
        "DefaultDimensionValue2": {
            "Type": "String"
        }
    },
    "Resources": {
        "ConfigSet": {
            "Type": "AWS::SES::ConfigurationSet",
            "Properties": {
                "Name": {
                    "Ref": "ConfigSetName"
                }
            }
        },
        "CWEventDestination": {
            "Type": "AWS::SES::ConfigurationSetEventDestination",
            "Properties": {
                "ConfigurationSetName": {
                    "Ref": "ConfigSet"
                },
                "EventDestination": {
                    "Name": {
                        "Ref": "EventDestinationName"
                    },
                    "Enabled": true,
                    "MatchingEventTypes": [
                        {
                            "Ref": "EventType1"
                        },
                        {
                            "Ref": "EventType2"
                        },
                        {
                            "Ref": "EventType3"
                        }
                    ],
                    "CloudWatchDestination": {
                        "DimensionConfigurations": [
                            {
                                "DimensionName": {
                                    "Ref": "DimensionName1"
                                },
                                "DimensionValueSource": {
                                    "Ref": "DimensionValueSource1"
                                },
                                "DefaultDimensionValue": {
                                    "Ref": "DefaultDimensionValue1"
                                }
                            },
                            {
                                "DimensionName": {
                                    "Ref": "DimensionName2"
                                },
                                "DimensionValueSource": {
                                    "Ref": "DimensionValueSource2"
                                },
                                "DefaultDimensionValue": {
                                    "Ref": "DefaultDimensionValue2"
                                }
                            }
                        ]
                    }
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ses-configurationseteventdestination--examples----yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS SES ConfigurationSetEventDestination Sample Template
Parameters:
  ConfigSetName:
    Type: String
  EventDestinationName:
    Type: String
  EventType1:
    Type: String
  EventType2:
    Type: String
  EventType3:
    Type: String
  DimensionName1:
    Type: String
  DimensionValueSource1:
    Type: String
  DefaultDimensionValue1:
    Type: String
  DimensionName2:
    Type: String
  DimensionValueSource2:
    Type: String
  DefaultDimensionValue2:
    Type: String
Resources:
  ConfigSet:
    Type: 'AWS::SES::ConfigurationSet'
    Properties:
      Name: !Ref ConfigSetName
  CWEventDestination:
    Type: 'AWS::SES::ConfigurationSetEventDestination'
    Properties:
      ConfigurationSetName: !Ref ConfigSet
      EventDestination:
        Name: !Ref EventDestinationName
        Enabled: true
        MatchingEventTypes:
          - !Ref EventType1
          - !Ref EventType2
          - !Ref EventType3
        CloudWatchDestination:
          DimensionConfigurations:
            - DimensionName: !Ref DimensionName1
              DimensionValueSource: !Ref DimensionValueSource1
              DefaultDimensionValue: !Ref DefaultDimensionValue1
            - DimensionName: !Ref DimensionName2
              DimensionValueSource: !Ref DimensionValueSource2
              DefaultDimensionValue: !Ref DefaultDimensionValue2
```
