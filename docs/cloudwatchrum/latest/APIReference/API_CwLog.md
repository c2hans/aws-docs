---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CwLog.html
---

# CwLog
<a name="API_CwLog"></a>

A structure that contains the information about whether the app monitor stores copies of the data that RUM collects in CloudWatch Logs. If it does, this structure also contains the name of the log group.

## Contents
<a name="API_CwLog_Contents"></a>

 ** CwLogEnabled **   <a name="cloudwatchrum-Type-CwLog-CwLogEnabled"></a>
Indicated whether the app monitor stores copies of the data that RUM collects in CloudWatch Logs.
Type: Boolean
Required: No

 ** CwLogGroup **   <a name="cloudwatchrum-Type-CwLog-CwLogGroup"></a>
The name of the log group where the copies are stored.
Type: String
Required: No

## See Also
<a name="API_CwLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/CwLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/CwLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/CwLog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
