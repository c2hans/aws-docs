---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_WorkspaceSummary.html
---

# WorkspaceSummary
<a name="API_WorkspaceSummary"></a>

An object that contains information about a workspace.

## Contents
<a name="API_WorkspaceSummary_Contents"></a>

 ** arn **   <a name="tm-Type-WorkspaceSummary-arn"></a>
The ARN of the workspace.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`
Required: Yes

 ** creationDateTime **   <a name="tm-Type-WorkspaceSummary-creationDateTime"></a>
The date and time when the workspace was created.
Type: Timestamp
Required: Yes

 ** updateDateTime **   <a name="tm-Type-WorkspaceSummary-updateDateTime"></a>
The date and time when the workspace was last updated.
Type: Timestamp
Required: Yes

 ** workspaceId **   <a name="tm-Type-WorkspaceSummary-workspaceId"></a>
The ID of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

 ** description **   <a name="tm-Type-WorkspaceSummary-description"></a>
The description of the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** linkedServices **   <a name="tm-Type-WorkspaceSummary-linkedServices"></a>
A list of services that are linked to the workspace.
Type: Array of strings
Pattern: `[a-zA-Z_0-9]+`
Required: No

## See Also
<a name="API_WorkspaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/WorkspaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/WorkspaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/WorkspaceSummary)
