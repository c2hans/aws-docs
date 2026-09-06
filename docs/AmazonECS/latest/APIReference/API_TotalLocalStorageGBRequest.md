---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TotalLocalStorageGBRequest.html
---

# TotalLocalStorageGBRequest
<a name="API_TotalLocalStorageGBRequest"></a>

The minimum and maximum total local storage in gigabytes (GB) for instance types with local storage. This is useful for workloads that require local storage for temporary data or caching.

## Contents
<a name="API_TotalLocalStorageGBRequest_Contents"></a>

 ** max **   <a name="ECS-Type-TotalLocalStorageGBRequest-max"></a>
The maximum total local storage in GB. Instance types with more local storage are excluded from selection.
Type: Double
Required: No

 ** min **   <a name="ECS-Type-TotalLocalStorageGBRequest-min"></a>
The minimum total local storage in GB. Instance types with less local storage are excluded from selection.
Type: Double
Required: No

## See Also
<a name="API_TotalLocalStorageGBRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TotalLocalStorageGBRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TotalLocalStorageGBRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TotalLocalStorageGBRequest)
