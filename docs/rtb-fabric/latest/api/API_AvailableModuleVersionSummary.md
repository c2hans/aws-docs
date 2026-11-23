---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_AvailableModuleVersionSummary.html
---

# AvailableModuleVersionSummary

A version of a module that you can attach, as ListAvailableModuleVersions returns it. ListAvailableModuleVersions and GetAvailableModuleVersion never return how a version is implemented.

## Contents
<a name="API_AvailableModuleVersionSummary_Contents"></a>

 ** createdAt **   <a name="rtbfabric-Type-AvailableModuleVersionSummary-createdAt"></a>
The time when the version was created.
Type: Timestamp
Required: Yes

 ** moduleVersionArn **   <a name="rtbfabric-Type-AvailableModuleVersionSummary-moduleVersionArn"></a>
The version's ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1011.
Pattern: `arn:aws[a-zA-Z-]*:rtbfabric:[a-z0-9-]+::modules/module-[a-zA-Z0-9]{1,25}/versions/(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})`
Required: Yes

 ** status **   <a name="rtbfabric-Type-AvailableModuleVersionSummary-status"></a>
ACTIVE or DEPRECATED.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DEPRECATED`
Required: Yes

 ** version **   <a name="rtbfabric-Type-AvailableModuleVersionSummary-version"></a>
The version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})`
Required: Yes

## See Also
<a name="API_AvailableModuleVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/AvailableModuleVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/AvailableModuleVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/AvailableModuleVersionSummary)
