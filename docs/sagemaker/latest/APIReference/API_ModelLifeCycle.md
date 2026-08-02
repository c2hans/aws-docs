---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelLifeCycle.html
---

# ModelLifeCycle
<a name="API_ModelLifeCycle"></a>

 A structure describing the current state of the model in its life cycle.

## Contents
<a name="API_ModelLifeCycle_Contents"></a>

 ** Stage **   <a name="sagemaker-Type-ModelLifeCycle-Stage"></a>
 The current stage in the model life cycle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** StageStatus **   <a name="sagemaker-Type-ModelLifeCycle-StageStatus"></a>
 The current status of a stage in model life cycle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** StageDescription **   <a name="sagemaker-Type-ModelLifeCycle-StageDescription"></a>
 Describes the stage related details.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.{0,1024}`
Required: No

## See Also
<a name="API_ModelLifeCycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelLifeCycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelLifeCycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelLifeCycle)
