---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RunCommandParameters.html
---

# RunCommandParameters
<a name="API_RunCommandParameters"></a>

This parameter contains the criteria (either InstanceIds or a tag) used to specify which EC2 instances are to be sent the command.

## Contents
<a name="API_RunCommandParameters_Contents"></a>

 ** RunCommandTargets **   <a name="eventbridge-Type-RunCommandParameters-RunCommandTargets"></a>
Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.
Type: Array of [RunCommandTarget](API_RunCommandTarget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## See Also
<a name="API_RunCommandParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/RunCommandParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/RunCommandParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/RunCommandParameters)
