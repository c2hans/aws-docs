---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_KeyspacesRow.html
---

# KeyspacesRow
<a name="API_KeyspacesRow"></a>

Represents a row in an Amazon Keyspaces table, containing regular column values, static column values, and row-level metadata.

## Contents
<a name="API_KeyspacesRow_Contents"></a>

 ** rowMetadata **   <a name="keyspaces-Type-KeyspacesRow-rowMetadata"></a>
Metadata that applies to the entire row, such as timestamps and TTL information.
Type: [KeyspacesMetadata](API_KeyspacesMetadata.md) object
Required: No

 ** staticCells **   <a name="keyspaces-Type-KeyspacesRow-staticCells"></a>
A map of static column cells shared by all rows with the same partition key, where keys are column names and values are the corresponding cells.
Type: String to [KeyspacesCell](API_KeyspacesCell.md) object map
Required: No

 ** valueCells **   <a name="keyspaces-Type-KeyspacesRow-valueCells"></a>
A map of regular (non-static) column cells in the row, where keys are column names and values are the corresponding cells.
Type: String to [KeyspacesCell](API_KeyspacesCell.md) object map
Required: No

## See Also
<a name="API_KeyspacesRow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/KeyspacesRow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/KeyspacesRow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/KeyspacesRow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
