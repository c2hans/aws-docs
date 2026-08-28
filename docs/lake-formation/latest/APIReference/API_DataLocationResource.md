---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DataLocationResource.html
---

# DataLocationResource
<a name="API_DataLocationResource"></a>

A structure for a data location object where permissions are granted or revoked.

## Contents
<a name="API_DataLocationResource_Contents"></a>

 ** ResourceArn **   <a name="lakeformation-Type-DataLocationResource-ResourceArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
Type: String
Required: Yes

 ** CatalogId **   <a name="lakeformation-Type-DataLocationResource-CatalogId"></a>
The identifier for the Data Catalog where the location is registered with AWS Lake Formation. By default, it is the account ID of the caller.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_DataLocationResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DataLocationResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DataLocationResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DataLocationResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
