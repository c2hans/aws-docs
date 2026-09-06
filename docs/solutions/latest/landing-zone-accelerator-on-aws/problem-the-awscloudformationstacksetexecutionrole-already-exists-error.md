---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-the-awscloudformationstacksetexecutionrole-already-exists-error.html
---

# Problem: "AWSCloudFormationStackSetExecutionRole already exists" error
<a name="problem-the-awscloudformationstacksetexecutionrole-already-exists-error"></a>

When creating AWS CloudFormation [StackSets](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.CloudFormationStackSetConfig.html) using Landing Zone Accelerator on AWS, the solution attempts to create IAM roles required for deploying StackSets with [self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html#prereqs-self-managed-permissions). Specifically, the two required roles are:
+  **AWSCloudFormationStackSetAdministrationRole** - This role is deployed to the Management account.
+  **AWSCloudFormationStackSetExecutionRole** - This role is deployed to all accounts.

When deploying Landing Zone Accelerator on AWS to an environment where these roles already exist, the pipeline will fail with the `AWSCloudFormationStackSetAdministrationRole already exists` or `AWSCloudFormationStackSetExecutionRole already exists` error.

## Resolution
<a name="resolution-10"></a>

1.  [Delete](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#roles-managingrole-deleting-console) the `AWSCloudFormationStackSetAdministrationRole` IAM role from the Management account.

1. Delete the `AWSCloudFormationStackSetExecutionRole` IAM role from all accounts.

1. Retry the failed pipeline stage.
