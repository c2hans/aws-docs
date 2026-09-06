---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/cutover.html
---

# Cutover
<a name="cutover"></a>

In mainframe modernization, one of the most critical challenges is minimizing downtime and risk during the transition to a new platform. The blue/green deployment strategy offers a powerful and flexible approach to system migration.

Blue/green deployment is a technique that reduces downtime and risk by running two identical production environments called *blue* and *green*. Here's how it works in the mainframe modernization context:
+ Blue environment: This is your current mainframe system that's handling all the production traffic.
+ Green environment: This is your new, modernized platform on AWS that's ready to take over.

The blue/green cutover strategy includes these steps: provision, go live, roll back if issues arise, and conclude.

## Provision
<a name="provision"></a>

In this stage, you provision the new (green) environment on AWS by following these steps:

1. **Replatform the environment**: The [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) hosted zone must contain a [DNS record](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.html) that points to the mainframe environment (blue).

1. **Verify connectivity:** Ensure proper connection between your AWS account and on-premises transaction managers and Db2 for z/OS database.

1. **Run smoke tests:** Use the AWS load balancer address to access the replatformed environment and perform comprehensive smoke tests to verify the following:
   + All expected workloads are available.
   + 3270 transactions are processing correctly.
   + Data interactions with Db2 for z/OS are functioning as expected.

## Go live
<a name="go-live"></a>

In this stage, you shift the traffic to the green environment and monitor the changes.

1. Use the traffic routing policies in Route 53 to shift traffic:
   + Option A: You can shift traffic all at once.
   + Option B: Alternatively, you can use a gradual weighted distribution.

1. Monitor and validate:
   + Closely watch the AWS environment as traffic shifts.
   + Check 3270 transaction processing.
   + Verify Db2 for z/OS communication.
   + Monitor for performance issues.
   + Have users validate transaction results.

## Rollback
<a name="rollback"></a>

If issues arise, you can quickly update Route 53 to redirect traffic back to the on-premises mainframe (blue) environment.

You should investigate and resolve problems before you attempt another cutover.

## Conclude
<a name="complete-migration"></a>

After you've monitored the traffic and validated that your green environment is functioning correctly, you can gradually increase the application traffic to AWS.

After a stable period, you can decommission the mainframe transaction (blue) environment, and keep the Db2 for z/OS database on premises.

## Architecture
<a name="cutover-architecture"></a>

The following diagram illustrates the cutover flow.

![Cutover architecture for replatforming mainframe applications on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/images/guide-img/b5c7b078-cfe6-46c4-b120-94b5824d3c88/images/024f696a-2549-407b-8c10-e794db21daae.png)

The cutover process consists of the following:

1. The client applications, frontends, and backends for frontends (BFFs) send transactions to the Route 53 domain name.

1. Route 53 routes the connection to the mainframe transaction manager or to the Network Load Balancer, depending on the defined routing policy.

1. The transaction manager processes the transactions that are sent to the mainframe.

1. The Network Load Balancer distributes transactions to the available replatform environments for processing.

1. The AWS Mainframe Modernization replatform environments process the requests.
