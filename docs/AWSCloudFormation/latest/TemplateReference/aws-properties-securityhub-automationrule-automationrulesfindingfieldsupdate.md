---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRule AutomationRulesFindingFieldsUpdate
<a name="aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate"></a>

 Identifies the finding fields that the automation rule action updates when a finding matches the defined criteria.

## Syntax
<a name="aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate-syntax.json"></a>

```
{
  "[Confidence](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-confidence)" : {{Integer}},
  "[Criticality](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-criticality)" : {{Integer}},
  "[Note](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-note)" : {{NoteUpdate}},
  "[RelatedFindings](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-relatedfindings)" : {{[ RelatedFinding, ... ]}},
  "[Severity](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-severity)" : {{SeverityUpdate}},
  "[Types](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-types)" : {{[ String, ... ]}},
  "[UserDefinedFields](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-userdefinedfields)" : {{{{{Key}}: {{Value}}, ...}}},
  "[VerificationState](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-verificationstate)" : {{String}},
  "[Workflow](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-workflow)" : {{WorkflowUpdate}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate-syntax.yaml"></a>

```
  [Confidence](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-confidence): {{Integer}}
  [Criticality](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-criticality): {{Integer}}
  [Note](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-note): {{
    NoteUpdate}}
  [RelatedFindings](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-relatedfindings): {{
    - RelatedFinding}}
  [Severity](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-severity): {{
    SeverityUpdate}}
  [Types](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-types): {{
    - String}}
  [UserDefinedFields](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-userdefinedfields): {{
    {{Key}}: {{Value}}}}
  [VerificationState](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-verificationstate): {{String}}
  [Workflow](#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-workflow): {{
    WorkflowUpdate}}
```

## Properties
<a name="aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate-properties"></a>

`Confidence`  <a name="cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-confidence"></a>
 The rule action updates the `Confidence` field of a finding.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Criticality`  <a name="cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-criticality"></a>
 The rule action updates the `Criticality` field of a finding.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Note`  <a name="cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-note"></a>
 The rule action will update the `Note` field of a finding.
*Required*: No
*Type*: [NoteUpdate](aws-properties-securityhub-automationrule-noteupdate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelatedFindings`  <a name="cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-relatedfindings"></a>
 The rule action will update the `RelatedFindings` field of a finding.
*Required*: No
*Type*: Array of [RelatedFinding](aws-properties-securityhub-automationrule-relatedfinding.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Severity`  <a name="cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-severity"></a>
 The rule action will update the `Severity` field of a finding.
*Required*: No
*Type*: [SeverityUpdate](aws-properties-securityhub-automationrule-severityupdate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Types`  <a name="cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-types"></a>
 The rule action updates the `Types` field of a finding.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserDefinedFields`  <a name="cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-userdefinedfields"></a>
 The rule action updates the `UserDefinedFields` field of a finding.
*Required*: No
*Type*: Object of String
*Pattern*: `^[-_+=.:/@\w\s]{1,128}$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerificationState`  <a name="cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-verificationstate"></a>
 The rule action updates the `VerificationState` field of a finding.
*Required*: No
*Type*: String
*Allowed values*: `UNKNOWN | TRUE_POSITIVE | FALSE_POSITIVE | BENIGN_POSITIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Workflow`  <a name="cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-workflow"></a>
 The rule action will update the `Workflow` field of a finding.
*Required*: No
*Type*: [WorkflowUpdate](aws-properties-securityhub-automationrule-workflowupdate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
