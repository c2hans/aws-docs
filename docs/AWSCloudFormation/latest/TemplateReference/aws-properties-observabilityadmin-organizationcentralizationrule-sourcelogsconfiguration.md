---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule SourceLogsConfiguration
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration"></a>

Configuration for selecting and handling source log groups for centralization.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-syntax.json"></a>

```
{
  "[DataSourceSelectionCriteria](#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-datasourceselectioncriteria)" : {{String}},
  "[EncryptedLogGroupStrategy](#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-encryptedloggroupstrategy)" : {{String}},
  "[LogGroupSelectionCriteria](#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-loggroupselectioncriteria)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-syntax.yaml"></a>

```
  [DataSourceSelectionCriteria](#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-datasourceselectioncriteria): {{String}}
  [EncryptedLogGroupStrategy](#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-encryptedloggroupstrategy): {{String}}
  [LogGroupSelectionCriteria](#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-loggroupselectioncriteria): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-properties"></a>

`DataSourceSelectionCriteria`  <a name="cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-datasourceselectioncriteria"></a>
The selection criteria that specifies which data sources to centralize. The selection criteria uses the same filter expression format as `LogGroupSelectionCriteria`, but operates on `DataSourceName` and `DataSourceType` operands. When both `LogGroupSelectionCriteria` and `DataSourceSelectionCriteria` are specified, a log event must match both criteria to be centralized.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptedLogGroupStrategy`  <a name="cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-encryptedloggroupstrategy"></a>
A strategy determining whether to centralize source log groups that are encrypted with customer managed KMS keys (CMK). ALLOW will consider CMK encrypted source log groups for centralization while SKIP will skip CMK encrypted source log groups from centralization.
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW | SKIP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupSelectionCriteria`  <a name="cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-loggroupselectioncriteria"></a>
The selection criteria that specifies which source log groups to centralize. The selection criteria uses the same format as OAM link filters.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
