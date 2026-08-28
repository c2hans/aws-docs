---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentFilter.html
---

# DocumentFilter
<a name="API_DocumentFilter"></a>

This data type is deprecated. Instead, use [DocumentKeyValuesFilter](API_DocumentKeyValuesFilter.md).

## Contents
<a name="API_DocumentFilter_Contents"></a>

 ** key **   <a name="systemsmanager-Type-DocumentFilter-key"></a>
The name of the filter.
Type: String
Valid Values: `Name | Owner | PlatformTypes | DocumentType`
Required: Yes

 ** value **   <a name="systemsmanager-Type-DocumentFilter-value"></a>
The value of the filter.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_DocumentFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
