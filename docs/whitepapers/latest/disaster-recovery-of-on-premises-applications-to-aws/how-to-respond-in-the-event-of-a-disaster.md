---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/how-to-respond-in-the-event-of-a-disaster.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# How to respond in the event of a disaster
<a name="how-to-respond-in-the-event-of-a-disaster"></a>

 The following section explains how to respond in the event of a disaster, including how to perform a failover and how to perform a failback and return to normal operations.

## Performing a failover
<a name="performing-a-failover"></a>

 An actual failover is very similar to a drill. The two main differences are that during an actual failover, your users will be redirected to the disaster recovery site, and that a failback may be needed when the disaster is over. In the event of planned or unplanned downtime, begin the failover process by using the Elastic Disaster Recovery console to launch recovery instances on AWS from the latest state or a point in time you select.

1.  Launch recovery instances for a single source server or multiple source servers. This action is recorded in [AWS CloudTrail](https://aws.amazon.com/cloudtrail/).

1.  Perform the actual failover (directing traffic to your recovery instances) using the tool or the means you use for directing traffic. For a Domain Name System (DNS) redirect, AWS recommends using [Amazon Route 53 Application Recovery Controller](https://aws.amazon.com/route53/application-recovery-controller/).

1.  After a successful failover, and after the downtime is over, you can prepare for failback.

## Performing a failback and returning to normal operations
<a name="performing-a-failback-and-returning-to-normal-operations"></a>

 After performing a successful failover, verify that any data that was written to your recovery systems is replicated back to your original systems before you perform the actual failback and redirect users to your primary systems. This can be data from changes that occurred while the disaster recovery site was active and that needs to merged back into the source applications, or all the data may need to be copied back in case the data of the source site cannot be recovered after the disaster is over.

 To fail back to the source servers (or to new servers, if the original source servers are no longer available after the disaster is over), follow these steps:

1.  Start by replicating the data from the disaster recovery site back to the source site (when using Elastic Disaster Recovery, replicate the data from your recovery instances on AWS back to your source servers [using the Failback Client](https://docs.aws.amazon.com/drs/latest/userguide/failback-performing.html)).

1.  Continue using the disaster recovery site while the data is being replicated. When using Elastic Disaster Recovery, you can track failback replication progress from the console.

1.  Choose a failback window that minimizes the impact on users (because during failback a short amount of downtime may occur).

1.  During the failback window, go to the disaster recovery site and stop the application.

1.  Make sure that all the data finishes replicating to the source site.

1.  Start the application in the source site.

1.  Make sure the application launches correctly.

1.  Once you have verified that the application is running properly, redirect users back to the application in the source site.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
