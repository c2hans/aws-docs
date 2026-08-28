---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_LFTagPolicyResource.html
---

# LFTagPolicyResource
<a name="API_LFTagPolicyResource"></a>

A structure containing a list of LF-tag conditions or saved LF-Tag expressions that apply to a resource's LF-tag policy.

## Contents
<a name="API_LFTagPolicyResource_Contents"></a>

 ** ResourceType **   <a name="lakeformation-Type-LFTagPolicyResource-ResourceType"></a>
The resource type for which the LF-tag policy applies.
Type: String
Valid Values: `DATABASE | TABLE`
Required: Yes

 ** CatalogId **   <a name="lakeformation-Type-LFTagPolicyResource-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Expression **   <a name="lakeformation-Type-LFTagPolicyResource-Expression"></a>
A list of LF-tag conditions or a saved expression that apply to the resource's LF-tag policy.
Type: Array of [LFTag](API_LFTag.md) objects
Required: No

 ** ExpressionName **   <a name="lakeformation-Type-LFTagPolicyResource-ExpressionName"></a>
If provided, permissions are granted to the Data Catalog resources whose assigned LF-Tags match the expression body of the saved expression under the provided `ExpressionName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_LFTagPolicyResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/LFTagPolicyResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/LFTagPolicyResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/LFTagPolicyResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
