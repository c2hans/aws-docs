---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-iam-role-overview.html
---

# IAM roles for Amazon ECS
<a name="ecs-iam-role-overview"></a>

An IAM role is an IAM identity that you can create in your account that has specific permissions. In Amazon ECS, you can create roles to grant permissions to Amazon ECS resource such as containers or services.

The roles Amazon ECS requires depend on the task definition launch type and the features that you use. Use the following table to determine which IAM roles you need for Amazon ECS.

| Role | Definition | When required | More information |
| --- | --- | --- | --- |
| Task execution role | This role allows Amazon ECS to use other AWS services on your behalf. | Your task is hosted on AWS Fargate or on external instances and:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-iam-role-overview.html)<br />Your task is hosted on either AWS Fargate or Amazon EC2 instances and:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-iam-role-overview.html) | [Amazon ECS task execution IAM role](task_execution_IAM_role.md) |
| Task role | This role allows your application code (on the container) to use other AWS services. | Your application accesses other AWS services, such as Amazon S3. | [Amazon ECS task IAM role](task-iam-roles.md) |
| Container instance role | This role allows your EC2 instances or external instances to register with the cluster. | Your task is hosted on Amazon EC2 instances or an external instance. | [Amazon ECS container instance IAM role](instance_IAM_role.md) |
| Amazon ECS Anywhere role | This role allows your external instances to access AWS APIs. | Your task is hosted on external instances. | [Amazon ECS Anywhere IAM role](iam-role-ecsanywhere.md) |
| Amazon ECS infrastructure for load balancers role | This role allows Amazon ECS to manage load balancer resources in your clusters on your behalf for blue/green deployments. | You want to use Amazon ECS blue/green deployments. | [Amazon ECS infrastructure IAM role for load balancers](AmazonECSInfrastructureRolePolicyForLoadBalancers.md) |
| Amazon ECS CodeDeploy role | This role allows CodeDeploy to make updates to your services. | You use the CodeDeploy blue/green deployment type to deploy services. | [Amazon ECS CodeDeploy IAM Role](codedeploy_IAM_role.md) |
| Amazon ECS EventBridge role | This role allows EventBridge to make updates to your services. | You use the EventBridge rules and targets to schedule your tasks. | [Amazon ECS EventBridge IAM Role](CWE_IAM_role.md) |
| Amazon ECS infrastructure role | This role allows Amazon ECS to manage infrastructure resources in your clusters.  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-iam-role-overview.html) | [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md) |
| Instance profile | This role allows allows Amazon ECS Managed Instances to assume the infrastructure role securely. | You use Amazon ECS Managed Instances in your clusters. | [Amazon ECS Managed Instances instance profile](managed-instances-instance-profile.md) |
