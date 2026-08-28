---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ReportStatus.html
---

# ReportStatus
<a name="API_cur_ReportStatus"></a>

A two element dictionary with a `lastDelivery` and `lastStatus` key whose values describe the date and status of the last delivered report for a particular report definition.

## Contents
<a name="API_cur_ReportStatus_Contents"></a>

 ** lastDelivery **   <a name="awscostmanagement-Type-cur_ReportStatus-lastDelivery"></a>
A timestamp that gives the date of a report delivery.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 20.
Pattern: `[0-9]{8}[T][0-9]{6}([Z]|[+-][0-9]{4})`
Required: No

 ** lastStatus **   <a name="awscostmanagement-Type-cur_ReportStatus-lastStatus"></a>
An enum that gives the status of a report delivery.
Type: String
Valid Values: `SUCCESS | ERROR_PERMISSIONS | ERROR_NO_BUCKET`
Required: No

## See Also
<a name="API_cur_ReportStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cur-2017-01-06/ReportStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cur-2017-01-06/ReportStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cur-2017-01-06/ReportStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
