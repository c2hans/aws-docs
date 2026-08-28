---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_FailureDetails.html
---

# FailureDetails
<a name="API_FailureDetails"></a>

The details of the step failure. The service attempts to detect the root cause for many common failures.

## Contents
<a name="API_FailureDetails_Contents"></a>

 ** LogFile **   <a name="EMR-Type-FailureDetails-LogFile"></a>
The path to the log file where the step failure root cause was originally recorded.
Type: String
Required: No

 ** Message **   <a name="EMR-Type-FailureDetails-Message"></a>
The descriptive message including the error the Amazon EMR service has identified as the cause of step failure. This is text from an error log that describes the root cause of the failure.
Type: String
Required: No

 ** Reason **   <a name="EMR-Type-FailureDetails-Reason"></a>
The reason for the step failure. In the case where the service cannot successfully determine the root cause of the failure, it returns "Unknown Error" as a reason.
Type: String
Required: No

## See Also
<a name="API_FailureDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/FailureDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/FailureDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/FailureDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
