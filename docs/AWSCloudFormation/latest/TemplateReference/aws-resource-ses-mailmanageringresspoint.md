---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-mailmanageringresspoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerIngressPoint
<a name="aws-resource-ses-mailmanageringresspoint"></a>

Resource to provision an ingress endpoint for receiving email. An ingress endpoint serves as the entry point for incoming emails, allowing you to define how emails are received and processed within your AWS environment.

## Syntax
<a name="aws-resource-ses-mailmanageringresspoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-mailmanageringresspoint-syntax.json"></a>

```
{
  "Type" : "AWS::SES::MailManagerIngressPoint",
  "Properties" : {
      "[IngressPointConfiguration](#cfn-ses-mailmanageringresspoint-ingresspointconfiguration)" : {{IngressPointConfiguration}},
      "[IngressPointName](#cfn-ses-mailmanageringresspoint-ingresspointname)" : {{String}},
      "[NetworkConfiguration](#cfn-ses-mailmanageringresspoint-networkconfiguration)" : {{NetworkConfiguration}},
      "[RuleSetId](#cfn-ses-mailmanageringresspoint-rulesetid)" : {{String}},
      "[StatusToUpdate](#cfn-ses-mailmanageringresspoint-statustoupdate)" : {{String}},
      "[Tags](#cfn-ses-mailmanageringresspoint-tags)" : {{[ Tag, ... ]}},
      "[TlsPolicy](#cfn-ses-mailmanageringresspoint-tlspolicy)" : {{String}},
      "[TrafficPolicyId](#cfn-ses-mailmanageringresspoint-trafficpolicyid)" : {{String}},
      "[Type](#cfn-ses-mailmanageringresspoint-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ses-mailmanageringresspoint-syntax.yaml"></a>

```
Type: AWS::SES::MailManagerIngressPoint
Properties:
  [IngressPointConfiguration](#cfn-ses-mailmanageringresspoint-ingresspointconfiguration): {{
    IngressPointConfiguration}}
  [IngressPointName](#cfn-ses-mailmanageringresspoint-ingresspointname): {{String}}
  [NetworkConfiguration](#cfn-ses-mailmanageringresspoint-networkconfiguration): {{
    NetworkConfiguration}}
  [RuleSetId](#cfn-ses-mailmanageringresspoint-rulesetid): {{String}}
  [StatusToUpdate](#cfn-ses-mailmanageringresspoint-statustoupdate): {{String}}
  [Tags](#cfn-ses-mailmanageringresspoint-tags): {{
    - Tag}}
  [TlsPolicy](#cfn-ses-mailmanageringresspoint-tlspolicy): {{String}}
  [TrafficPolicyId](#cfn-ses-mailmanageringresspoint-trafficpolicyid): {{String}}
  [Type](#cfn-ses-mailmanageringresspoint-type): {{String}}
```

## Properties
<a name="aws-resource-ses-mailmanageringresspoint-properties"></a>

`IngressPointConfiguration`  <a name="cfn-ses-mailmanageringresspoint-ingresspointconfiguration"></a>
The configuration of the ingress endpoint resource.
*Required*: No
*Type*: [IngressPointConfiguration](aws-properties-ses-mailmanageringresspoint-ingresspointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IngressPointName`  <a name="cfn-ses-mailmanageringresspoint-ingresspointname"></a>
A user friendly name for an ingress endpoint resource.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_\-]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-ses-mailmanageringresspoint-networkconfiguration"></a>
The network type (IPv4-only, Dual-Stack, PrivateLink) of the ingress endpoint resource.
*Required*: No
*Type*: [NetworkConfiguration](aws-properties-ses-mailmanageringresspoint-networkconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuleSetId`  <a name="cfn-ses-mailmanageringresspoint-rulesetid"></a>
The identifier of an existing rule set that you attach to an ingress endpoint resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusToUpdate`  <a name="cfn-ses-mailmanageringresspoint-statustoupdate"></a>
The update status of an ingress endpoint.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | CLOSED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ses-mailmanageringresspoint-tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-mailmanageringresspoint-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TlsPolicy`  <a name="cfn-ses-mailmanageringresspoint-tlspolicy"></a>
The text of the policy in JSON format. The policy cannot exceed 4 KB.
For information about the syntax of sending authorization policies, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html).
*Required*: No
*Type*: String
*Allowed values*: `REQUIRED | OPTIONAL | FIPS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrafficPolicyId`  <a name="cfn-ses-mailmanageringresspoint-trafficpolicyid"></a>
The identifier of an existing traffic policy that you attach to an ingress endpoint resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-ses-mailmanageringresspoint-type"></a>
The type of the ingress endpoint to create.
*Required*: Yes
*Type*: String
*Allowed values*: `OPEN | AUTH | MTLS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ses-mailmanageringresspoint-return-values"></a>

### Ref
<a name="aws-resource-ses-mailmanageringresspoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ses-mailmanageringresspoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-mailmanageringresspoint-return-values-fn--getatt-fn--getatt"></a>

`ARecord`  <a name="ARecord-fn::getatt"></a>
 The DNS A Record that identifies your ingress endpoint. Configure your DNS Mail Exchange (MX) record with this value to route emails to Mail Manager.

`IngressPointArn`  <a name="IngressPointArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the ingress endpoint resource.

`IngressPointId`  <a name="IngressPointId-fn::getatt"></a>
The identifier of the ingress endpoint resource.

`Status`  <a name="Status-fn::getatt"></a>
The status of the ingress endpoint resource.
