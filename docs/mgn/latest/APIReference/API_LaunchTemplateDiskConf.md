---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_LaunchTemplateDiskConf.html
---

# LaunchTemplateDiskConf
<a name="API_LaunchTemplateDiskConf"></a>

Launch template disk configuration.

## Contents
<a name="API_LaunchTemplateDiskConf_Contents"></a>

 ** iops **   <a name="mgn-Type-LaunchTemplateDiskConf-iops"></a>
Launch template disk iops configuration.
Type: Long
Valid Range: Minimum value of 100. Maximum value of 64000.
Required: No

 ** throughput **   <a name="mgn-Type-LaunchTemplateDiskConf-throughput"></a>
Launch template disk throughput configuration.
Type: Long
Valid Range: Minimum value of 125. Maximum value of 1000.
Required: No

 ** volumeType **   <a name="mgn-Type-LaunchTemplateDiskConf-volumeType"></a>
Launch template disk volume type configuration.
Type: String
Valid Values: `io1 | io2 | gp3 | gp2 | st1 | sc1 | standard`
Required: No

## See Also
<a name="API_LaunchTemplateDiskConf_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/LaunchTemplateDiskConf)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/LaunchTemplateDiskConf)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/LaunchTemplateDiskConf)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
