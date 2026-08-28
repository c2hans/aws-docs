---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IntermediateTableDependency.html
---

# IntermediateTableDependency
<a name="API_IntermediateTableDependency"></a>

Contains information about a base table that an intermediate table depends on.

## Contents
<a name="API_IntermediateTableDependency_Contents"></a>

 ** creatorAccountId **   <a name="API-Type-IntermediateTableDependency-creatorAccountId"></a>
The AWS account ID of the member who owns the dependency table.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** id **   <a name="API-Type-IntermediateTableDependency-id"></a>
The unique identifier of the dependency table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-IntermediateTableDependency-name"></a>
The name of the dependency table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** parentType **   <a name="API-Type-IntermediateTableDependency-parentType"></a>
The type of dependency, either direct or indirect. A direct dependency is a table explicitly referenced in the stored query. An indirect dependency is a table referenced through another intermediate table.
Type: String
Valid Values: `DIRECT | INDIRECT`
Required: Yes

 ** type **   <a name="API-Type-IntermediateTableDependency-type"></a>
The type of the dependency table.
Type: String
Valid Values: `TABLE | INTERMEDIATE_TABLE | ID_MAPPING_TABLE`
Required: Yes

## See Also
<a name="API_IntermediateTableDependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IntermediateTableDependency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IntermediateTableDependency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IntermediateTableDependency)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
