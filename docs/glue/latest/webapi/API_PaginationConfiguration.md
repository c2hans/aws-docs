---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PaginationConfiguration.html
---

# PaginationConfiguration
<a name="API_PaginationConfiguration"></a>

Configuration that defines how to handle paginated responses from REST APIs, supporting different pagination strategies used by various services.

## Contents
<a name="API_PaginationConfiguration_Contents"></a>

 ** CursorConfiguration **   <a name="Glue-Type-PaginationConfiguration-CursorConfiguration"></a>
Configuration for cursor-based pagination, where the API provides a cursor or token to retrieve the next page of results.
Type: [CursorConfiguration](API_CursorConfiguration.md) object
Required: No

 ** OffsetConfiguration **   <a name="Glue-Type-PaginationConfiguration-OffsetConfiguration"></a>
Configuration for offset-based pagination, where the API uses numeric offsets and limits to control which results are returned.
Type: [OffsetConfiguration](API_OffsetConfiguration.md) object
Required: No

## See Also
<a name="API_PaginationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PaginationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PaginationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PaginationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
