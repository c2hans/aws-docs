---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-parameters.html
---

# ECS architecture template parameters
<a name="ecs-parameters"></a>

|  **Parameter**  |  **Default**  |  **Description**  |
| --- | --- | --- |
|  **Admin Email**  | <Requires input> | The email address of the admin user for the Admin UI. Must be a valid email address (7-100 characters). This email will receive the initial login credentials for the administrative interface. |
|  **Deployment Size**  | small | T-shirt sizing for ECS Fargate deployment configuration. Options: small, medium, large, xlarge. This determines the number of ECS tasks, CPU, and memory allocation. Refer to [sizing guidance](choosing-deployment-architecture.md) for details. |
|  **Origin Override Header**  |  *<Optional input>*  | HTTP header name used to override the origin destination for image requests. Must be a valid HTTP header name or empty. Useful for routing requests to different origins based on custom headers. |
|  **Cors Origin Parameter**  |  *<Optional input>*  | If you would like to specify an origin to use for CORS, specify an origin value here. We recommend specifying an origin (for example, https://example.domain) to restrict cross-site access to your API. Leave empty to default to wildcard (\*). |

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 20 minutes.
