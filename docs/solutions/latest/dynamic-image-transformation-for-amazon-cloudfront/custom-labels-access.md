---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/custom-labels-access.html
---

# Amazon Rekognition Custom Labels access and lifecycle (ECS architecture)
<a name="custom-labels-access"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

Smart cropping can use an Amazon Rekognition Custom Labels model to detect objects specific to your use case. You reference the model by its ARN in the `smartCrop.customModelArn` parameter (see [Smart crop parameters](ecs-smart-crop-parameters.md)). Because there is no template parameter to collect your model ARN at deployment time, review the access and lifecycle requirements below.

The ECS task role created by the stack is pre-provisioned with `rekognition:DetectCustomLabels` permission scoped to all Custom Labels projects and versions in the **same AWS account and same AWS Region** as your DIT deployment. The action you must take depends on where your model lives:
+  **Same account, same Region as the deployment**: No IAM action is required. Reference the model ARN in your smart crop policy or request parameter and it works as-is. This is the common case.
+  **Same account, different Region**: The pre-provisioned permission is Region-scoped and does not cover a model in another Region. Either redeploy the solution in your model’s Region, or add a policy statement to the ECS task role granting `rekognition:DetectCustomLabels` on the model in that Region.
+  **Different account (cross-account)**: This is an advanced scenario that requires both a grant from the account that owns the model and permission on the DIT task role to call into it. Work with the model owner to establish cross-account access, then add the statement below to the DIT task role.

To add permission to the ECS task role:

1. In the CloudFormation console, open your DIT stack and locate the ECS task role (from the `AWS::ECS::TaskDefinition` resource in the stack’s **Resources** tab).

1. In the IAM console, open that role and add an inline policy with a statement like the following, replacing the resource ARN with your specific model’s project and version ARN.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "rekognition:DetectCustomLabels",
         "Resource": "arn:aws:rekognition:<region>:<account-id>:project/<project-name>/version/<version-name>/<timestamp>"
       }
     ]
   }
   ```

**Note**
Scope the statement to the specific model ARN rather than a `project/*/version/*/*` wildcard, so the task role can call only the model you intend to use.

A Custom Labels model is a provisioned inference endpoint, not a serverless resource. You manage its lifecycle:
+ Start the model with `StartProjectVersion` before referencing it in a smart crop policy. Smart cropping can call the model only while it is running.
+ A running model is billed at $4.00 per inference hour per inference unit continuously while running, regardless of request volume.
+ Stop the model with `StopProjectVersion` when it is no longer needed to stop incurring the hourly charge.

If a request references a model that is not running, smart cropping does not fail the image request; it proceeds with the other detection methods and applies the configured fallback if no targets are found. For how to confirm a stopped model is the cause and how to detect it from the solution’s logs, see [Custom Labels detection has no effect](custom-labels-model-stopped.md).

For predictable traffic windows, consider automating start and stop on a schedule: for example, an Amazon EventBridge rule that invokes an AWS Lambda function to call `StartProjectVersion` and `StopProjectVersion` at set times.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
