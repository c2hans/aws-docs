---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

**Important**
 **Data Loss Warning**: Deleting the solution will permanently delete all origins, transformation policies, and mappings configured in the Admin UI. This data cannot be recovered after deletion. If you need to preserve your configuration, take manual backups of your origins, policies, and mappings before proceeding with the uninstall process.

You can uninstall the solution from the [AWS Management Console](https://aws.amazon.com/console/) or by using the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI). You must manually delete the S3 buckets created by this solution. AWS solutions don’t automatically delete these resources in case you have stored data to retain.
