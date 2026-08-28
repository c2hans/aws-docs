---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Architecture
<a name="architecture"></a>

 This Quick Start provides two deployment options. Depending upon which option you choose, it creates and configures the necessary AWS components in the AWS Cloud.

 Deploying this Quick Start **with default parameters for end-to-end deployment** (which creates a new VPC) builds the following Magento environment in the AWS Cloud.

## Architecture flow of AWS components
<a name="architecture-flow-of-aws-components"></a>

![Reference architecture diagram showing components deployed by AWS Quick Start for Magento Open Source](http://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/images/quick-start-magento-reference-architecture.png)

1.  Amazon CloudFront is deployed as a content delivery network (CDN). CloudFront speeds up distribution of static and dynamic web content.

1.  First Elastic Load Balancing (Application Load Balancer) distributes traffic across Varnish instances in an AWS Auto Scaling group in multiple Availability Zones.

1.  Varnish deployed on Amazon EC2, Varnish Cache is a web application accelerator caching HTTP reverse proxy. Balancer distributes traffic from Varnish Cache across the AWS Auto Scaling group of Magento instances in multiple Availability Zones.

1.  Second Elastic Load Balancing (Application Load Balancer) distributes traffic from Varnish Cache across the AWS Auto Scaling group of Magento instances in multiple Availability Zones.

1.  Magento web server on Amazon EC2 instances launched in the private subnets.

1.  Amazon OpenSearch Service for Magento catalog search.

1.  An Amazon ElastiCache cluster with the Redis cache engine launched in the private subnets.

1.  Either an Amazon RDS for MySQL or an Amazon Aurora database engine deployed via Amazon RDS in the first private subnet. If you choose Multi-AZ deployment, a synchronously replicated secondary database is deployed in the second private subnet. This provides high availability and built-in automated failover from the primary database.

1.  Amazon S3 created as remote storage for web server instances to store shared media files.

1.  Amazon MQ (optional) is a message broker that offers a reliable, highly available, scalable, and portable messaging system. The Message Queue Framework (MQF) is a system that allows a [module](https://glossary.magento.com/module) to publish messages to queues for [Magento flow](https://devdocs.magento.com/guides/v2.4/config-guide/mq/rabbitmq-overview.html). It also defines the consumers that will receive the messages asynchronously. Bulk operations are actions that are performed on a large scale. Example bulk operations tasks include importing or exporting items, changing prices on a mass scale, and assigning products to a warehouse. For each individual task of a bulk operation, the system creates a message that is published in a [message queue](https://devdocs.magento.com/guides/v2.4/config-guide/mq/rabbitmq-overview.html) and processed by background consumer runs.

## Magento Open Source components
<a name="magento-open-source-components"></a>

 This Quick Start deploys Magento Open Source (2.4.3) with the following prerequisite software:
+  Operating system: Amazon Linux x86-64 or Debian
+  Web server: NGINX
+  Database: Amazon RDS for MySQL 5.6 or Amazon Aurora 5.7
+  Programming language: PHP 7.4, including the required extensions
+  Message broker: Amazon 3.8.11
+  Database Cache: Amazon ElastiCache Redis 6.x
+  Page Cache: Varnish 6.5
+  Content Catalog Search: Amazon OpenSearch Service 7.10

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
