---
source_url: https://docs.aws.amazon.com/linux/al2/ug/php.html
---

# PHP in AL2
<a name="php"></a>

 AL2 currently provides two fully supported versions of the [PHP](https://www.php.net/) programming language as part of [AL2 Extras Library](al2-extras.md). Each PHP version is supported for the same time frame as upstream PHP as listed under deprecated date in [List of Amazon Linux 2 Extras](al2-extras-list.md).

For information about how to use AL2 Extras to install application and software updates on your instances, see [AL2 Extras Library](al2-extras.md).

 To assist migration to AL2023, both PHP 8.1 and 8.2 are available on AL2 and AL2023.

**Note**
 AL2 includes PHP 7.1, 7.2, 7.3, and 7.4 in `amazon-linux-extras`. All of these Extras are EOL and are not guaranteed to get any additional security updates.
 To find out when each version of PHP is deprecated in AL2, see the [List of Amazon Linux 2 Extras](al2-extras-list.md).

## Migrating from earlier PHP 8.x versions
<a name="php-migration"></a>

 The upstream PHP community put together [ comprehensive migration documentation for moving to PHP 8.2 from PHP 8.1](https://www.php.net/migration82). Documentation also exists for [migrating from PHP 8.0 to 8.1](https://www.php.net/migration81).

 AL2 includes PHP 8.0, 8.1, and 8.2 in `amazon-linux-extras` that enables an efficient upgrade path to AL2023. To find out when each version of PHP is deprecated in AL2, see the [List of Amazon Linux 2 Extras](al2-extras-list.md).

## Migrating from PHP 7.x versions
<a name="php-migration-7x"></a>

 The upstream PHP community put together [ comprehensive migration documentation for moving to PHP 8.0 from PHP 7.4](https://www.php.net/migration80). Combined with the documentation referenced in the previous section on migrating to PHP 8.1, and PHP 8.2, you have all of the steps needed to migrate your PHP based application to modern PHP.

The [PHP](https://www.php.net/) project maintains a list and schedule of [supported versions](https://www.php.net/supported-versions.php), along with a list of [unsupported branches](https://www.php.net/eol.php).

**Note**
 When AL2023 was released, all 7.x and 5.x versions of [PHP](https://www.php.net/) were not supported by the [PHP](https://www.php.net/) community, and were not included as options in AL2023.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
