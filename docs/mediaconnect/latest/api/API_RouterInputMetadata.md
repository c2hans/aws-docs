---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputMetadata.html
---

# RouterInputMetadata
<a name="API_RouterInputMetadata"></a>

Metadata information associated with the router input, including stream details and connection state.

## Contents
<a name="API_RouterInputMetadata_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** transportStreamMediaInfo **   <a name="mediaconnect-Type-RouterInputMetadata-transportStreamMediaInfo"></a>
 The metadata of the transport stream in the current flow's source.
Type: [TransportMediaInfo](API_TransportMediaInfo.md) object
Required: No

## See Also
<a name="API_RouterInputMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
