---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ApplicationTagResult.html
---

# ApplicationTagResult
<a name="API_app-registry_ApplicationTagResult"></a>

 The result of the application tag that's applied to a resource.

## Contents
<a name="API_app-registry_ApplicationTagResult_Contents"></a>

 ** applicationTagStatus **   <a name="servicecatalog-Type-app-registry_ApplicationTagResult-applicationTagStatus"></a>
 The application tag is in the process of being applied to a resource, was successfully applied to a resource, or failed to apply to a resource.
Type: String
Valid Values: `IN_PROGRESS | SUCCESS | FAILURE`
Required: No

 ** errorMessage **   <a name="servicecatalog-Type-app-registry_ApplicationTagResult-errorMessage"></a>
 The message returned if the call fails.
Type: String
Required: No

 ** nextToken **   <a name="servicecatalog-Type-app-registry_ApplicationTagResult-nextToken"></a>
 A unique pagination token for each page of results. Make the call again with the returned token to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2024.
Pattern: `[A-Za-z0-9+/=]+`
Required: No

 ** resources **   <a name="servicecatalog-Type-app-registry_ApplicationTagResult-resources"></a>
 The resources associated with an application
Type: Array of [ResourcesListItem](API_app-registry_ResourcesListItem.md) objects
Required: No

## See Also
<a name="API_app-registry_ApplicationTagResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ApplicationTagResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ApplicationTagResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ApplicationTagResult)
