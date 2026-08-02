---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ControlPlaneTagFilter.html
---

# ControlPlaneTagFilter
<a name="API_ControlPlaneTagFilter"></a>

An object that can be used to specify Tag conditions inside the `SearchFilter`. This accepts an `OR` of `AND` (List of List) input where:
+ Top level list specifies conditions that need to be applied with `OR` operator
+ Inner list specifies conditions that need to be applied with `AND` operator.

## Contents
<a name="API_ControlPlaneTagFilter_Contents"></a>

 ** AndConditions **   <a name="connect-Type-ControlPlaneTagFilter-AndConditions"></a>
A list of conditions which would be applied together with an `AND` condition.
Type: Array of [TagCondition](API_TagCondition.md) objects
Required: No

 ** OrConditions **   <a name="connect-Type-ControlPlaneTagFilter-OrConditions"></a>
A list of conditions which would be applied together with an `OR` condition.
Type: Array of arrays of [TagCondition](API_TagCondition.md) objects
Required: No

 ** TagCondition **   <a name="connect-Type-ControlPlaneTagFilter-TagCondition"></a>
A leaf node condition which can be used to specify a tag condition.
Type: [TagCondition](API_TagCondition.md) object
Required: No

## See Also
<a name="API_ControlPlaneTagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ControlPlaneTagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ControlPlaneTagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ControlPlaneTagFilter)
