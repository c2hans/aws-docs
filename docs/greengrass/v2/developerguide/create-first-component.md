---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/create-first-component.html
---

# Step 4: Develop and test a component on your device
<a name="create-first-component"></a>

A component is a software module that runs on AWS IoT Greengrass core devices. Components enable you to create and manage complex applications as discrete building blocks that you can reuse from one Greengrass core device to another. Every component is composed of a *recipe* and *artifacts*.
+ <a name="component-recipe-definition"></a>**Recipes**

  Every component contains a recipe file, which defines its metadata. The recipe also specifies the component's configuration parameters, component dependencies, lifecycle, and platform compatibility. The component lifecycle defines the commands that install, run, and shut down the component. For more information, see [AWS IoT Greengrass component recipe reference](component-recipe-reference.md).

  You can define recipes in [JSON](https://en.wikipedia.org/wiki/JSON) or [YAML](https://en.wikipedia.org/wiki/YAML) format.
+ <a name="component-artifacts-definition"></a>**Artifacts**

  Components can have any number of artifacts, which are component binaries. Artifacts can include scripts, compiled code, static resources, and any other files that a component consumes. Components can also consume artifacts from component dependencies.

With AWS IoT Greengrass, you can use the Greengrass CLI to develop and test components locally on a Greengrass core device without interaction with the AWS Cloud. When you complete your local component, you can use the component recipe and artifacts to create that component in the AWS IoT Greengrass service in the AWS Cloud, and then deploy it to all of your Greengrass core devices. For more information about components, see [Develop AWS IoT Greengrass components](develop-greengrass-components.md).

In this section, you learn how to create and run a basic Hello World component locally on your core device.

**To develop a Hello World component on your device**

1. <a name="create-component-recipes-artifacts-folder-step"></a>Create a folder for your components with subfolders for recipes and artifacts. Run the following commands on your Greengrass core device to create these folders and change to the component folder. Replace {{\~/greengrassv2}} or {{%USERPROFILE%\\greengrassv2}} with the path to the folder to use for local development.

------
#### [ Linux or Unix ]

   ```
   mkdir -p {{~/greengrassv2}}/{recipes,artifacts}
   cd {{~/greengrassv2}}
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   mkdir {{%USERPROFILE%\greengrassv2}}\\recipes, {{%USERPROFILE%\greengrassv2}}\\artifacts
   cd {{%USERPROFILE%\greengrassv2}}
   ```

------
#### [ PowerShell ]

   ```
   mkdir {{~/greengrassv2}}/recipes, {{~/greengrassv2}}/artifacts
   cd {{~/greengrassv2}}
   ```

------

1. <a name="create-component-recipe-file-step"></a>Use a text editor to create a recipe file that defines your component's metadata, parameters, dependencies, lifecycle, and platform capability. Include the component version in the recipe file name so that you can identify which recipe reflects which component version. You can choose YAML or JSON format for your recipe.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

------
#### [ JSON ]

   ```
   nano recipes/{{com.example.HelloWorld}}-{{1.0.0}}.json
   ```

------
#### [ YAML ]

   ```
   nano recipes/{{com.example.HelloWorld}}-{{1.0.0}}.yaml
   ```

------
**Note**
<a name="semver-para"></a>AWS IoT Greengrass uses semantic versions for components. Semantic versions follow a *major*.*minor*.*patch* number system. For example, version `1.0.0` represents the first major release for a component. For more information, see the [semantic version specification](https://semver.org/).

1. Paste the following recipe into the file.

------
#### [ JSON ]

   ```
   {
     "RecipeFormatVersion": "2020-01-25",
     "ComponentName": "com.example.HelloWorld",
     "ComponentVersion": "1.0.0",
     "ComponentDescription": "My first AWS IoT Greengrass component.",
     "ComponentPublisher": "Amazon",
     "ComponentConfiguration": {
       "DefaultConfiguration": {
         "Message": "world"
       }
     },
     "Manifests": [
       {
         "Platform": {
           "os": "linux"
         },
         "Lifecycle": {
           "run": "python3 -u {artifacts:path}/hello_world.py {configuration:/Message}"
         }
       },
       {
         "Platform": {
           "os": "windows"
         },
         "Lifecycle": {
           "run": "py -3 -u {artifacts:path}/hello_world.py {configuration:/Message}"
         }
       }
     ]
   }
   ```

------
#### [ YAML ]

   ```
   ---
   RecipeFormatVersion: '2020-01-25'
   ComponentName: com.example.HelloWorld
   ComponentVersion: '1.0.0'
   ComponentDescription: My first AWS IoT Greengrass component.
   ComponentPublisher: Amazon
   ComponentConfiguration:
     DefaultConfiguration:
       Message: world
   Manifests:
     - Platform:
         os: linux
       Lifecycle:
         run: |
           python3 -u {artifacts:path}/hello_world.py "{configuration:/Message}"
     - Platform:
         os: windows
       Lifecycle:
         run: |
           py -3 -u {artifacts:path}/hello_world.py "{configuration:/Message}"
   ```

------

   This recipe's `ComponentConfiguration` section defines a parameter, `Message`, that defaults to `world`. The `Manifests` section defines a *manifest*, which is a set of lifecycle instructions and artifacts for a platform. You can define multiple manifests to specify different install instructions for various platforms, for example. In the manifest, the `Lifecycle` section instructs the Greengrass core device to run the Hello World script with the `Message` parameter value as an argument.

1. Run the following command to create a folder for the component artifacts.

------
#### [ Linux or Unix ]

   ```
   mkdir -p artifacts/com.example.HelloWorld/1.0.0
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   mkdir artifacts\com.example.HelloWorld\1.0.0
   ```

------
#### [ PowerShell ]

   ```
   mkdir artifacts\com.example.HelloWorld\1.0.0
   ```

------
**Important**  <a name="local-artifact-folder-name-requirements"></a>
You must use the following format for the artifact folder path. Include the component name and version that you specify in the recipe.

   ```
   artifacts/{{componentName}}/{{componentVersion}}/
   ```

1. Use a text editor to create a Python script artifact file for your Hello World component.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano artifacts/com.example.HelloWorld/1.0.0/hello_world.py
   ```

   Copy and paste the following Python script into the file.

   ```
   import sys

   message = "Hello, %s!" % sys.argv[1]

   # Print the message to stdout, which Greengrass saves in a log file.
   print(message)
   ```

1. Use the local AWS IoT Greengrass CLI to manage components on your Greengrass core device.

   Run the following command to deploy the component to the AWS IoT Greengrass core. Replace `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}} with your AWS IoT Greengrass V2 root folder, and replace {{\~/greengrassv2}} or {{%USERPROFILE%\\greengrassv2}} with your component development folder.

