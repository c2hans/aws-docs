---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeploymentComponentUpdatePolicy.html
---

# DeploymentComponentUpdatePolicy
<a name="API_DeploymentComponentUpdatePolicy"></a>

Contains information about a deployment's policy that defines when components are safe to update.

Each component on a device can report whether or not it's ready to update. After a component and its dependencies are ready, they can apply the update in the deployment. You can configure whether or not the deployment notifies components of an update and waits for a response. You specify the amount of time each component has to respond to the update notification.

## Contents
<a name="API_DeploymentComponentUpdatePolicy_Contents"></a>

 ** action **   <a name="greengrassv2-Type-DeploymentComponentUpdatePolicy-action"></a>
Whether or not to notify components and wait for components to become safe to update. Choose from the following options:
+  `NOTIFY_COMPONENTS` – The deployment notifies each component before it stops and updates that component. Components can use the [SubscribeToComponentUpdates](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-subscribetocomponentupdates) IPC operation to receive these notifications. Then, components can respond with the [DeferComponentUpdate](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-defercomponentupdate) IPC operation. For more information, see [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) in the * AWS IoT Greengrass V2 Developer Guide*.
+  `SKIP_NOTIFY_COMPONENTS` – The deployment doesn't notify components or wait for them to be safe to update.
Default: `NOTIFY_COMPONENTS`
Type: String
Valid Values: `NOTIFY_COMPONENTS | SKIP_NOTIFY_COMPONENTS`
Required: No

 ** timeoutInSeconds **   <a name="greengrassv2-Type-DeploymentComponentUpdatePolicy-timeoutInSeconds"></a>
The amount of time in seconds that each component on a device has to report that it's safe to update. If the component waits for longer than this timeout, then the deployment proceeds on the device.
Default: `60`
Type: Integer
Required: No

## See Also
<a name="API_DeploymentComponentUpdatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/DeploymentComponentUpdatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/DeploymentComponentUpdatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/DeploymentComponentUpdatePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
