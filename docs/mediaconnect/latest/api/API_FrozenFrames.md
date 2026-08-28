---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_FrozenFrames.html
---

# FrozenFrames
<a name="API_FrozenFrames"></a>

 Configures settings for the `FrozenFrames` metric.

## Contents
<a name="API_FrozenFrames_Contents"></a>

 ** state **   <a name="mediaconnect-Type-FrozenFrames-state"></a>
Indicates whether the `FrozenFrames` metric is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** thresholdSeconds **   <a name="mediaconnect-Type-FrozenFrames-thresholdSeconds"></a>
 Specifies the number of consecutive seconds of a static image that triggers an event or alert.
Type: Integer
Required: No

## See Also
<a name="API_FrozenFrames_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/FrozenFrames)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/FrozenFrames)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/FrozenFrames)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
