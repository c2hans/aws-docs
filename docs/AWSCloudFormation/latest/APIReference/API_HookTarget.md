---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_HookTarget.html
---

# HookTarget
<a name="API_HookTarget"></a>

The `HookTarget` data type.

## Contents
<a name="API_HookTarget_Contents"></a>

 ** Action **
The action that invoked the Hook.
Type: String
Valid Values: `CREATE | UPDATE | DELETE | IMPORT`
Required: Yes

 ** TargetId **
The unique identifier of the Hook invocation target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^_]*`
Required: Yes

 ** TargetType **
The target type.
Type: String
Valid Values: `RESOURCE`
Required: Yes

 ** TargetTypeName **
The target name, for example, `AWS::S3::Bucket`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}$`
Required: Yes

## See Also
<a name="API_HookTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/HookTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/HookTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/HookTarget)