------
#### [ Linux or Unix ]

   ```
   sudo {{/greengrass/v2}}/bin/greengrass-cli deployment create \
     --recipeDir {{~/greengrassv2}}/recipes \
     --artifactDir {{~/greengrassv2}}/artifacts \
     --merge "com.example.HelloWorld=1.0.0"
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli deployment create ^
     --recipeDir {{%USERPROFILE%\greengrassv2}}\recipes ^
     --artifactDir {{%USERPROFILE%\greengrassv2}}\artifacts ^
     --merge "com.example.HelloWorld=1.0.0"
   ```

------
#### [ PowerShell ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli deployment create `
     --recipeDir {{~/greengrassv2}}/recipes `
     --artifactDir {{~/greengrassv2}}/artifacts `
     --merge "com.example.HelloWorld=1.0.0"
   ```

------

   This command adds the component that uses the recipe in `recipes` and the Python script in `artifacts`. The `--merge` option adds or updates the component and version that you specify.

1. The AWS IoT Greengrass Core software saves stdout from component process to log files in the `logs` folder. Run the following command to verify that the Hello World component runs and prints messages.

------
#### [ Linux or Unix ]

   ```
   sudo tail -f {{/greengrass/v2}}/logs/com.example.HelloWorld.log
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   type {{C:\greengrass\v2}}\logs\com.example.HelloWorld.log
   ```

   <a name="windows-cmd-type-observe-logs"></a>The `type` command writes the file's contents to the terminal. Run this command multiple times to observe changes in the file.

------
#### [ PowerShell ]

   ```
   gc {{C:\greengrass\v2}}\logs\com.example.HelloWorld.log -Tail 10 -Wait
   ```

------

   You should see messages similar to the following example.

   ```
   Hello, world!
   ```
**Note**
If the file doesn't exist, the local deployment may not be complete yet. If the file doesn't exist within 15 seconds, the deployment likely failed. This can occur if your recipe isn't valid, for example. Run the following command to view the AWS IoT Greengrass core log file. This file includes logs from the Greengrass core device's deployment service.

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

1. Modify the local component to iterate and test your code. Open `hello_world.py` in a text editor, and add the following code at line 4 to edit the message that the AWS IoT Greengrass core logs.

   ```
   message += " Greetings from your first Greengrass component."
   ```

   The `hello_world.py` script should now have the following contents.

   ```
   import sys

   message = "Hello, %s!" % sys.argv[1]
   message += " Greetings from your first Greengrass component."

   # Print the message to stdout, which Greengrass saves in a log file.
   print(message)
   ```

1. Run the following command to update the component with your changes.

------
#### [ Linux or Unix ]

   ```
   sudo {{/greengrass/v2}}/bin/greengrass-cli deployment create \
     --recipeDir {{~/greengrassv2}}/recipes \
     --artifactDir {{~/greengrassv2}}/artifacts \
     --merge "com.example.HelloWorld=1.0.0"
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli deployment create ^
     --recipeDir {{%USERPROFILE%\greengrassv2}}\recipes ^
     --artifactDir {{%USERPROFILE%\greengrassv2}}\artifacts ^
     --merge "com.example.HelloWorld=1.0.0"
   ```

------
#### [ PowerShell ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli deployment create `
     --recipeDir {{~/greengrassv2}}/recipes `
     --artifactDir {{~/greengrassv2}}/artifacts `
     --merge "com.example.HelloWorld=1.0.0"
   ```

------

   This command updates the `com.example.HelloWorld` component with the latest Hello World artifact.

1. Run the following command to restart the component. When you restart a component, the core device uses the latest changes.

------
#### [ Linux or Unix ]

   ```
   sudo {{/greengrass/v2}}/bin/greengrass-cli component restart \
     --names "com.example.HelloWorld"
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli component restart ^
     --names "com.example.HelloWorld"
   ```

------
#### [ PowerShell ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli component restart `
     --names "com.example.HelloWorld"
   ```

------

1. Check the log again to verify that the Hello World component prints the new message.

------
#### [ Linux or Unix ]

   ```
   sudo tail -f {{/greengrass/v2}}/logs/com.example.HelloWorld.log
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   type {{C:\greengrass\v2}}\logs\com.example.HelloWorld.log
   ```

   <a name="windows-cmd-type-observe-logs"></a>The `type` command writes the file's contents to the terminal. Run this command multiple times to observe changes in the file.

------
#### [ PowerShell ]

   ```
   gc {{C:\greengrass\v2}}\logs\com.example.HelloWorld.log -Tail 10 -Wait
   ```

------

   You should see messages similar to the following example.

   ```
   Hello, world! Greetings from your first Greengrass component.
   ```

1. You can update the component's configuration parameters to test different configurations. When you deploy a component, you can specify a *configuration update*, which defines how to modify the component's configuration on the core device. You can specify which configuration values to reset to default values and the new configuration values to merge onto the core device. For more information, see [Update component configurations](update-component-configurations.md).

   Do the following:

   1. Use a text editor to create a file called `hello-world-config-update.json` to contain the configuration update

      <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

      ```
      nano hello-world-config-update.json
      ```

   1. Copy and paste the following JSON object into the file. This JSON object defines a configuration update that merges the value `friend` to the `Message` parameter to update its value. This configuration update doesn't specify any values to reset. You don't need to reset the `Message` parameter because the merge update replaces the existing value.

      ```
      {
        "com.example.HelloWorld": {
          "MERGE": {
            "Message": "friend"
          }
        }
      }
      ```

   1. Run the following command to deploy the configuration update to the Hello World component.

------
#### [ Linux or Unix ]

      ```
      sudo {{/greengrass/v2}}/bin/greengrass-cli deployment create \
        --merge "com.example.HelloWorld=1.0.0" \
        --update-config hello-world-config-update.json
      ```

------
#### [ Windows Command Prompt (CMD) ]

      ```
      {{C:\greengrass\v2}}\bin\greengrass-cli deployment create ^
        --merge "com.example.HelloWorld=1.0.0" ^
        --update-config hello-world-config-update.json
      ```

------
#### [ PowerShell ]

      ```
      {{C:\greengrass\v2}}\bin\greengrass-cli deployment create `
        --merge "com.example.HelloWorld=1.0.0" `
        --update-config hello-world-config-update.json
      ```

------

   1. Check the log again to verify that the Hello World component outputs the new message.

------
#### [ Linux or Unix ]

      ```
      sudo tail -f {{/greengrass/v2}}/logs/com.example.HelloWorld.log
      ```

------
#### [ Windows Command Prompt (CMD) ]

      ```
      type {{C:\greengrass\v2}}\logs\com.example.HelloWorld.log
      ```

      <a name="windows-cmd-type-observe-logs"></a>The `type` command writes the file's contents to the terminal. Run this command multiple times to observe changes in the file.

------
#### [ PowerShell ]

      ```
      gc {{C:\greengrass\v2}}\logs\com.example.HelloWorld.log -Tail 10 -Wait
      ```

------

      You should see messages similar to the following example.

      ```
      Hello, friend! Greetings from your first Greengrass component.
      ```

1. After you finish testing your component, remove it from your core device. Run the following command.

------
#### [ Linux or Unix ]

   ```
   sudo {{/greengrass/v2}}/bin/greengrass-cli deployment create --remove="com.example.HelloWorld"
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli deployment create --remove="com.example.HelloWorld"
   ```

------
#### [ PowerShell ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli deployment create --remove="com.example.HelloWorld"
   ```

------
**Important**
This step is required for you to deploy the component back to the core device after you upload it to AWS IoT Greengrass. Otherwise, the deployment fails with a version compatibility error because the local deployment specifies a different version of the component.

   Run the following command and verify that the `com.example.HelloWorld` component doesn't appear in the list of components on your device.

------
#### [ Linux or Unix ]

   ```
   sudo {{/greengrass/v2}}/bin/greengrass-cli component list
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli component list
   ```

------
#### [ PowerShell ]

   ```
   {{C:\greengrass\v2}}\bin\greengrass-cli component list
   ```

------

Your Hello World component is complete, and you can now upload it to the AWS IoT Greengrass cloud service. Then, you can deploy the component to Greengrass core devices.
