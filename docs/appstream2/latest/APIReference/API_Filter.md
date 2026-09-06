---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A filter for narrowing down the results when listing export image tasks. Filters allow you to specify criteria such as task state or creation date.

## Contents
<a name="API_Filter_Contents"></a>

 ** Name **   <a name="WorkSpacesApplications-Type-Filter-Name"></a>
The name of the filter. Valid filter names depend on the operation being performed.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** Values **   <a name="WorkSpacesApplications-Type-Filter-Values"></a>
The values for the filter. Multiple values can be specified for a single filter name.
Type: Array of strings
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_:/.-]{0,200}$`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/Filter)
