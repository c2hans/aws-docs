---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-policystatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy PolicyStatement
<a name="aws-properties-ses-mailmanagertrafficpolicy-policystatement"></a>

The structure containing traffic policy conditions and actions.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-policystatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-policystatement-syntax.json"></a>

```
{
  "[Action](#cfn-ses-mailmanagertrafficpolicy-policystatement-action)" : {{String}},
  "[Conditions](#cfn-ses-mailmanagertrafficpolicy-policystatement-conditions)" : {{[ PolicyCondition, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-policystatement-syntax.yaml"></a>

```
  [Action](#cfn-ses-mailmanagertrafficpolicy-policystatement-action): {{String}}
  [Conditions](#cfn-ses-mailmanagertrafficpolicy-policystatement-conditions): {{
    - PolicyCondition}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-policystatement-properties"></a>

`Action`  <a name="cfn-ses-mailmanagertrafficpolicy-policystatement-action"></a>
The action that informs a traffic policy resource to either allow or block the email if it matches a condition in the policy statement.
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Conditions`  <a name="cfn-ses-mailmanagertrafficpolicy-policystatement-conditions"></a>
The list of conditions to apply to incoming messages for filtering email traffic.
*Required*: Yes
*Type*: Array of [PolicyCondition](aws-properties-ses-mailmanagertrafficpolicy-policycondition.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
