---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ResourceErrorsDetails.html
---

# ResourceErrorsDetails
<a name="API_ResourceErrorsDetails"></a>

 A list of errors retrieving an application's resources.

## Contents
<a name="API_ResourceErrorsDetails_Contents"></a>

 ** hasMoreErrors **   <a name="resiliencehub-Type-ResourceErrorsDetails-hasMoreErrors"></a>
 This indicates if there are more errors not listed in the `resourceErrors` list.
Type: Boolean
Required: No

 ** resourceErrors **   <a name="resiliencehub-Type-ResourceErrorsDetails-resourceErrors"></a>
 A list of errors retrieving an application's resources.
Type: Array of [ResourceError](API_ResourceError.md) objects
Required: No

## See Also
<a name="API_ResourceErrorsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ResourceErrorsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ResourceErrorsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ResourceErrorsDetails)
