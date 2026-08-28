---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/upload-first-component.html
---

# Step 5: Create your component in the AWS IoT Greengrass service
<a name="upload-first-component"></a>

When you finish developing a component on your core device, you can upload it to the AWS IoT Greengrass service in the AWS Cloud. You can also directly create the component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass). AWS IoT Greengrass provides a component management service that hosts your components so that you can deploy them to individual devices or fleets of devices. To upload a component to the AWS IoT Greengrass service, you complete the following steps:
+ Upload component artifacts to an S3 bucket.
+ Add each artifact's Amazon Simple Storage Service (Amazon S3) URI to the component recipe.
+ Create a component in AWS IoT Greengrass from the component recipe.

In this section, you complete these steps on your Greengrass core device to upload your Hello World component to the AWS IoT Greengrass service.

## Create your component in AWS IoT Greengrass (console)
<a name="upload-first-component-console"></a>

1. Use an S3 bucket in your AWS account to host AWS IoT Greengrass component artifacts. When you deploy the component to a core device, the device downloads the component's artifacts from the bucket.

   You can use an existing S3 bucket, or you can create a new bucket.

   1. In the [Amazon S3 console](https://console.aws.amazon.com/s3), under **Buckets**, choose **Create bucket**.

   1. For **Bucket name**, enter a unique bucket name. For example, you can use **greengrass-component-artifacts-{{region}}-{{123456789012}}**. Replace {{123456789012}} with your AWS account ID and {{region}} with the AWS Region that you use for this tutorial.

   1. For **AWS region**, select the AWS Region that you use for this tutorial.

   1. Choose **Create bucket**.

   1. Under **Buckets**, choose the bucket that you created, upload the `hello_world.py` script to the `artifacts/com.example.HelloWorld/1.0.0` folder in the bucket. For information about uploading objects to S3 buckets, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the *Amazon Simple Storage Service User Guide*.

   1. Copy the S3 URI of the `hello_world.py` object in the S3 bucket. This URI should look similar to the following example. Replace amzn-s3-demo-bucket with the name of the S3 bucket.

      ```
      s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py
      ```

1. <a name="core-device-allow-s3-bucket-access-console"></a><a name="core-device-allow-s3-bucket-access-console-intro-1"></a>Allow the core device to access component artifacts in the S3 bucket.

   <a name="core-device-allow-s3-bucket-access-console-intro-2"></a>Each core device has a [core device IAM role](device-service-role.md) that allows it to interact with AWS IoT and send logs to the AWS Cloud. This device role doesn't allow access to S3 buckets by default, so you must create and attach a policy that allows the core device to retrieve component artifacts from the S3 bucket.

   <a name="core-device-allow-s3-bucket-access-console-intro-3"></a>If your device's role already allows access to the S3 bucket, you can skip this step. Otherwise, create an IAM policy that allows access and attach it to the role, as follows:

   1. <a name="core-device-allow-s3-bucket-access-console-step-1"></a>In the [IAM console](https://console.aws.amazon.com/iam) navigation menu, choose **Policies**, and then choose **Create policy**.

   1. <a name="core-device-allow-s3-bucket-access-console-step-2"></a>On the **JSON** tab, replace the placeholder content with the following policy. Replace amzn-s3-demo-bucket with the name of the S3 bucket that contains component artifacts for the core device to download.

      ```
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": [
              "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
          }
        ]
      }
      ```

   1. <a name="core-device-allow-s3-bucket-access-console-step-3"></a>Choose **Next**.

   1. <a name="core-device-allow-s3-bucket-access-console-step-4"></a>In the **Policy details section**, for **Name**, enter **MyGreengrassV2ComponentArtifactPolicy**.

   1. <a name="core-device-allow-s3-bucket-access-console-step-5"></a>Choose **Create policy**.

   1. <a name="core-device-allow-s3-bucket-access-console-step-6"></a>In the [IAM console](https://console.aws.amazon.com/iam) navigation menu, choose **Role**, and then choose the name of the role for the core device. You specified this role name when you installed the AWS IoT Greengrass Core software. If you did not specify a name, the default is `GreengrassV2TokenExchangeRole`.

   1. <a name="core-device-allow-s3-bucket-access-console-step-7"></a>Under **Permissions**, choose **Add permissions**, then choose **Attach policies**.

   1. <a name="core-device-allow-s3-bucket-access-console-step-8"></a>On the **Add permissions** page, select the check box next to the `MyGreengrassV2ComponentArtifactPolicy` policy that you created, and then choose **Add permissions**.

1. Use the component recipe to create a component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass).

   1. In the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass) navigation menu, choose **Components**, and then choose **Create component**.

   1. Under **Component information**, choose **Enter recipe as JSON**. The placeholder recipe should look similar to the following example.

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
              "Run": "python3 -u {artifacts:path}/hello_world.py \"{configuration:/Message}\""
            },
            "Artifacts": [
              {
                "URI": "s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py"
              }
            ]
          },
          {
            "Platform": {
              "os": "windows"
            },
            "Lifecycle": {
              "Run": "py -3 -u {artifacts:path}/hello_world.py \"{configuration:/Message}\""
            },
            "Artifacts": [
              {
                "URI": "s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py"
              }
            ]
          }
        ]
      }
      ```

   1. Replace the placeholder URI in each `Artifacts` section with S3 URI of your `hello_world.py` object.

   1. Choose **Create component**.

   1. On the **com.example.HelloWorld** component page, verify that the **Status** of the component is **Deployable**.

## Create your component in AWS IoT Greengrass (AWS CLI)
<a name="upload-first-component-cli"></a>

**To upload your Hello World component**

1. Use an S3 bucket in your AWS account to host AWS IoT Greengrass component artifacts. When you deploy the component to a core device, the device downloads the component's artifacts from the bucket.

   You can use an existing S3 bucket, or run the following command to create a bucket. This command creates a bucket with your AWS account ID and AWS Region to form a unique bucket name. Replace {{123456789012}} with your AWS account ID and {{region}} with the AWS Region that you use for this tutorial.

   ```
   aws s3 mb s3://greengrass-component-artifacts-{{123456789012}}-{{region}}
   ```

   The command outputs the following information if the request succeeds.

   ```
   make_bucket: greengrass-component-artifacts-{{123456789012}}-{{region}}
   ```

1. <a name="core-device-allow-s3-bucket-access-cli"></a>Allow the core device to access component artifacts in the S3 bucket.

   Each core device has a [core device IAM role](device-service-role.md) that allows it to interact with AWS IoT and send logs to the AWS Cloud. This device role doesn't allow access to S3 buckets by default, so you must create and attach a policy that allows the core device to retrieve component artifacts from the S3 bucket.

   If the core device's role already allows access to the S3 bucket, you can skip this step. Otherwise, create an IAM policy that allows access and attach it to the role, as follows:

   1. Create a file called `component-artifact-policy.json` and copy the following JSON into the file. This policy allows access to all files in an S3 bucket. Replace amzn-s3-demo-bucket with the name of the S3 bucket.

      ```
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": [
              "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
          }
        ]
      }
      ```

   1. Run the following command to create the policy from the policy document in `component-artifact-policy.json`.

------
#### [ Linux or Unix ]

      ```
      aws iam create-policy \\
        --policy-name {{MyGreengrassV2ComponentArtifactPolicy}} \\
        --policy-document file://component-artifact-policy.json
      ```

------
#### [ Windows Command Prompt (CMD) ]

      ```
      aws iam create-policy ^
        --policy-name {{MyGreengrassV2ComponentArtifactPolicy}} ^
        --policy-document file://component-artifact-policy.json
      ```

------
#### [ PowerShell ]

      ```
      aws iam create-policy `
        --policy-name {{MyGreengrassV2ComponentArtifactPolicy}} `
        --policy-document file://component-artifact-policy.json
      ```

------

      Copy the policy Amazon Resource Name (ARN) from the policy metadata in the output. You use this ARN to attach this policy to the core device role in the next step.

   1. Run the following command to attach the policy to the core device role. Replace {{GreengrassV2TokenExchangeRole}} with the name of the role for the core device. You specified this role name when you installed the AWS IoT Greengrass Core software. Replace the policy ARN with the ARN from the previous step.

------
#### [ Linux or Unix ]

      ```
      aws iam attach-role-policy \\
        --role-name {{GreengrassV2TokenExchangeRole}} \\
        --policy-arn arn:aws:iam::{{123456789012}}:policy/{{MyGreengrassV2ComponentArtifactPolicy}}
      ```

------
#### [ Windows Command Prompt (CMD) ]

      ```
      aws iam attach-role-policy ^
        --role-name {{GreengrassV2TokenExchangeRole}} ^
        --policy-arn arn:aws:iam::{{123456789012}}:policy/{{MyGreengrassV2ComponentArtifactPolicy}}
      ```

------
#### [ PowerShell ]

      ```
      aws iam attach-role-policy `
        --role-name {{GreengrassV2TokenExchangeRole}} `
        --policy-arn arn:aws:iam::{{123456789012}}:policy/{{MyGreengrassV2ComponentArtifactPolicy}}
      ```

------

      If the command has no output, it succeeded. The core device can now access artifacts that you upload to this S3 bucket.

1. Upload the Hello World Python script artifact to the S3 bucket.

   Run the following command to upload the script to the same path in the bucket where the script exists on your AWS IoT Greengrass core. Replace amzn-s3-demo-bucket with the name of the S3 bucket.

------
#### [ Linux or Unix ]

   ```
   aws s3 cp \
     artifacts/com.example.HelloWorld/1.0.0/hello_world.py \
     s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   aws s3 cp ^
     artifacts/com.example.HelloWorld/1.0.0/hello_world.py ^
     s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py
   ```

------
#### [ PowerShell ]

   ```
   aws s3 cp `
     artifacts/com.example.HelloWorld/1.0.0/hello_world.py `
     s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py
   ```

------

   The command outputs a line that starts with `upload:` if the request succeeds.

1. Add the artifact's Amazon S3 URI to the component recipe.

   The Amazon S3 URI is composed of the bucket name and the path to the artifact object in the bucket. Your script artifact's Amazon S3 URI is the URI that you upload the artifact to in the previous step. This URI should look similar to the following example. Replace amzn-s3-demo-bucket with the name of the S3 bucket.

   ```
   s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py
   ```

   To add the artifact to the recipe, add a list of `Artifacts` that contains a structure with the Amazon S3 URI.

------
#### [ JSON ]

   ```
   "Artifacts": [
     {
       "URI": "s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py"
     }
   ]
   ```

   Open the recipe file in a text editor.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano recipes/com.example.HelloWorld-1.0.0.json
   ```

   Add the artifact to the recipe. Your recipe file should look similar to the following example.

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
           "Run": "python3 -u {artifacts:path}/hello_world.py \"{configuration:/Message}\""
         },
         "Artifacts": [
           {
             "URI": "s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py"
           }
         ]
       },
       {
         "Platform": {
           "os": "windows"
         },
         "Lifecycle": {
           "Run": "py -3 -u {artifacts:path}/hello_world.py \"{configuration:/Message}\""
         },
         "Artifacts": [
           {
             "URI": "s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py"
           }
         ]
       }
     ]
   }
   ```

------
#### [ YAML ]

   ```
   Artifacts:
     - URI: s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py
   ```

   Open the recipe file in a text editor.

   <a name="nano-command-intro"></a>For example, on a Linux-based system, you can run the following command to use GNU nano to create the file.

   ```
   nano recipes/com.example.HelloWorld-1.0.0.yaml
   ```

   Add the artifact to the recipe. Your recipe file should look similar to the following example.

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
         Run: |
           python3 -u {artifacts:path}/hello_world.py "{configuration:/Message}"
       Artifacts:
         - URI: s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py
     - Platform:
         os: windows
       Lifecycle:
         Run: |
           py -3 -u {artifacts:path}/hello_world.py "{configuration:/Message}"
       Artifacts:
         - URI: s3://amzn-s3-demo-bucket/artifacts/com.example.HelloWorld/1.0.0/hello_world.py
   ```

