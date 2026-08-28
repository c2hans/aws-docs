---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AppMonitorSummary.html
---

# AppMonitorSummary
<a name="API_AppMonitorSummary"></a>

A structure that includes some data about app monitors and their settings.

## Contents
<a name="API_AppMonitorSummary_Contents"></a>

 ** Created **   <a name="cloudwatchrum-Type-AppMonitorSummary-Created"></a>
The date and time that the app monitor was created.
Type: String
Length Constraints: Fixed length of 19.
Required: No

 ** Id **   <a name="cloudwatchrum-Type-AppMonitorSummary-Id"></a>
The unique ID of this app monitor.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: No

 ** LastModified **   <a name="cloudwatchrum-Type-AppMonitorSummary-LastModified"></a>
The date and time of the most recent changes to this app monitor's configuration.
Type: String
Length Constraints: Fixed length of 19.
Required: No

 ** Name **   <a name="cloudwatchrum-Type-AppMonitorSummary-Name"></a>
The name of this app monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: No

 ** State **   <a name="cloudwatchrum-Type-AppMonitorSummary-State"></a>
The current state of this app monitor.
Type: String
Valid Values: `CREATED | DELETING | ACTIVE`
Required: No

## See Also
<a name="API_AppMonitorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/AppMonitorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/AppMonitorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/AppMonitorSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
