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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
