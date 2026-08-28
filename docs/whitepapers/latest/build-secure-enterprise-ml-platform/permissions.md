---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/permissions.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Permissions
<a name="permissions"></a>

IAM policies need to be created and attached to different roles to perform different operations. IAM provides fine-grained controls to allow / deny access to different SageMaker AI operations such as launching SageMaker AI Notebook instances or starting SageMaker AI training jobs. Following are some example IAM policies for controlling access to various SageMaker AI operations for the different roles. Note that the following IAM policies serve as examples only. It is important that you modify and test them for your specific needs.
+ **Data scientist/ML engineer role **— Data scientists/ML engineers mainly need access to SageMaker AI Notebook instances or Studio for experimentation, or SageMaker AI console to view job status or other metadata. The following sample policies provide the data scientist / ML engineer role with controlled access to the SageMaker AI Notebook instance or SageMaker AI Studio domain.
+ **SageMaker Console access** — The following sample policy enables an AWS user to gain read-only permission to the SageMaker AI console, so the user can navigate inside the console and perform additional privileged operations such as launching a SageMaker AI Notebook instance if additional permissions are granted in other policies. If you need to restrict read-only access to a subset of actions, you can replace `List*`, `Describe*`, and `Get*` with specific actions instead.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerReadAccess",
        "Effect": "Allow",
        "Action": [
          "sagemaker:List*",
          "sagemaker:Describe*",
          "sagemaker:Get*"
        ],
        "Resource": "*"
      }
    ]
  }
  ```

------
+ **SageMaker Notebook Access** — The following sample policy enables an AWS user to launch a SageMaker AI Notebook instance from the SageMaker AI console when the user has an AWS `userid` (for example, `AXXXXXXXXXXXXXXXXXXXX` or `<IAM Role ID>:<user name>` for a Security Assertion Markup Language (SAML) federated user) that matches the value of the “owner” tag associated with the notebook instance. The Governance section of this guide covers more detail on resource tagging and how it is used for permission management. The following IAM policy can be attached to an IAM user directly, or to an IAM role (for example, a data scientist role) that a user assumes.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerNotebookAccessbyOwner",
        "Effect": "Allow",
        "Action": [
          "sagemaker:StartNotebookInstance",
          "sagemaker:StopNotebookInstance",
          "sagemaker:CreatePresignedNotebookInstanceUrl"
        ],
        "Resource": "*",
        "Condition": {
          "StringEquals": {
            "sagemaker:ResourceTag/owner": "${aws:userid}"
          }
        }
      }
    ]
  }
  ```

------

  The previous example uses `aws:userid` to manage fine-grained access to the SageMaker AI Notebook instances by the individual users. Another option is to use the `Session` tags and match the tag on the principal to resource, as shown in the following code sample. For more information about the `Principal` tag, see [Working backward: From IAM policies and principal tags to standardized names and tags for your AWS resources](https://aws.amazon.com/blogs/security/working-backward-from-iam-policies-and-principal-tags-to-standardized-names-and-tags-for-your-aws-resources/).

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerNotebookAccessbyOwner",
        "Effect": "Allow",
        "Action": [
          "sagemaker:StartNotebookInstance",
          "sagemaker:StopNotebookInstance",
          "sagemaker:CreatePresignedNotebookInstanceUrl"
        ],
        "Resource": "*",
        "Condition": {
          "StringEquals": {
            "sagemaker:ResourceTag/owner": "${aws:PrincipalTag/owner}"
          }
        }
      }
    ]
  }
  ```

------
+ **SageMaker AI Studio access** — The following sample policy enables a SageMaker AI Studio user to access the SageMaker AI Studio where the user profile matches the user ID. This IAM policy can be attached to an IAM user directly, or an IAM role (for example, a data scientist role) that a user assumes. Similar to the previous example, you can also use `Session` tags and match the principal and resource tags in the condition. From an authentication perspective, SageMaker AI Studio also supports [AWS Single-Sign-On based authentication](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-sso-users.html).

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Sid": "SageMakerStudioAccessbyOwner",
              "Effect": "Allow",
              "Action": [
                  "sagemaker:CreatePresignedDomainUrl"
              ],
              "Resource": "*",
              "Condition": {
                  "StringLike": {
                      "sagemaker:ResourceTag/owner": "${aws:userid}"
                  }
              }
          }
      ]
  }
  ```

------
+ **SageMaker AI Notebook execution role** — The SageMaker AI notebook execution role needs access to data stored in S3, and permission to run SageMaker AI processing, training, or tuning jobs.

  The following sample policy allows a SageMaker AI notebook execution role to create a SageMaker AI processing, training, and tuning job and pass a job execution role to it.

  For quick experimentation, data scientists can build and push Docker images for model training to an Amazon ECR repo from the SageMaker AI Notebook instance. The following sample policy can be attached to the SageMaker AI Notebook execution role to enable this. The following policy also checks for ECR repos with resource tag equal to SageMaker AI to provide fine-grained access control to the different repos in the ECR. SageMaker AI also provides a suite of built-in algorithms containers and managed machine learning framework containers. These containers are accessible by various SageMaker AI jobs such as training jobs without the need for additional permission.

  The following sample policy, when attached to the SageMaker AI notebook execution role, enables a user to create a model and deploy an endpoint in SageMaker AI.
+ **Training / tuning / processing job role** — When the SageMaker AI processing, training, or tuning job runs, it needs access to resources such as [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS), CloudWatch Logs, and access to S3 data sources and ECR repository.

  The following sample shows a policy that can be attached to a training / tuning / processing job role to run the SageMaker AI training / processing / tuning job and use an S3 bucket as the input source and output target. This policy also allows the SageMaker AI job to create Elastic Network Interface (ENI) and communicate to other VPC resources with actions such as `ec2:CreateNetworkInterface`.
+ **SageMaker AI Model hosting role **— the IAM policies for the SageMaker AI model will need access to EC2, AWS KMS, CloudWatch, and application auto-scaling to host the model in a SageMaker AI endpoint.

  The following example shows a policy that can be attached to the model hosting role to set up a SageMaker AI endpoint. You should further specify the resources to restrict access by the different actions based on requirements.
+ **VPC endpoint** — You can create VPC endpoint policy to restrict access to resources behind VPC endpoints. The following policy will allow any user or service within the VPC to access the specified S3 buckets.

There are additional sample [managed policies](https://docs.aws.amazon.com/sagemaker/latest/dg/access-policy-aws-managed-policies.html) and [custom policies](https://docs.aws.amazon.com/sagemaker/latest/dg/security_iam_id-based-policy-examples.html) that can be used as references for building IAM policies to meet different needs. For pushing containers from within Studio notebooks to ECR, see [Using the Amazon SageMaker Studio Image Build CLI to build container images from your Studio notebooks](https://aws.amazon.com/blogs/machine-learning/using-the-amazon-sagemaker-studio-image-build-cli-to-build-container-images-from-your-studio-notebooks/). Guardrails can be set up at the account level to enforce policies such as network isolation or limiting training to a specific VPC. See the **[Guardrails](governance-and-control.md#guardrails)** section of this document for additional detail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
