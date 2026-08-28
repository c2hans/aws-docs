---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_ModalityRoutingConfiguration.html
---

# ModalityRoutingConfiguration
<a name="API_data-automation_ModalityRoutingConfiguration"></a>

This element allows you to set up where JPEG, PNG, MOV, and MP4 files get routed to for processing. JPEG routing applies to both "JPEG" and "JPG" file extensions.

## Contents
<a name="API_data-automation_ModalityRoutingConfiguration_Contents"></a>

 ** jpeg **   <a name="bedrock-Type-data-automation_ModalityRoutingConfiguration-jpeg"></a>
Sets whether JPEG files are routed to document or image processing.
Type: String
Valid Values: `IMAGE | DOCUMENT | AUDIO | VIDEO`
Required: No

 ** mov **   <a name="bedrock-Type-data-automation_ModalityRoutingConfiguration-mov"></a>
Sets whether MOV files are routed to audio or video processing.
Type: String
Valid Values: `IMAGE | DOCUMENT | AUDIO | VIDEO`
Required: No

 ** mp4 **   <a name="bedrock-Type-data-automation_ModalityRoutingConfiguration-mp4"></a>
Sets whether MP4 files are routed to audio or video processing.
Type: String
Valid Values: `IMAGE | DOCUMENT | AUDIO | VIDEO`
Required: No

 ** png **   <a name="bedrock-Type-data-automation_ModalityRoutingConfiguration-png"></a>
Sets whether PNG files are routed to document or image processing.
Type: String
Valid Values: `IMAGE | DOCUMENT | AUDIO | VIDEO`
Required: No

## See Also
<a name="API_data-automation_ModalityRoutingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/ModalityRoutingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/ModalityRoutingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/ModalityRoutingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
