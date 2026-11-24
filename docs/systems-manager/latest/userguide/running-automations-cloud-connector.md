---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-cloud-connector.html
---

# Run automations on multicloud resources

With AWS Systems Manager Automation, you can run a runbook on Microsoft Azure and Google Cloud resources through a Systems Manager Cloud Connector. Automation assumes the connector's IAM federation role and exchanges a web identity token for short-lived Azure or Google Cloud credentials. You don't store Azure or Google Cloud credentials in AWS.

You can run an automation on the resources that a Cloud Connector reaches in the following ways.

Rate control with a Cloud Connector target
You choose a Cloud Connector and optional filters. Automation finds the resources that match and runs the runbook once for each one. By default, the target finds the running virtual machines (VMs) in every subscription or project that the connector covers. Use this method to run a runbook on many VMs.

Rate control with **Parameter Values**
You enter the IDs of up to 50 VMs. For more than 50 VMs, use a Cloud Connector target.

Simple execution or Manual execution
For a runbook that has a Cloud Connector input, you choose the connector and enter the IDs of the resources in the runbook's inputs. The automation runs once, on those resources.

API actions or a script in your own runbook
In a runbook step, you call Azure or Google Cloud APIs through the connector, with the actions `aws:executeAzureApi`, `aws:assertAzureResourceProperty`, `aws:waitForAzureResourceProperty`, and their Google Cloud equivalents, or with a Python script in `aws:executeScript`. The step works with the resources that you name in its inputs, and it doesn't need SSM Agent on the VMs. For more information, see [Create runbooks that call Azure and Google Cloud APIs](automation-multicloud-runbooks.md).

Multi-account and Region
This execution mode doesn't support Cloud Connector targets. For more information, see [Running automations in multiple AWS Regions and accounts](running-automations-multiple-accounts-regions.md).

Before you run an automation through a Cloud Connector, complete the following prerequisites.
+ Create a Cloud Connector. For Azure, see [Set up a Cloud Connector for Microsoft Azure in Systems Manager](systems-manager-cloud-connector.md). For Google Cloud, see [Set up a Cloud Connector for Google Cloud Platform in Systems Manager](systems-manager-cloud-connector-gcp.md).
+ We recommend that you run the automation with the connector's automation assume role. Systems Manager creates this role when you enable node management for the connector and keep the default **Automation execution role**. If you didn't, create the role as described in [Create the automation assume role](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-create-role). You can also use a role that you chose under **Additional trusted roles** when you created the connector. For more information, see [Use another role](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-other-role).
+ If the runbook has a Cloud Connector ID input, set it to the same connector as the target. Automation doesn't set it from the target. The console sets it for you only when the input is named `CloudConnector`.
+ Use a runbook that has an input for the resource ID. With a Cloud Connector target, Automation passes each resource's ID in that input. To check a runbook, open it on the **Documents** page of the Systems Manager console, choose the **Content** tab, and look in `parameters` for one of the following inputs:
  + An input whose type is a resource type, such as `microsoft.Compute/VirtualMachines` or `compute.googleapis.com/Instance`. For the types, see [Parameter types for Azure and Google Cloud resources](automation-multicloud-parameter-types.md).
  + A `String` input whose `allowedPattern` accepts the resource IDs in the form that Automation passes. Automation passes Azure resource IDs in lowercase. With a Cloud Connector target, it passes a Google Cloud VM as `projects/{{project}}/zones/{{zone}}/instances/{{name}}`, without the `//compute.googleapis.com/` prefix. It passes any other Google Cloud resource as its full Cloud Asset name, with the service prefix, such as `//storage.googleapis.com/{{bucket}}`.

  On the **Execute automation** page, the **Parameter** list shows the matching inputs first. To write your own runbook that calls APIs through a Cloud Connector, see [Create runbooks that call Azure and Google Cloud APIs](automation-multicloud-runbooks.md).
+ To filter resources by managed node status, make sure that SSM Agent is installed on the VMs.

**Note**
A Cloud Connector belongs to the AWS Region where you create it. Start the automation in that Region. For example, to use a connector that you created in the US East (N. Virginia) Region, start the automation in US East (N. Virginia). In another Region, Automation can't read the connector. For that error, see [An error occurred reading the provided CloudConnector](automation-cloud-connector-troubleshooting.md#automation-cloud-connector-troubleshooting-reading). You can use a Cloud Connector target in every AWS Region where you can create a Cloud Connector.

**Where to see results**

Automation runs the runbook for each resource in a separate automation, called a child automation. The automation that you start has one step for each resource, and the step's execution ID is the ID of that resource's child automation. To see the child automations, choose **Show child automations** on the **Automation** page of the Systems Manager console. For more information, see the console and command line procedures that follow.

**Topics**
+ [Run an automation on Azure or Google Cloud resources (console)](running-automations-cloud-connector-console.md)
+ [Run an automation on Azure or Google Cloud resources (command line)](running-automations-cloud-connector-cli.md)
+ [Create runbooks that call Azure and Google Cloud APIs](automation-multicloud-runbooks.md)
+ [Azure and Google Cloud SDK packages](automation-multicloud-packages.md)
+ [Cloud Connector target reference](automation-cloud-connector-target.md)
+ [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md)
+ [Choosing Azure resources with Azure sign-in](automation-azure-sign-in.md)
+ [Troubleshooting automations that use a Cloud Connector](automation-cloud-connector-troubleshooting.md)
