---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DocumentMetadata.html
---

# DocumentMetadata
<a name="API_agent_DocumentMetadata"></a>

Contains information about the metadata associate with the content to ingest into a knowledge base. Choose a `type` and include the field that corresponds to it.

## Contents
<a name="API_agent_DocumentMetadata_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_DocumentMetadata-type"></a>
The type of the source source from which to add metadata.
Type: String
Valid Values: `IN_LINE_ATTRIBUTE | S3_LOCATION`
Required: Yes

 ** accessControlList **   <a name="bedrock-Type-agent_DocumentMetadata-accessControlList"></a>
Access control list for the document. Used when metadata type is IN\_LINE\_ATTRIBUTE.
Type: Array of [DocumentAccessControlEntry](API_agent_DocumentAccessControlEntry.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** inlineAttributes **   <a name="bedrock-Type-agent_DocumentMetadata-inlineAttributes"></a>
An array of objects, each of which defines a metadata attribute to associate with the content to ingest. You define the attributes inline.
Type: Array of [MetadataAttribute](API_agent_MetadataAttribute.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** s3Location **   <a name="bedrock-Type-agent_DocumentMetadata-s3Location"></a>
The Amazon S3 location of the file containing metadata to associate with the content to ingest.
Type: [CustomS3Location](API_agent_CustomS3Location.md) object
Required: No

## See Also
<a name="API_agent_DocumentMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DocumentMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DocumentMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DocumentMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
