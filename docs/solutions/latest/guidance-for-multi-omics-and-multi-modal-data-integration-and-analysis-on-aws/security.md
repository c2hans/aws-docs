---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/security.html
---

# Security
<a name="security"></a>

 This guidance is preconfigured with all of the IAM policies and roles necessary to run the guidance with least privileges.

 When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This shared model can reduce your operational burden as AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the services operate. For more information about security on AWS, visit the [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

 AWS Identity and Access Management (IAM) roles allow you to secure jobs and crawlers running in AWS Glue, and restrict access to the data catalog, the data lake bucket, and the notebook instance. All of the IAM roles in this guidance have been defined with least privileges. For details about roles and permissions used in this guidance, refer to [Roles and permissions](roles-and-permissions.md).
