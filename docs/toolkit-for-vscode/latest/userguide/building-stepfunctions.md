---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/building-stepfunctions.html
---

# Working with AWS Step Functions
<a name="building-stepfunctions"></a>

The following sections describe how to work with AWS Step Functions `Amazon State Language (ASL)` files containing state machine definitions in the AWS Toolkit. For detailed information about AWS Step Functions state machines, see the [Learn about state machines in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html) topic in the *AWS Step Functions* Developer Guide.

## Viewing Step Functions state machines
<a name="starting-sfn-list"></a>

To view your existing `ASL` files containing state machine definitions in the AWS Toolkit Explorer, complete the following steps.

1. From the AWS Toolkit Explorer, expand the region that contains the `ASL` file that you want to view.

1. Expand the **Step Functions** heading.

1. Your `ASL` files are displayed in the AWS Explorer.

## Creating a Step Functions state machine
<a name="starting-sfn-create"></a>

In the AWS Toolkit, you can create a new Step Functions state machine from a file or you can use a template. The following procedure describes how to create a Step Functions state machine from a file. For details about creating a SFN; state machine from a template, see the *State machine templates* section located below, in this User Guide topic.

**Note**
To work with Step Functions in VS Code, the extension of your `Amazon State Language`(ASL) file that contains your state machine definition must end with `asl.json`, `asl.yml`, or `.asl.yaml`.
By default, relevant Step Functions files open in Workflow Studio. For detailed information about working in Workflow Studio through the AWS Toolkit, see the [Working with Workflow Studio](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/stepfunctions-workflowstudio.html) topic in this User Guide.

1. From your workspace in VS Code, create a new file.

1. Name your file and specify the file extension as `asl.json`, `asl.yml`, or `.asl.yaml`.

1. Upon creation, the AWS Toolkit opens the new file in AWS Step Functions Workflow Studio.

1. From **Workflow Studio** choose the **Save** button from the utility menu to save your new `ASL` file.

## Creating a Step Functions state machine from a template
<a name="templates-stepfunctions"></a>

In the AWS Toolkit, you can create a Step Functions state machine from a template. The template process creates a `ASL` file that contains a state machine definition, providing a starting point for your project. The following procedure describes how to create a Step Functions state machine from a template in the AWS Toolkit.

1. From the AWS Toolkit Explorer, expand the region that you want to create a Step Functions state machine in.

1. Open the context menu for (right-click) **Step Functions** and choose **Create a new Step Functions state machine** to open the **Select a starter template(1/2)** wizard in VS Code.

1. From the **Select a starter template(1/2)** wizard, choose the template type for your Step Functions state machine to proceed.

1. From the **Select template format(2/2)** screen, choose either **YAML** or **JSON** for your template format.

1. A new `ASL` file containing your state machine definition is opened in the VS Code editor.

## Downloading a Step Functions state machine
<a name="sfn-download"></a>

To download a remotely stored Step Functions state machine to your local instance of VS Code, complete the following steps.

1. From the AWS Toolkit Explorer, expand the region that contains the Step Functions state machine that your want to download.

1. Expand **Step Functions**, then right-click the Step Functions state machine you want to download and choose **Download Definition...**.

1. Specify a location to store your Step Functions state machine locally to proceed.

1. The Step Functions state machine opens in Workflow Studio when the procedure is complete.

## Saving changes to a Step Functions state machine
<a name="starting-sfn-update"></a>

The following procedure describes how to save changes made to your Step Functions state machine.

**Note**
Edits made in Workflow Studio sync to your local file, but remain unsaved until your work is saved in the VS Code editor or Workflow Studio. If you local file is modified and saved while Workflow Studio is open and there are no errors detected in your `ASL` file, then you receive a **Success** notification in Workflow Studio, when saving is complete. However, if your local file contains invalid `JSON` or `YAML` and you attempt to save, then your local file fails to sync and you receive a **Warning** notification in Workflow Studio.

1. From an open `ASL` file containing a state machine definition in Workflow Studio, navigate to the **Utility buttons**.

1. Choose the **Save** button.

1. VS Code notifies you when the file has been saved.

## Running a Step Functions state machine
<a name="starting-sfn-execute"></a>

The following procedure describes how to run a Step Functions state machine in the AWS Toolkit.

1. From the AWS Toolkit Explorer, expand the region containing the Step Functions state machine that you want to run.

1. Expand **Step Functions**, then right-click the Step Functions state machine that you want to run.

1. From the context menu, choose **Start Execution** to initiate the launch process.

1. The status of the launch is displayed in the **AWS Toolkit Output** window in VS Code.

## Working with code snippets
<a name="building-stepfunctions-code-snippets"></a>

Code snippets are automated suggestions that generate based on the code that you're working on. To work with code snippets with Step Functions in the toolkit, complete the following steps.

**Note**
To work with Step Functions code snippets in VS Code, the extension of your `ASL` file that contains your state machine definition must end with `.asl.json`, `.asl.yml`, or `.asl.yaml`.
By default, your relevant Step Functions files open in Workflow Studio.

1. From VS Code, open an `ASL` file containing the state machine definition that you want to modify or create a new `ASL` file.

1. From Workflow Studio, switch to **Code** mode if you're in **Design** mode.

1. From the Workflow Studio code editor, place your cursor in the `"States"` property.

1. Press **control \+ space** to open the code snippets menu, additional properties can be accessed by pressing **control \+ space** and are based on the `"State"` `"Type"`.

1. Choose the code snippet that you want from the list.

## Code validation
<a name="building-stepfunctions-code-completion"></a>

As you work on Step Functions in Workflow Studio, code validation actively identifies errors and makes suggestions for the following:
+ Missing properties
+ Incorrect values
+ Non terminal state
+ Nonexistent states that are pointed to

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
