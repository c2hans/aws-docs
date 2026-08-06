---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestSummary.html
---

# TestSummary
<a name="API_TestSummary"></a>

Contains summary information about a test.

## Contents
<a name="API_TestSummary_Contents"></a>

 ** creationTime **   <a name="ngresiliencehub-Type-TestSummary-creationTime"></a>
The timestamp when the test was created.
Type: Timestamp
Required: Yes

 ** serviceArn **   <a name="ngresiliencehub-Type-TestSummary-serviceArn"></a>
The ARN of the service the test belongs to.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** successfulTestRuns **   <a name="ngresiliencehub-Type-TestSummary-successfulTestRuns"></a>
The number of successful runs of the test.
Type: Integer
Required: Yes

 ** testId **   <a name="ngresiliencehub-Type-TestSummary-testId"></a>
The unique identifier of the test.
Type: String
Required: Yes

 ** testTemplateArn **   <a name="ngresiliencehub-Type-TestSummary-testTemplateArn"></a>
The ARN of the test template the test was created from.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):([0-9]{12}|aws):[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** totalTestRuns **   <a name="ngresiliencehub-Type-TestSummary-totalTestRuns"></a>
The total number of runs of the test.
Type: Integer
Required: Yes

## See Also
<a name="API_TestSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestSummary)
