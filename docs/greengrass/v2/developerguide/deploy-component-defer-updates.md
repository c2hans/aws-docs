---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/deploy-component-defer-updates.html
---

# Step 4: Deploy and test the component on a core device
<a name="deploy-component-defer-updates"></a>

In this section, you deploy the component to the core device to test its functionality. On the core device, you create the virtual battery level file to imitate a real battery. Then, you create additional deployments and observe the component log files on the core device to see the component defer and acknowledge updates.

**To deploy and test the Hello World component that defers updates**

1. Use a text editor to create a virtual battery level file. This file imitates a real battery.
   + On Linux core devices, create a file named `/home/ggc_user/virtual_battery.json`. Run the text editor with `sudo` permissions.
   + On Windows core devices, create a file named `C:\Users\ggc_user\virtual_battery.json`. Run the text editor as an administrator.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   sudo nano /home/ggc_user/virtual_battery.json
   ```

   Copy the following JSON into the file.

   ```
   {
     "battery_level": 50
   }
   ```

1. Deploy the Hello World component to the core device. Do the following:

   1. In the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass) navigation menu, choose **Components**.

   1. On the **Components** page, choose the **My components** tab, and then choose **com.example.BatteryAwareHelloWorld**.

   1. On the **com.example.BatteryAwareHelloWorld** page, choose **Deploy**.

   1. <a name="deploy-component-choose-deployment-step"></a>From **Add to deployment**, choose an existing deployment to revise, or choose to create a new deployment, and then choose **Next**.

   1. <a name="deploy-component-choose-target-step"></a>If you chose to create a new deployment, choose the target core device or thing group for the deployment. On the **Specify target** page, under **Deployment target**, choose a core device or thing group, and then choose **Next**.

   1. On the **Select components** page, verify that the **com.example.BatteryAwareHelloWorld** component is selected, choose **Next**.

   1. On the **Configure components** page, select **com.example.BatteryAwareHelloWorld**, and then do the following:

      1. Choose **Configure component**.

      1. In the **Configure com.example.BatteryAwareHelloWorld** modal, under **Configuration update**, in **Configuration to merge**, enter the following configuration update.

         ```
         {
           "BatteryThreshold": 70
         }
         ```

      1. Choose **Confirm** to close the modal, and then choose **Next**.

   1. On the **Confirm advanced settings** page, in the **Deployment policies** section, under **Component update policy**, confirm that **Notify components** is selected. **Notify components** is selected by default when you create a new deployment.

   1. <a name="deploy-component-review-and-deploy-step"></a>On the **Review** page, choose **Deploy**.

      The deployment can take up to a minute to complete.

1. The AWS IoT Greengrass Core software saves stdout from component processes to log files in the `logs` folder. Run the following command to verify that the Hello World component runs and prints status messages.

------
#### [ Linux or Unix ]

   ```
   sudo tail -f {{/greengrass/v2}}/logs/com.example.BatteryAwareHelloWorld.log
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   type {{C:\greengrass\v2}}\logs\com.example.BatteryAwareHelloWorld.log
   ```

------
#### [ PowerShell ]

   ```
   gc {{C:\greengrass\v2}}\logs\com.example.BatteryAwareHelloWorld.log -Tail 10 -Wait
   ```

------

   You should see messages similar to the following example.

   ```
   Hello, World! Battery level (50) is below threshold (70), so the component will defer updates.
   ```
**Note**
If the file doesn't exist, the deployment may not be complete yet. If the file doesn't exist within 30 seconds, the deployment likely failed. This can occur if the core device doesn't have permission to download the component's artifacts from the S3 bucket, for example. Run the following command to view the AWS IoT Greengrass Core software log file. This file includes logs from the Greengrass core device's deployment service.

   ```
   sudo tail -f {{/greengrass/v2}}/logs/greengrass.log
   ```

   ```
   type {{C:\greengrass\v2}}\logs\greengrass.log
   ```
<a name="windows-cmd-type-observe-logs"></a>The `type` command writes the file's contents to the terminal. Run this command multiple times to observe changes in the file.

   ```
   gc {{C:\greengrass\v2}}\logs\greengrass.log -Tail 10 -Wait
   ```

1. Create a new deployment to the core device to verify that the component defers the update. Do the following:

   1. In the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass) navigation menu, choose **Deployments**.

   1. Choose the deployment that you created or revised earlier.

   1. On the deployment page, choose **Revise**.

   1. In the **Revise deployment** modal, choose **Revise deployment**.

   1. Choose **Next** at each step, and then choose **Deploy**.

1. Run the following command to view the component's logs again, and verify that it defers the update.

------
#### [ Linux or Unix ]

   ```
   sudo tail -f {{/greengrass/v2}}/logs/com.example.BatteryAwareHelloWorld.log
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   type {{C:\greengrass\v2}}\logs\com.example.BatteryAwareHelloWorld.log
   ```

------
#### [ PowerShell ]

   ```
   gc {{C:\greengrass\v2}}\logs\com.example.BatteryAwareHelloWorld.log -Tail 10 -Wait
   ```

------

   You should see messages similar to the following example. The component defers the update for 30 seconds, so the component prints this message repeatedly.

   ```
   Deferred update for deployment 50722a95-a05f-4e2a-9414-da80103269aa.
   ```

1. Use a text editor to edit the virtual battery level file and change the battery level to a value above the threshold, so the deployment can proceed.
   + On Linux core devices, edit the file named `/home/ggc_user/virtual_battery.json`. Run the text editor with `sudo` permissions.
   + On Windows core devices, edit the file named `C:\Users\ggc_user\virtual_battery.json`. Run the text editor as an administrator.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   sudo nano /home/ggc_user/virtual_battery.json
   ```

   Change the battery level to `80`.

   ```
   {
     "battery_level": 80
   }
   ```

1. Run the following command to view the component's logs again, and verify that it acknowledges the update.

------
#### [ Linux or Unix ]

   ```
   sudo tail -f {{/greengrass/v2}}/logs/com.example.BatteryAwareHelloWorld.log
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   type {{C:\greengrass\v2}}\logs\com.example.BatteryAwareHelloWorld.log
   ```

------
#### [ PowerShell ]

   ```
   gc {{C:\greengrass\v2}}\logs\com.example.BatteryAwareHelloWorld.log -Tail 10 -Wait
   ```

------

   You should see messages similar to the following examples.

   ```
   Hello, World! Battery level (80) is above threshold (70), so the component will acknowledge updates.
   Acknowledged update for deployment f9499eb2-4a40-40a7-86c1-c89887d859f1.
   ```
