---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxCacheStorageConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxCacheStorageConfiguration
<a name="API_KxCacheStorageConfiguration"></a>

The configuration for read only disk cache associated with a cluster.

## Contents
<a name="API_KxCacheStorageConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** size **   <a name="finspace-Type-KxCacheStorageConfiguration-size"></a>
The size of cache in Gigabytes.
Type: Integer
Required: Yes

 ** type **   <a name="finspace-Type-KxCacheStorageConfiguration-type"></a>
The type of cache storage. The valid values are:
+ CACHE\_1000 – This type provides at least 1000 MB/s disk access throughput.
+ CACHE\_250 – This type provides at least 250 MB/s disk access throughput.
+ CACHE\_12 – This type provides at least 12 MB/s disk access throughput.
For cache type `CACHE_1000` and `CACHE_250` you can select cache size as 1200 GB or increments of 2400 GB. For cache type `CACHE_12` you can select the cache size in increments of 6000 GB.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 10.
Required: Yes

## See Also
<a name="API_KxCacheStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxCacheStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxCacheStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxCacheStorageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
