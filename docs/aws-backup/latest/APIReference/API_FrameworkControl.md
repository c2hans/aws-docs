---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_FrameworkControl.html
---

# FrameworkControl
<a name="API_FrameworkControl"></a>

Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.

## Contents
<a name="API_FrameworkControl_Contents"></a>

 ** ControlName **   <a name="Backup-Type-FrameworkControl-ControlName"></a>
The name of a control. This name is between 1 and 256 characters.
Type: String
Required: Yes

 ** ControlInputParameters **   <a name="Backup-Type-FrameworkControl-ControlInputParameters"></a>
The name/value pairs.
Type: Array of [ControlInputParameter](API_ControlInputParameter.md) objects
Required: No

 ** ControlScope **   <a name="Backup-Type-FrameworkControl-ControlScope"></a>
The scope of a control. The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans.
For more information, see [`ControlScope`.](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlScope.html)
Type: [ControlScope](API_ControlScope.md) object
Required: No

## See Also
<a name="API_FrameworkControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/FrameworkControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/FrameworkControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/FrameworkControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
