---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/uninstall-the-solution.html
---

# Uninstall the guidance
<a name="uninstall-the-solution"></a>

You can uninstall the guidance by directly deleting the stacks from the AWS CloudFormation console.

To uninstall the guidance, delete the stacks from the **AWSCloudFormation** console,

1. Go to the AWS CloudFormation console, and

1. Find and delete all the stacks with the prefix `DruidEc2Stack` or `DruidEksStack`.

Alternatively, to uninstall the guidance, navigate to the `source` folder, and run `npm run cdk destroy`.
