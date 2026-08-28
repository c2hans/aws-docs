---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/describe-scan-findings.html
---

# Retrieving the findings for basic scans in Amazon ECR
<a name="describe-scan-findings"></a>

You can retrieve the scan findings for the last completed basic image scan. The software vulnerabilities that were discovered are listed by severity based on the Common Vulnerabilities and Exposures (CVEs) database.

For troubleshooting details for some common issues when scanning images, see [Troubleshooting image scanning in Amazon ECR](image-scanning-troubleshooting.md).

------
#### [ AWS Management Console ]

Use the following steps to retrieve image scan findings using the AWS Management Console.

**To retrieve image scan findings**

1.  Open the Amazon ECR console at [ https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories)

1. From the navigation bar, choose the Region to create your repository in.

1. In the navigation pane, choose **Repositories** .

1. On the **Repositories** page, choose the repository that contains the image to retrieve the scan findings for.

1. On the **Images** page, under the **Image tag** column, select the image tag to retrieve the scan findings.

------
#### [ AWS CLI ]

Use the following AWS CLI command to retrieve image scan findings using the AWS CLI. You can specify an image using the `imageTag` or ` imageDigest`, both of which can be obtained using the [list-images](https://docs.aws.amazon.com/cli/latest/reference/ecr/list-images.html) CLI command.
+ [ describe-image-scan-findings](https://docs.aws.amazon.com/cli/latest/reference/ecr/describe-image-scan-findings.html) (AWS CLI)

  The following example uses an image tag.

  ```
  aws ecr describe-image-scan-findings --repository-name {{name}} --image-id imageTag={{tag_name}} --region {{us-east-2}}
  ```

  The following example uses an image digest.

  ```
  aws ecr describe-image-scan-findings --repository-name {{name}} --image-id imageDigest={{sha256_hash}} --region {{us-east-2}}
  ```

------
#### [ AWS Tools for Windows PowerShell ]
+ [ Get-ECRImageScanFinding](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ECRImageScanFinding.html) (AWS Tools for Windows PowerShell)

  The following example uses an image tag.

  ```
  Get-ECRImageScanFinding -RepositoryName {{name}} -ImageId_ImageTag {{tag_name}} -Region {{us-east-2}}
  ```

  The following example uses an image digest.

  ```
  Get-ECRImageScanFinding -RepositoryName {{name}} -ImageId_ImageDigest {{sha256_hash}} -Region {{us-east-2}}
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
