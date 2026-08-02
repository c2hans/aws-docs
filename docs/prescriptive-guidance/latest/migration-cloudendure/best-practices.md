---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/best-practices.html
---

# Best practices
<a name="best-practices"></a>

The following video covers best practices and troubleshooting tips for using CloudEndure Migration.

To ensure project success:
+ Train a field technical team, and assign a CloudEndure subject matter expert (SME).
+ Share project timelines with CloudEndure.
+ Monitor data replication progress and report any issues in advance.
+ Perform a test for every machine in advance, and report issues to CloudEndure.
+ Coordinate cutover windows with CloudEndure in advance.

Follow these best practices to implement a smooth and efficient migration process:
+ Create a service account in the CloudEndure User Console instead of using individual administrator accounts.
+ Make sure that you have sufficient migration licenses for your project.
+ Install CloudEndure Agent on your source machines at least three weeks before your planned cutover. This will give you enough time to test and help identify any issues in advance.
+ Install CloudEndure Agents on the source machines by using the --no-replication argument, to prevent the replication from starting automatically.
+ When scheduling your cutover, allow enough time for data replication to complete and for all necessary testing to be carried out.
+ Complete cutover within 90 days after you install the CloudEndure Agent. Migration licenses expire after 90 days.
+ Do not perform any reboots on the source machines before a cutover.
+ Perform a test cutover at least one week before you plan to migrate your source machines. This will help you identify potential problems and solve them before the actual cutover takes place. After performing the test launch:
  + Validate connectivity to your target machines (using SSH for Linux or RDP for Windows), and perform acceptance tests for your application.
  + Verify that the subnet of the target site is isolated, to prevent conflicts with the source site.
  + Verify that your network works as expected.
  + Verify service configuration and other settings.
+ For **Network Bandwidth Throttling**, select **Disabled**. Enable this option only if you want to control the amount of bandwidth used for replication traffic.
+ Remove the source machines from the CloudEndure User Console after cutover is complete, to clean up the staging area, remove the replication resources that are no longer needed, and reduce your costs.
+ If you're replicating a large instance, use a dedicated replication server to accelerate replication.
+ After final cutover, verify that the launched Amazon Elastic Compute Cloud (Amazon EC2) instance passes health checks (*2/2 checks passed* status) on AWS.
