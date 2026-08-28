---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_ExpandConfiguration.html
---

# ExpandConfiguration
<a name="API_ExpandConfiguration"></a>

Specifies the configuration information needed to customize how collapsed search result groups expand.

## Contents
<a name="API_ExpandConfiguration_Contents"></a>

 ** MaxExpandedResultsPerItem **   <a name="kendra-Type-ExpandConfiguration-MaxExpandedResultsPerItem"></a>
The number of expanded results to show per collapsed primary document. For instance, if you set this value to 3, then at most 3 results per collapsed group will be displayed.
Type: Integer
Required: No

 ** MaxResultItemsToExpand **   <a name="kendra-Type-ExpandConfiguration-MaxResultItemsToExpand"></a>
The number of collapsed search result groups to expand. If you set this value to 10, for example, only the first 10 out of 100 result groups will have expand functionality.
Type: Integer
Required: No

## See Also
<a name="API_ExpandConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ExpandConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ExpandConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ExpandConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
