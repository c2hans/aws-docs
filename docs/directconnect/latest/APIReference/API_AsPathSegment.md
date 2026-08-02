---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AsPathSegment.html
---

# AsPathSegment
<a name="API_AsPathSegment"></a>

A segment of an autonomous system (AS) path.

## Contents
<a name="API_AsPathSegment_Contents"></a>

 ** path **   <a name="DX-Type-AsPathSegment-path"></a>
The autonomous system (AS) numbers in the segment.
Type: Array of longs
Required: No

 ** pathType **   <a name="DX-Type-AsPathSegment-pathType"></a>
The type of the AS path segment.
The valid values are `seq` (an ordered `AS_SEQUENCE`) and `set` (an unordered `AS_SET`).
Type: String
Valid Values: `seq | set`
Required: No

## See Also
<a name="API_AsPathSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AsPathSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AsPathSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AsPathSegment)
