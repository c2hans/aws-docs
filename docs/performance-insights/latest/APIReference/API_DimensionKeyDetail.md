---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DimensionKeyDetail.html
---

# DimensionKeyDetail
<a name="API_DimensionKeyDetail"></a>

An object that describes the details for a specified dimension.

## Contents
<a name="API_DimensionKeyDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimension **   <a name="performanceinsights-Type-DimensionKeyDetail-Dimension"></a>
The full name of the dimension. The full name includes the group name and key name. The following values are valid:
+  `db.query.statement` (Amazon DocumentDB)
+  `db.sql.statement` (Amazon RDS and Aurora)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="performanceinsights-Type-DimensionKeyDetail-Status"></a>
The status of the dimension detail data. Possible values include the following:
+  `AVAILABLE` - The dimension detail data is ready to be retrieved.
+  `PROCESSING` - The dimension detail data isn't ready to be retrieved because more processing time is required. If the requested detail data has the status `PROCESSING`, Performance Insights returns the truncated query.
+  `UNAVAILABLE` - The dimension detail data could not be collected successfully.
Type: String
Valid Values: `AVAILABLE | PROCESSING | UNAVAILABLE`
Required: No

 ** Value **   <a name="performanceinsights-Type-DimensionKeyDetail-Value"></a>
The value of the dimension detail data. Depending on the return status, this value is either the full or truncated SQL query for the following dimensions:
+  `db.query.statement` (Amazon DocumentDB)
+  `db.sql.statement` (Amazon RDS and Aurora)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_DimensionKeyDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/DimensionKeyDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/DimensionKeyDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/DimensionKeyDetail)
