---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UserDefinedFunction.html
---

# UserDefinedFunction
<a name="API_UserDefinedFunction"></a>

Represents the equivalent of a Hive user-defined function (`UDF`) definition.

## Contents
<a name="API_UserDefinedFunction_Contents"></a>

 ** CatalogId **   <a name="Glue-Type-UserDefinedFunction-CatalogId"></a>
The ID of the Data Catalog in which the function resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ClassName **   <a name="Glue-Type-UserDefinedFunction-ClassName"></a>
The Java class that contains the function code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** CreateTime **   <a name="Glue-Type-UserDefinedFunction-CreateTime"></a>
The time at which the function was created.
Type: Timestamp
Required: No

 ** DatabaseName **   <a name="Glue-Type-UserDefinedFunction-DatabaseName"></a>
The name of the catalog database that contains the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** FunctionName **   <a name="Glue-Type-UserDefinedFunction-FunctionName"></a>
The name of the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** FunctionType **   <a name="Glue-Type-UserDefinedFunction-FunctionType"></a>
The type of the function.
Type: String
Valid Values: `REGULAR_FUNCTION | AGGREGATE_FUNCTION | STORED_PROCEDURE`
Required: No

 ** OwnerName **   <a name="Glue-Type-UserDefinedFunction-OwnerName"></a>
The owner of the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** OwnerType **   <a name="Glue-Type-UserDefinedFunction-OwnerType"></a>
The owner type.
Type: String
Valid Values: `USER | ROLE | GROUP`
Required: No

 ** ResourceUris **   <a name="Glue-Type-UserDefinedFunction-ResourceUris"></a>
The resource URIs for the function.
Type: Array of [ResourceUri](API_ResourceUri.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

## See Also
<a name="API_UserDefinedFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UserDefinedFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UserDefinedFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UserDefinedFunction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
