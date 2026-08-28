---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/stepfunctions-workflowstudio.html
---

# Working with AWS Step Functions Workflow Studio
<a name="stepfunctions-workflowstudio"></a>

The following sections describe how to work with AWS Step Functions Workflow Studio in the AWS Toolkit for Visual Studio Code. For detailed information about AWS Step Functions Workflow Studio, see the [Developing workflows](https://docs.aws.amazon.com/step-functions/latest/dg/developing-workflows.html) topic in the *AWS Step Functions* Developer Guide

## Opening Workflow Studio
<a name="w2aac17c55b9b5"></a>

The following list describes the different paths available for you to open Workflow Studio in VS Code.

**Note**
To work with Workflow Studio in VS Code, the extension of your `Amazon State Language`(ASL) file that contains your state machine definition, must end with `asl.json`, `asl.yml` or `asl.yaml`. For details about downloading or creating a new state machine definition in the AWS Toolkit, see the *Downloading state machines* and *Creating a state machine* sections in the [Working with AWS Step Functions](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/building-stepfunctions.html) topic of this User Guide.
+ From the AWS Explorer, open the context menu for (right-click) an `ASL` file containing a state machine definition, then choose **Open in Workflow Studio**.
+ From an open `ASL` file containing a state machine definition, choose the **Open with Workflow Studio** icon located next to the tabs in the VS Code editor window.
+ From an open `ASL` file containing a state machine definition, choose the CodeLens command **Open with Workflow Studio**, located at the top of the file.
+ Closing and reopening an `ASL` file containing a state machine definition automatically reopens the file in Workflow Studio, unless the default Workflow Studio is disabled manually.

## Design mode and Code mode
<a name="w2aac17c55b9b7"></a>

Workflow Studio has two modes for working with your `ASL` files containing a state machine definition: **Design** mode and **Code** mode. **Design** mode provides a graphic interface to visualize your workflows as you build prototypes. **Code** mode has an integrated code editor where you can view, write, and edit the `ASL` definitions in your workflows.

**Note**
For detailed information about each of the UI sections in both Design and Code modes, see the [Using Workflow Studio](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio.html) topic in the *AWS Step Functions* Developer Guide. Not all Workflow Studio features are available in the AWS Toolkit, such as **Config mode**, for example.

The **Design** mode UI has 7 main sections, as labeled and described in the following image.

1. Mode Buttons: Buttons for switching between **Design** and **Code** modes.

1. Utility buttons: A set of buttons for performing tasks, such as exiting Workflow Studio, saving your workflows, or exporting `ASL` definitions in a JSON or YAML file.

1. Design toolbar: Toolbar containing a set of buttons that perform common actions, such as undo, delete, and zoom control.

1. States Browser: Browser containing drag-and-drop states for your workflow canvas. States are organized into tabs and defined as **Actions**, **Flow**, and **Patterns**.

1. The Canvas and workflow graph: A visual rendering of your workflow where you can drop, reorganize, and select states for configuration.

1. Inspector Panel: View and edit the properties of any state selected on the canvas. Depending on the state selected in the canvas workflow graph, tabs populate with state-specific options for **Configuration**, **Input/Output**, **Variables**, and **Error handling**.

1. Info links: Opens a panel with contextual information when you need help. These panels also include links to related topics in the *AWS Step Functions* Developer Guide.

![The Design mode of the Workflow Studio UI in the AWS Toolkit](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/SFNWFS022025.png)

## Using single-state tests during design
<a name="w2aac17c55b9b9"></a>

From the Workflow Studio test-state UI, you can test the individual states of your state machine. This includes the ability to provide state inputs, set variables, and make both AWS SAM and CloudFormation definition substitutions.

To learn more about infrastructure as code (IaC), resource definitions, and transforming data, see the [Using AWS SAM to build Step Functions workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-sam-sfn.html) and [Transforming data with JSONata in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/transforming-data.html) topics in the *AWS Step Functions* Developer Guide.

The following procedure describes how to open the test-state UI in Workflow Studio.

**Opening the test state UI**

1. From the **Design** mode tab in Workflow Studio, navigate to the canvas and choose a state to open it in the **Inspector** panel.

1. From the **Inspector** panel, choose the **Test state** button.

1. The **Test state** UI opens in VS Code.

The test-state UI has 3 main tabs, **Test input**, **Arguments & Output**, **State definition**. The **Test input** tab has 3 additional fields that allow you to provide **State input**, set **variables**, and specify **Definition substitutions** from your AWS SAM or CloudFormation templates. In the **State definition** tab, you can adjust the workflow and re-test. When you're finished running tests, you can apply and save changes to your state machine definition.

The following screenshot shows the test-state UI, which includes a topic-resources definition.

![The Workflow Studio test state UI in the AWS Toolkit](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/SFNWFSteststate022025.png)

## Disabling Workflow Studio by default
<a name="w2aac17c55b9c11"></a>

By default, Workflow Studio is the default editor for `ASL` files containing a state machine definition. You can disable the default setting by modifying your `settings.json` file in your local `.vscode` directory. If you disable Workflow Studio by default, it is still accessible through the methods listed in the *Opening Workflow Studio* section, located in this topic.

To edit your `settings.json` file from VS Code, complete the following steps.

1. From VS Code, open the **Command Palette** by pressing **option\+shift\+p** (Mac) or **ctrl\+shift\+p** (Windows).

1. From the VS Code **Command Palette**, enter **Open User Settings (JSON)** into the search field and choose the option when it populates in the list.

1. From `settings.json` in your editor, add the following modification to your file.

   ```
                   {
                       "workbench.editorAssociations": {
                       // Use all the following overrides or a specific one for a certain file type
                       "*.asl.json": "default",
                       "*.asl.yaml": "default",
                       "*.asl.yml": "default"
                       }
                   }
   ```

1. Save your changes to `settings.json` and refresh or restart VS Code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
