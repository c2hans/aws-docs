---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Test.html
---

# Test
<a name="API_Test"></a>

Represents a test created for a service by configuring a test template.

## Contents
<a name="API_Test_Contents"></a>

 ** creationTime **   <a name="ngresiliencehub-Type-Test-creationTime"></a>
The timestamp when the test was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="ngresiliencehub-Type-Test-name"></a>
The name of the test.
Type: String
Required: Yes

 ** serviceArn **   <a name="ngresiliencehub-Type-Test-serviceArn"></a>
The ARN of the service the test belongs to.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** successfulTestRuns **   <a name="ngresiliencehub-Type-Test-successfulTestRuns"></a>
The number of successful runs of the test.
Type: Integer
Required: Yes

 ** testId **   <a name="ngresiliencehub-Type-Test-testId"></a>
The unique identifier of the test.
Type: String
Required: Yes

 ** testTemplateArn **   <a name="ngresiliencehub-Type-Test-testTemplateArn"></a>
The ARN of the test template the test was created from.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):([0-9]{12}|aws):[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** totalTestRuns **   <a name="ngresiliencehub-Type-Test-totalTestRuns"></a>
The total number of runs of the test.
Type: Integer
Required: Yes

 ** actions **   <a name="ngresiliencehub-Type-Test-actions"></a>
The fault actions the test runs.
Type: Array of [TestAction](API_TestAction.md) objects
Required: No

 ** loggingConfiguration **   <a name="ngresiliencehub-Type-Test-loggingConfiguration"></a>
The logging configuration for the test.
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object
Required: No

 ** parameters **   <a name="ngresiliencehub-Type-Test-parameters"></a>
The parameter values configured for the test.
Type: String to array of strings map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[\w.-]+`
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** roleName **   <a name="ngresiliencehub-Type-Test-roleName"></a>
The name of the IAM execution role used to run the test.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** stopConditions **   <a name="ngresiliencehub-Type-Test-stopConditions"></a>
The stop conditions for the test.
Type: Array of [StopCondition](API_StopCondition.md) objects
Required: No

## See Also
<a name="API_Test_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/Test)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/Test)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/Test)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
