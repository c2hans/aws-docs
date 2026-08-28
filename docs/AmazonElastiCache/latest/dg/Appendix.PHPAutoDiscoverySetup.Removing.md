---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.PHPAutoDiscoverySetup.Removing.html
---

# Removing the PHP cluster client
<a name="Appendix.PHPAutoDiscoverySetup.Removing"></a>

**Topics**
+ [Removing an earlier version of PHP 7](#Appendix.PHPAutoDiscoverySetup.Removing.PHP7x)
+ [Removing an earlier version of PHP 5](#Appendix.PHPAutoDiscoverySetup.Removing.PHP5x)

## Removing an earlier version of PHP 7
<a name="Appendix.PHPAutoDiscoverySetup.Removing.PHP7x"></a>

**To remove an earlier version of PHP 7**

1. Remove the `amazon-elasticache-cluster-client.so` file from the appropriate PHP lib directory as previously indicated in the installation instructions. See the section for your installation at [For users who already have *php-memcached* extension installed](Appendix.PHPAutoDiscoverySetup.md#Appendix.PHPAutoDiscoverySetup.InstallingExisting).

1. Remove the line `extension=amazon-elasticache-cluster-client.so` from the `php.ini` file.

1. Start or restart your Apache server.

   ```
   sudo /etc/init.d/httpd start
   ```

## Removing an earlier version of PHP 5
<a name="Appendix.PHPAutoDiscoverySetup.Removing.PHP5x"></a>

**To remove an earlier version of PHP 5**

1. Remove the `php-memcached` extension:

   ```
   sudo pecl uninstall __uri/AmazonElastiCacheClusterClient
   ```

1.  Remove the `memcached.ini` file added in the appropriate directory as indicated in the previous installation steps.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
