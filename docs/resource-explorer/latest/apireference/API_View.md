---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_View.html
---

# View
<a name="API_View"></a>

A view is a structure that defines a set of filters that provide a view into the information in the AWS Resource Explorer index. The filters specify which information from the index is visible to the users of the view. For example, you can specify filters that include only resources that are tagged with the key "ENV" and the value "DEVELOPMENT" in the results returned by this view. You could also create a second view that includes only resources that are tagged with "ENV" and "PRODUCTION".

## Contents
<a name="API_View_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Filters **   <a name="resourceexplorer-Type-View-Filters"></a>
An array of [SearchFilter](API_SearchFilter.md) objects that specify which resources can be included in the results of queries made using this view.
Type: [SearchFilter](API_SearchFilter.md) object
Required: No

 ** IncludedProperties **   <a name="resourceexplorer-Type-View-IncludedProperties"></a>
A structure that contains additional information about the view.
Type: Array of [IncludedProperty](API_IncludedProperty.md) objects
Required: No

 ** LastUpdatedAt **   <a name="resourceexplorer-Type-View-LastUpdatedAt"></a>
The date and time when this view was last modified.
Type: Timestamp
Required: No

 ** Owner **   <a name="resourceexplorer-Type-View-Owner"></a>
The AWS account that owns this view.
Type: String
Required: No

 ** Scope **   <a name="resourceexplorer-Type-View-Scope"></a>
An [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an AWS account, an organization, or an organizational unit (OU) that specifies whether this view includes resources from only the specified AWS account, all accounts in the specified organization, or all accounts in the specified OU.
If not specified, the value defaults to the AWS account used to call this operation.
Type: String
Required: No

 ** ViewArn **   <a name="resourceexplorer-Type-View-ViewArn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the view.
Type: String
Required: No

## See Also
<a name="API_View_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/View)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/View)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/View)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
