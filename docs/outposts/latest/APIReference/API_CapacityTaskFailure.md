---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CapacityTaskFailure.html
---

# CapacityTaskFailure
<a name="API_CapacityTaskFailure"></a>

The capacity tasks that failed.

## Contents
<a name="API_CapacityTaskFailure_Contents"></a>

 ** Reason **   <a name="outposts-Type-CapacityTaskFailure-Reason"></a>
The reason that the specified capacity task failed.
Type: String
Length Constraints: Maximum length of 128.
Required: Yes

 ** Type **   <a name="outposts-Type-CapacityTaskFailure-Type"></a>
The type of failure.
Type: String
Valid Values: `UNSUPPORTED_CAPACITY_CONFIGURATION | UNEXPECTED_ASSET_STATE | BLOCKING_INSTANCES_NOT_EVACUATED | INTERNAL_SERVER_ERROR | RESOURCE_NOT_FOUND`
Required: No

## See Also
<a name="API_CapacityTaskFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CapacityTaskFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CapacityTaskFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CapacityTaskFailure)
