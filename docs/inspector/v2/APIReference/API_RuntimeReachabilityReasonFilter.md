---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_RuntimeReachabilityReasonFilter.html
---

# RuntimeReachabilityReasonFilter

An object that describes the details of a runtime reachability reason filter.

## Contents
<a name="API_RuntimeReachabilityReasonFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-RuntimeReachabilityReasonFilter-comparison"></a>
The operator to use when comparing values in the filter.
Type: String
Valid Values: `EQUALS | NOT_EQUALS`
Required: Yes

 ** value **   <a name="inspector2-Type-RuntimeReachabilityReasonFilter-value"></a>
The runtime reachability reason to filter on.
Type: String
Valid Values: `PACKAGE_IN_DOCKERFILE_WORKLOAD_PATH | PACKAGE_NOT_IN_DOCKERFILE_WORKLOAD_PATH | PROCESS_OBSERVED_IN_EC2_RUNTIME | PROCESS_NOT_OBSERVED_IN_EC2_RUNTIME`
Required: Yes

## See Also
<a name="API_RuntimeReachabilityReasonFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/RuntimeReachabilityReasonFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/RuntimeReachabilityReasonFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/RuntimeReachabilityReasonFilter)
