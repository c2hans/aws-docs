---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-route53healthcheckconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Route53HealthCheckConfiguration
<a name="aws-properties-arcregionswitch-plan-route53healthcheckconfiguration"></a>

The Amazon Route 53 health check configuration.

## Syntax
<a name="aws-properties-arcregionswitch-plan-route53healthcheckconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-route53healthcheckconfiguration-syntax.json"></a>

```
{
  "[CrossAccountRole](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-externalid)" : {{String}},
  "[HostedZoneId](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-hostedzoneid)" : {{String}},
  "[RecordName](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-recordname)" : {{String}},
  "[RecordSets](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-recordsets)" : {{[ Route53ResourceRecordSet, ... ]}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-timeoutminutes)" : {{Number}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-route53healthcheckconfiguration-syntax.yaml"></a>

```
  [CrossAccountRole](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-externalid): {{String}}
  [HostedZoneId](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-hostedzoneid): {{String}}
  [RecordName](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-recordname): {{String}}
  [RecordSets](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-recordsets): {{
    - Route53ResourceRecordSet}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-route53healthcheckconfiguration-timeoutminutes): {{Number}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-route53healthcheckconfiguration-properties"></a>

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-route53healthcheckconfiguration-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-route53healthcheckconfiguration-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostedZoneId`  <a name="cfn-arcregionswitch-plan-route53healthcheckconfiguration-hostedzoneid"></a>
The Amazon Route 53 health check configuration hosted zone ID.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordName`  <a name="cfn-arcregionswitch-plan-route53healthcheckconfiguration-recordname"></a>
The Amazon Route 53 health check configuration record name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordSets`  <a name="cfn-arcregionswitch-plan-route53healthcheckconfiguration-recordsets"></a>
The Amazon Route 53 health check configuration record sets.
*Required*: No
*Type*: Array of [Route53ResourceRecordSet](aws-properties-arcregionswitch-plan-route53resourcerecordset.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-route53healthcheckconfiguration-timeoutminutes"></a>
The Amazon Route 53 health check configuration time out (in minutes).
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
