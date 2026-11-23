---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_RuntimeReachabilityFilter.html
---

# RuntimeReachabilityFilter

An object that describes the details of a runtime reachability filter.

## Contents
<a name="API_RuntimeReachabilityFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-RuntimeReachabilityFilter-comparison"></a>
The operator to use when comparing values in the filter.
Type: String
Valid Values: `EQUALS | NOT_EQUALS`
Required: Yes

 ** value **   <a name="inspector2-Type-RuntimeReachabilityFilter-value"></a>
The runtime reachability status to filter on.
Type: String
Valid Values: `REACHABLE | NOT_REACHABLE | UNKNOWN`
Required: Yes

## See Also
<a name="API_RuntimeReachabilityFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/RuntimeReachabilityFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/RuntimeReachabilityFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/RuntimeReachabilityFilter)
