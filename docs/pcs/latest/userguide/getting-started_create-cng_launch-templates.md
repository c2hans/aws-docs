---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-cng_launch-templates.html
---

# Create launch templates for AWS PCS
<a name="getting-started_create-cng_launch-templates"></a>

 When you create a compute node group, you provide an EC2 launch template that AWS PCS uses to configure EC2 instances it launches. The launch template defines settings such as security groups and the SSH key pair for access. File system mounting is handled separately through node lifecycle actions, which you configure when you create the node group (see [Create compute node group for login nodes](getting-started_create-cng_login-nodes.md) and [Create compute node group for jobs](getting-started_create-cng_workers.md)).

 In this step, one CloudFormation template will be used to create two EC2 launch templates. One template will be used to create login nodes, and the other will be used to create compute nodes. The key difference between them is that the login nodes can be configured to allow inbound SSH access.

## Access the CloudFormation template
<a name="getting-started_create-cng_launch-templates_get-cfn-template"></a>

 Use the following URL to download the CloudFormation template, then upload the template in the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home#/stacks/create) to create a new CloudFormation stack. For more information, see [Using the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console.html) in the *AWS CloudFormation User Guide*.

```
https://aws-hpc-recipes.s3.amazonaws.com/main/recipes/pcs/getting_started/assets/pcs-lt-efs-fsxl.yaml
```

## Use the CloudFormation template to create EC2 launch templates
<a name="getting-started_create-cng_launch-templates_use-cfn-template"></a>

 Use the following procedure to complete the CloudFormation template in the CloudFormation console
+ Under **Provide a stack name**:
  + Under **Stack name**, enter `getstarted-lt`.
+ Under **Parameters**:
  + Under **Security**
    + For **VpcSecurityGroupId**, select the security group named `default` in your cluster VPC.
    + For **ClusterSecurityGroupId**, select the group named `cluster-getstarted-sg`
    + For **SshSecurityGroupId**, select the group named `inbound-ssh-getstarted-sg`
    + For **SshKeyName**, select your preferred SSH key pair.
+ Choose **Next**, then choose **Next** again.
+ Choose **Submit**.

 Monitor the status of the CloudFormation stack. When it reaches `CREATE_COMPLETE` the launch template is ready to be used.

**Note**
To see all the resources the CloudFormation template created, open the [CloudFormation console](https://console.aws.amazon.com/cloudformation). Choose the `getstarted-lt` stack and then choose the **Resources** tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
