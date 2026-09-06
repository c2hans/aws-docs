---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_AbbreviatedPlan.html
---

# AbbreviatedPlan
<a name="API_AbbreviatedPlan"></a>

A summarized representation of a Region switch plan. This structure contains key information about a plan without all the detailed workflow and step data.

## Contents
<a name="API_AbbreviatedPlan_Contents"></a>

 ** arn **   <a name="regionswitch-Type-AbbreviatedPlan-arn"></a>
The Amazon Resource Name (ARN) of the Region switch plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** name **   <a name="regionswitch-Type-AbbreviatedPlan-name"></a>
The name of a Region switch plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?`
Required: Yes

 ** owner **   <a name="regionswitch-Type-AbbreviatedPlan-owner"></a>
The owner of a Region switch plan.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** recoveryApproach **   <a name="regionswitch-Type-AbbreviatedPlan-recoveryApproach"></a>
The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).
Type: String
Valid Values: `activeActive | activePassive`
Required: Yes

 ** regions **   <a name="regionswitch-Type-AbbreviatedPlan-regions"></a>
The AWS Region specified for a Region switch plan.
Type: Array of strings
Array Members: Fixed number of 2 items.
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: Yes

 ** activePlanExecution **   <a name="regionswitch-Type-AbbreviatedPlan-activePlanExecution"></a>
Specifies if this is the active plan execution at this time.
Type: String
Required: No

 ** description **   <a name="regionswitch-Type-AbbreviatedPlan-description"></a>
The description of a Region switch plan.
Type: String
Required: No

 ** executionRole **   <a name="regionswitch-Type-AbbreviatedPlan-executionRole"></a>
The execution role is a way to categorize a Region switch plan.
Type: String
Required: No

 ** primaryRegion **   <a name="regionswitch-Type-AbbreviatedPlan-primaryRegion"></a>
The primary Region for a plan.
Type: String
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: No

 ** recoveryTimeObjectiveMinutes **   <a name="regionswitch-Type-AbbreviatedPlan-recoveryTimeObjectiveMinutes"></a>
The recovery time objective that you've specified.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10080.
Required: No

 ** updatedAt **   <a name="regionswitch-Type-AbbreviatedPlan-updatedAt"></a>
The timestamp when the plan execution was last updated.
Type: Timestamp
Required: No

 ** version **   <a name="regionswitch-Type-AbbreviatedPlan-version"></a>
The version for the plan.
Type: String
Required: No

## See Also
<a name="API_AbbreviatedPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/AbbreviatedPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/AbbreviatedPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/AbbreviatedPlan)
