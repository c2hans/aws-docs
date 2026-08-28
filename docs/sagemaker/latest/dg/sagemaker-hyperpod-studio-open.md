---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-open.html
---

# Connecting to HyperPod clusters and submitting tasks to clusters
<a name="sagemaker-hyperpod-studio-open"></a>

You can launch machine learning workloads on HyperPod clusters within Amazon SageMaker Studio IDEs. When you launch Studio IDEs on a HyperPod cluster, a set of commands are available to help you get started. You can work on your training scripts, use Docker containers for the training scripts, and submit jobs to the cluster, all from within the Studio IDEs. The following section provides information on how to connect your cluster to Studio IDEs.

In Amazon SageMaker Studio you can navigate to one of your clusters in **HyperPod clusters** (under **Compute**) and view your list of clusters. You can connect your cluster to an IDE listed under **Actions**.

You can also choose your custom file system from the list of options. For information on how to get this set up, see [Setting up HyperPod in Studio](sagemaker-hyperpod-studio-setup.md).

Alternatively, you can create a space and launch an IDE using the AWS CLI. Use the following commands to do so. The following example creates a `Private` `JupyterLab` space for `{{user-profile-name}}` with the `{{fs-id}}` FSx for Lustre file system attached.

1. Create a space using the [`create-space`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html) AWS CLI.

   ```
   aws sagemaker create-space \
   --region {{your-region}} \
   --ownership-settings "OwnerUserProfileName={{user-profile-name}}" \
   --space-sharing-settings "SharingType=Private" \
   --space-settings "AppType=JupyterLab,CustomFileSystems=[{FSxLustreFileSystem={FileSystemId={{fs-id}}}}]"
   ```

1. Create the app using the [`create-app`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-app.html) AWS CLI.

   ```
   aws sagemaker create-app \
   --region {{your-region}} \
   --space-name {{space-name}} \
   --resource-spec '{"ec2InstanceType":"'"{{instance-type}}"'","appEnvironmentArn":"'"{{image-arn}}"'"}'
   ```

Once you have your applications open, you can submit tasks directly to the clusters you are connected to.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
