---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Control.html
---

# Control
<a name="API_Control"></a>

 A control in AWS Audit Manager.

## Contents
<a name="API_Control_Contents"></a>

 ** actionPlanInstructions **   <a name="auditmanager-Type-Control-actionPlanInstructions"></a>
 The recommended actions to carry out if the control isn't fulfilled.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** actionPlanTitle **   <a name="auditmanager-Type-Control-actionPlanTitle"></a>
 The title of the action plan for remediating the control.
Type: String
Length Constraints: Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** arn **   <a name="auditmanager-Type-Control-arn"></a>
 The Amazon Resource Name (ARN) of the control.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:auditmanager:.*`
Required: No

 ** controlMappingSources **   <a name="auditmanager-Type-Control-controlMappingSources"></a>
 The data mapping sources for the control.
Type: Array of [ControlMappingSource](API_ControlMappingSource.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** controlSources **   <a name="auditmanager-Type-Control-controlSources"></a>
 The data source types that determine where Audit Manager collects evidence from for the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z_0-9-\s.,]+$`
Required: No

 ** createdAt **   <a name="auditmanager-Type-Control-createdAt"></a>
 The time when the control was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="auditmanager-Type-Control-createdBy"></a>
 The user or role that created the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9\s-_()\[\]]+$`
Required: No

 ** description **   <a name="auditmanager-Type-Control-description"></a>
 The description of the control.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** id **   <a name="auditmanager-Type-Control-id"></a>
 The unique identifier for the control.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdatedAt **   <a name="auditmanager-Type-Control-lastUpdatedAt"></a>
 The time when the control was most recently updated.
Type: Timestamp
Required: No

 ** lastUpdatedBy **   <a name="auditmanager-Type-Control-lastUpdatedBy"></a>
 The user or role that most recently updated the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9\s-_()\[\]]+$`
Required: No

 ** name **   <a name="auditmanager-Type-Control-name"></a>
 The name of the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** state **   <a name="auditmanager-Type-Control-state"></a>
The state of the control. The `END_OF_SUPPORT` state is applicable to standard controls only. This state indicates that the standard control can still be used to collect evidence, but Audit Manager is no longer updating or maintaining that control.
Type: String
Valid Values: `ACTIVE | END_OF_SUPPORT`
Required: No

 ** tags **   <a name="auditmanager-Type-Control-tags"></a>
 The tags associated with the control.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.{0,255}`
Required: No

 ** testingInformation **   <a name="auditmanager-Type-Control-testingInformation"></a>
 The steps that you should follow to determine if the control has been satisfied.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** type **   <a name="auditmanager-Type-Control-type"></a>
 Specifies whether the control is a standard control or a custom control.
Type: String
Valid Values: `Standard | Custom | Core`
Required: No

## See Also
<a name="API_Control_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Control)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Control)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Control)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
