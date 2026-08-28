---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-script.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy Script
<a name="aws-properties-dlm-lifecyclepolicy-script"></a>

**[Custom snapshot policies that target instances only]** Information about pre and/or post scripts for a snapshot lifecycle policy that targets instances. For more information, see [ Automating application-consistent snapshots with pre and post scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html).

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-script-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-script-syntax.json"></a>

```
{
  "[ExecuteOperationOnScriptFailure](#cfn-dlm-lifecyclepolicy-script-executeoperationonscriptfailure)" : {{Boolean}},
  "[ExecutionHandler](#cfn-dlm-lifecyclepolicy-script-executionhandler)" : {{String}},
  "[ExecutionHandlerService](#cfn-dlm-lifecyclepolicy-script-executionhandlerservice)" : {{String}},
  "[ExecutionTimeout](#cfn-dlm-lifecyclepolicy-script-executiontimeout)" : {{Integer}},
  "[MaximumRetryCount](#cfn-dlm-lifecyclepolicy-script-maximumretrycount)" : {{Integer}},
  "[Stages](#cfn-dlm-lifecyclepolicy-script-stages)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-script-syntax.yaml"></a>

```
  [ExecuteOperationOnScriptFailure](#cfn-dlm-lifecyclepolicy-script-executeoperationonscriptfailure): {{Boolean}}
  [ExecutionHandler](#cfn-dlm-lifecyclepolicy-script-executionhandler): {{String}}
  [ExecutionHandlerService](#cfn-dlm-lifecyclepolicy-script-executionhandlerservice): {{String}}
  [ExecutionTimeout](#cfn-dlm-lifecyclepolicy-script-executiontimeout): {{Integer}}
  [MaximumRetryCount](#cfn-dlm-lifecyclepolicy-script-maximumretrycount): {{Integer}}
  [Stages](#cfn-dlm-lifecyclepolicy-script-stages): {{
    - String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-script-properties"></a>

`ExecuteOperationOnScriptFailure`  <a name="cfn-dlm-lifecyclepolicy-script-executeoperationonscriptfailure"></a>
Indicates whether Amazon Data Lifecycle Manager should default to crash-consistent snapshots if the pre script fails.
+ To default to crash consistent snapshot if the pre script fails, specify `true`.
+ To skip the instance for snapshot creation if the pre script fails, specify `false`.
This parameter is supported only if you run a pre script. If you run a post script only, omit this parameter.
Default: true
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionHandler`  <a name="cfn-dlm-lifecyclepolicy-script-executionhandler"></a>
The SSM document that includes the pre and/or post scripts to run.
+ If you are automating VSS backups, specify `AWS_VSS_BACKUP`. In this case, Amazon Data Lifecycle Manager automatically uses the `AWSEC2-CreateVssSnapshot` SSM document.
+ If you are automating application-consistent snapshots for SAP HANA workloads, specify `AWSSystemsManagerSAP-CreateDLMSnapshotForSAPHANA`.
+ If you are using a custom SSM document that you own, specify either the name or ARN of the SSM document. If you are using a custom SSM document that is shared with you, specify the ARN of the SSM document.
*Required*: No
*Type*: String
*Pattern*: `^([a-zA-Z0-9_\-.]{3,128}|[a-zA-Z0-9_\-.:/]{3,200}|[A-Z0-9_]+)$`
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionHandlerService`  <a name="cfn-dlm-lifecyclepolicy-script-executionhandlerservice"></a>
Indicates the service used to execute the pre and/or post scripts.
+ If you are using custom SSM documents or automating application-consistent snapshots of SAP HANA workloads, specify `AWS_SYSTEMS_MANAGER`.
+ If you are automating VSS Backups, omit this parameter.
Default: AWS\_SYSTEMS\_MANAGER
*Required*: No
*Type*: String
*Allowed values*: `AWS_SYSTEMS_MANAGER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionTimeout`  <a name="cfn-dlm-lifecyclepolicy-script-executiontimeout"></a>
Specifies a timeout period, in seconds, after which Amazon Data Lifecycle Manager fails the script run attempt if it has not completed. If a script does not complete within its timeout period, Amazon Data Lifecycle Manager fails the attempt. The timeout period applies to the pre and post scripts individually.
If you are automating VSS Backups, omit this parameter.
Default: 10
*Required*: No
*Type*: Integer
*Minimum*: `10`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumRetryCount`  <a name="cfn-dlm-lifecyclepolicy-script-maximumretrycount"></a>
Specifies the number of times Amazon Data Lifecycle Manager should retry scripts that fail.
+ If the pre script fails, Amazon Data Lifecycle Manager retries the entire snapshot creation process, including running the pre and post scripts.
+ If the post script fails, Amazon Data Lifecycle Manager retries the post script only; in this case, the pre script will have completed and the snapshot might have been created.
If you do not want Amazon Data Lifecycle Manager to retry failed scripts, specify `0`.
Default: 0
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stages`  <a name="cfn-dlm-lifecyclepolicy-script-stages"></a>
Indicate which scripts Amazon Data Lifecycle Manager should run on target instances. Pre scripts run before Amazon Data Lifecycle Manager initiates snapshot creation. Post scripts run after Amazon Data Lifecycle Manager initiates snapshot creation.
+ To run a pre script only, specify `PRE`. In this case, Amazon Data Lifecycle Manager calls the SSM document with the `pre-script` parameter before initiating snapshot creation.
+ To run a post script only, specify `POST`. In this case, Amazon Data Lifecycle Manager calls the SSM document with the `post-script` parameter after initiating snapshot creation.
+ To run both pre and post scripts, specify both `PRE` and `POST`. In this case, Amazon Data Lifecycle Manager calls the SSM document with the `pre-script` parameter before initiating snapshot creation, and then it calls the SSM document again with the `post-script` parameter after initiating snapshot creation.
If you are automating VSS Backups, omit this parameter.
Default: PRE and POST
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
