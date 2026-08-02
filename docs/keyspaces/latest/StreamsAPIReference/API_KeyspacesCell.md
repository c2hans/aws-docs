---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_KeyspacesCell.html
---

# KeyspacesCell
<a name="API_KeyspacesCell"></a>

Represents a cell in an Amazon Keyspaces table, containing both the value and metadata about the cell.

## Contents
<a name="API_KeyspacesCell_Contents"></a>

 ** metadata **   <a name="keyspaces-Type-KeyspacesCell-metadata"></a>
Metadata associated with this cell, such as time-to-live (TTL) expiration time and write timestamp.
Type: [KeyspacesMetadata](API_KeyspacesMetadata.md) object
Required: No

 ** value **   <a name="keyspaces-Type-KeyspacesCell-value"></a>
The value stored in this cell, which can be of various data types supported by Amazon Keyspaces.
Type: [KeyspacesCellValue](API_KeyspacesCellValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_KeyspacesCell_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/KeyspacesCell)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/KeyspacesCell)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/KeyspacesCell)
