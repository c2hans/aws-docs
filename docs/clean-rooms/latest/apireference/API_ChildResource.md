---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ChildResource.html
---

# ChildResource
<a name="API_ChildResource"></a>

Contains information about a child resource of a given resource in a collaboration.

## Contents
<a name="API_ChildResource_Contents"></a>

 ** ownerAccountId **   <a name="API-Type-ChildResource-ownerAccountId"></a>
The AWS account ID of the member who owns the child resource.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** resourceName **   <a name="API-Type-ChildResource-resourceName"></a>
The name of the child resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** resourceType **   <a name="API-Type-ChildResource-resourceType"></a>
The type of the child resource.
Type: String
Valid Values: `INTERMEDIATE_TABLE`
Required: Yes

 ** resourceId **   <a name="API-Type-ChildResource-resourceId"></a>
The unique identifier of the child resource.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** resourceStatus **   <a name="API-Type-ChildResource-resourceStatus"></a>
The current status of the child resource.
Type: String
Valid Values: `CREATED | POPULATE_STARTED | POPULATE_SUCCESS | POPULATE_FAILED | DISALLOWED_BY_DATA_PROVIDER | BASE_TABLE_REMOVED | RETENTION_PERIOD_EXPIRED`
Required: No

## See Also
<a name="API_ChildResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ChildResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ChildResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ChildResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
