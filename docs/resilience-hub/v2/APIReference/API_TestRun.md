---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRun.html
---

# TestRun
<a name="API_TestRun"></a>

Represents a single run of a test. Configuration is snapshotted from the test and service at the time the run is started.

## Contents
<a name="API_TestRun_Contents"></a>

 ** startedAt **   <a name="ngresiliencehub-Type-TestRun-startedAt"></a>
The timestamp when the test run started.
Type: Timestamp
Required: Yes

 ** status **   <a name="ngresiliencehub-Type-TestRun-status"></a>
The current status of the test run.
Type: String
Valid Values: `INITIALIZING | RUNNING | STOPPING | PASSED | FAILED | STOPPED | ERROR`
Required: Yes

 ** testId **   <a name="ngresiliencehub-Type-TestRun-testId"></a>
The identifier of the test that was run.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** testRunId **   <a name="ngresiliencehub-Type-TestRun-testRunId"></a>
The unique identifier of the test run.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** testTemplateArn **   <a name="ngresiliencehub-Type-TestRun-testTemplateArn"></a>
The ARN of the test template snapshotted from the test when the run was started.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):([0-9]{12}|aws):[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** accountTargeting **   <a name="ngresiliencehub-Type-TestRun-accountTargeting"></a>
Indicates whether the test run targets resources in a single AWS account or across multiple accounts.
Type: String
Valid Values: `SINGLE_ACCOUNT | MULTI_ACCOUNT`
Required: No

 ** endedAt **   <a name="ngresiliencehub-Type-TestRun-endedAt"></a>
The timestamp when the test run ended.
Type: Timestamp
Required: No

 ** errorMessage **   <a name="ngresiliencehub-Type-TestRun-errorMessage"></a>
A human-readable reason for test run failure. Only present when the status is FAILED or ERROR.
Type: String
Required: No

 ** eventCount **   <a name="ngresiliencehub-Type-TestRun-eventCount"></a>
The number of events recorded for the test run. Use ListTestRunEvents to retrieve the details.
Type: Integer
Required: No

 ** experiments **   <a name="ngresiliencehub-Type-TestRun-experiments"></a>
The AWS Fault Injection Service (AWS FIS) experiments run as part of the test run.
Type: Array of [ExperimentDetails](API_ExperimentDetails.md) objects
Required: No

 ** loggingConfiguration **   <a name="ngresiliencehub-Type-TestRun-loggingConfiguration"></a>
The logging configuration snapshotted from the test when the run was started.
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object
Required: No

 ** parameters **   <a name="ngresiliencehub-Type-TestRun-parameters"></a>
The parameter values used for the test run.
Type: String to array of strings map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[\w.-]+`
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** permissionModel **   <a name="ngresiliencehub-Type-TestRun-permissionModel"></a>
The permission model snapshotted from the service when the run was started.
Type: [PermissionModel](API_PermissionModel.md) object
Required: No

 ** policy **   <a name="ngresiliencehub-Type-TestRun-policy"></a>
The resilience policy snapshotted from the service when the run was started.
Type: [TestRunPolicySnapshot](API_TestRunPolicySnapshot.md) object
Required: No

 ** regions **   <a name="ngresiliencehub-Type-TestRun-regions"></a>
The Regions snapshotted from the service when the run was started.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

 ** regionSwitchExecutionId **   <a name="ngresiliencehub-Type-TestRun-regionSwitchExecutionId"></a>
The identifier of the ARC Region switch execution detected during the test run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z]{2}(-[a-z]+)+-[0-9]+/[0-9a-fA-F]{16}`
Required: No

 ** regionSwitchPlanArn **   <a name="ngresiliencehub-Type-TestRun-regionSwitchPlanArn"></a>
The ARN of the ARC Region switch plan associated with the test run.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** reportConfiguration **   <a name="ngresiliencehub-Type-TestRun-reportConfiguration"></a>
The report configuration snapshotted from the service when the run was started.
Type: [TestRunReportConfiguration](API_TestRunReportConfiguration.md) object
Required: No

 ** reportOutput **   <a name="ngresiliencehub-Type-TestRun-reportOutput"></a>
The report generation result for the test run. Present after report generation completes or fails.
Type: [ReportGenerationResult](API_ReportGenerationResult.md) object
Required: No

 ** roleName **   <a name="ngresiliencehub-Type-TestRun-roleName"></a>
The IAM execution role name snapshotted from the test when the run was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 576.
Pattern: `([A-Za-z0-9_+=,.@\-]+/)*[A-Za-z0-9_+=,.@\-]+`
Required: No

 ** serviceArn **   <a name="ngresiliencehub-Type-TestRun-serviceArn"></a>
The ARN of the service the test run belongs to.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** stopConditions **   <a name="ngresiliencehub-Type-TestRun-stopConditions"></a>
The stop conditions snapshotted from the test when the run was started.
Type: Array of [StopCondition](API_StopCondition.md) objects
Required: No

## See Also
<a name="API_TestRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRun)
