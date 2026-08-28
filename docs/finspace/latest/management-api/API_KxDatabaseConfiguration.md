---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDatabaseConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxDatabaseConfiguration
<a name="API_KxDatabaseConfiguration"></a>

The configuration of data that is available for querying from this database.

## Contents
<a name="API_KxDatabaseConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** databaseName **   <a name="finspace-Type-KxDatabaseConfiguration-databaseName"></a>
The name of the kdb database. When this parameter is specified in the structure, S3 with the whole database is included by default.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** cacheConfigurations **   <a name="finspace-Type-KxDatabaseConfiguration-cacheConfigurations"></a>
Configuration details for the disk cache used to increase performance reading from a kdb database mounted to the cluster.
Type: Array of [KxDatabaseCacheConfiguration](API_KxDatabaseCacheConfiguration.md) objects
Required: No

 ** changesetId **   <a name="finspace-Type-KxDatabaseConfiguration-changesetId"></a>
A unique identifier of the changeset that is associated with the cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** dataviewConfiguration **   <a name="finspace-Type-KxDatabaseConfiguration-dataviewConfiguration"></a>
 The configuration of the dataview to be used with specified cluster.
Type: [KxDataviewConfiguration](API_KxDataviewConfiguration.md) object
Required: No

 ** dataviewName **   <a name="finspace-Type-KxDatabaseConfiguration-dataviewName"></a>
 The name of the dataview to be used for caching historical data on disk.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

## See Also
<a name="API_KxDatabaseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxDatabaseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxDatabaseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxDatabaseConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
