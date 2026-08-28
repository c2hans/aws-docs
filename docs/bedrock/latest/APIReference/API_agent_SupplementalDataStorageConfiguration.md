---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_SupplementalDataStorageConfiguration.html
---

# SupplementalDataStorageConfiguration
<a name="API_agent_SupplementalDataStorageConfiguration"></a>

Specifies configurations for the storage location of multimedia content (images, audio, and video) extracted from multimodal documents in your data source. This content can be retrieved and returned to the end user with timestamp references for audio and video segments.

## Contents
<a name="API_agent_SupplementalDataStorageConfiguration_Contents"></a>

 ** storageLocations **   <a name="bedrock-Type-agent_SupplementalDataStorageConfiguration-storageLocations"></a>
A list of objects specifying storage locations for multimedia content (images, audio, and video) extracted from multimodal documents in your data source.
Type: Array of [SupplementalDataStorageLocation](API_agent_SupplementalDataStorageLocation.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## See Also
<a name="API_agent_SupplementalDataStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/SupplementalDataStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/SupplementalDataStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/SupplementalDataStorageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
