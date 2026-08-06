---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunSummary.html
---

# TestRunSummary
<a name="API_TestRunSummary"></a>

Contains summary information about a test run.

## Contents
<a name="API_TestRunSummary_Contents"></a>

 ** startedAt **   <a name="ngresiliencehub-Type-TestRunSummary-startedAt"></a>
The timestamp when the test run started.
Type: Timestamp
Required: Yes

 ** status **   <a name="ngresiliencehub-Type-TestRunSummary-status"></a>
The current status of the test run.
Type: String
Valid Values: `INITIALIZING | RUNNING | STOPPING | PASSED | FAILED | STOPPED | ERROR`
Required: Yes

 ** testRunId **   <a name="ngresiliencehub-Type-TestRunSummary-testRunId"></a>
The unique identifier of the test run.
Type: String
Required: Yes

 ** testTemplateArn **   <a name="ngresiliencehub-Type-TestRunSummary-testTemplateArn"></a>
The ARN of the test template the test run was based on.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):([0-9]{12}|aws):[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** accountTargeting **   <a name="ngresiliencehub-Type-TestRunSummary-accountTargeting"></a>
Indicates whether the test run targets resources in a single AWS account or across multiple accounts.
Type: String
Valid Values: `SINGLE_ACCOUNT | MULTI_ACCOUNT`
Required: No

 ** endedAt **   <a name="ngresiliencehub-Type-TestRunSummary-endedAt"></a>
The timestamp when the test run ended.
Type: Timestamp
Required: No

 ** errorMessage **   <a name="ngresiliencehub-Type-TestRunSummary-errorMessage"></a>
A human-readable reason for test run failure. Only present when the status is FAILED or ERROR.
Type: String
Required: No

 ** serviceArn **   <a name="ngresiliencehub-Type-TestRunSummary-serviceArn"></a>
The ARN of the service the test run belongs to.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

## See Also
<a name="API_TestRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunSummary)
