---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_AllowedStatistics.html
---

# AllowedStatistics
<a name="API_AllowedStatistics"></a>

Configuration of statistics that are allowed to be run on columns that contain detected entities. When undefined, no statistics will be computed on columns that contain detected entities.

## Contents
<a name="API_AllowedStatistics_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Statistics **   <a name="databrew-Type-AllowedStatistics-Statistics"></a>
One or more column statistics to allow for columns that contain detected entities.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Z\_]+$`
Required: Yes

## See Also
<a name="API_AllowedStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/AllowedStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/AllowedStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/AllowedStatistics)
