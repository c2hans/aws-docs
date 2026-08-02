---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/switch-core-device-connectivity.html
---

# Switch a Greengrass core device to a different AWS account or Region
<a name="switch-core-device-connectivity"></a>

You can deploy a nucleus configuration update to switch a core device's IoT connectivity from one AWS account or Region to another. This is useful in the following scenarios:
+ **Manufacturing to production transition** – You provision devices in a staging account during manufacturing and move them to the destination account during field installation.
+ **Geographic relocation** – Devices that move from one Region to another must connect to the local Region's AWS IoT endpoint to reduce latency.
+ **Failure impact reduction** – You redistribute devices initially concentrated in a single account across multiple accounts to limit the impact of account-level issues such as service quota limits or security incidents.

When you deploy an IoT connectivity switch, the nucleus validates connectivity to the new endpoint before applying the change and automatically rolls back if the connection fails.

This feature requires Greengrass nucleus v2.18.0 or later, or Greengrass nucleus lite v2.6.0 or later.

**Topics**
+ [Prerequisites](#switch-connectivity-prerequisites)
+ [Create the deployment](#switch-connectivity-create-deployment)
+ [What to expect](#switch-connectivity-what-to-expect)
+ [Verify the switch](#switch-connectivity-verify)

## Prerequisites
<a name="switch-connectivity-prerequisites"></a>

Before you deploy a connectivity switch, set up the following in the destination AWS account and Region:
+ **AWS IoT thing** – Create a thing with the same name as in the source account.
+ **Certificate** – Register the same device certificate in the destination account. The certificate must be the same certificate that the device uses in the source account.
+ **AWS IoT policy** – Attach a policy to the certificate. The policy must allow `iot:Connect` with a resource ARN that uses a wildcard suffix for the client ID:

  ```
  "Resource": "arn:aws:iot:*:*:client/${iot:Connection.Thing.ThingName}*"
  ```

  You must include the wildcard suffix because the nucleus pre-flight connectivity check uses client ID `{{thing-name}}#endpoint-switch`.
+ **AWS IoT role alias** – Create a role alias in the destination Region with the appropriate IAM role permissions for Greengrass operations.

**Note**
To use AWS IoT thing policy variables such as `${iot:Connection.Thing.ThingName}` in the AWS IoT policy, you must attach the certificate exclusively to the AWS IoT thing in the destination account.

For Greengrass nucleus core devices, you must also set `greengrassDataPlaneEndpoint` to **iotdata** in the nucleus configuration. Include this setting in the connectivity switch deployment or during initial provisioning.

Without this setting, the data plane stays bound to the original account after the switch. This breaks component artifact downloads and control plane operations. For more information, see the `greengrassDataPlaneEndpoint` configuration parameter in [Greengrass nucleus](greengrass-nucleus-component.md).

For Greengrass nucleus lite core devices, you must create a private `aws.greengrass.NucleusLite` component in your account before you can deploy configuration updates to the nucleus. AWS IoT Greengrass deployments can only target components that exist in the account's component registry, and there is no public component for nucleus lite.

Create a component with the `aws_nucleus_lite` runtime and an empty lifecycle (no actions). The component version must match the version of nucleus lite running on the device.

## Create the deployment
<a name="switch-connectivity-create-deployment"></a>

Create a deployment that targets the core device or its thing group in the source account. The deployment sends a merge configuration update to the nucleus component with the new AWS IoT endpoint values.

**To deploy a connectivity switch (AWS CLI)**

1. Create a file called `switch-deployment.json` with the following content. Replace the placeholder values with your destination account's values.
   + Replace {{targetArn}} with the ARN of the AWS IoT thing group or the core device in the source account.
   + Replace {{componentName}} with `aws.greengrass.Nucleus` for nucleus or `aws.greengrass.NucleusLite` for nucleus lite.
   + Replace {{componentVersion}} with the version of the nucleus running on the device.

   ```
   {
     "targetArn": "{{targetArn}}",
     "deploymentName": "SwitchConnectivity",
     "components": {
       "{{componentName}}": {
         "componentVersion": "{{componentVersion}}",
         "configurationUpdate": {
           "merge": "{\"iotDataEndpoint\":\"{{account-prefix}}-ats.iot.{{region}}.amazonaws.com\",\"iotCredEndpoint\":\"{{account-prefix}}.credentials.iot.{{region}}.amazonaws.com\",\"awsRegion\":\"{{region}}\",\"iotRoleAlias\":\"{{role-alias-name}}\"}"
         }
       }
     },
     "deploymentPolicies": {
       "failureHandlingPolicy": "ROLLBACK"
     }
   }
   ```

   For Greengrass nucleus core devices that do not already have `greengrassDataPlaneEndpoint` set to **iotdata**, add it to the merge configuration:

   ```
   "merge": "{\"iotDataEndpoint\":\"...\",\"iotCredEndpoint\":\"...\",\"awsRegion\":\"...\",\"iotRoleAlias\":\"...\",\"greengrassDataPlaneEndpoint\":\"iotdata\"}"
   ```

   Encode the `merge` value as a JSON string. Escape all inner quotes with backslashes (`\"`). Use a JSON validation tool to verify syntax before creating the deployment.

1. Run the following command to create the deployment.

   ```
   aws greengrassv2 create-deployment \
     --cli-input-json file://switch-deployment.json
   ```

## What to expect
<a name="switch-connectivity-what-to-expect"></a>

The nucleus validates connectivity to the new endpoint before applying the change. If the device cannot connect to the new endpoint, the deployment fails and the device remains connected to the source account.

The nucleus uses client ID `{{thing-name}}#endpoint-switch` for the pre-flight connectivity check.

After applying the configuration, the nucleus tests connectivity to the new endpoint. If connectivity fails, the nucleus automatically rolls back to the original configuration. The deployment reports `FAILED` in the source account.

If the connectivity switch succeeds, the deployment reports `SUCCEEDED` in the source account. AWS IoT Greengrass creates a core device in the account and Region associated with the new endpoint.

**Note**
During the connectivity switch, the nucleus restarts components that have a hard dependency on the token exchange service. This restart refreshes credentials from the new AWS IoT credential endpoint. The nucleus does not restart other components, and they continue running with their existing state.

## Verify the switch
<a name="switch-connectivity-verify"></a>

After the deployment completes, verify that the connectivity switch succeeded.

**To verify the connectivity switch**

1. Check the deployment status in the source account. The deployment reports `SUCCEEDED` after the device connects to the new endpoint.

   ```
   aws greengrassv2 list-effective-deployments \
     --core-device-thing-name {{thing-name}}
   ```

1. Verify that the core device appears in the destination account. Open the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass) or run the following command.

   ```
   aws greengrassv2 get-core-device \
     --core-device-thing-name {{thing-name}}
   ```

The AWS IoT thing and core device record remain in the source account after the switch. To prevent future deployments from targeting the device, remove it from the source account's thing group.

If the deployment status is not `SUCCEEDED`, check the Greengrass log at `{{/greengrass/v2}}/logs/greengrass.log` on the device for error details. For common error codes related to connectivity switch operations, see [Detailed deployment error codes](troubleshooting-deployment.md).
