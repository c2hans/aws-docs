---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonopensearchserviceRetryOptions.html
---

# AmazonopensearchserviceRetryOptions
<a name="API_AmazonopensearchserviceRetryOptions"></a>

Configures retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service.

## Contents
<a name="API_AmazonopensearchserviceRetryOptions_Contents"></a>

 ** DurationInSeconds **   <a name="Firehose-Type-AmazonopensearchserviceRetryOptions-DurationInSeconds"></a>
After an initial failure to deliver to Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 7200.
Required: No

## See Also
<a name="API_AmazonopensearchserviceRetryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/AmazonopensearchserviceRetryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/AmazonopensearchserviceRetryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/AmazonopensearchserviceRetryOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
