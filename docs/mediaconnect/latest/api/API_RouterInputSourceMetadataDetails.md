---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputSourceMetadataDetails.html
---

# RouterInputSourceMetadataDetails
<a name="API_RouterInputSourceMetadataDetails"></a>

Detailed metadata information about a router input source.

## Contents
<a name="API_RouterInputSourceMetadataDetails_Contents"></a>

 ** sourceMetadataMessages **   <a name="mediaconnect-Type-RouterInputSourceMetadataDetails-sourceMetadataMessages"></a>
Collection of metadata messages associated with the router input source.
Type: Array of [RouterInputMessage](API_RouterInputMessage.md) objects
Required: Yes

 ** timestamp **   <a name="mediaconnect-Type-RouterInputSourceMetadataDetails-timestamp"></a>
The timestamp when the metadata was last updated.
Type: Timestamp
Required: Yes

 ** routerInputMetadata **   <a name="mediaconnect-Type-RouterInputSourceMetadataDetails-routerInputMetadata"></a>
Metadata information specific to the router input configuration and state.
Type: [RouterInputMetadata](API_RouterInputMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_RouterInputSourceMetadataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputSourceMetadataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputSourceMetadataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputSourceMetadataDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
