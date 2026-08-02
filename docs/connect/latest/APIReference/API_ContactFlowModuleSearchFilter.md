---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowModuleSearchFilter.html
---

# ContactFlowModuleSearchFilter
<a name="API_ContactFlowModuleSearchFilter"></a>

The search criteria to be used to return flow modules.

## Contents
<a name="API_ContactFlowModuleSearchFilter_Contents"></a>

 ** TagFilter **   <a name="connect-Type-ContactFlowModuleSearchFilter-TagFilter"></a>
An object that can be used to specify Tag conditions inside the `SearchFilter`. This accepts an `OR` of `AND` (List of List) input where:
+ Top level list specifies conditions that need to be applied with `OR` operator
+ Inner list specifies conditions that need to be applied with `AND` operator.
Type: [ControlPlaneTagFilter](API_ControlPlaneTagFilter.md) object
Required: No

## See Also
<a name="API_ContactFlowModuleSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowModuleSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowModuleSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowModuleSearchFilter)
