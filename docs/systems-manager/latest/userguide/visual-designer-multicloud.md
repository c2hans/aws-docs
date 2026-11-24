---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/visual-designer-multicloud.html
---

# Using Azure and Google Cloud actions in the visual design experience

In the visual design experience, you can add steps that call Microsoft Azure and Google Cloud APIs through a Cloud Connector. These steps run on the Azure and Google Cloud resources that the connector can reach. You can also set the clouds that the runbook declares in the **Cloud providers** field.

## Hybrid and multicloud actions
<a name="visual-designer-multicloud-actions"></a>

The **Actions** browser groups the following actions under a **Hybrid and multicloud** heading. Each action adds an Automation action to your runbook. The cloud API actions start as Azure actions and switch to the matching Google Cloud action when you choose a Google Cloud connector for the step.
+ **Call a cloud API** adds an [`aws:executeAzureApi` – Call and run Azure API operations](automation-action-executeAzureApi.md) or [`aws:executeGcpApi` – Call and run Google Cloud API operations](automation-action-executeGcpApi.md) step.
+ **Assert a cloud resource property** adds an [`aws:assertAzureResourceProperty` – Assert an Azure resource state](automation-action-assertAzureResourceProperty.md) or [`aws:assertGcpResourceProperty` – Assert a Google Cloud resource state](automation-action-assertGcpResourceProperty.md) step.
+ **Wait on a cloud resource** adds an [`aws:waitForAzureResourceProperty` – Wait on an Azure resource property](automation-action-waitForAzureResourceProperty.md) or [`aws:waitForGcpResourceProperty` – Wait on a Google Cloud resource property](automation-action-waitForGcpResourceProperty.md) step.
+ **Install package on Azure VM** adds an [`aws:installDistributorPackageOnAzure` – Install a package on an Azure VM](automation-action-installDistributorPackageOnAzure.md) step.

## Adding an Azure or Google Cloud API step
<a name="visual-designer-multicloud-add-step"></a>

**To add an Azure or Google Cloud API step**

1. From the **Actions** browser, under **Hybrid and multicloud**, drag the action you want into your workflow graph.

1. Choose the action in the canvas to open the **Form** panel.

1. For **Cloud connector**, choose a connector. The step calls the APIs of the connector's cloud, so the step becomes the Azure action or the Google Cloud action to match the connector you chose.

1. For **Package**, **Service**, and **API**, enter the SDK bundle, service, and API operation that the step calls. For an Azure step, also enter the **Subscription ID** that the step calls. The connector must allow that subscription.

1. Enter any other parameters that the API operation takes. For an **Assert a cloud resource property** or **Wait on a cloud resource** step, also enter the **Property selector** and **Desired values**.

1. Define the step's outputs with a name, a selector into the API response, and a type. For more information, see [Using action outputs as inputs](automation-action-outputs-inputs.md).

## Parameter types for Azure and Google Cloud
<a name="visual-designer-multicloud-parameter-types"></a>

A runbook that targets Azure and Google Cloud resources can declare input parameters with Azure and Google Cloud resource types. For the list of parameter types, see [Parameter types for Azure and Google Cloud resources](automation-multicloud-parameter-types.md).

## The runbook's cloud providers
<a name="visual-designer-multicloud-cloud-providers"></a>

The **Cloud providers** field sets the clouds that the runbook declares. It appears in the runbook's attributes, in the **Cloud providers** section. Its description is **The clouds that the runbook runs against. Select at least one.** For more information about this metadata, see [Specifying cloud providers for SSM documents](documents-cloud-providers.md).

For a new runbook, the field is selected from the runbook's Azure and Google Cloud API steps, and shows the hint **Selected from the runbook's Azure and Google Cloud API steps.** At least one cloud provider must stay selected.

If the runbook's API steps call a cloud that isn't selected, the field shows the warning **The runbook's API steps call clouds that aren't selected: {{providers}}.**

When the account can't set cloud providers, the field is disabled. For a new version, it shows the message **This account can't set cloud providers. The new version keeps the latest version's.**

## Availability
<a name="visual-designer-multicloud-availability"></a>

The **Hybrid and multicloud** actions are available in the AWS Regions where Cloud Connector is available.

The **Cloud providers** field is available in commercial AWS Regions only. It isn't available in the AWS GovCloud (US) Regions or the China Regions.
