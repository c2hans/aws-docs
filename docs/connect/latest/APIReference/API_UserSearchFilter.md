---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserSearchFilter.html
---

# UserSearchFilter
<a name="API_UserSearchFilter"></a>

Filters to be applied to search results.

## Contents
<a name="API_UserSearchFilter_Contents"></a>

 ** TagFilter **   <a name="connect-Type-UserSearchFilter-TagFilter"></a>
An object that can be used to specify Tag conditions inside the `SearchFilter`. This accepts an `OR` of `AND` (List of List) input where:
+ Top level list specifies conditions that need to be applied with `OR` operator
+ Inner list specifies conditions that need to be applied with `AND` operator.
Type: [ControlPlaneTagFilter](API_ControlPlaneTagFilter.md) object
Required: No

 ** UserAttributeFilter **   <a name="connect-Type-UserSearchFilter-UserAttributeFilter"></a>
An object that can be used to specify Tag conditions or Hierarchy Group conditions inside the SearchFilter.
This accepts an `OR` of `AND` (List of List) input where:
+ The top level list specifies conditions that need to be applied with `OR` operator.
+ The inner list specifies conditions that need to be applied with `AND` operator.
Only one field can be populated. This object can’t be used along with TagFilter. Request can either contain TagFilter or UserAttributeFilter if SearchFilter is specified, combination of both is not supported and such request will throw AccessDeniedException.
Type: [ControlPlaneUserAttributeFilter](API_ControlPlaneUserAttributeFilter.md) object
Required: No

## See Also
<a name="API_UserSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserSearchFilter)
