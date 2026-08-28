---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-deployments.html
---

# Deploy AWS IoT Greengrass components to devices
<a name="manage-deployments"></a>

You can use AWS IoT Greengrass to deploy components to devices or groups of devices. You use *deployments* to define the components and configurations that are sent to the devices. AWS IoT Greengrass deploys to *targets*, AWS IoT things or thing groups that represent Greengrass core devices. AWS IoT Greengrass uses [AWS IoT Core jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) to deploy to your core devices. You can configure how the job rolls out to your devices.

## Core device deployments
<a name="core-device-deployments"></a>

Each core device runs the components of the deployments for that device. A new deployment to the same target overwrites the previous deployment to the target. When you create a deployment, you define the components and configurations to apply to the core device's existing software.

When you revise a deployment for a target, you replace the components from the previous revision with the components in the new revision. For example, you deploy the [Log manager](log-manager-component.md) and [Secret manager](secret-manager-component.md) components to the thing group `TestGroup`. Then you create another deployment for `TestGroup` that specifies only the secret manager component. As a result, the core devices in that group no longer run the log manager.

## Platform dependency resolution
<a name="platform-dependency-resolution"></a>

When a core device receives a deployment, it checks to make sure that the components are compatible with the core device. For example, if you deploy the [Firehose](kinesis-firehose-component.md) to a Windows target, the deployment will fail.

## Component dependency resolution
<a name="component-dependency-resolution"></a>

During a component deployment, the core device verifies compatibility of all components' dependencies and version requirements across a thing group. This verification ensures that version contraints are satisfied for all components and their dependencies before proceeding with the deployment.

The dependency resolution process begins with identifying target components that have no dependencies in their recipes. Then, the system constructs a dependency tree using breadth-first search (BFS) which systematically explores each target node and finds their dependencies first before moving on to the next node. Each node includes the target component as the key and the version requirements as the value.

The version requirements combine three sets of constraints:
+ The version requirements that are already established in the existing thing group.
+ The component version required by the deployment. You must select a component version when you make or update a deployment.
+ Any component version constraints that are defined within the recipe's dependency section.

### Resolve component dependencies
<a name="resolving-dependencies"></a>

During a deployment, the Greengrass nucleus first attempts to find the local candidate currently running on the device that satisfies the requirements. If the running component satisfies the requirements, the nucleus gets the stored recipe path from the recipe folder and finds the latest local version in the local store.

For AWS Cloud deployments, the nucleus will then call the [ResolveComponentCandidates API](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ResolveComponentCandidates.html). This API will start with the latest available version and check if it satisfies the dependencies and requirements. When the nucleus gets the response from the API, it selects that latest version. If there is no version found from the AWS Cloud that satisfies the requirements, the deployment fails. If the device is offline, it falls back to the original local candidate found. If there is no local candidate found that satisfies the requirements, the deployment fails.

For local deployments, the nucleus exclusively uses local candidates if they exist and if they satisfy the requirements without negotiating to AWS Cloud. If there is no such candidate, the deployment fails.

**Note**
All resolved recipes are stored locally for future reference.

