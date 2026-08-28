---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_EKS.html
---

# Using Amazon ECR Images with Amazon EKS
<a name="ECR_on_EKS"></a>

You can use your Amazon ECR images with Amazon EKS.

When referencing an image from Amazon ECR, you must use the full `registry/repository:tag` naming for the image. For example, `{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com``/{{my-repository}}:{{latest}}`.

## Required IAM permissions
<a name="ECR_on_EKS_iampermissions"></a>

If you have Amazon EKS workloads hosted on managed nodes, self-managed nodes, or AWS Fargate, review the following:
+ Amazon EKS workloads hosted on managed or self-managed nodes: The Amazon EKS worker node IAM role (`NodeInstanceRole`) is required. The Amazon EKS worker node IAM role must contain the following IAM policy permissions for Amazon ECR.

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ecr:BatchCheckLayerAvailability",
                  "ecr:BatchGetImage",
                  "ecr:GetDownloadUrlForLayer",
                  "ecr:GetAuthorizationToken"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

------
**Note**
If you used `eksctl` or the CloudFormation templates in [Getting Started with Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) to create your cluster and worker node groups, these IAM permissions are applied to your worker node IAM role by default.
+ Amazon EKS workloads hosted on AWS Fargate: Use the Fargate pod execution role, which provides your pods permission to pull images from private Amazon ECR repositories. For more information, see [Create a Fargate pod execution role](https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html#fargate-sg-pod-execution-role).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