------

1. Create a component resource in AWS IoT Greengrass from the recipe. Run the following command to create the component from the recipe, which you provide as a binary file.

------
#### [ JSON ]

   ```
   aws greengrassv2 create-component-version --inline-recipe fileb://recipes/com.example.HelloWorld-1.0.0.json
   ```

------
#### [ YAML ]

   ```
   aws greengrassv2 create-component-version --inline-recipe fileb://recipes/com.example.HelloWorld-1.0.0.yaml
   ```

------

   The response looks similar to the following example if the request succeeds.

   ```
   {
     "arn": "arn:aws:greengrass:{{region}}:{{123456789012}}:components:com.example.HelloWorld:versions:1.0.0",
     "componentName": "com.example.HelloWorld",
     "componentVersion": "1.0.0",
     "creationTimestamp": "Mon Nov 30 09:04:05 UTC 2020",
     "status": {
       "componentState": "REQUESTED",
       "message": "NONE",
       "errors": {}
     }
   }
   ```

   Copy the `arn` from the output to check the state of the component in the next step.
**Note**
You can also see your Hello World component in the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass) on the **Components** page.

1. Verify that the component creates and is ready to be deployed. When you create a component, its state is `REQUESTED`. Then, AWS IoT Greengrass validates that the component is deployable. You can run the following command to query the component status and verify that your component is deployable. Replace the `arn` with the ARN from the previous step.

   ```
   aws greengrassv2 describe-component --arn "arn:aws:greengrass:{{region}}:{{123456789012}}:components:com.example.HelloWorld:versions:1.0.0"
   ```

   If the component validates, the response indicates that the component state is `DEPLOYABLE`.

   ```
   {
     "arn": "arn:aws:greengrass:{{region}}:{{123456789012}}:components:com.example.HelloWorld:versions:1.0.0",
     "componentName": "com.example.HelloWorld",
     "componentVersion": "1.0.0",
     "creationTimestamp": "2020-11-30T18:04:05.823Z",
     "publisher": "Amazon",
     "description": "My first Greengrass component.",
     "status": {
       "componentState": "DEPLOYABLE",
       "message": "NONE",
       "errors": {}
     },
     "platforms": [
       {
         "os": "linux",
         "architecture": "all"
       }
     ]
   }
   ```

Your Hello World component is now available in AWS IoT Greengrass. You can deploy it back to this Greengrass core device or to other core devices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
