---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_WorkspaceErrorDetails.html
---

# WorkspaceErrorDetails
<a name="API_WorkspaceErrorDetails"></a>

Contains the details of an error associated with a workspace.

## Contents
<a name="API_WorkspaceErrorDetails_Contents"></a>

 ** code **   <a name="iotsitewise-Type-WorkspaceErrorDetails-code"></a>
The error code.
Type: String
Valid Values: `VALIDATION_ERROR | INTERNAL_FAILURE`
Required: Yes

 ** message **   <a name="iotsitewise-Type-WorkspaceErrorDetails-message"></a>
The error message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

## See Also
<a name="API_WorkspaceErrorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/WorkspaceErrorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/WorkspaceErrorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/WorkspaceErrorDetails)
