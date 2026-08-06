---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-release-2021-02-04.html
---

# Release: AWS IoT Greengrass Core v2.0.4 software update on February 04, 2021
<a name="greengrass-release-2021-02-04"></a>

This release provides version 2.0.4 of the Greengrass nucleus component. It includes the new `greengrassDataPlanePort` parameter to configure HTTPS communication over port 443 and fixes bugs. The minimal IAM policy now requires the `iam:GetPolicy` and `sts:GetCallerIdentity` when the AWS IoT Greengrass Core software installer is run with `--provision true`.

**Release date:** February 04, 2021

## Public component updates
<a name="greengrass-2021-02-04-components"></a>

The following table lists AWS-provided components that include new and updated features.

**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).

| **Component** | **Details** |
| --- | --- |
| Greengrass nucleus | Version 2.0.4 of the [Greengrass nucleus](greengrass-nucleus-component.md) is available.<a name="changelog-nucleus-2.0.4"></a>**New features**<br />   Enables HTTPS traffic over port 443. You can use the new `greengrassDataPlanePort` configuration parameter for version 2.0.4 of the nucleus component to configure HTTPS communication to travel over port 443 instead of the default port 8443. For more information, see [Configure HTTPS over port 443](configure-greengrass-core-v2.md#configure-https-port-443).   Adds the work path recipe variable. You can use this recipe variable to get the path to components' work folders, which you can use to share files between components and their dependencies. For more information, see the [work path recipe variable](component-recipe-reference.md#component-recipe-work-path).   <br />**Bug fixes and improvements**<br />   Prevents the creation of the token exchange AWS Identity and Access Management (IAM) role policy if a role policy already exists. <br />As a result of this change, the installer now requires the `iam:GetPolicy` and `sts:GetCallerIdentity` when run with `--provision true`. For more information, see [Minimal IAM policy for installer to provision resources](provision-minimal-iam-policy.md).   Correctly handles the cancellation of a deployment that has not yet been registered successfully.   Updates the configuration to remove older entries with newer timestamps when rolling back a deployment.   Additional minor fixes and improvements. For more information, see the [releases](https://github.com/aws-greengrass/aws-greengrass-nucleus/releases) on GitHub.    |
