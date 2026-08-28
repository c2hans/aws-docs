---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_KeyspacesCellMapDefinition.html
---

# KeyspacesCellMapDefinition
<a name="API_KeyspacesCellMapDefinition"></a>

Represents a key-value pair within a map data type in Amazon Keyspaces, including the associated metadata.

## Contents
<a name="API_KeyspacesCellMapDefinition_Contents"></a>

 ** key **   <a name="keyspaces-Type-KeyspacesCellMapDefinition-key"></a>
The key of this map entry in the Amazon Keyspaces cell.
Type: [KeyspacesCellValue](API_KeyspacesCellValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** metadata **   <a name="keyspaces-Type-KeyspacesCellMapDefinition-metadata"></a>
Metadata for this specific key-value pair within the map, such as timestamps and TTL information.
Type: [KeyspacesMetadata](API_KeyspacesMetadata.md) object
Required: No

 ** value **   <a name="keyspaces-Type-KeyspacesCellMapDefinition-value"></a>
The value associated with the key in this map entry.
Type: [KeyspacesCellValue](API_KeyspacesCellValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_KeyspacesCellMapDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/KeyspacesCellMapDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/KeyspacesCellMapDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/KeyspacesCellMapDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
