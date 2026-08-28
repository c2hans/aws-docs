---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/push-array-image.html
---

# Push your image to Amazon ECR
<a name="push-array-image"></a>

Now that you built and tested your Docker container, push it to an image repository. This example uses Amazon ECR, but you can use another registry, such as DockerHub.

1. Create an Amazon ECR image repository to store your container image. This example only uses the AWS CLI, but you can also use the AWS Management Console. For more information, see [Creating a Repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) in the *Amazon Elastic Container Registry User Guide*.

   ```
   $ aws ecr create-repository --repository-name print-color
   ```

1. Tag your `print-color` image with your Amazon ECR repository URI that was returned from the previous step.

   ```
   $ docker tag print-color {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/print-color
   ```

1. Log in to your Amazon ECR registry. For more information, see [Registry Authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth) in the *Amazon Elastic Container Registry User Guide*.

   ```
   $ aws ecr get-login-password \
       --region {{region}} | docker login \
       --username AWS \
       --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com
   ```

1. Push your image to Amazon ECR.

   ```
   $ docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/print-color
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
