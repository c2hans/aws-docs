---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-patchbaseline-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::PatchBaseline Rule
<a name="aws-properties-ssm-patchbaseline-rule"></a>

The `Rule` property type specifies an approval rule for a Systems Manager patch baseline.

The `PatchRules` property of the [RuleGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html) property type contains a list of `Rule` property types.

## Syntax
<a name="aws-properties-ssm-patchbaseline-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-patchbaseline-rule-syntax.json"></a>

```
{
  "[ApproveAfterDays](#cfn-ssm-patchbaseline-rule-approveafterdays)" : {{Integer}},
  "[ApproveUntilDate](#cfn-ssm-patchbaseline-rule-approveuntildate)" : {{String}},
  "[ComplianceLevel](#cfn-ssm-patchbaseline-rule-compliancelevel)" : {{String}},
  "[EnableNonSecurity](#cfn-ssm-patchbaseline-rule-enablenonsecurity)" : {{Boolean}},
  "[PatchFilterGroup](#cfn-ssm-patchbaseline-rule-patchfiltergroup)" : {{PatchFilterGroup}}
}
```

### YAML
<a name="aws-properties-ssm-patchbaseline-rule-syntax.yaml"></a>

```
  [ApproveAfterDays](#cfn-ssm-patchbaseline-rule-approveafterdays): {{Integer}}
  [ApproveUntilDate](#cfn-ssm-patchbaseline-rule-approveuntildate): {{String}}
  [ComplianceLevel](#cfn-ssm-patchbaseline-rule-compliancelevel): {{String}}
  [EnableNonSecurity](#cfn-ssm-patchbaseline-rule-enablenonsecurity): {{Boolean}}
  [PatchFilterGroup](#cfn-ssm-patchbaseline-rule-patchfiltergroup): {{
    PatchFilterGroup}}
```

## Properties
<a name="aws-properties-ssm-patchbaseline-rule-properties"></a>

`ApproveAfterDays`  <a name="cfn-ssm-patchbaseline-rule-approveafterdays"></a>
The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of `7` means that patches are approved seven days after they are released.
Patch Manager evaluates patch release dates using Coordinated Universal Time (UTC). If a patch is released at `2025-11-09T18:00:00Z` and `ApproveAfterDays` is set to `7`, the patch will be approved after `2025-11-16T18:00:00Z`.
This parameter is marked as `Required: No`, but your request must include a value for either `ApproveAfterDays` or `ApproveUntilDate`.
Not supported for Debian Server or Ubuntu Server.
Use caution when setting this value for Windows Server patch baselines. Because patch updates that are replaced by later updates are removed, setting too broad a value for this parameter can result in crucial patches not being installed. For more information, see the **Windows Server** tab in the topic [How security patches are selected](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-selecting-patches.html) in the *AWS Systems Manager User Guide*.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `360`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApproveUntilDate`  <a name="cfn-ssm-patchbaseline-rule-approveuntildate"></a>
The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically.
Enter dates in the format `YYYY-MM-DD`. For example, `2025-11-16`.
Patch Manager evaluates patch release dates using Coordinated Universal Time (UTC). If you enter the date `2025-11-16`, patches released between `2025-11-16T00:00:00Z` and `2025-11-16T23:59:59Z` will be included in the approval.
This parameter is marked as `Required: No`, but your request must include a value for either `ApproveUntilDate` or `ApproveAfterDays`.
Not supported for Debian Server or Ubuntu Server.
Use caution when setting this value for Windows Server patch baselines. Because patch updates that are replaced by later updates are removed, setting too broad a value for this parameter can result in crucial patches not being installed. For more information, see the **Windows Server** tab in the topic [How security patches are selected](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-selecting-patches.html) in the *AWS Systems Manager User Guide*.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComplianceLevel`  <a name="cfn-ssm-patchbaseline-rule-compliancelevel"></a>
A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: `UNSPECIFIED`, `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, and `INFORMATIONAL`.
*Required*: No
*Type*: String
*Allowed values*: `CRITICAL | HIGH | INFORMATIONAL | LOW | MEDIUM | UNSPECIFIED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableNonSecurity`  <a name="cfn-ssm-patchbaseline-rule-enablenonsecurity"></a>
For managed nodes identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is `false`. Applies to Linux managed nodes only.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PatchFilterGroup`  <a name="cfn-ssm-patchbaseline-rule-patchfiltergroup"></a>
The patch filter group that defines the criteria for the rule.
*Required*: No
*Type*: [PatchFilterGroup](aws-properties-ssm-patchbaseline-patchfiltergroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ssm-patchbaseline-rule--seealso"></a>
+ [PatchRule](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchRule.html) in the *AWS Systems Manager API Reference*.
