---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDataviewSegmentConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxDataviewSegmentConfiguration
<a name="API_KxDataviewSegmentConfiguration"></a>

 The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.

## Contents
<a name="API_KxDataviewSegmentConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** dbPaths **   <a name="finspace-Type-KxDataviewSegmentConfiguration-dbPaths"></a>
 The database path of the data that you want to place on each selected volume for the segment. Each segment must have a unique database path for each volume.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 1025.
Pattern: `^(\*)*[\/\?\*]([^\/]+\/){0,2}[^\/]*$`
Required: Yes

 ** volumeName **   <a name="finspace-Type-KxDataviewSegmentConfiguration-volumeName"></a>
 The name of the volume where you want to add data.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** onDemand **   <a name="finspace-Type-KxDataviewSegmentConfiguration-onDemand"></a>
Enables on-demand caching on the selected database path when a particular file or a column of the database is accessed. When on demand caching is **True**, dataviews perform minimal loading of files on the filesystem as needed. When it is set to **False**, everything is cached. The default value is **False**.
Type: Boolean
Required: No

## See Also
<a name="API_KxDataviewSegmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxDataviewSegmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxDataviewSegmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxDataviewSegmentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
