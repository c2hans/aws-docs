---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ReportGenerationResult.html
---

# ReportGenerationResult
<a name="API_ReportGenerationResult"></a>

Result of a report generation attempt.

## Contents
<a name="API_ReportGenerationResult_Contents"></a>

 ** reportType **   <a name="ngresiliencehub-Type-ReportGenerationResult-reportType"></a>
The type of the generated report.
Type: String
Valid Values: `FAILURE_MODE | TESTING`
Required: Yes

 ** status **   <a name="ngresiliencehub-Type-ReportGenerationResult-status"></a>
The status of the report generation.
Type: String
Valid Values: `PENDING | SUCCEEDED | FAILED`
Required: Yes

 ** assessmentId **   <a name="ngresiliencehub-Type-ReportGenerationResult-assessmentId"></a>
Present for FAILURE\_MODE reports.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: No

 ** createdAt **   <a name="ngresiliencehub-Type-ReportGenerationResult-createdAt"></a>
The timestamp when the report was created.
Type: Timestamp
Required: No

 ** reportOutput **   <a name="ngresiliencehub-Type-ReportGenerationResult-reportOutput"></a>
Present when status is SUCCEEDED or FAILED.
Type: [ReportOutput](API_ReportOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** serviceArn **   <a name="ngresiliencehub-Type-ReportGenerationResult-serviceArn"></a>
The service this report was generated for.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** testRunId **   <a name="ngresiliencehub-Type-ReportGenerationResult-testRunId"></a>
The unique identifier of a test run.
Type: String
Required: No

 ** testTemplateArn **   <a name="ngresiliencehub-Type-ReportGenerationResult-testTemplateArn"></a>
An ARN owned by the service. Accepts either a standard 12-digit account ID or the literal "aws" for AWS-managed resources, such as AWS-managed test templates.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):([0-9]{12}|aws):[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

## See Also
<a name="API_ReportGenerationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ReportGenerationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ReportGenerationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ReportGenerationResult)
