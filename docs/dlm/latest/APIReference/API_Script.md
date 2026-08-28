---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_Script.html
---

# Script
<a name="API_Script"></a>

 **[Custom snapshot policies that target instances only]** Information about pre and/or post scripts for a snapshot lifecycle policy that targets instances. For more information, see [ Automating application-consistent snapshots with pre and post scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html).

## Contents
<a name="API_Script_Contents"></a>

 ** ExecutionHandler **   <a name="dlm-Type-Script-ExecutionHandler"></a>
The SSM document that includes the pre and/or post scripts to run.
+ If you are automating VSS backups, specify `AWS_VSS_BACKUP`. In this case, Amazon Data Lifecycle Manager automatically uses the `AWSEC2-CreateVssSnapshot` SSM document.
+ If you are automating application-consistent snapshots for SAP HANA workloads, specify `AWSSystemsManagerSAP-CreateDLMSnapshotForSAPHANA`.
+ If you are using a custom SSM document that you own, specify either the name or ARN of the SSM document. If you are using a custom SSM document that is shared with you, specify the ARN of the SSM document.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `^([a-zA-Z0-9_\-.]{3,128}|[a-zA-Z0-9_\-.:/]{3,200}|[A-Z0-9_]+)$`
Required: Yes

 ** ExecuteOperationOnScriptFailure **   <a name="dlm-Type-Script-ExecuteOperationOnScriptFailure"></a>
Indicates whether Amazon Data Lifecycle Manager should default to crash-consistent snapshots if the pre script fails.
+ To default to crash consistent snapshot if the pre script fails, specify `true`.
+ To skip the instance for snapshot creation if the pre script fails, specify `false`.
This parameter is supported only if you run a pre script. If you run a post script only, omit this parameter.
Default: true
Type: Boolean
Required: No

 ** ExecutionHandlerService **   <a name="dlm-Type-Script-ExecutionHandlerService"></a>
Indicates the service used to execute the pre and/or post scripts.
+ If you are using custom SSM documents or automating application-consistent snapshots of SAP HANA workloads, specify `AWS_SYSTEMS_MANAGER`.
+ If you are automating VSS Backups, omit this parameter.
Default: AWS\_SYSTEMS\_MANAGER
Type: String
Valid Values: `AWS_SYSTEMS_MANAGER`
Required: No

 ** ExecutionTimeout **   <a name="dlm-Type-Script-ExecutionTimeout"></a>
Specifies a timeout period, in seconds, after which Amazon Data Lifecycle Manager fails the script run attempt if it has not completed. If a script does not complete within its timeout period, Amazon Data Lifecycle Manager fails the attempt. The timeout period applies to the pre and post scripts individually.
If you are automating VSS Backups, omit this parameter.
Default: 10
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 120.
Required: No

 ** MaximumRetryCount **   <a name="dlm-Type-Script-MaximumRetryCount"></a>
Specifies the number of times Amazon Data Lifecycle Manager should retry scripts that fail.
+ If the pre script fails, Amazon Data Lifecycle Manager retries the entire snapshot creation process, including running the pre and post scripts.
+ If the post script fails, Amazon Data Lifecycle Manager retries the post script only; in this case, the pre script will have completed and the snapshot might have been created.
If you do not want Amazon Data Lifecycle Manager to retry failed scripts, specify `0`.
Default: 0
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3.
Required: No

 ** Stages **   <a name="dlm-Type-Script-Stages"></a>
Indicate which scripts Amazon Data Lifecycle Manager should run on target instances. Pre scripts run before Amazon Data Lifecycle Manager initiates snapshot creation. Post scripts run after Amazon Data Lifecycle Manager initiates snapshot creation.
+ To run a pre script only, specify `PRE`. In this case, Amazon Data Lifecycle Manager calls the SSM document with the `pre-script` parameter before initiating snapshot creation.
+ To run a post script only, specify `POST`. In this case, Amazon Data Lifecycle Manager calls the SSM document with the `post-script` parameter after initiating snapshot creation.
+ To run both pre and post scripts, specify both `PRE` and `POST`. In this case, Amazon Data Lifecycle Manager calls the SSM document with the `pre-script` parameter before initiating snapshot creation, and then it calls the SSM document again with the `post-script` parameter after initiating snapshot creation.
If you are automating VSS Backups, omit this parameter.
Default: PRE and POST
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `PRE | POST`
Required: No

## See Also
<a name="API_Script_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/Script)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/Script)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/Script)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
