---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-mailmanagertrafficpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy
<a name="aws-resource-ses-mailmanagertrafficpolicy"></a>

Resource to create a traffic policy for a Mail Manager ingress endpoint which contains policy statements used to evaluate whether incoming emails should be allowed or denied.

## Syntax
<a name="aws-resource-ses-mailmanagertrafficpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-mailmanagertrafficpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::SES::MailManagerTrafficPolicy",
  "Properties" : {
      "[DefaultAction](#cfn-ses-mailmanagertrafficpolicy-defaultaction)" : {{String}},
      "[MaxMessageSizeBytes](#cfn-ses-mailmanagertrafficpolicy-maxmessagesizebytes)" : {{Number}},
      "[PolicyStatements](#cfn-ses-mailmanagertrafficpolicy-policystatements)" : {{[ PolicyStatement, ... ]}},
      "[Tags](#cfn-ses-mailmanagertrafficpolicy-tags)" : {{[ Tag, ... ]}},
      "[TrafficPolicyName](#cfn-ses-mailmanagertrafficpolicy-trafficpolicyname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ses-mailmanagertrafficpolicy-syntax.yaml"></a>

```
Type: AWS::SES::MailManagerTrafficPolicy
Properties:
  [DefaultAction](#cfn-ses-mailmanagertrafficpolicy-defaultaction): {{String}}
  [MaxMessageSizeBytes](#cfn-ses-mailmanagertrafficpolicy-maxmessagesizebytes): {{Number}}
  [PolicyStatements](#cfn-ses-mailmanagertrafficpolicy-policystatements): {{
    - PolicyStatement}}
  [Tags](#cfn-ses-mailmanagertrafficpolicy-tags): {{
    - Tag}}
  [TrafficPolicyName](#cfn-ses-mailmanagertrafficpolicy-trafficpolicyname): {{String}}
```

## Properties
<a name="aws-resource-ses-mailmanagertrafficpolicy-properties"></a>

`DefaultAction`  <a name="cfn-ses-mailmanagertrafficpolicy-defaultaction"></a>
Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxMessageSizeBytes`  <a name="cfn-ses-mailmanagertrafficpolicy-maxmessagesizebytes"></a>
The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyStatements`  <a name="cfn-ses-mailmanagertrafficpolicy-policystatements"></a>
Conditional statements for filtering email traffic.
*Required*: Yes
*Type*: Array of [PolicyStatement](aws-properties-ses-mailmanagertrafficpolicy-policystatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ses-mailmanagertrafficpolicy-tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-mailmanagertrafficpolicy-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrafficPolicyName`  <a name="cfn-ses-mailmanagertrafficpolicy-trafficpolicyname"></a>
The name of the policy.
The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_\-]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-mailmanagertrafficpolicy-return-values"></a>

### Ref
<a name="aws-resource-ses-mailmanagertrafficpolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ses-mailmanagertrafficpolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-mailmanagertrafficpolicy-return-values-fn--getatt-fn--getatt"></a>

`TrafficPolicyArn`  <a name="TrafficPolicyArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the traffic policy resource.

`TrafficPolicyId`  <a name="TrafficPolicyId-fn::getatt"></a>
The identifier of the traffic policy resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
