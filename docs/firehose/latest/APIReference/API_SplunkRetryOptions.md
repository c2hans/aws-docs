---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkRetryOptions.html
---

# SplunkRetryOptions
<a name="API_SplunkRetryOptions"></a>

Configures retry behavior in case Firehose is unable to deliver documents to Splunk, or if it doesn't receive an acknowledgment from Splunk.

## Contents
<a name="API_SplunkRetryOptions_Contents"></a>

 ** DurationInSeconds **   <a name="Firehose-Type-SplunkRetryOptions-DurationInSeconds"></a>
The total amount of time that Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn't include the periods during which Firehose waits for acknowledgment from Splunk after each attempt.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 7200.
Required: No

## See Also
<a name="API_SplunkRetryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SplunkRetryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SplunkRetryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SplunkRetryOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
