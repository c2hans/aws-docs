---
source_url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-upload.html
---

# Upload your alert manager configuration file to Amazon Managed Service for Prometheus
<a name="AMP-alertmanager-upload"></a>

Once you know what you want in your Alert manager configuration file, you can create and edit it within the console, or you can upload an existing file with the Amazon Managed Service for Prometheus console or AWS CLI.

**Note**
If you are running an Amazon EKS cluster, you can also upload an Alert manager configuration file using [AWS Controllers for Kubernetes](integrating-ack.md).

**To use the Amazon Managed Service for Prometheus console to edit or replace your alert manager configuration**

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home).

1. In the upper left corner of the page, choose the menu icon, and then choose **All workspaces**.

1. Choose the workspace ID of the workspace, and then choose the **Alert manager** tab.

1. If the workspace doesn't already have an alert manager definition, choose **Add definition**.
**Note**
If the workspace has an alert manager definition that you want to replace, choose **Modify** instead.

1. Choose **Choose file**, select the alert manager definition file, and choose **Continue**.
**Note**
Alternately, you can create a new file and edit it directly in the console, by choosing the **Create definition** option. This will create a sample default configuration that you edit before uploading.

**To use the AWS CLI to upload an alert manager configuration to a workspace for the first time**

1. Base64 encode the contents of your alert manager file. On Linux, you can use the following command:

   ```
   base64 {{input-file}} {{output-file}}
   ```

   On macOS, you can use the following command:

   ```
   openssl base64 {{input-file}} {{output-file}}
   ```

1. To upload the file, enter one of the following commands.

   On AWS CLI version 2, enter:

   ```
   aws amp create-alert-manager-definition --data file://{{path_to_base_64_output_file}} --workspace-id {{my-workspace-id}} --region {{region}}
   ```

   On AWS CLI version 1, enter:

   ```
   aws amp create-alert-manager-definition --data fileb://{{path_to_base_64_output_file}} --workspace-id {{my-workspace-id}} --region {{region}}
   ```

1. It takes a few seconds for your alert manager configuration to become active. To check the status, enter the following command:

   ```
   aws amp describe-alert-manager-definition --workspace-id {{workspace_id}} --region {{region}}
   ```

   If the `status` is `ACTIVE`, your new alert manager definition has taken effect.

**To use the AWS CLI to replace a workspace's alert manager configuration with a new one**

1. Base64 encode the contents of your alert manager file. On Linux, you can use the following command:

   ```
   base64 {{input-file}} {{output-file}}
   ```

   On macOS, you can use the following command:

   ```
   openssl base64 {{input-file}} {{output-file}}
   ```

1. To upload the file, enter one of the following commands.

   On AWS CLI version 2, enter:

   ```
   aws amp put-alert-manager-definition --data file://{{path_to_base_64_output_file}} --workspace-id {{my-workspace-id}} --region {{region}}
   ```

   On AWS CLI version 1, enter:

   ```
   aws amp put-alert-manager-definition --data file://{{path_to_base_64_output_file}} --workspace-id {{my-workspace-id}} --region {{region}}
   ```

1. It takes a few seconds for your new alert manager configuration to become active. To check the status, enter the following command:

   ```
   aws amp describe-alert-manager-definition --workspace-id {{workspace_id}} --region {{region}}
   ```

   If the `status` is `ACTIVE`, your new alert manager definition has taken effect. Until that time, your previous alert manager configuration is still active.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
