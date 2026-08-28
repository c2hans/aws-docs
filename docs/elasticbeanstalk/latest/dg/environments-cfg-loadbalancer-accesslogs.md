---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-loadbalancer-accesslogs.html
---

# Configuring access logs
<a name="environments-cfg-loadbalancer-accesslogs"></a>

You can use [configuration files](ebextensions.md) to configure your environment's load balancer to upload access logs to an Amazon S3 bucket. See the following example configuration files on GitHub for instructions:
+ `[loadbalancer-accesslogs-existingbucket.config](https://github.com/awslabs/elastic-beanstalk-samples/blob/master/configuration-files/aws-provided/resource-configuration/loadbalancer-accesslogs-existingbucket.config)` – Configure the load balancer to upload access logs to an existing Amazon S3 bucket.
+ `[loadbalancer-accesslogs-newbucket.config](https://github.com/awslabs/elastic-beanstalk-samples/blob/master/configuration-files/aws-provided/resource-configuration/loadbalancer-accesslogs-newbucket.config)` – Configure the load balancer to upload access logs to a new bucket.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
