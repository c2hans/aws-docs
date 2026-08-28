---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_Diagnostics.html
---

# Diagnostics
<a name="API_Diagnostics"></a>

Diagnostic information about executable scripts that are part of a deployment.

## Contents
<a name="API_Diagnostics_Contents"></a>

 ** errorCode **   <a name="CodeDeploy-Type-Diagnostics-errorCode"></a>
The associated error code:
+ Success: The specified script ran.
+ ScriptMissing: The specified script was not found in the specified location.
+ ScriptNotExecutable: The specified script is not a recognized executable file type.
+ ScriptTimedOut: The specified script did not finish running in the specified time period.
+ ScriptFailed: The specified script failed to run as expected.
+ UnknownError: The specified script did not run for an unknown reason.
Type: String
Valid Values: `Success | ScriptMissing | ScriptNotExecutable | ScriptTimedOut | ScriptFailed | UnknownError`
Required: No

 ** logTail **   <a name="CodeDeploy-Type-Diagnostics-logTail"></a>
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.
Type: String
Required: No

 ** message **   <a name="CodeDeploy-Type-Diagnostics-message"></a>
The message associated with the error.
Type: String
Required: No

 ** scriptName **   <a name="CodeDeploy-Type-Diagnostics-scriptName"></a>
The name of the script.
Type: String
Required: No

## See Also
<a name="API_Diagnostics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/Diagnostics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/Diagnostics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/Diagnostics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