For more information, see the [dependency resolution](https://github.com/aws-greengrass/aws-greengrass-nucleus/wiki/Deployment#dependency-resolution) section in GitHub.

If the Greengrass nucleus is able to successfully resolve all components, the nucleus log will contain the following line.

```
resolve-all-group-dependencies-finish. Finish resolving all groups dependencies.
```

**Example**
The following is an example of how the nucleus will resolve the component requirements.
+ You deploy ComponentA which depends on ComponentC versions 1.0.0-1.9.0.
+ You also deploy ComponentB which depends on ComponentC versions 1.4.0-1.9.5.
With component dependency resolution, the nucleus will deploy the latest version of ComponentC version to satisfy the requirements of ComponentA and ComponentB. This latest version of ComponentC is version 1.9.0.

#### Common component dependency resolution failures
<a name="w2ab1c24c25b9c11c19"></a>

The component dependency resolution may fail for two main reasons: target version requirement conflict or component dependency requirement conflict.

##### Scenario 1: Target version requirement conflict
<a name="w2ab1c24c25b9c11c19b5"></a>
+ A thing exists in one thing group and you also want to add that thing to a new thing group. The deployment will fail if the new thing group requires a different thing version.
+ A deployment may also fail if a thing belongs to a thing group and wants to update the component version through a thing deployment.

![Component dependencies that result in a failed deployment.](http://docs.aws.amazon.com/greengrass/v2/developerguide/images/dependency-4.png)

*Failure log sample:*

```
2025-04-11T06:16:03.315Z [ERROR] (pool-3-thread-27) com.aws.greengrass.componentmanager.ComponentManager: Failed to negotiate version with cloud and no local version to fall back to. {componentName=ComponentC, versionRequirement={thing/ABC==2.0.0, thinggroup/ThingGroupA==1.0.0}}
2025-04-11T06:16:03.316Z [ERROR] (pool-3-thread-26) com.aws.greengrass.deployment.DeploymentService: Error occurred while processing deployment. {deploymentId=fbac24de-4ef9-44b0-a685-fdc63b0f02b8, serviceName=DeploymentService, currentState=RUNNING}
java.util.concurrent.ExecutionException: com.aws.greengrass.componentmanager.exceptions.NoAvailableComponentVersionException: No local or cloud component version satisfies the requirements Check whether the version constraints conflict and that the component exists in your AWS account with a version that matches the version constraints. If the version constraints conflict, revise deployments to resolve the conflict. Component ComponentC version constraints: thing/ABC requires =2.0.0, thinggroup/ThingGroupA requires =1.0.0.
    at java.base/java.util.concurrent.FutureTask.report(FutureTask.java:122)
    at java.base/java.util.concurrent.FutureTask.get(FutureTask.java:191)
    at com.aws.greengrass.deployment.DefaultDeploymentTask.call(DefaultDeploymentTask.java:127)
    at com.aws.greengrass.deployment.DefaultDeploymentTask.call(DefaultDeploymentTask.java:50)
    at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
    at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)
    at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)
    at java.base/java.lang.Thread.run(Thread.java:829)
Caused by: com.aws.greengrass.componentmanager.exceptions.NoAvailableComponentVersionException: No local or cloud component version satisfies the requirements Check whether the version constraints conflict and that the component exists in your AWS account with a version that matches the version constraints. If the version constraints conflict, revise deployments to resolve the conflict. Component ComponentC version constraints: thing/ABC requires =2.0.0, thinggroup/ThingGroupA requires =1.0.0.
    at com.aws.greengrass.componentmanager.ComponentManager.negotiateVersionWithCloud(ComponentManager.java:232)
    at com.aws.greengrass.componentmanager.ComponentManager.resolveComponentVersion(ComponentManager.java:167)
    at com.aws.greengrass.componentmanager.DependencyResolver.lambda$resolveDependencies$0(DependencyResolver.java:134)
    at com.aws.greengrass.componentmanager.DependencyResolver.resolveComponentDependencies(DependencyResolver.java:231)
    at com.aws.greengrass.componentmanager.DependencyResolver.resolveDependencies(DependencyResolver.java:131)
    at com.aws.greengrass.deployment.DefaultDeploymentTask.lambda$call$2(DefaultDeploymentTask.java:125)
    ... 4 more
```

The logs indicate a version conflict error because the nucleus can't find a component version that simultaneously meetings two conflicting requirements.

##### How to resolve it
<a name="w2ab1c24c25b9c11c19b5c13"></a>
+ If you want to keep the component in each thing group, select the same version of that component in each thing group.
+ Select a component version that meets the deployment requirement.
+ If you want to use a component version that doesn't meet both thing group requirements, select the component version that meets the thing group version requirement and use that component only in that thing group.

##### Scenario 2: Component dependency version requirement conflict
<a name="w2ab1c24c25b9c11c19b7"></a>

If a component is a dependency of different components and the components require different versions or different version ranges of that component, there a possibility that there are no available versions to satisfy all version requirements. In this scenario, the deployment will fail.

**Example**
Deployment of ComponentA (v2.5.0), ComponentB (v1.3.0), and ComponentC (v1.0.0)
+ ComponentA requires ComponentB version >=1.0.0.

  ```
  ---
  ...
  ComponentName: ComponentA
  ComponentVersion: "2.5.0"
  ComponentDependencies:
      ComponentB:
          VersionRequirement: ">=1.0.0"
          DependencyType: "HARD"
  ...
  ```
+ ComponentC requires ComponentA version <2.0.0.

  ```
  ---
  ...
  ComponentName: ComponentC
  ComponentVersion: "1.0.0"
  ComponentDependencies:
      ComponentA:
          VersionRequirement: "<2.0.0"
          DependencyType: "HARD"
  ...
  ```
There's a version conflict between two requirements for ComponentA:
+ ComponentA requires version 2.5.0 in this deployment
+ ComponentC requires ComponentA versions lower than 2.0.0
These two requirements contradict each other, making it impossible for the nucleus to find a ComponentA version that satisfies both requirements. Therefore, the dependency resolution fails.

![Component dependencies that result in a failed deployment.](http://docs.aws.amazon.com/greengrass/v2/developerguide/images/dependency-3.png)

*Failure log sample:*

```
2025-04-11T06:07:18.291Z [ERROR] (pool-3-thread-25) com.aws.greengrass.componentmanager.ComponentManager: Failed to negotiate version with cloud and no local version to fall back to. {componentName=ComponentA, versionRequirement={ComponentC=<2.0.0, thinggroup/ThingGroupA==2.5.0}}
2025-04-11T06:07:18.292Z [ERROR] (pool-3-thread-24) com.aws.greengrass.deployment.DeploymentService: Error occurred while processing deployment. {deploymentId=2ffac4df-1ac9-405c-8c11-28494a1b4382, serviceName=DeploymentService, currentState=RUNNING}
java.util.concurrent.ExecutionException: com.aws.greengrass.componentmanager.exceptions.NoAvailableComponentVersionException: No local or cloud component version satisfies the requirements Check whether the version constraints conflict and that the component exists in your AWS account with a version that matches the version constraints. If the version constraints conflict, revise deployments to resolve the conflict. Component ComponentA version constraints: ComponentC requires <2.0.0, thinggroup/ThingGroupA requires =2.5.0.
    at java.base/java.util.concurrent.FutureTask.report(FutureTask.java:122)
    at java.base/java.util.concurrent.FutureTask.get(FutureTask.java:191)
    at com.aws.greengrass.deployment.DefaultDeploymentTask.call(DefaultDeploymentTask.java:127)
    at com.aws.greengrass.deployment.DefaultDeploymentTask.call(DefaultDeploymentTask.java:50)
    at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
    at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)
    at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)
    at java.base/java.lang.Thread.run(Thread.java:829)
Caused by: com.aws.greengrass.componentmanager.exceptions.NoAvailableComponentVersionException: No local or cloud component version satisfies the requirements Check whether the version constraints conflict and that the component exists in your AWS account with a version that matches the version constraints. If the version constraints conflict, revise deployments to resolve the conflict. Component ComponentA version constraints: ComponentC requires <2.0.0, thinggroup/ThingGroupA requires =2.5.0.
    at com.aws.greengrass.componentmanager.ComponentManager.negotiateVersionWithCloud(ComponentManager.java:232)
    at com.aws.greengrass.componentmanager.ComponentManager.resolveComponentVersion(ComponentManager.java:167)
    at com.aws.greengrass.componentmanager.DependencyResolver.lambda$resolveDependencies$0(DependencyResolver.java:134)
    at com.aws.greengrass.componentmanager.DependencyResolver.resolveComponentDependencies(DependencyResolver.java:231)
    at com.aws.greengrass.componentmanager.DependencyResolver.resolveDependencies(DependencyResolver.java:131)
    at com.aws.greengrass.deployment.DefaultDeploymentTask.lambda$call$2(DefaultDeploymentTask.java:125)
    ... 4 more
```

The logs indicate that the nucleus can't find a version of ComponentA that satisfies the following requirements.
+ The requirements for ComponentA to be exactly version 2.5.0 (from ThingGroupA).
+ The requirement to work with ComponentC versions below 2.0.0.

##### How to resolve it
<a name="w2ab1c24c25b9c11c19b7c17"></a>
+ If you want to keep the component in each thing group, select the same version of that component in each thing group.
+ Select a component version that meets the deployment requirement.
+ If you want to use a component version that doesn't meet both thing group requirements, select the component version that meets the thing group version requirement and use that component only in that thing group.

**Tip**
If you see this error on any AWS provided component, you can resolve it by updating the conflicted components to the latest version.

## Removing a device from a thing group
<a name="thing-group-removal-behavior"></a>

When you remove a core device from a thing group, the component deployment behavior depends on the version of the [Greengrass nucleus](greengrass-nucleus-component.md) that the core device runs.

------
#### [ 2.5.1 and later ]

When you remove a core device from a thing group, the behavior depends on whether the AWS IoT policy grants the `greengrass:ListThingGroupsForCoreDevice` permission. For more information about this permission and AWS IoT policies for core devices, see [Device authentication and authorization for AWS IoT Greengrass](device-auth.md).
+ **If the AWS IoT policy grants this permission**

  <a name="thing-group-removal-behavior-remove-components"></a>When you remove a core device from a thing group, AWS IoT Greengrass removes the thing group's components the next time a deployment is made to the device. If a component on the device is included in the next deployment, that component is not removed from the device.
+ **If the AWS IoT policy doesn't grant this permission**

  <a name="thing-group-removal-behavior-no-remove-components"></a>When you remove a core device from a thing group, AWS IoT Greengrass doesn't delete that thing group's components from the device.

  <a name="thing-group-removal-behavior-no-remove-components-how-to-remove"></a>To remove a component from a device, use the [deployment create](gg-cli-deployment.md#deployment-create) command of the Greengrass CLI. Specify the component to remove with the `--remove` argument, and specify the thing group with the `--groupId` argument.

------
#### [ 2.5.0 ]

<a name="thing-group-removal-behavior-remove-components"></a>When you remove a core device from a thing group, AWS IoT Greengrass removes the thing group's components the next time a deployment is made to the device. If a component on the device is included in the next deployment, that component is not removed from the device.

This behavior requires that the core device's AWS IoT policy grants the `greengrass:ListThingGroupsForCoreDevice` permission. If a core device doesn't have this permission, the core device fails to apply deployments. For more information, see [Device authentication and authorization for AWS IoT Greengrass](device-auth.md).

------
#### [ 2.0.x - 2.4.x ]

<a name="thing-group-removal-behavior-no-remove-components"></a>When you remove a core device from a thing group, AWS IoT Greengrass doesn't delete that thing group's components from the device.

<a name="thing-group-removal-behavior-no-remove-components-how-to-remove"></a>To remove a component from a device, use the [deployment create](gg-cli-deployment.md#deployment-create) command of the Greengrass CLI. Specify the component to remove with the `--remove` argument, and specify the thing group with the `--groupId` argument.

------

## Deployments
<a name="deployments"></a>

Deployments are continuous. When you create a deployment, AWS IoT Greengrass rolls out the deployment to target devices that are online. If a target device isn't online, then it receives the deployment the next time it connects to AWS IoT Greengrass. When you add a core device to a target thing group, AWS IoT Greengrass sends the device the latest deployment for that thing group.

Before a core device deploys a component, by default it notifies each component on the device. Greengrass components can respond to the notification to defer deployment. You might want to defer deployment if the device has a low battery level or is running a process that can't be interrupted. For more information, see [Tutorial: Develop a Greengrass component that defers component updates](defer-component-updates-tutorial.md). When you create a deployment you can configure it to deploy without notifying components.

Each target thing or thing group can have one deployment at a time. This means that when you create a deployment for a target, AWS IoT Greengrass no longer deploys the previous revision of that target's deployment.

## Deployment options
<a name="deployment-options"></a>

Deployments provide several options that let you control which devices receive an update and how the update deploys. When you create a deployment, you can configure the following options:
+ **AWS IoT Greengrass components**

  Define the components to install and run on the target devices. AWS IoT Greengrass components are software modules that you deploy and run on Greengrass core devices. Devices receive components only if the component supports the device's platform. This lets you deploy to groups of devices even if the target devices run on multiple platforms. If a component doesn't support the device's platform, the component doesn't deploy to the device.

  You can deploy custom components and AWS-provided components to your devices. When you deploy a component, AWS IoT Greengrass identifies any component dependencies and deploys them too. For more information, see [Develop AWS IoT Greengrass components](develop-greengrass-components.md) and [AWS-provided components](public-components.md).

  You define the version and configuration update to deploy for each component. The *configuration update* specifies how to modify the component's existing configuration on the core device, or the component's default configuration if the component doesn't exist on the core device. You can specify which configuration values to reset to default values and the new configuration values to merge onto the core device. When a core device receives deployments for different targets, and each deployment specifies compatible component versions, the core device applies configuration updates in order based on the timestamp of when you create the deployment. For more information, see [Update component configurations](update-component-configurations.md).
**Important**  <a name="component-patch-update-note"></a>
<a name="component-patch-update"></a>When you deploy a component, AWS IoT Greengrass installs the latest supported versions of all of that component's dependencies. Because of this, new patch versions of AWS-provided public components might be automatically deployed to your core devices if you add new devices to a thing group, or you update the deployment that targets those devices. Some automatic updates, such as a nucleus update, can cause your devices to restart unexpectedly.
<a name="component-version-pinning"></a>To prevent unintended updates for a component that is running on your device, we recommend that you directly include your preferred version of that component when you [create a deployment](create-deployments.md). For more information about update behavior for AWS IoT Greengrass Core software, see [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md).
+ **Deployment policies**

  Define when it's safe to deploy a configuration and what to do if the deployment fails. You can specify whether or not to wait for components to report that they can update. You can also specify whether or not to roll back devices to their previous configuration if they apply a deployment that fails.
+ **Stop configuration**

  Define when and how to stop a deployment. The deployment stops and fails if the criteria that you define are met. For example, you can configure a deployment to stop if a percentage of devices fail to apply that deployment after a minimum number of devices receive it.
+ **Rollout configuration**

  Define the rate at which a deployments rolls out to the target devices. You can configure an exponential rate increase with minimum and maximum rate bounds.
+ **Timeout configuration**

  Define the maximum amount of time each device has to apply a deployment. If a device exceeds the duration that you specify, then the device fails to apply the deployment.

**Important**
Custom components can define artifacts in S3 buckets. When the AWS IoT Greengrass Core software deploys a component, it downloads the component's artifacts from the AWS Cloud. Core device roles don't allow access to S3 buckets by default. To deploy custom components that define artifacts in an S3 bucket, the core device role must grant permissions to download artifacts from that bucket. For more information, see [Allow access to S3 buckets for component artifacts](device-service-role.md#device-service-role-access-s3-bucket).

**Topics**
+ [Core device deployments](#core-device-deployments)
+ [Platform dependency resolution](#platform-dependency-resolution)
+ [Component dependency resolution](#component-dependency-resolution)
+ [Removing a device from a thing group](#thing-group-removal-behavior)
+ [Deployments](#deployments)
+ [Deployment options](#deployment-options)
+ [Create deployments](create-deployments.md)
+ [Create subdeployments](create-subdeployments.md)
+ [Revise deployments](revise-deployments.md)
+ [Cancel deployments](cancel-deployments.md)
+ [Check deployment status](check-deployment-status.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
