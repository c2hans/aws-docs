---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/php.html
---

# PHP in AL2023
<a name="php"></a>

 AL2023 currently provides the [PHP](https://www.php.net/) programming language, versions 8.1, 8.2, 8.3, 8.4, and 8.5. Each version is supported for same period of time as upstream PHP. For more information, see [Package support statements](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html).

## Migrating from older PHP versions
<a name="php-migration"></a>

**The upstream PHP community put together comprehensive migration documentation for moving:**
+ [ from PHP 8.4.x to PHP 8.5.x](https://www.php.net/migration85)
+ [ from PHP 8.3.x to PHP 8.4.x](https://www.php.net/migration84)
+ [ from PHP 8.2.x to PHP 8.3.x](https://www.php.net/migration83)
+ [ from PHP 8.1.x to PHP 8.2.x](https://www.php.net/migration82)
+ [ from PHP 8.0.x to PHP 8.1.x](https://www.php.net/migration81)

 AL2 includes PHP 8.0, 8.1, and 8.2 in `amazon-linux-extras` enabling an easy upgrade path to AL2023.

## Migrating from PHP 7.x versions
<a name="php-migration-7x"></a>

**Note**
 The [PHP](https://www.php.net/) project maintains a list and schedule of [supported versions](https://www.php.net/supported-versions.php), as well as a list of [unsupported branches](https://www.php.net/eol.php).
 When AL2023 was released, all 7.x and 5.x versions of [PHP](https://www.php.net/) were unsupported by the PHP community, and were not included as options in AL2023.

 The upstream PHP community put together [ comprehensive migration documentation for moving to PHP 8.0 from PHP 7.4](https://www.php.net/migration80). Combined with the documentation referenced in the previous section on migrating to PHP 8.1 and PHP 8.2, you can migrate your PHP based application to modern PHP.

**Note**
 AL2 includes PHP 7.1, 7.2, 7.3, and 7.4 in `amazon-linux-extras`. It is important to note that all of these Extras are end-of-life and are not guaranteed to get any further security updates.

## PHP modules in AL2023
<a name="php-modules"></a>

 AL2023 includes many PHP modules that are included in PHP Core. AL2023 does not aim to include all of the packages in the [PHP Extension Community Library (PECL)](https://pecl.php.net/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
