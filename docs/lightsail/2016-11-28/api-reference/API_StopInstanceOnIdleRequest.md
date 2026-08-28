---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_StopInstanceOnIdleRequest.html
---

# StopInstanceOnIdleRequest
<a name="API_StopInstanceOnIdleRequest"></a>

Describes a request to create or edit the `StopInstanceOnIdle` add-on.

**Important**
This add-on only applies to Lightsail for Research resources.

## Contents
<a name="API_StopInstanceOnIdleRequest_Contents"></a>

 ** duration **   <a name="Lightsail-Type-StopInstanceOnIdleRequest-duration"></a>
The amount of idle time in minutes after which your virtual computer will automatically stop.
Type: String
Required: No

 ** threshold **   <a name="Lightsail-Type-StopInstanceOnIdleRequest-threshold"></a>
The value to compare with the duration.
Type: String
Required: No

## See Also
<a name="API_StopInstanceOnIdleRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/StopInstanceOnIdleRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/StopInstanceOnIdleRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/StopInstanceOnIdleRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
