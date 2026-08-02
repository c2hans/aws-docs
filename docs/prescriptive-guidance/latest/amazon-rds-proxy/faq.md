---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-proxy/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about using Amazon RDS Proxy.

## What is the additional cost of using Amazon RDS Proxy?
<a name="q-what-is-the-additional-cost-pf-using-amazon-rds-proxy"></a>

RDS Proxy pricing is based on the number of vCPUs used by the underlying database instance. For pricing details, see [Amazon RDS Proxy pricing](https://aws.amazon.com/rds/proxy/pricing/).

## How do I know if connections are pinned inside Amazon RDS Proxy?
<a name="q-how-do-i-know-if-connections-are-pinned-inside-amazon-rds-proxy"></a>

To check whether client sessions created by your application are getting pinned, you can view the Amazon CloudWatch logs and CloudWatch metrics for the proxy:
+ An overall high `DatabaseConnections:ClientConnections` ratio could indicate pinning in your proxy. Confirm using the next two indicators.
+ The `DatabaseConnectionsCurrentlySessionPinned` metric shows the number of connections pinned on the proxy at any given time.
+ The proxy log also logs an event for each client session that is pinned to a database connection, along with the reason for pinning.

For help with preventing pinning, see [Avoiding pinning](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html#rds-proxy-pinning).

## Do I need to change application code to enable RDS Proxy?
<a name="q-do-i-need-to-change-application-code-to-enable-rds-proxy"></a>

No, code changes are not needed for most applications when using RDS Proxy. The application code uses the new endpoint provided by RDS Proxy for communicating with the database.

Additional FAQs can be found at [Amazon RDS Proxy FAQs](https://aws.amazon.com/rds/proxy/faqs/).
