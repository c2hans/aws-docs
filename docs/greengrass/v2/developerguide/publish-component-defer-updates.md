---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/publish-component-defer-updates.html
---

# Step 3: Publish the component to the AWS IoT Greengrass service
<a name="publish-component-defer-updates"></a>

In this section, you publish the Hello World component to the AWS IoT Greengrass cloud service. After a component is available in the AWS IoT Greengrass cloud service, you can deploy it to core devices. You use the GDK CLI to publish the component from your development computer to the AWS IoT Greengrass cloud service. The GDK CLI uploads the component's recipe and artifacts for you.

**To publish the Hello World component to the AWS IoT Greengrass service**

1. Run the following command to build the component using the GDK CLI. The [component build command](greengrass-development-kit-cli-component.md#greengrass-development-kit-cli-component-build) creates a recipe and artifacts based on the GDK CLI configuration file. In this process, the GDK CLI creates a ZIP file that contains the component's source code.

   ```
   gdk component build
   ```

   You should see messages similar to the following example.

   ```
   [2022-04-28 11:20:16] INFO - Getting project configuration from gdk-config.json
   [2022-04-28 11:20:16] INFO - Found component recipe file 'recipe.yaml' in the  project directory.
   [2022-04-28 11:20:16] INFO - Building the component 'com.example.BatteryAwareHelloWorld' with the given project configuration.
   [2022-04-28 11:20:16] INFO - Using 'zip' build system to build the component.
   [2022-04-28 11:20:16] WARNING - This component is identified as using 'zip' build system. If this is incorrect, please exit and specify custom build command in the 'gdk-config.json'.
   [2022-04-28 11:20:16] INFO - Zipping source code files of the component.
   [2022-04-28 11:20:16] INFO - Copying over the build artifacts to the greengrass component artifacts build folder.
   [2022-04-28 11:20:16] INFO - Updating artifact URIs in the recipe.
   [2022-04-28 11:20:16] INFO - Creating component recipe in 'C:\Users\finthomp\greengrassv2\com.example.BatteryAwareHelloWorld\greengrass-build\recipes'.
   ```

1. Run the following command to publish the component to the AWS IoT Greengrass cloud service. The [component publish command](greengrass-development-kit-cli-component.md#greengrass-development-kit-cli-component-publish) uploads the component's ZIP file artifact to an S3 bucket. Then, it updates the ZIP file's S3 URI in the component recipe and uploads the recipe to the AWS IoT Greengrass service. In this process, the GDK CLI checks what version of the Hello World component is already available in the AWS IoT Greengrass cloud service, so it can choose the next patch version after that version. If the component doesn't exist yet, the GDK CLI uses version `1.0.0`.

   ```
   gdk component publish
   ```

   You should see messages similar to the following example. The output tells you the version of the component that the GDK CLI created.

   ```
   [2022-04-28 11:20:29] INFO - Getting project configuration from gdk-config.json
   [2022-04-28 11:20:29] INFO - Found component recipe file 'recipe.yaml' in the  project directory.
   [2022-04-28 11:20:29] INFO - Found credentials in shared credentials file: ~/.aws/credentials
   [2022-04-28 11:20:30] INFO - No private version of the component 'com.example.BatteryAwareHelloWorld' exist in the account. Using '1.0.0' as the next version to create.
   [2022-04-28 11:20:30] INFO - Publishing the component 'com.example.BatteryAwareHelloWorld' with the given project configuration.
   [2022-04-28 11:20:30] INFO - Uploading the component built artifacts to s3 bucket.
   [2022-04-28 11:20:30] INFO - Uploading component artifacts to S3 bucket: greengrass-component-artifacts-us-west-2-123456789012. If this is your first time using this bucket, add the 's3:GetObject' permission to each core device's token exchange role to allow it to download the component artifacts. For more information, see https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html.
   [2022-04-28 11:20:30] INFO - Not creating an artifacts bucket as it already exists.
   [2022-04-28 11:20:30] INFO - Updating the component recipe com.example.BatteryAwareHelloWorld-1.0.0.
   [2022-04-28 11:20:31] INFO - Creating a new greengrass component com.example.BatteryAwareHelloWorld-1.0.0
   [2022-04-28 11:20:31] INFO - Created private version '1.0.0' of the component in the account.'com.example.BatteryAwareHelloWorld'.
   ```

1. Copy the S3 bucket name from the output. You use the bucket name later to allow the core device to download component artifacts from this bucket.

1. (Optional) View the component in the AWS IoT Greengrass console to verify that it uploaded successfully. Do the following:

   1. In the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass) navigation menu, choose **Components**.

   1. On the **Components** page, choose the **My components** tab, and then choose **com.example.BatteryAwareHelloWorld**.

      On this page, you can see the component's recipe and other information about the component.

1. <a name="core-device-allow-s3-bucket-access-console-intro-1"></a>Allow the core device to access component artifacts in the S3 bucket.

   <a name="core-device-allow-s3-bucket-access-console-intro-2"></a>Each core device has a [core device IAM role](device-service-role.md) that allows it to interact with AWS IoT and send logs to the AWS Cloud. This device role doesn't allow access to S3 buckets by default, so you must create and attach a policy that allows the core device to retrieve component artifacts from the S3 bucket.

   <a name="core-device-allow-s3-bucket-access-console-intro-3"></a>If your device's role already allows access to the S3 bucket, you can skip this step. Otherwise, create an IAM policy that allows access and attach it to the role, as follows:

   1. <a name="core-device-allow-s3-bucket-access-console-step-1"></a>In the [IAM console](https://console.aws.amazon.com/iam) navigation menu, choose **Policies**, and then choose **Create policy**.

   1. On the **JSON** tab, replace the placeholder content with the following policy. Replace {{greengrass-component-artifacts-us-west-2-123456789012}} with the name of the S3 bucket where the GDK CLI uploaded the component's artifacts.

      For example, if you specified **greengrass-component-artifacts** and **us-west-2** in the GDK CLI configuration file, and your AWS account ID is **123456789012**, the GDK CLI uses the S3 bucket named `greengrass-component-artifacts-us-west-2-123456789012`.

------
#### [ JSON ]

****

      ```
      {
        "Version":"2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": [
              "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::{{greengrass-component-artifacts-us-west-2-123456789012}}/*"
          }
        ]
      }
      ```

------

   1. <a name="core-device-allow-s3-bucket-access-console-step-3"></a>Choose **Next**.

   1. <a name="core-device-allow-s3-bucket-access-console-step-4"></a>In the **Policy details section**, for **Name**, enter **MyGreengrassV2ComponentArtifactPolicy**.

   1. <a name="core-device-allow-s3-bucket-access-console-step-5"></a>Choose **Create policy**.

   1. <a name="core-device-allow-s3-bucket-access-console-step-6"></a>In the [IAM console](https://console.aws.amazon.com/iam) navigation menu, choose **Role**, and then choose the name of the role for the core device. You specified this role name when you installed the AWS IoT Greengrass Core software. If you did not specify a name, the default is `GreengrassV2TokenExchangeRole`.

   1. <a name="core-device-allow-s3-bucket-access-console-step-7"></a>Under **Permissions**, choose **Add permissions**, then choose **Attach policies**.

   1. <a name="core-device-allow-s3-bucket-access-console-step-8"></a>On the **Add permissions** page, select the check box next to the `MyGreengrassV2ComponentArtifactPolicy` policy that you created, and then choose **Add permissions**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
