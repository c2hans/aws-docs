---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Plan.html
---

# Plan
<a name="API_Plan"></a>

Represents a Region switch plan. A plan defines the steps required to shift traffic from one AWS Region to another.

## Contents
<a name="API_Plan_Contents"></a>

 ** arn **   <a name="regionswitch-Type-Plan-arn"></a>
The Amazon Resource Name (ARN) of the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** executionRole **   <a name="regionswitch-Type-Plan-executionRole"></a>
The execution role for a plan.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** name **   <a name="regionswitch-Type-Plan-name"></a>
The name for a plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?`
Required: Yes

 ** owner **   <a name="regionswitch-Type-Plan-owner"></a>
The owner of a plan.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** recoveryApproach **   <a name="regionswitch-Type-Plan-recoveryApproach"></a>
The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).
Type: String
Valid Values: `activeActive | activePassive`
Required: Yes

 ** regions **   <a name="regionswitch-Type-Plan-regions"></a>
The AWS Regions for a plan.
Type: Array of strings
Array Members: Fixed number of 2 items.
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: Yes

 ** workflows **   <a name="regionswitch-Type-Plan-workflows"></a>
The workflows for a plan.
Type: Array of [Workflow](API_Workflow.md) objects
Required: Yes

 ** associatedAlarms **   <a name="regionswitch-Type-Plan-associatedAlarms"></a>
The associated application health alarms for a plan.
Type: String to [AssociatedAlarm](API_AssociatedAlarm.md) object map
Required: No

 ** description **   <a name="regionswitch-Type-Plan-description"></a>
The description for a plan.
Type: String
Required: No

 ** primaryRegion **   <a name="regionswitch-Type-Plan-primaryRegion"></a>
The primary Region for a plan.
Type: String
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: No

 ** recoveryTimeObjectiveMinutes **   <a name="regionswitch-Type-Plan-recoveryTimeObjectiveMinutes"></a>
The recovery time objective for a plan.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10080.
Required: No

 ** reportConfiguration **   <a name="regionswitch-Type-Plan-reportConfiguration"></a>
The report configuration for a plan.
Type: [ReportConfiguration](API_ReportConfiguration.md) object
Required: No

 ** triggers **   <a name="regionswitch-Type-Plan-triggers"></a>
The triggers for a plan.
Type: Array of [Trigger](API_Trigger.md) objects
Required: No

 ** updatedAt **   <a name="regionswitch-Type-Plan-updatedAt"></a>
The timestamp when the plan was last updated.
Type: Timestamp
Required: No

 ** version **   <a name="regionswitch-Type-Plan-version"></a>
The version for the plan.
Type: String
Required: No

## See Also
<a name="API_Plan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Plan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Plan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Plan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
