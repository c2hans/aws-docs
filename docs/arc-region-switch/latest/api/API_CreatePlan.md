---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CreatePlan.html
---

# CreatePlan
<a name="API_CreatePlan"></a>

Creates a new Region switch plan. A plan defines the steps required to shift traffic from one AWS Region to another.

You must specify a name for the plan, the primary Region, and at least one additional Region. You can also provide a description, execution role, recovery time objective, associated alarms, triggers, and workflows that define the steps to execute during a Region switch.

## Request Parameters
<a name="API_CreatePlan_RequestParameters"></a>

 ** associatedAlarms **
The alarms associated with a Region switch plan.
Type: String to [AssociatedAlarm](API_AssociatedAlarm.md) object map
Required: No

 ** description **
The description of a Region switch plan.
Type: String
Required: No

 ** executionRole **
An execution role is a way to categorize a Region switch plan.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** name **
The name of a Region switch plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?`
Required: Yes

 ** primaryRegion **
The primary AWS Region for the application. This is the Region where the application normally runs before any Region switch occurs.
Type: String
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: No

 ** recoveryApproach **
The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).
Type: String
Valid Values: `activeActive | activePassive`
Required: Yes

 ** recoveryTimeObjectiveMinutes **
Optionally, you can specify an recovery time objective for a Region switch plan, in minutes.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10080.
Required: No

 ** regions **
An array that specifies the AWS Regions for a Region switch plan. Specify two Regions.
Type: Array of strings
Array Members: Fixed number of 2 items.
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: Yes

 ** reportConfiguration **
Configuration for automatic report generation for plan executions. When configured, Region switch automatically generates a report after each plan execution that includes execution events, plan configuration, and CloudWatch alarm states.
Type: [ReportConfiguration](API_ReportConfiguration.md) object
Required: No

 ** tags **
The tags to apply to the Region switch plan.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** triggers **
The triggers associated with a Region switch plan.
Type: Array of [Trigger](API_Trigger.md) objects
Required: No

 ** workflows **
An array of workflows included in a Region switch plan.
Type: Array of [Workflow](API_Workflow.md) objects
Required: Yes

## Response Elements
<a name="API_CreatePlan_ResponseElements"></a>

The following element is returned by the service.

 ** plan **
The details of the created Region switch plan.
Type: [Plan](API_Plan.md) object

## Errors
<a name="API_CreatePlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreatePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/CreatePlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/CreatePlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/CreatePlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/CreatePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/CreatePlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/CreatePlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/CreatePlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/CreatePlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/CreatePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/CreatePlan)
