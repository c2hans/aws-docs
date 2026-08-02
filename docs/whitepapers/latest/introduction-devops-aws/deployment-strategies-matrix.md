---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies-matrix.html
---

# Deployment strategies matrix
<a name="deployment-strategies-matrix"></a>

 The following matrix lists the supported deployment strategies for [Amazon Elastic Container Service](https://aws.amazon.com/ecs) (Amazon ECS), AWS Lambda, and Amazon EC2/on-premises.
+ Amazon ECS is a fully managed orchestration service.
+ AWS Lambda lets you run code without provisioning or managing servers.
+ Amazon EC2 enables you to run secure, resizable compute capacity in the cloud.

| Deployment strategy | Amazon ECS | AWS Lambda | Amazon EC2/on-premises |
| --- | --- | --- | --- |
| In-place | ✓ | ✓ | ✓ |
| Blue/green | ✓ | ✓ | ✓\* |
| Canary | ✓ | ✓ | X |
| Linear | ✓ | ✓ | X |
| All-at-once | ✓ | ✓ | X |

**Note**
Blue/green deployment with EC2/on-premises works only with EC2 instances.
