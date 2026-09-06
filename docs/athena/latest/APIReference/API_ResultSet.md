---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ResultSet.html
---

# ResultSet
<a name="API_ResultSet"></a>

The metadata and rows that make up a query result set. The metadata describes the column structure and data types. To return a `ResultSet` object, use [GetQueryResults](API_GetQueryResults.md).

## Contents
<a name="API_ResultSet_Contents"></a>

 ** ResultSetMetadata **   <a name="athena-Type-ResultSet-ResultSetMetadata"></a>
The metadata that describes the column structure and data types of a table of query results.
Type: [ResultSetMetadata](API_ResultSetMetadata.md) object
Required: No

 ** Rows **   <a name="athena-Type-ResultSet-Rows"></a>
The rows in the table.
Type: Array of [Row](API_Row.md) objects
Required: No

## See Also
<a name="API_ResultSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ResultSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ResultSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ResultSet)
