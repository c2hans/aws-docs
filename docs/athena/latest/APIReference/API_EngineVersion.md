---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_EngineVersion.html
---

# EngineVersion
<a name="API_EngineVersion"></a>

The Athena engine version for running queries, or the PySpark engine version for running sessions.

## Contents
<a name="API_EngineVersion_Contents"></a>

 ** EffectiveEngineVersion **   <a name="athena-Type-EngineVersion-EffectiveEngineVersion"></a>
Read only. The engine version on which the query runs. If the user requests a valid engine version other than Auto, the effective engine version is the same as the engine version that the user requested. If the user requests Auto, the effective engine version is chosen by Athena. When a request to update the engine version is made by a `CreateWorkGroup` or `UpdateWorkGroup` operation, the `EffectiveEngineVersion` field is ignored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SelectedEngineVersion **   <a name="athena-Type-EngineVersion-SelectedEngineVersion"></a>
The engine version requested by the user. Possible values are determined by the output of `ListEngineVersions`, including AUTO. The default is AUTO.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_EngineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/EngineVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/EngineVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/EngineVersion)
