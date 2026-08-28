---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-mailmanageraddoninstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerAddonInstance
<a name="aws-resource-ses-mailmanageraddoninstance"></a>

Creates an Add On instance for the subscription indicated in the request. The resulting Amazon Resource Name (ARN) can be used in a conditional statement for a rule set or traffic policy.

## Syntax
<a name="aws-resource-ses-mailmanageraddoninstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-mailmanageraddoninstance-syntax.json"></a>

```
{
  "Type" : "AWS::SES::MailManagerAddonInstance",
  "Properties" : {
      "[AddonSubscriptionId](#cfn-ses-mailmanageraddoninstance-addonsubscriptionid)" : {{String}},
      "[Tags](#cfn-ses-mailmanageraddoninstance-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ses-mailmanageraddoninstance-syntax.yaml"></a>

```
Type: AWS::SES::MailManagerAddonInstance
Properties:
  [AddonSubscriptionId](#cfn-ses-mailmanageraddoninstance-addonsubscriptionid): {{String}}
  [Tags](#cfn-ses-mailmanageraddoninstance-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ses-mailmanageraddoninstance-properties"></a>

`AddonSubscriptionId`  <a name="cfn-ses-mailmanageraddoninstance-addonsubscriptionid"></a>
The subscription ID for the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^as-[a-zA-Z0-9]{1,64}$`
*Minimum*: `4`
*Maximum*: `67`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ses-mailmanageraddoninstance-tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-mailmanageraddoninstance-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-mailmanageraddoninstance-return-values"></a>

### Ref
<a name="aws-resource-ses-mailmanageraddoninstance-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ses-mailmanageraddoninstance-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-mailmanageraddoninstance-return-values-fn--getatt-fn--getatt"></a>

`AddonInstanceArn`  <a name="AddonInstanceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Add On instance.

`AddonInstanceId`  <a name="AddonInstanceId-fn::getatt"></a>
The unique ID of the Add On instance.

`AddonName`  <a name="AddonName-fn::getatt"></a>
The name of the Add On for the instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
