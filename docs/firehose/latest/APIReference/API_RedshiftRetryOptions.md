---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_RedshiftRetryOptions.html
---

# RedshiftRetryOptions
<a name="API_RedshiftRetryOptions"></a>

Configures retry behavior in case Firehose is unable to deliver documents to Amazon Redshift.

## Contents
<a name="API_RedshiftRetryOptions_Contents"></a>

 ** DurationInSeconds **   <a name="Firehose-Type-RedshiftRetryOptions-DurationInSeconds"></a>
The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of `DurationInSeconds` is 0 (zero) or if the first delivery attempt takes longer than the current value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 7200.
Required: No

## See Also
<a name="API_RedshiftRetryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/RedshiftRetryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/RedshiftRetryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/RedshiftRetryOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
