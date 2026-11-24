---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-private-install.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure private installation for hybrid nodes

This topic describes how to install hybrid nodes dependencies in a private environment using a VPC endpoint for Amazon S3. This approach is suitable for environments with restricted internet access where hybrid nodes need to download artifacts through private networking only. By using this method, all `nodeadm` artifact downloads will go through your VPC endpoint rather than over the public internet.

## Prerequisites
<a name="_prerequisites"></a>

Before setting up private installation for hybrid nodes, make sure you have completed the following prerequisites:
+ You have network connectivity from your on-premises environment to the AWS Region hosting your Amazon EKS cluster. See [Prepare networking for hybrid nodes](hybrid-nodes-networking.md) for more information.
+ You have a compatible operating system for hybrid nodes installed on your on-premises hosts. See [Prepare operating system for hybrid nodes](hybrid-nodes-os.md) for more information.
+ You have created your Hybrid Nodes IAM role and set up your on-premises credential provider (AWS Systems Manager hybrid activations or AWS IAM Roles Anywhere). See [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md) for more information.
+ You have created your hybrid nodes-enabled Amazon EKS cluster. See [Create an Amazon EKS cluster with hybrid nodes](hybrid-nodes-cluster-create.md) for more information.
+ You have associated your Hybrid Nodes IAM role with Kubernetes Role-Based Access Control (RBAC) permissions. See [Prepare cluster access for hybrid nodes](hybrid-nodes-cluster-prep.md) for more information.
+ You have administrative access to manage VPC resources, security groups, and S3 resources in your AWS account.

## Step 1: Create a security group for the VPC endpoint
<a name="_step_1_create_a_security_group_for_the_vpc_endpoint"></a>

Create a security group that will be used by the S3 VPC endpoint. This security group should only allow inbound and outbound connections within your VPC.

1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.

1. In the navigation pane, choose **Security Groups**.

1. Choose **Create security group**.

1. For **Security group name**, enter a name such as `hybrid-nodes-s3-vpc-endpoint-sg`.

1. For **Description**, enter a description such as `Security group for S3 VPC endpoint used by hybrid nodes`.

1. For **VPC**, select the VPC where your EKS cluster is located.

1. Configure the following rules:

   1.  **Inbound rules**: Add a rule that allows HTTPS traffic (port 443) from your VPC CIDR block.

      1.  **Type**: `HTTPS`

      1.  **Protocol**: `TCP`

      1.  **Port range**: `443`

      1.  **Source**: Your VPC CIDR (for example, `10.0.0.0/16`)

   1.  **Outbound rules**: Add a rule that allows HTTPS traffic (port 443) to your VPC CIDR block.

      1.  **Type**: `HTTPS`

      1.  **Protocol**: `TCP`

      1.  **Port range**: `443`

      1.  **Destination**: Your VPC CIDR (for example, `10.0.0.0/16`)

1. Choose **Create security group**.

## Step 2: Create an Interface VPC endpoint for Amazon S3
<a name="_step_2_create_an_interface_vpc_endpoint_for_amazon_s3"></a>

Create a VPC endpoint for Amazon S3 to enable private access to S3 resources from your VPC.

1. In the Amazon VPC console, in the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. For **Service category**, select ** AWS services**.

1. For **Service**, search for and select `com.amazonaws.{{REGION}}.s3`. Replace {{REGION}} with your AWS Region (for example, `us-west-2`).

1. For **VPC**, select the same VPC where your EKS cluster is located.

1. For **Route tables**, select the route tables associated with the subnets where your hybrid nodes will access S3.

1. For **Policy**, you can select **Full access** for simplicity, or create a custom policy that restricts access to specific S3 buckets if needed.

1. For **Security groups**, select the security group you created in Step 1.

1. Choose **Create endpoint**.

1. Note the VPC endpoint ID (it will look like `vpce-12345678`) as you will need it in Step 5.

## Step 3: Add outbound rule for Amazon S3 prefix list
<a name="_step_3_add_outbound_rule_for_amazon_s3_prefix_list"></a>

Modify the security group created in Step 1 to allow outbound traffic to the Amazon S3 prefix list for your region.

1. In the Amazon VPC console, navigate to your security group created in Step 1.

1. Choose the **Outbound rules** tab.

1. Choose **Edit outbound rules**.

1. Choose **Add rule** and configure the following:

   1.  **Type**: `HTTPS`

   1.  **Protocol**: `TCP`

   1.  **Port range**: `443`

   1.  **Destination**: Select **Prefix list** and then search for `com.amazonaws.{{REGION}}.s3`. For example, if you are in the `us-west-2` region, the prefix list ID will be `pl-68a54001`.

1. Choose **Save rules**.

**Note**
The prefix list ID varies by region. You can find the correct prefix list ID by searching for the S3 service endpoint in your region. Only the endpoint for your current region will be available in the search results.

