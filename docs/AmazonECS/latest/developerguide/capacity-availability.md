---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-availability.html
---

# Amazon ECS Auto scaling and capacity management best practices
<a name="capacity-availability"></a>

You can run containerized application workloads of all sizes on Amazon ECS. This includes minimal testing environments and large production environments that operate at a global scale.

With Amazon ECS, like all AWS services, you pay only for what you use. When you architect your application appropriately, you can save costs by consuming only the resources that you need when you need them.

The following recommendations show you how to run your Amazon ECS workloads to meet your service-level objectives while operating cost-effectively.

**Topics**
+ [Determining the task size for Amazon ECS](capacity-tasksize-best-practice.md)
+ [Optimizing Amazon ECS service auto scaling](capacity-autoscaling-best-practice.md)
+ [Amazon ECS capacity and availability](capacity-availability-best-practice.md)
+ [Amazon ECS cluster capacity](capacity-cluster-best-practice.md)
+ [Choosing Fargate task sizes for Amazon ECS](fargate-task-size-best-practice.md)
+ [Speeding up Amazon ECS cluster capacity provisioning with capacity providers on Amazon EC2](capacity-cluster-speed-up-ec2-best-practice.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
