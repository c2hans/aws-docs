---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-delete-cidr-collection.html
---

# Deleting a CIDR collection
<a name="resource-record-sets-delete-cidr-collection"></a>

<a name="CIDR-collection-delete-procedure"></a>

**To delete a CIDR collection, its locations, and blocks by using the Route 53 console**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **IP-based routing** and then **CIDR collections**.

1. In the **CIDR collections** section, choose the linked name of the collection that you want to delete.

1. On the **CIDR locations** page, select each location one at a time, choose **Delete**, enter its name in the dialog box, and then choose **Delete**. You must delete each location associated with a CIDR collection before you can delete the collection.

1. After the deletion of each CIDR location is complete, on the **CIDR locations** page, choose the radio button next to the collection you want to delete, and then choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