## Step 4: Create an S3 bucket for nodeadm artifacts
<a name="_step_4_create_an_s3_bucket_for_nodeadm_artifacts"></a>

Create an S3 bucket that will store the `nodeadm` artifacts for private installation.

1. Open the Amazon S3 console at https://console.aws.amazon.com/s3/.

1. Choose **Create bucket**.

1. For **Bucket name**, enter a unique name such as ` {{YOUR-ACCOUNT-ID}}-hybrid-nodes-artifacts-{{REGION}} `.

1. For ** AWS Region**, select the same region as your EKS cluster.

1. Leave the default settings for **Block Public Access settings for this bucket** (all options should be enabled for security).

1. Choose **Create bucket**.

1. Note the bucket name as you will need it for subsequent steps.

## Step 5: Create a bucket policy for VPC endpoint access
<a name="_step_5_create_a_bucket_policy_for_vpc_endpoint_access"></a>

Create a bucket policy that restricts access to the S3 bucket to only come through the VPC endpoint you created.

1. In the Amazon S3 console, navigate to your bucket created in Step 4.

1. Choose the **Permissions** tab.

1. In the **Bucket policy** section, choose **Edit**.

1. Enter the following policy, replacing the placeholders:

   1. Replace {{BUCKET\_NAME}} with your bucket name from Step 4.

   1. Replace {{VPC\_ENDPOINT\_ID}} with the VPC endpoint ID from Step 2.

      ```json
      {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Sid": "Access-to-specific-VPCE-only",
                  "Effect": "Deny",
                  "Principal": "*",
                  "Action": "s3:GetObject",
                  "Resource": "arn:aws:s3:::BUCKET_NAME/*",
                  "Condition": {
                      "StringNotEquals": {
                          "aws:SourceVpce": "VPC_ENDPOINT_ID"
                      }
                  }
              }
          ]
      }
      ```

1. Choose **Save changes**.

## Step 6: Sync nodeadm artifacts to your private bucket
<a name="_step_6_sync_nodeadm_artifacts_to_your_private_bucket"></a>

Use the `nodeadm sync-artifacts` command to download and upload the required artifacts to your private S3 bucket. This command must be run from an environment that has internet access and appropriate AWS credentials.

**Important**
This step requires internet access to download the artifacts from the public Amazon EKS Hybrid Nodes distribution. Run this command from a machine with internet access and AWS CLI configured with permissions to write to your S3 bucket.

1. Install the `nodeadm` CLI on a machine with internet access. Download the binary using the commands from [Step 1](hybrid-nodes-join.md).

1. Run the following command to sync artifacts to your private bucket:

   ```bash
   ./nodeadm sync-artifacts \
       --bucket {{BUCKET_NAME}} \
       --key-prefix artifacts \
       --kubernetes-version {{K8S_VERSION}} \
       --credential-provider {{CREDS_PROVIDER}}
   ```

   Replace the following values: \* {{BUCKET\_NAME}} with your bucket name from Step 4 \* {{K8S\_VERSION}} with the Kubernetes minor version of your Amazon EKS cluster (for example, `1.31`) \* {{CREDS\_PROVIDER}} with your credential provider (`ssm` or `iam-ra`)

1. The command will output a manifest file path. Note this path as you will need it for Step 7.

## Step 7: Install hybrid nodes dependencies using the private artifacts
<a name="_step_7_install_hybrid_nodes_dependencies_using_the_private_artifacts"></a>

Use the manifest file generated in Step 6 to install the hybrid nodes dependencies on your on-premises hosts.

**Important**
The hybrid nodes CLI (`nodeadm`) must be run with a user that has sudo/root access on your host.

1. Copy the `nodeadm` binary and the manifest file generated in Step 6 to each on-premises host where you want to install hybrid nodes dependencies.

1. On each host, run the following command:

   ```bash
   sudo ./nodeadm install --source file://{{MANIFEST_FILE_PATH}}
   ```

   Replace {{MANIFEST\_FILE\_PATH}} with the path to the manifest file from Step 6.

1. Verify that the installation completed successfully by checking the output for any error messages.

## Next steps
<a name="_next_steps"></a>

After completing the private installation, you can proceed to connect your hybrid nodes to your Amazon EKS cluster following the steps in [Step 3: Connect hybrid nodes to your cluster](hybrid-nodes-join.md).

## Troubleshooting
<a name="_troubleshooting"></a>

If you encounter issues during the private installation:
+ Verify that your VPC endpoint is correctly configured and accessible from your hybrid nodes.
+ Check that your security group rules allow the necessary traffic flows.
+ Ensure that your S3 bucket policy correctly references your VPC endpoint ID.
+ Verify that your hybrid nodes have the necessary IAM permissions to access the S3 bucket through the VPC endpoint.
+ Review the `nodeadm` logs for specific error messages that can help identify the issue.

For additional troubleshooting information, see [Troubleshooting hybrid nodes](hybrid-nodes-troubleshooting.md).
