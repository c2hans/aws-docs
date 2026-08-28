---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_LifeCycleLastLaunch.html
---

# LifeCycleLastLaunch
<a name="API_LifeCycleLastLaunch"></a>

An object containing information regarding the last launch of a Source Server.

## Contents
<a name="API_LifeCycleLastLaunch_Contents"></a>

 ** initiated **   <a name="drs-Type-LifeCycleLastLaunch-initiated"></a>
An object containing information regarding the initiation of the last launch of a Source Server.
Type: [LifeCycleLastLaunchInitiated](API_LifeCycleLastLaunchInitiated.md) object
Required: No

 ** status **   <a name="drs-Type-LifeCycleLastLaunch-status"></a>
Status of Source Server's last launch.
Type: String
Valid Values: `PENDING | IN_PROGRESS | LAUNCHED | FAILED | TERMINATED`
Required: No

## See Also
<a name="API_LifeCycleLastLaunch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/LifeCycleLastLaunch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/LifeCycleLastLaunch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/LifeCycleLastLaunch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
