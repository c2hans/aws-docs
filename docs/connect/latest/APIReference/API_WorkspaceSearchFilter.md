---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_WorkspaceSearchFilter.html
---

# WorkspaceSearchFilter
<a name="API_WorkspaceSearchFilter"></a>

Defines filters to apply when searching for workspaces, such as tag-based filters.

## Contents
<a name="API_WorkspaceSearchFilter_Contents"></a>

 ** AttributeFilter **   <a name="connect-Type-WorkspaceSearchFilter-AttributeFilter"></a>
An object that can be used to specify Tag conditions inside the `SearchFilter`. This accepts an `OR` or `AND` (List of List) input where:
+ The top level list specifies conditions that need to be applied with `OR` operator.
+ The inner list specifies conditions that need to be applied with `AND` operator.
Type: [ControlPlaneAttributeFilter](API_ControlPlaneAttributeFilter.md) object
Required: No

## See Also
<a name="API_WorkspaceSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/WorkspaceSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/WorkspaceSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/WorkspaceSearchFilter)
