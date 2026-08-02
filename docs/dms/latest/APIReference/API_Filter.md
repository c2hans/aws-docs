---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Identifies the name and value of a filter object. This filter is used to limit the number and type of AWS DMS objects that are returned for a particular `Describe*` call or similar operation. Filters are used as an optional parameter for certain API operations.

## Contents
<a name="API_Filter_Contents"></a>

 ** Name **   <a name="DMS-Type-Filter-Name"></a>
The name of the filter as specified for a `Describe*` or similar operation.
Type: String
Required: Yes

 ** Values **   <a name="DMS-Type-Filter-Values"></a>
The filter value, which can specify one or more values used to narrow the returned results.
Type: Array of strings
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Filter)
