---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTable.html
---

# ConfiguredTable
<a name="API_ConfiguredTable"></a>

A table that has been configured for use in a collaboration.

## Contents
<a name="API_ConfiguredTable_Contents"></a>

 ** allowedColumns **   <a name="API-Type-ConfiguredTable-allowedColumns"></a>
The columns within the underlying AWS Glue table that can be used within collaborations.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** analysisMethod **   <a name="API-Type-ConfiguredTable-analysisMethod"></a>
The analysis method for the configured table.
 `DIRECT_QUERY` allows SQL queries to be run directly on this table.
 `DIRECT_JOB` allows PySpark jobs to be run directly on this table.
 `MULTIPLE` allows both SQL queries and PySpark jobs to be run directly on this table.
Type: String
Valid Values: `DIRECT_QUERY | DIRECT_JOB | MULTIPLE`
Required: Yes

 ** analysisRuleTypes **   <a name="API-Type-ConfiguredTable-analysisRuleTypes"></a>
The types of analysis rules associated with this configured table. Currently, only one analysis rule may be associated with a configured table.
Type: Array of strings
Valid Values: `AGGREGATION | LIST | CUSTOM`
Required: Yes

 ** arn **   <a name="API-Type-ConfiguredTable-arn"></a>
The unique ARN for the configured table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:configuredtable/[\d\w-]+`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredTable-createTime"></a>
The time the configured table was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-ConfiguredTable-id"></a>
The unique ID for the configured table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-ConfiguredTable-name"></a>
A name for the configured table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** tableReference **   <a name="API-Type-ConfiguredTable-tableReference"></a>
The table that this configured table represents.
Type: [TableReference](API_TableReference.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredTable-updateTime"></a>
The time the configured table was last updated
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-ConfiguredTable-description"></a>
A description for the configured table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** selectedAnalysisMethods **   <a name="API-Type-ConfiguredTable-selectedAnalysisMethods"></a>
 The selected analysis methods for the configured table.
Type: Array of strings
Valid Values: `DIRECT_QUERY | DIRECT_JOB`
Required: No

## See Also
<a name="API_ConfiguredTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTable)
