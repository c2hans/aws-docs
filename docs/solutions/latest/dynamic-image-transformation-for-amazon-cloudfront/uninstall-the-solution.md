---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

**Important**
 **Data Loss Warning**: Deleting the solution will permanently delete all origins, transformation policies, and mappings configured in the Admin UI. This data cannot be recovered after deletion. If you need to preserve your configuration, take manual backups of your origins, policies, and mappings before proceeding with the uninstall process.

You can uninstall the solution from the [AWS Management Console](https://aws.amazon.com/console/) or by using the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI). You must manually delete the S3 buckets created by this solution. AWS solutions don’t automatically delete these resources in case you have stored data to retain.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
