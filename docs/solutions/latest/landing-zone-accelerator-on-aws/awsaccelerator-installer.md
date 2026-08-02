---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/awsaccelerator-installer.html
---

# Installer pipeline
<a name="awsaccelerator-installer"></a>

This pipeline runs the following stages:

1.  **Source** - The Landing Zone Accelerator on AWS source code from the AWS Solutions [GitHub](https://github.com/awslabs/landing-zone-accelerator-on-aws) repository

1.  **Install** - A CodeBuild project is used to run the Landing Zone Accelerator on AWS pipeline CDK project, resulting in the deployment of the `AWSAccelerator-PipelineStack`

**Note**
The Landing Zone Accelerator on AWS Installer and Core pipelines are separate by design. The functionality of the `AWSAccelerator-InstallerStack` has been minimized to purely support deployment of the Core pipeline, `AWSAccelerator-Pipeline`. This will allow you to update your version of the Landing Zone Accelerator on AWS by updating a single parameter through the AWS CloudFormation update stack console. See [Update the solution](update-the-solution.md) for more information.
