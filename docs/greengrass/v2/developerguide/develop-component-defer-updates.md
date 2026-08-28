---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/develop-component-defer-updates.html
---

# Step 2: Develop a component that defers updates
<a name="develop-component-defer-updates"></a>

In this section, you develop a Hello World component in Python that defers component updates when the core device's battery level is below a threshold that you configure when you deploy the component. In this component, you use the [interprocess communication (IPC) interface](interprocess-communication.md) in the AWS IoT Device SDK v2 for Python. You use the [SubscribeToComponentUpdates](ipc-component-lifecycle.md#ipc-operation-subscribetocomponentupdates) IPC operation to receive notifications when the core device receives a deployment. Then, you use the [DeferComponentUpdate](ipc-component-lifecycle.md#ipc-operation-defercomponentupdate) IPC operation to defer or acknowledge the update based on the device's battery level.

**To develop a Hello World component that defers updates**

1. On your development computer, create a folder for the component source code.

   ```
   mkdir com.example.BatteryAwareHelloWorld
   cd com.example.BatteryAwareHelloWorld
   ```

1. Use a text editor to create a file named `gdk-config.json`. The GDK CLI reads from the [GDK CLI configuration file](gdk-cli-configuration-file.md), named `gdk-config.json`, to build and publish components. This configuration file exists in the root of the component folder.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano gdk-config.json
   ```

   Copy the following JSON into the file.
   + Replace {{Amazon}} with your name.
   + Replace {{us-west-2}} with the AWS Region where your core device operates. The GDK CLI publishes the component in this AWS Region.
   + Replace {{greengrass-component-artifacts}} with the S3 bucket prefix to use. When you use the GDK CLI to publish the component, the GDK CLI uploads the component's artifacts to the S3 bucket whose name is formed from this value, the AWS Region, and your AWS account ID using the following format: `{{bucketPrefix}}-{{region}}-{{accountId}}`.

     For example, if you specify **greengrass-component-artifacts** and **us-west-2**, and your AWS account ID is **123456789012**, the GDK CLI uses the S3 bucket named `greengrass-component-artifacts-us-west-2-123456789012`.

   ```
   {
     "component": {
       "com.example.BatteryAwareHelloWorld": {
         "author": "{{Amazon}}",
         "version": "NEXT_PATCH",
         "build": {
           "build_system" : "zip"
         },
         "publish": {
           "region": "{{us-west-2}}",
           "bucket": "{{greengrass-component-artifacts}}"
         }
       }
     },
     "gdk_version": "1.0.0"
   }
   ```

   The configuration file specifies the following:
   + The version to use when the GDK CLI publishes the Greengrass component to the AWS IoT Greengrass cloud service. `NEXT_PATCH` specifies to choose the next patch version after the latest version available in the AWS IoT Greengrass cloud service. If the component doesn't have a version in the AWS IoT Greengrass cloud service yet, the GDK CLI uses `1.0.0`.
   + The build system for the component. When you use the `zip` build system, the GDK CLI packages the component's source into a ZIP file that becomes the component's single artifact.
   + The AWS Region where the GDK CLI publishes the Greengrass component.
   + The prefix for the S3 bucket where the GDK CLI uploads the component's artifacts.

1. Use a text editor to create the component source code in a file named `main.py`.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano main.py
   ```

   Copy the following Python code into the file.

   ```
   import json
   import os
   import sys
   import time
   import traceback

   from pathlib import Path

   from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2

   HELLO_WORLD_PRINT_INTERVAL = 15  # Seconds
   DEFER_COMPONENT_UPDATE_INTERVAL = 30 * 1000  # Milliseconds

   class BatteryAwareHelloWorldPrinter():
       def __init__(self, ipc_client: GreengrassCoreIPCClientV2, battery_file_path: Path, battery_threshold: float):
           self.battery_file_path = battery_file_path
           self.battery_threshold = battery_threshold
           self.ipc_client = ipc_client
           self.subscription_operation = None

       def on_component_update_event(self, event):
           try:
               if event.pre_update_event is not None:
                   if self.is_battery_below_threshold():
                       self.defer_update(event.pre_update_event.deployment_id)
                       print('Deferred update for deployment %s' %
                             event.pre_update_event.deployment_id)
                   else:
                       self.acknowledge_update(
                           event.pre_update_event.deployment_id)
                       print('Acknowledged update for deployment %s' %
                             event.pre_update_event.deployment_id)
               elif event.post_update_event is not None:
                   print('Applied update for deployment')
           except:
               traceback.print_exc()

       def subscribe_to_component_updates(self):
           if self.subscription_operation == None:
               # SubscribeToComponentUpdates returns a tuple with the response and the operation.
               _, self.subscription_operation = self.ipc_client.subscribe_to_component_updates(
                   on_stream_event=self.on_component_update_event)

       def close_subscription(self):
           if self.subscription_operation is not None:
               self.subscription_operation.close()
               self.subscription_operation = None

       def defer_update(self, deployment_id):
           self.ipc_client.defer_component_update(
               deployment_id=deployment_id, recheck_after_ms=DEFER_COMPONENT_UPDATE_INTERVAL)

       def acknowledge_update(self, deployment_id):
           # Specify recheck_after_ms=0 to acknowledge a component update.
           self.ipc_client.defer_component_update(
               deployment_id=deployment_id, recheck_after_ms=0)

       def is_battery_below_threshold(self):
           return self.get_battery_level() < self.battery_threshold

       def get_battery_level(self):
           # Read the battery level from the virtual battery level file.
           with self.battery_file_path.open('r') as f:
               data = json.load(f)
               return float(data['battery_level'])

       def print_message(self):
           message = 'Hello, World!'
           if self.is_battery_below_threshold():
               message += ' Battery level (%d) is below threshold (%d), so the component will defer updates' % (
                   self.get_battery_level(), self.battery_threshold)
           else:
               message += ' Battery level (%d) is above threshold (%d), so the component will acknowledge updates' % (
                   self.get_battery_level(), self.battery_threshold)
           print(message)

   def main():
       # Read the battery threshold and virtual battery file path from command-line args.
       args = sys.argv[1:]
       battery_threshold = float(args[0])
       battery_file_path = Path(args[1])
       print('Reading battery level from %s and deferring updates when below %d' % (
           str(battery_file_path), battery_threshold))

       try:
           # Create an IPC client and a Hello World printer that defers component updates.
           ipc_client = GreengrassCoreIPCClientV2()
           hello_world_printer = BatteryAwareHelloWorldPrinter(
               ipc_client, battery_file_path, battery_threshold)
           hello_world_printer.subscribe_to_component_updates()
           try:
               # Keep the main thread alive, or the process will exit.
               while True:
                   hello_world_printer.print_message()
                   time.sleep(HELLO_WORLD_PRINT_INTERVAL)
           except InterruptedError:
               print('Subscription interrupted')
           hello_world_printer.close_subscription()
       except Exception:
           print('Exception occurred', file=sys.stderr)
           traceback.print_exc()
           exit(1)

   if __name__ == '__main__':
       main()
   ```

   This Python application does the following:
   + Reads the core device's battery level from a virtual battery level file that you'll create on the core device later. This virtual battery level file imitates a real battery, so you can complete this tutorial on core devices that don't have a battery.
   + Reads command-line arguments for the battery threshold and the path to the virtual battery level file. The component recipe sets these command-line arguments based on configuration parameters, so you can customize these values when you deploy the component.
   + Uses the IPC client V2 in the [AWS IoT Device SDK v2 for Python](https://github.com/aws/aws-iot-device-sdk-python-v2) to communicate with the AWS IoT Greengrass Core software. Compared to the original IPC client, the IPC client V2 reduces the amount of code that you need to write to use IPC in custom components.
   + Subscribes to update notifications using the [SubscribeToComponentUpdates](ipc-component-lifecycle.md#ipc-operation-subscribetocomponentupdates) IPC operation. The AWS IoT Greengrass Core software sends notifications before and after each deployment. The component calls the following function each time it receives a notification. If the notification is for an upcoming deployment, the component checks if the battery level is lower than a threshold. If the battery level is below the threshold, the component defers the update for 30 seconds using the [DeferComponentUpdate](ipc-component-lifecycle.md#ipc-operation-defercomponentupdate) IPC operation. Otherwise, if the battery level isn't below the threshold, the component acknowledges the update, so the update can proceed.

     ```
     def on_component_update_event(self, event):
         try:
             if event.pre_update_event is not None:
                 if self.is_battery_below_threshold():
                     self.defer_update(event.pre_update_event.deployment_id)
                     print('Deferred update for deployment %s' %
                           event.pre_update_event.deployment_id)
                 else:
                     self.acknowledge_update(
                         event.pre_update_event.deployment_id)
                     print('Acknowledged update for deployment %s' %
                           event.pre_update_event.deployment_id)
             elif event.post_update_event is not None:
                 print('Applied update for deployment')
         except:
             traceback.print_exc()
     ```
**Note**
The AWS IoT Greengrass Core software doesn't send update notifications for local deployments, so you deploy this component using the AWS IoT Greengrass cloud service to test it.

1. Use a text editor to create the component recipe in a file named `recipe.json` or `recipe.yaml`. The component *recipe* defines the component's metadata, default configuration parameters, and platform-specific lifecycle scripts.

------
#### [ JSON ]

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano recipe.json
   ```

   Copy the following JSON into the file.

   ```
   {
     "RecipeFormatVersion": "2020-01-25",
     "ComponentName": "COMPONENT_NAME",
     "ComponentVersion": "COMPONENT_VERSION",
     "ComponentDescription": "This Hello World component defers updates when the battery level is below a threshold.",
     "ComponentPublisher": "COMPONENT_AUTHOR",
     "ComponentConfiguration": {
       "DefaultConfiguration": {
         "BatteryThreshold": 50,
         "LinuxBatteryFilePath": "/home/ggc_user/virtual_battery.json",
         "WindowsBatteryFilePath": "C:\\Users\\ggc_user\\virtual_battery.json"
       }
     },
     "Manifests": [
       {
         "Platform": {
           "os": "linux"
         },
         "Lifecycle": {
           "install": "python3 -m pip install --user awsiotsdk --upgrade",
           "Run": "python3 -u {artifacts:decompressedPath}/com.example.BatteryAwareHelloWorld/main.py \"{configuration:/BatteryThreshold}\" \"{configuration:/LinuxBatteryFilePath}\""
         },
         "Artifacts": [
           {
             "Uri": "s3://BUCKET_NAME/COMPONENT_NAME/COMPONENT_VERSION/com.example.BatteryAwareHelloWorld.zip",
             "Unarchive": "ZIP"
           }
         ]
       },
       {
         "Platform": {
           "os": "windows"
         },
         "Lifecycle": {
           "install": "py -3 -m pip install --user awsiotsdk --upgrade",
           "Run": "py -3 -u {artifacts:decompressedPath}/com.example.BatteryAwareHelloWorld/main.py \"{configuration:/BatteryThreshold}\" \"{configuration:/WindowsBatteryFilePath}\""
         },
         "Artifacts": [
           {
             "Uri": "s3://BUCKET_NAME/COMPONENT_NAME/COMPONENT_VERSION/com.example.BatteryAwareHelloWorld.zip",
             "Unarchive": "ZIP"
           }
         ]
       }
     ]
   }
   ```

------
#### [ YAML ]

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano recipe.yaml
   ```

   Copy the following YAML into the file.

   ```
   ---
   RecipeFormatVersion: "2020-01-25"
   ComponentName: "COMPONENT_NAME"
   ComponentVersion: "COMPONENT_VERSION"
   ComponentDescription: "This Hello World component defers updates when the battery level is below a threshold."
   ComponentPublisher: "COMPONENT_AUTHOR"
   ComponentConfiguration:
     DefaultConfiguration:
       BatteryThreshold: 50
       LinuxBatteryFilePath: "/home/ggc_user/virtual_battery.json"
       WindowsBatteryFilePath: "C:\\Users\\ggc_user\\virtual_battery.json"
   Manifests:
     - Platform:
         os: linux
       Lifecycle:
         install: python3 -m pip install --user awsiotsdk --upgrade
         Run: python3 -u {artifacts:decompressedPath}/com.example.BatteryAwareHelloWorld/main.py "{configuration:/BatteryThreshold}" "{configuration:/LinuxBatteryFilePath}"
       Artifacts:
         - Uri: "s3://BUCKET_NAME/COMPONENT_NAME/COMPONENT_VERSION/com.example.BatteryAwareHelloWorld.zip"
           Unarchive: ZIP
     - Platform:
         os: windows
       Lifecycle:
         install: py -3 -m pip install --user awsiotsdk --upgrade
         Run: py -3 -u {artifacts:decompressedPath}/com.example.BatteryAwareHelloWorld/main.py "{configuration:/BatteryThreshold}" "{configuration:/WindowsBatteryFilePath}"
       Artifacts:
         - Uri: "s3://BUCKET_NAME/COMPONENT_NAME/COMPONENT_VERSION/com.example.BatteryAwareHelloWorld.zip"
           Unarchive: ZIP
   ```

------

   This recipe specifies the following:
   + Default configuration parameters for the battery threshold, the virtual battery file path on Linux core devices, and the virtual battery file path on Windows core devices.
   + An `install` lifecycle that installs the latest version of the AWS IoT Device SDK v2 for Python.
   + A `run` lifecycle that runs the Python application in `main.py`.
   + Placeholders, such as `COMPONENT_NAME` and `COMPONENT_VERSION`, where the GDK CLI replaces information when it builds the component recipe.

   For more information about component recipes, see [AWS IoT Greengrass component recipe reference](component-recipe-reference.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
