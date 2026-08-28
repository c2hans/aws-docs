---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/deploy-first-component.html
---

# Step 6: Deploy your component
<a name="deploy-first-component"></a>

With AWS IoT Greengrass, you can deploy components to individual devices or groups of devices. When you deploy a component, AWS IoT Greengrass installs and runs that component's software on each target device. You specify which components to deploy and the configuration update to deploy for each component. You can also control how the deployment rolls out to the devices that the deployment targets. For more information, see [Deploy AWS IoT Greengrass components to devices](manage-deployments.md).

In this section, you deploy your Hello World component back to your Greengrass core device.

## Deploy your component (console)
<a name="deploy-first-component-console"></a>

1. In the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass) navigation menu, choose **Components**.

1. On the **Components** page, on the **My components** tab, choose **com.example.HelloWorld**.

1. On the **com.example.HelloWorld** page, choose **Deploy**.

1. From **Add to deployment**, choose **Create new deployment**, then choose **Next**.

1. On the **Specify target** page, do the following:

   1. In the **Name** box, enter **Deployment for MyGreengrassCore**.

   1. For **Deployment target**, choose **Core device**, and the name of the AWS IoT thing for your core device. The default value in this tutorial is {{MyGreengrassCore}}.

   1. Choose **Next**.

1. On the **Select components** page, under **My components**, verify that the **com.example.HelloWorld** component is selected, and choose **Next**.

1. On the **Configure components** page, choose **com.example.HelloWorld**, and do the following:

   1. Choose **Configure component**.

   1. Under **Configuration update**, in **Configuration to merge**, enter the following configuration.

      ```
      {
        "Message": "universe"
      }
      ```

      This configuration update sets the Hello World `Message` parameter to `universe` for the device in this deployment.

   1. Choose **Confirm**.

   1. Choose **Next**.

1. On the **Configure advanced settings** page, keep the default configuration settings, and choose **Next**.

1. On the **Review** page, choose **Deploy**.

1. <a name="getting-started-verify-cloud-deployment-step"></a>Verify that the deployment completes successfully. The deployment can take several minutes to complete. Check the Hello World log to verify the change. Run the following command on your Greengrass core device.

------
#### [ Linux or Unix ]

   ```
   sudo tail -f {{/greengrass/v2}}/logs/com.example.HelloWorld.log
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   type {{C:\greengrass\v2}}\\logs\\com.example.HelloWorld.log
   ```

------
#### [ PowerShell ]

   ```
   gc {{C:\greengrass\v2}}\\logs\\com.example.HelloWorld.log -Tail 10 -Wait
   ```

------

   You should see messages similar to the following example.

   ```
   Hello, universe! Greetings from your first Greengrass component.
   ```
**Note**
If the log messages don't change, the deployment failed or didn't reach the core device. This can occur if your core device isn't connected to the internet or doesn't have permissions to retrieve artifacts from your S3 bucket. Run the following command on your core device to view the AWS IoT Greengrass Core software log file. This file includes logs from the Greengrass core device's deployment service.

   ```
   sudo tail -f {{/greengrass/v2}}/logs/greengrass.log
   ```

   ```
   type {{C:\greengrass\v2}}\\logs\\greengrass.log
   ```
<a name="windows-cmd-type-observe-logs"></a>The `type` command writes the file's contents to the terminal. Run this command multiple times to observe changes in the file.

   ```
   gc {{C:\greengrass\v2}}\\logs\\greengrass.log -Tail 10 -Wait
   ```
For more information, see [Troubleshooting AWS IoT Greengrass V2](troubleshooting.md).

## Deploy your component (AWS CLI)
<a name="deploy-first-component-cli"></a>

**To deploy your Hello World component**

1. On your development computer, create a file called `hello-world-deployment.json` and copy the following JSON into the file. This file defines the components and configurations to deploy.

   ```
   {
     "components": {
       "com.example.HelloWorld": {
         "componentVersion": "1.0.0",
         "configurationUpdate": {
           "merge": "{\"Message\":\"universe\"}"
         }
       }
     }
   }
   ```

   This configuration file specifies to deploy version `1.0.0` of the Hello World component that you developed and published in the previous procedure. The `configurationUpdate` specifies to merge the component configuration in a JSON-encoded string. This configuration update sets the Hello World `Message` parameter to `universe` for the device in this deployment.

1. Run the following command to deploy the component to your Greengrass core device. You can deploy to things, which are individual devices, or thing groups, which are groups of devices. Replace {{MyGreengrassCore}} with the name of the AWS IoT thing for your core device.

------
#### [ Linux or Unix ]

   ```
   aws greengrassv2 create-deployment \
     --target-arn "arn:aws:iot:{{region}}:{{account-id}}:thing/{{MyGreengrassCore}}" \
     --cli-input-json file://hello-world-deployment.json
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   aws greengrassv2 create-deployment ^
     --target-arn "arn:aws:iot:{{region}}:{{account-id}}:thing/{{MyGreengrassCore}}" ^
     --cli-input-json file://hello-world-deployment.json
   ```

------
#### [ PowerShell ]

   ```
   aws greengrassv2 create-deployment `
     --target-arn "arn:aws:iot:{{region}}:{{account-id}}:thing/{{MyGreengrassCore}}" `
     --cli-input-json file://hello-world-deployment.json
   ```

------

   The command outputs a response similar to the following example.

   ```
   {
     "deploymentId": "deb69c37-314a-4369-a6a1-3dff9fce73a9",
     "iotJobId": "b5d92151-6348-4941-8603-bdbfb3e02b75",
     "iotJobArn": "arn:aws:iot:{{region}}:{{account-id}}:job/b5d92151-6348-4941-8603-bdbfb3e02b75"
   }
   ```

1. <a name="getting-started-verify-cloud-deployment-step"></a>Verify that the deployment completes successfully. The deployment can take several minutes to complete. Check the Hello World log to verify the change. Run the following command on your Greengrass core device.

------
#### [ Linux or Unix ]

   ```
   sudo tail -f {{/greengrass/v2}}/logs/com.example.HelloWorld.log
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   type {{C:\greengrass\v2}}\\logs\\com.example.HelloWorld.log
   ```

------
#### [ PowerShell ]

   ```
   gc {{C:\greengrass\v2}}\\logs\\com.example.HelloWorld.log -Tail 10 -Wait
   ```

------

   You should see messages similar to the following example.

   ```
   Hello, universe! Greetings from your first Greengrass component.
   ```
**Note**
If the log messages don't change, the deployment failed or didn't reach the core device. This can occur if your core device isn't connected to the internet or doesn't have permissions to retrieve artifacts from your S3 bucket. Run the following command on your core device to view the AWS IoT Greengrass Core software log file. This file includes logs from the Greengrass core device's deployment service.

   ```
   sudo tail -f {{/greengrass/v2}}/logs/greengrass.log
   ```

   ```
   type {{C:\greengrass\v2}}\\logs\\greengrass.log
   ```
<a name="windows-cmd-type-observe-logs"></a>The `type` command writes the file's contents to the terminal. Run this command multiple times to observe changes in the file.

   ```
   gc {{C:\greengrass\v2}}\\logs\\greengrass.log -Tail 10 -Wait
   ```
For more information, see [Troubleshooting AWS IoT Greengrass V2](troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
