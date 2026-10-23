---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ApproximateDriftedResourceCount.html
---

# ApproximateDriftedResourceCount
<a name="API_ApproximateDriftedResourceCount"></a>

Contains an approximate count of the resources of a given type that are not yet in sync in a Region, along with the time the count was last calculated.

## Contents
<a name="API_ApproximateDriftedResourceCount_Contents"></a>

 ** Count **   <a name="connect-Type-ApproximateDriftedResourceCount-Count"></a>
The approximate number of resources of the requested type that are not yet in sync in the Region. A value of zero means the resources are in sync.
Type: Long
Required: Yes

 ** Region **   <a name="connect-Type-ApproximateDriftedResourceCount-Region"></a>
The AWS Region that the count applies to.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 31.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: Yes

 ** Timestamp **   <a name="connect-Type-ApproximateDriftedResourceCount-Timestamp"></a>
The time, in Unix epoch time, when the count was last calculated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_ApproximateDriftedResourceCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ApproximateDriftedResourceCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ApproximateDriftedResourceCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ApproximateDriftedResourceCount)
