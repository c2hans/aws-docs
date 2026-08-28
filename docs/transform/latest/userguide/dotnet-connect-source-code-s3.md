---
source_url: https://docs.aws.amazon.com/transform/latest/userguide/dotnet-connect-source-code-s3.html
---

# Connect to source code in Amazon S3
<a name="dotnet-connect-source-code-s3"></a>

You can connect AWS Transform to source code in Amazon S3 as an alternative to [connecting a source code repo](https://docs.aws.amazon.com/transform/latest/userguide/dotnet-creating-repo-connector.html).

## S3 bucket organization
<a name="s3-bucket-organization"></a>

Original source code and transformed code are stored in a common S3 bucket, organized as shown below. You must set up your S3 bucket in the same region as your AWS Transform job. Upload your source code to the bucket as a zip file at root level. The zip file must contain a top level folder for each repository.

During transformation, AWS Transform creates a transform-output folder, and stores the transformation results in that folder. Transformation creates a zip file named *transformed-code.zip* containing the transformed code. This includes a code differences report file name diff.txt that highlights file changes at a project level.

```
<customer-bucket>/
├── source-code.zip
         ├── repo 1
         ├── repo 2
         ├── ......
         ├── repo n
└── transform-output/
      ├── transformed-code.zip
```

## Adding a new S3 Connector
<a name="adding-new-s3-connector"></a>

To create a new S3 source code repository connector:

1. In the AWS console, create an S3 bucket.

1. Upload your source code as a zip file to the S3 bucket.

1. In the AWS Transform web app, start a .NET transformation job. In the **Connect a source code repository** step, select **Connect your source code in S3 bucket** and choose **Save**.

1. On the next page, enter your S3 bucket details and choose **Submit**.

   1. Connector name

   1. AWS Account ID

   1. S3 Bucket Arn

   1. S3 Bucket Encryption Key (optional)

1. Approve the connector:

   1. On the next page, copy the verification link.

   1. Have an approver browse to the link to reach the AWS Transform connector creation request page.

   1. Choose to create a new role or use an existing role.

   1. After reviewing the request, choose **Save** and **Approve** to approve it.

1. Specify the S3 zip file location:

   1. In the AWS Transform web app, wait for status to show **Approved**.

   1. On the **Specify asset location** page, enter an S3 URL for the code zip file in the format `s3://bucket-name/zip-file-name` and choose **Send to AWS Transform**.

   1. The job proceeds to the **Discovery** step to continue the transformation.

## Deleting an S3 Connector
<a name="deleting-s3-connector"></a>

To delete an existing S3 connector:

1. In the AWS Transform web app, select **Manage connectors** at the top right.

1. In the **Manage connectors** window, select the connector.

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transform` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
