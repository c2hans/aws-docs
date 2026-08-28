---
source_url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CacheAttributes.html
---

# CacheAttributes
<a name="API_CacheAttributes"></a>

The refresh cache information for the file share or FSx file systems.

## Contents
<a name="API_CacheAttributes_Contents"></a>

 ** CacheStaleTimeoutInSeconds **   <a name="StorageGateway-Type-CacheAttributes-CacheStaleTimeoutInSeconds"></a>
Refreshes a file share's cache by using Time To Live (TTL). TTL is the length of time since the last refresh after which access to the directory would cause the file gateway to first refresh that directory's contents from the Amazon S3 bucket or Amazon FSx file system. The TTL duration is in seconds.
Valid Values:0, 300 to 2,592,000 seconds (5 minutes to 30 days)
Type: Integer
Required: No

## See Also
<a name="API_CacheAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CacheAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CacheAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CacheAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
