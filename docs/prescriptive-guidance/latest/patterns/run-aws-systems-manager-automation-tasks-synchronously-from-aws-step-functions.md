---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions.html
---

# Run AWS Systems Manager Automation tasks synchronously from AWS Step Functions
<a name="run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions"></a>

*Elie El khoury, Amazon Web Services*

## Summary
<a name="run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions-summary"></a>

This pattern explains how to integrate AWS Step Functions with AWS Systems Manager. It uses AWS SDK service integrations to call the Systems Manager **startAutomationExecution** API with a task token from a state machine workflow, and pauses until the token returns with a success or failure call. To demonstrate the integration, this pattern implements an Automation document (runbook) wrapper around the `AWS-RunShellScript` or `AWS-RunPowerShellScript` document, and uses `.waitForTaskToken` to synchronously call `AWS-RunShellScript` or `AWS-RunPowerShellScript`. For more information about AWS SDK service integrations in Step Functions, see the [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/supported-services-awssdk.html).

Step Functions** **is a low-code, visual workflow service that you can use to build distributed applications, automate IT and business processes, and build data and machine learning pipelines by using AWS services. Workflows manage failures, retries, parallelization, service integrations, and observability so you can focus on higher-value business logic.

Automation, a capability of AWS Systems Manager, simplifies common maintenance, deployment, and remediation tasks for AWS services such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon Relational Database Service (Amazon RDS), Amazon Redshift, and Amazon Simple Storage Service (Amazon S3). Automation gives you granular control over the concurrency of your automations. For example, you can specify how many resources to target concurrently, and how many errors can occur before an automation is stopped.

