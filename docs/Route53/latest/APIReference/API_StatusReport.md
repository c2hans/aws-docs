---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_StatusReport.html
---

# StatusReport
<a name="API_StatusReport"></a>

A complex type that contains the status that one Amazon Route 53 health checker reports and the time of the health check.

## Contents
<a name="API_StatusReport_Contents"></a>

 ** CheckedTime **   <a name="Route53-Type-StatusReport-CheckedTime"></a>
The date and time that the health checker performed the health check in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) and Coordinated Universal Time (UTC). For example, the value `2017-03-27T17:48:16.751Z` represents March 27, 2017 at 17:48:16.751 UTC.
Type: Timestamp
Required: No

 ** Status **   <a name="Route53-Type-StatusReport-Status"></a>
A description of the status of the health check endpoint as reported by one of the Amazon Route 53 health checkers.
Type: String
Required: No

## See Also
<a name="API_StatusReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/StatusReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/StatusReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/StatusReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
