---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-info.html
---

# Viewing image details in Amazon ECR
<a name="image-info"></a>

After you push an image to your repository, you can view information about it. The details included are as follows:
+ Image URI
+ Image tags
+ Artifact media type
+ Image manifest type
+ Scanning status
+ The size of the image in MB
+ When the image was pushed to the repository
+ The replication status

**To view image details (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository containing your image.

1. In the navigation pane, under **Private registry**, choose **Repositories**.

1. On the **Private repositories** page, choose the repository to view.

1. On the **Repositories : {{repository\_name}}** page, choose the image to view the details of.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
