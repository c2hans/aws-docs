---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_InstalledComponent.html
---

# InstalledComponent
<a name="API_InstalledComponent"></a>

Contains information about a component on a Greengrass core device.

## Contents
<a name="API_InstalledComponent_Contents"></a>

 ** componentName **   <a name="greengrassv2-Type-InstalledComponent-componentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** componentVersion **   <a name="greengrassv2-Type-InstalledComponent-componentVersion"></a>
The version of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** isRoot **   <a name="greengrassv2-Type-InstalledComponent-isRoot"></a>
Whether or not the component is a root component.
Type: Boolean
Required: No

 ** lastInstallationSource **   <a name="greengrassv2-Type-InstalledComponent-lastInstallationSource"></a>
The most recent deployment source that brought the component to the Greengrass core device. For a thing group deployment or thing deployment, the source will be the ID of the last deployment that contained the component. For local deployments it will be `LOCAL`.
Any deployment will attempt to reinstall currently broken components on the device, which will update the last installation source.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** lastReportedTimestamp **   <a name="greengrassv2-Type-InstalledComponent-lastReportedTimestamp"></a>
The last time the Greengrass core device sent a message containing a component's state to the AWS Cloud.
A component does not need to see a state change for this field to update.
Type: Timestamp
Required: No

 ** lastStatusChangeTimestamp **   <a name="greengrassv2-Type-InstalledComponent-lastStatusChangeTimestamp"></a>
The status of how current the data is.
This response is based off of component state changes. The status reflects component disruptions and deployments. If a component only sees a configuration update during a deployment, it might not undergo a state change and this status would not be updated.
Type: Timestamp
Required: No

 ** lifecycleState **   <a name="greengrassv2-Type-InstalledComponent-lifecycleState"></a>
The lifecycle state of the component.
Type: String
Valid Values: `NEW | INSTALLED | STARTING | RUNNING | STOPPING | ERRORED | BROKEN | FINISHED`
Required: No

 ** lifecycleStateDetails **   <a name="greengrassv2-Type-InstalledComponent-lifecycleStateDetails"></a>
A detailed response about the lifecycle state of the component that explains the reason why a component has an error or is broken.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** lifecycleStatusCodes **   <a name="greengrassv2-Type-InstalledComponent-lifecycleStatusCodes"></a>
The status codes that indicate the reason for failure whenever the `lifecycleState` has an error or is in a broken state.
Greengrass nucleus v2.8.0 or later is required to get an accurate `lifecycleStatusCodes` response. This response can be inaccurate in earlier Greengrass nucleus versions.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_InstalledComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/InstalledComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/InstalledComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/InstalledComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
