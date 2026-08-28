---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ControlInputParameter.html
---

# ControlInputParameter
<a name="API_ControlInputParameter"></a>

The parameters for a control. A control can have zero, one, or more than one parameter. An example of a control with two parameters is: "backup plan frequency is at least `daily` and the retention period is at least `1 year`". The first parameter is `daily`. The second parameter is `1 year`.

## Contents
<a name="API_ControlInputParameter_Contents"></a>

 ** ParameterName **   <a name="Backup-Type-ControlInputParameter-ParameterName"></a>
The name of a parameter, for example, `BackupPlanFrequency`.
Type: String
Required: No

 ** ParameterValue **   <a name="Backup-Type-ControlInputParameter-ParameterValue"></a>
The value of parameter, for example, `hourly`.
Type: String
Required: No

## See Also
<a name="API_ControlInputParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ControlInputParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ControlInputParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ControlInputParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
