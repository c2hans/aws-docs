---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDatabaseCacheConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxDatabaseCacheConfiguration
<a name="API_KxDatabaseCacheConfiguration"></a>

The structure of database cache configuration that is used for mapping database paths to cache types in clusters.

## Contents
<a name="API_KxDatabaseCacheConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** cacheType **   <a name="finspace-Type-KxDatabaseCacheConfiguration-cacheType"></a>
The type of disk cache. This parameter is used to map the database path to cache storage. The valid values are:
+ CACHE\_1000 – This type provides at least 1000 MB/s disk access throughput.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 10.
Required: Yes

 ** dbPaths **   <a name="finspace-Type-KxDatabaseCacheConfiguration-dbPaths"></a>
Specifies the portions of database that will be loaded into the cache for access.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1025.
Pattern: `^(\*)*[\/\?\*]([^\/]+\/){0,2}[^\/]*$`
Required: Yes

 ** dataviewName **   <a name="finspace-Type-KxDatabaseCacheConfiguration-dataviewName"></a>
 The name of the dataview to be used for caching historical data on disk.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

## See Also
<a name="API_KxDatabaseCacheConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxDatabaseCacheConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxDatabaseCacheConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxDatabaseCacheConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
