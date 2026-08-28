---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.PHPAutoDiscoverySetup.html
---

# Installing the ElastiCache cluster client for PHP
<a name="Appendix.PHPAutoDiscoverySetup"></a>

This section describes how to install, update, and remove the PHP components for the ElastiCache Cluster Client on Amazon EC2 instances. For more information about Auto Discovery, see [Automatically identify nodes in your cluster (Memcached)](AutoDiscovery.md). For sample PHP code to use the client. see [Using the ElastiCache Cluster Client for PHP](AutoDiscovery.Using.ModifyApp.PHP.md).

**Topics**
+ [Downloading the installation package](Appendix.PHPAutoDiscoverySetup.Downloading.md)
+ [For users who already have *php-memcached* extension installed](#Appendix.PHPAutoDiscoverySetup.InstallingExisting)
+ [Installation steps for new users](Appendix.PHPAutoDiscoverySetup.Installing.md)
+ [Removing the PHP cluster client](Appendix.PHPAutoDiscoverySetup.Removing.md)

## For users who already have *php-memcached* extension installed
<a name="Appendix.PHPAutoDiscoverySetup.InstallingExisting"></a>

**To update the `php-memcached` installation**

1. Remove the previous installation of the Memcached extension for PHP as described by the topic [Removing the PHP cluster client](Appendix.PHPAutoDiscoverySetup.Removing.md).

1. Install the new ElastiCache `php-memcached` extension as described previously in [Installation steps for new users](Appendix.PHPAutoDiscoverySetup.Installing.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
