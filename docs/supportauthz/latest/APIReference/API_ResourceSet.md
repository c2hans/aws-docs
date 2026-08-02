---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_ResourceSet.html
---

# ResourceSet
<a name="API_ResourceSet"></a>

The set of resources authorized by a permit. Specify either all resources in the Region or a list of specific resources.

## Contents
<a name="API_ResourceSet_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** allResourcesInRegion **   <a name="supportauthorization-Type-ResourceSet-allResourcesInRegion"></a>
Authorizes the support operator to act on all resources in the Region.
Type: Structure
Required: No

 ** resources **   <a name="supportauthorization-Type-ResourceSet-resources"></a>
A list of specific resource identifiers that the support operator is authorized to act upon. Maximum of 5 resources.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/_.-]+`
Required: No

## See Also
<a name="API_ResourceSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/ResourceSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/ResourceSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/ResourceSet)
