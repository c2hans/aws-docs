---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MessageData.html
---

# MessageData
<a name="API_MessageData"></a>

A message returned by the `GetMetricData`API, including a code and a description.

If a cross-Region `GetMetricData` operation fails with a code of `Forbidden` and a value of `Authentication too complex to retrieve cross region data`, you can correct the problem by running the `GetMetricData` operation in the same Region where the metric data is.

## Contents
<a name="API_MessageData_Contents"></a>

 ** Code **   <a name="ACW-Type-MessageData-Code"></a>
The error code or status code associated with the message.
Type: String
Required: No

 ** Value **   <a name="ACW-Type-MessageData-Value"></a>
The message text.
Type: String
Required: No

## See Also
<a name="API_MessageData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MessageData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MessageData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MessageData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
