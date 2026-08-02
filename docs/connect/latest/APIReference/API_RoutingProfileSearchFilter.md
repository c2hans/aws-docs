---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfileSearchFilter.html
---

# RoutingProfileSearchFilter
<a name="API_RoutingProfileSearchFilter"></a>

Filters to be applied to search results.

## Contents
<a name="API_RoutingProfileSearchFilter_Contents"></a>

 ** TagFilter **   <a name="connect-Type-RoutingProfileSearchFilter-TagFilter"></a>
An object that can be used to specify Tag conditions inside the `SearchFilter`. This accepts an `OR` of `AND` (List of List) input where:
+ Top level list specifies conditions that need to be applied with `OR` operator
+ Inner list specifies conditions that need to be applied with `AND` operator.
Type: [ControlPlaneTagFilter](API_ControlPlaneTagFilter.md) object
Required: No

## See Also
<a name="API_RoutingProfileSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RoutingProfileSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RoutingProfileSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RoutingProfileSearchFilter)
