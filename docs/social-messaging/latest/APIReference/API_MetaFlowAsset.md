---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_MetaFlowAsset.html
---

# MetaFlowAsset
<a name="API_MetaFlowAsset"></a>

Represents a single asset file associated with a WhatsApp Flow, including a presigned download URL.

## Contents
<a name="API_MetaFlowAsset_Contents"></a>

 ** assetType **   <a name="Social-Type-MetaFlowAsset-assetType"></a>
The type of asset. Currently the only supported value is FLOW\_JSON.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** downloadUrl **   <a name="Social-Type-MetaFlowAsset-downloadUrl"></a>
A presigned URL from Meta for downloading the asset. The URL expires after a short period.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** name **   <a name="Social-Type-MetaFlowAsset-name"></a>
The filename of the asset (for example, flow.json).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## See Also
<a name="API_MetaFlowAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/MetaFlowAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/MetaFlowAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/MetaFlowAsset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
