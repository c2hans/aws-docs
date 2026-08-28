---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DataStorage.html
---

# DataStorage
<a name="API_DataStorage"></a>

A structure that contains information about whether this app monitor stores a copy of the telemetry data that RUM collects using CloudWatch Logs.

## Contents
<a name="API_DataStorage_Contents"></a>

 ** CwLog **   <a name="cloudwatchrum-Type-DataStorage-CwLog"></a>
A structure that contains the information about whether the app monitor stores copies of the data that RUM collects in CloudWatch Logs. If it does, this structure also contains the name of the log group.
Type: [CwLog](API_CwLog.md) object
Required: No

## See Also
<a name="API_DataStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/DataStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/DataStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/DataStorage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
