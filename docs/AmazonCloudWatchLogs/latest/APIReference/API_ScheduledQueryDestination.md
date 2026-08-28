---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ScheduledQueryDestination.html
---

# ScheduledQueryDestination
<a name="API_ScheduledQueryDestination"></a>

Information about a destination where scheduled query results are processed, including processing status and any error messages.

## Contents
<a name="API_ScheduledQueryDestination_Contents"></a>

 ** destinationIdentifier **   <a name="CWL-Type-ScheduledQueryDestination-destinationIdentifier"></a>
The identifier for the destination where results are delivered.
Type: String
Required: No

 ** destinationType **   <a name="CWL-Type-ScheduledQueryDestination-destinationType"></a>
The type of destination for query results.
Type: String
Valid Values: `S3 | LOOKUP_TABLE`
Required: No

 ** errorMessage **   <a name="CWL-Type-ScheduledQueryDestination-errorMessage"></a>
Error message if destination processing failed.
Type: String
Required: No

 ** processedIdentifier **   <a name="CWL-Type-ScheduledQueryDestination-processedIdentifier"></a>
The identifier of the processed result at the destination.
Type: String
Required: No

 ** status **   <a name="CWL-Type-ScheduledQueryDestination-status"></a>
The processing status of the destination delivery.
Type: String
Valid Values: `IN_PROGRESS | CLIENT_ERROR | FAILED | COMPLETE`
Required: No

## See Also
<a name="API_ScheduledQueryDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ScheduledQueryDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ScheduledQueryDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ScheduledQueryDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
