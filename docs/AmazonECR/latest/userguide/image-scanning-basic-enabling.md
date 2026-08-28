---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-basic-enabling.html
---

# Configuring basic scanning for images in Amazon ECR
<a name="image-scanning-basic-enabling"></a>

By default, Amazon ECR turns on basic scanning for all private registries. As a result, unless you've changed the scanning settings on your private registry there is no need to turn on basic scanning.

You can use the following steps to define one or more scan on push filters.

**To turn on basic scanning for your private registry**

1.  Open the Amazon ECR console at [ https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories)

1. From the navigation bar, choose the Region to set the scanning configuration for.

1. In the navigation pane, choose **Private registry**, ** Scanning**.

1. On the **Scanning configuration** page, For **Scan type** choose **Basic scanning**.

1. By default all of your repositories are set for **Manual** scanning. You can optionally configure scan on push by specifying **Scan on push filters**. You can set scan on push for all repositories or individual repositories. For more information, see [Filters to choose which repositories are scanned in Amazon ECR](image-scanning-filters.md).
**Note**
If scan on push is enabled for a repository, scans are also done on images that are restored after being archived. No old scans will be available from the restored image.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
