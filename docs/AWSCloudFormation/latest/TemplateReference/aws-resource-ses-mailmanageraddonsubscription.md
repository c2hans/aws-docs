---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-mailmanageraddonsubscription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerAddonSubscription
<a name="aws-resource-ses-mailmanageraddonsubscription"></a>

Creates a subscription for an Add On representing the acceptance of its terms of use and additional pricing. The subscription can then be used to create an instance for use in rule sets or traffic policies.

## Syntax
<a name="aws-resource-ses-mailmanageraddonsubscription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-mailmanageraddonsubscription-syntax.json"></a>

```
{
  "Type" : "AWS::SES::MailManagerAddonSubscription",
  "Properties" : {
      "[AddonName](#cfn-ses-mailmanageraddonsubscription-addonname)" : {{String}},
      "[Tags](#cfn-ses-mailmanageraddonsubscription-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ses-mailmanageraddonsubscription-syntax.yaml"></a>

```
Type: AWS::SES::MailManagerAddonSubscription
Properties:
  [AddonName](#cfn-ses-mailmanageraddonsubscription-addonname): {{String}}
  [Tags](#cfn-ses-mailmanageraddonsubscription-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ses-mailmanageraddonsubscription-properties"></a>

`AddonName`  <a name="cfn-ses-mailmanageraddonsubscription-addonname"></a>
The name of the Add On to subscribe to. You can only have one subscription for each Add On name.
Valid Values: `TRENDMICRO_VSAPI | SPAMHAUS_DBL | ABUSIX_MAIL_INTELLIGENCE | VADE_ADVANCED_EMAIL_SECURITY`
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ses-mailmanageraddonsubscription-tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-mailmanageraddonsubscription-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-mailmanageraddonsubscription-return-values"></a>

### Ref
<a name="aws-resource-ses-mailmanageraddonsubscription-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ses-mailmanageraddonsubscription-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-mailmanageraddonsubscription-return-values-fn--getatt-fn--getatt"></a>

`AddonSubscriptionArn`  <a name="AddonSubscriptionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Add On subscription.

`AddonSubscriptionId`  <a name="AddonSubscriptionId-fn::getatt"></a>
The unique ID of the Add On subscription.
