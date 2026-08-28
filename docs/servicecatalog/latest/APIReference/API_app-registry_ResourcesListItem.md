---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ResourcesListItem.html
---

# ResourcesListItem
<a name="API_app-registry_ResourcesListItem"></a>

 The resource in a list of resources.

## Contents
<a name="API_app-registry_ResourcesListItem_Contents"></a>

 ** errorMessage **   <a name="servicecatalog-Type-app-registry_ResourcesListItem-errorMessage"></a>
 The message returned if the call fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** resourceArn **   <a name="servicecatalog-Type-app-registry_ResourcesListItem-resourceArn"></a>
 The Amazon resource name (ARN) of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

 ** resourceType **   <a name="servicecatalog-Type-app-registry_ResourcesListItem-resourceType"></a>
 Provides information about the AppRegistry resource type.
Type: String
Pattern: `AWS::[a-zA-Z0-9]+::\w+`
Required: No

 ** status **   <a name="servicecatalog-Type-app-registry_ResourcesListItem-status"></a>
 The status of the list item.
Type: String
Required: No

## See Also
<a name="API_app-registry_ResourcesListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ResourcesListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ResourcesListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ResourcesListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