For implementation details, including runbook steps, parameters, and examples, see the [Additional information](#run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions-additional) section.

## Prerequisites and limitations
<a name="run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS Identity and Access Management (IAM) permissions to access Step Functions and Systems Manager
+ An EC2 instance with Systems Manager Agent (SSM Agent) [installed](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-install-ssm-agent.html) on the instance
+ [An IAM instance profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html) attached to the instance where you plan to run the runbook
+ A Step Functions role that has the following IAM permissions (which follow the principle of least privilege):

```
{
             "Effect": "Allow",
             "Action": "ssm:StartAutomationExecution",
             "Resource": "*"
 }
```

**Product versions**
+ SSM document schema version 0.3 or later
+ SSM Agent version 2.3.672.0 or later

## Architecture
<a name="run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions-architecture"></a>

**Target technology stack  **
+ AWS Step Functions
+ AWS Systems Manager Automation

**Target architecture**

![Architecture for running Systems Manager automation tasks synchronously from Step Functions](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/47c19e4f-d68d-4f91-bb68-202098757529/images/2d248aae-d858-4565-8af2-593cde0da780.png)

**Automation and scale**
+ This pattern provides an AWS CloudFormation template that you can use to deploy the runbooks on multiple instances. (See the GitHub [Step Functions and Systems Manager implementation](https://github.com/aws-samples/amazon-stepfunctions-ssm-waitfortasktoken) repository.)

## Tools
<a name="run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.

**Code **

The code for this pattern is available in the GitHub [Step Functions and Systems Manager implementation](https://github.com/aws-samples/amazon-stepfunctions-ssm-waitfortasktoken) repository.

## Epics
<a name="run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions-epics"></a>

### Create runbooks
<a name="create-runbooks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the CloudFormation template. | Download the `ssm-automation-documents.cfn.json` template from the `cloudformation `folder of the GitHub repository. | AWS DevOps |
| Create runbooks. | Sign in to the AWS Management Console, open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), and deploy the template. For more information about deploying CloudFormation templates, see [Creating a stack on the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. <br />The CloudFormation template deploys three resources:+ `SfnRunCommandByInstanceIds` – Runbook that lets you run `AWS-RunShellScript` or `AWS-RunPowerShellScript` by using instance IDs.<br />+ `SfnRunCommandByTargets` – Runbook that lets you run `AWS-RunShellScript` or `AWS-RunPowerShellScript` by using targets.<br />+ `SSMSyncRole` – The IAM role assumed by the runbooks. | AWS DevOps |

### Create a sample state machine
<a name="create-a-sample-state-machine"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a test state machine.  | Follow the instructions in the [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started-with-sfn.html) to create and run a state machine. For the definition, use the following code. Make sure to update the `InstanceIds` value with the ID of a valid Systems Manager-enabled instance in your account.<pre>{<br />  "Comment": "A description of my state machine",<br />  "StartAt": "StartAutomationWaitForCallBack",<br />  "States": {<br />    "StartAutomationWaitForCallBack": {<br />      "Type": "Task",<br />      "Resource": "arn:aws:states:::aws-sdk:ssm:startAutomationExecution.waitForTaskToken",<br />      "Parameters": {<br />        "DocumentName": "SfnRunCommandByInstanceIds",<br />        "Parameters": {<br />          "InstanceIds": [<br />            "i-1234567890abcdef0"<br />          ],<br />          "taskToken.$": "States.Array($$.Task.Token)",<br />          "workingDirectory": [<br />            "/home/ssm-user/"<br />          ],<br />          "Commands": [<br />            "echo \"This is a test running automation waitForTaskToken\" >> automation.log",<br />            "sleep 100"<br />          ],<br />          "executionTimeout": [<br />              "10800"<br />          ],<br />          "deliveryTimeout": [<br />              "30"<br />          ],<br />          "shell": [<br />              "Shell"<br />          ]<br />            }<br />      },<br />      "End": true<br />    }<br />  }<br />}</pre><br />This code calls the runbook to run two commands that demonstrate the `waitForTaskToken` call to Systems Manager Automation.<br />The `shell` parameter value (`Shell` or `PowerShell`) determines whether the Automation document runs `AWS-RunShellScript` or `AWS-RunPowerShellScript`.<br />The task writes "This is a test running automation waitForTaskToken" into the `/home/ssm-user/automation.log` file, and then sleeps for 100 seconds before it responds with the task token and releases the next task in the workflow.<br />If you want to call the `SfnRunCommandByTargets` runbook instead, replace the `Parameters` section of the previous code with the following:<pre>"Parameters": {<br />          "Targets": [<br />            {<br />              "Key": "InstanceIds",<br />              "Values": [<br />                "i-02573cafcfEXAMPLE",<br />                "i-0471e04240EXAMPLE"<br />              ]<br />            }<br />          ],</pre> | AWS DevOps |
| Update the IAM role for the state machine. | The previous step automatically creates a dedicated IAM role for the state machine. However, it doesn’t grant permissions to call the runbook. Update the role by adding the following permissions:<pre>{<br />      "Effect": "Allow",<br />      "Action": "ssm:StartAutomationExecution",<br />      "Resource": "*"<br /> }</pre> | AWS DevOps |
| Validate the synchronous calls. | Run the state machine to validate the synchronous call between Step Functions and Systems Manager Automation. <br />For sample output, see the [Additional information](#run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions-additional) section.  | AWS DevOps |

## Related resources
<a name="run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions-resources"></a>
+ [Getting started with AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started-with-sfn.html) (*AWS Step Functions Developer Guide*)
+ [Wait for a callback with the task token](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token) (*AWS Step Functions Developer Guide*, service integration patterns)
+ [send\_task\_success](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/send_task_success.html) and [send\_task\_failure](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/send_task_failure.html) API calls (Boto3 documentation)
+ [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) (*AWS Systems Manager User Guide*)

## Additional information
<a name="run-aws-systems-manager-automation-tasks-synchronously-from-aws-step-functions-additional"></a>

**Implementation details**

This pattern provides a CloudFormation template that deploys two Systems Manager runbooks:
+ `SfnRunCommandByInstanceIds` runs the `AWS-RunShellScript` or `AWS-RunPowerShellScript` command by using instance IDs.
+ `SfnRunCommandByTargets` runs the `AWS-RunShellScript` or `AWS-RunPowerShellScript` command by using targets.

Each runbook implements four steps to achieve a synchronous call when using the `.waitForTaskToken` option in Step Functions.

|
|
| Step | Action | Description |
| --- |--- |--- |
| **1** | `Branch` | Checks the `shell` parameter value (`Shell` or `PowerShell`) to decide whether to run `AWS-RunShellScript` for Linux or `AWS-RunPowerShellScript` for Windows. |
| **2** | `RunCommand_Shell` or `RunCommand_PowerShell` | Takes several inputs and runs the `RunShellScript` or `RunPowerShellScript` command. For more information, check the **Details** tab for the `RunCommand_Shell` or `RunCommand_PowerShell` Automation document on the Systems Manager console. |
| **3** | `SendTaskFailure` | Runs when step 2 is aborted or canceled. It calls the Step Functions [send\_task\_failure](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/send_task_failure.html) API, which accepts three parameters as input: the token passed by the state machine, the failure error, and a description of the cause of the failure. |
| **4** | `SendTaskSuccess` | Runs when step 2 is successful. It calls the Step Functions [send\_task\_success](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/send_task_success.html) API, which accepts the token passed by the state machine as input. |

**Runbook parameters**

`SfnRunCommandByInstanceIds` runbook:

|
|
| Parameter name | Type | Optional or required | Description |
| --- |--- |--- |--- |
| `shell` | String | Required | The instances shell to decide whether to run `AWS-RunShellScript` for Linux or `AWS-RunPowerShellScript` for Windows. |
| `deliveryTimeout` | Integer | Optional | The time, in seconds, to wait for a command to deliver to the SSM Agent on an instance. This parameter has a minimum value of 30 (0.5 minute) and a maximum value of 2592000 (720 hours). |
| `executionTimeout` | String | Optional | The time, in seconds, for a command to complete before it is considered to have failed. The default value is 3600 (1 hour). The maximum value is 172800 (48 hours). |
| `workingDirectory` | String | Optional | The path to the working directory on your instance. |
| `Commands` | StringList | Required | The shell script or command to run. |
| `InstanceIds` | StringList | Required | The IDs of the instances where you want to run the command. |
| `taskToken` | String | Required | The task token to use for callback responses. |

`SfnRunCommandByTargets` runbook:

|
|
| Name | Type | Optional or required | Description |
| --- |--- |--- |--- |
| `shell` | String | Required | The instances shell to decide whether to run `AWS-RunShellScript` for Linux or `AWS-RunPowerShellScript` for Windows. |
| `deliveryTimeout` | Integer | Optional | The time, in seconds, to wait for a command to deliver to the SSM Agent on an instance. This parameter has a minimum value of 30 (0.5 minute) and a maximum value of 2592000 (720 hours). |
| `executionTimeout` | Integer | Optional | The time, in seconds, for a command to complete before it is considered to have failed. The default value is 3600 (1 hour). The maximum value is 172800 (48 hours). |
| `workingDirectory` | String | Optional | The path to the working directory on your instance. |
| `Commands` | StringList | Required | The shell script or command to run. |
| `Targets` | MapList | Required | An array of search criteria that identifies instances by using key-value pairs that you specify. For example: `[{"Key":"InstanceIds","Values":["i-02573cafcfEXAMPLE","i-0471e04240EXAMPLE"]}]` |
| `taskToken` | String | Required | The task token to use for callback responses. |

**Sample output**

The following table provides sample output from the step function. It shows that the total run time is over 100 seconds between step 5 (`TaskSubmitted`) and step 6 (`TaskSucceeded`). This demonstrates that the step function waited for the `sleep 100` command to finish before moving to the next task in the workflow.

|
|
| ID | Type | Step | Resource | Elapsed Time (ms) | Timestamp |
| --- |--- |--- |--- |--- |--- |
| **  1** | `ExecutionStarted` |  | - | 0 | Mar 11, 2022 02:50:34.303 PM |
| **  2** | `TaskStateEntered` | `StartAutomationWaitForCallBack` | - | 40 | Mar 11, 2022 02:50:34.343 PM |
| **  3** | `TaskScheduled` | `StartAutomationWaitForCallBack` | - | 40 | Mar 11, 2022 02:50:34.343 PM |
| **  4** | `TaskStarted` | `StartAutomationWaitForCallBack` | - | 154 | Mar 11, 2022 02:50:34.457 PM |
| **  5** | `TaskSubmitted` | `StartAutomationWaitForCallBack` | - | 657 | Mar 11, 2022 02:50:34.960 PM |
| **  6** | `TaskSucceeded` | `StartAutomationWaitForCallBack` | - | 103835 | Mar 11, 2022 02:52:18.138 PM |
| **  7** | `TaskStateExited` | `StartAutomationWaitForCallBack` | - | 103860 | Mar 11, 2022 02:52:18.163 PM |
| **  8** | `ExecutionSucceeded` |  | - | 103897 | Mar 11, 2022 02:52:18.200 PM |
