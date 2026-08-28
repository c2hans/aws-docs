---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

Represents a cross-account destination that receives subscription log events.

## Contents
<a name="API_Destination_Contents"></a>

 ** accessPolicy **   <a name="CWL-Type-Destination-accessPolicy"></a>
An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** arn **   <a name="CWL-Type-Destination-arn"></a>
The ARN of this destination.
Type: String
Required: No

 ** creationTime **   <a name="CWL-Type-Destination-creationTime"></a>
The creation time of the destination, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** destinationName **   <a name="CWL-Type-Destination-destinationName"></a>
The name of the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** roleArn **   <a name="CWL-Type-Destination-roleArn"></a>
A role for impersonation, used when delivering log events to the target.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** targetArn **   <a name="CWL-Type-Destination-targetArn"></a>
The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/Destination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
