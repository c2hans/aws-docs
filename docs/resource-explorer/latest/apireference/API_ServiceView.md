---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ServiceView.html
---

# ServiceView
<a name="API_ServiceView"></a>

Contains the configuration and properties of a Resource Explorer service view.

## Contents
<a name="API_ServiceView_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ServiceViewArn **   <a name="resourceexplorer-Type-ServiceView-ServiceViewArn"></a>
The Amazon Resource Name (ARN) of the service view.
Type: String
Required: Yes

 ** Filters **   <a name="resourceexplorer-Type-ServiceView-Filters"></a>
A search filter defines which resources can be part of a search query result set.
Type: [SearchFilter](API_SearchFilter.md) object
Required: No

 ** IncludedProperties **   <a name="resourceexplorer-Type-ServiceView-IncludedProperties"></a>
A list of additional resource properties that are included in this view for search and filtering purposes.
Type: Array of [IncludedProperty](API_IncludedProperty.md) objects
Required: No

 ** ScopeType **   <a name="resourceexplorer-Type-ServiceView-ScopeType"></a>
The scope type of the service view, which determines what resources are included.
Type: String
Required: No

 ** StreamingAccessForService **   <a name="resourceexplorer-Type-ServiceView-StreamingAccessForService"></a>
The AWS service that has streaming access to this view's data.
Type: String
Required: No

## See Also
<a name="API_ServiceView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ServiceView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ServiceView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ServiceView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
