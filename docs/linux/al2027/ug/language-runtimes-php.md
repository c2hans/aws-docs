---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/language-runtimes-php.html
---

# PHP in AL2027
<a name="language-runtimes-php"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 AL2027 currently provides version 8.5 of the [PHP](https://www.php.net/) programming language on the PHP website. Each version is supported for the same period of time as upstream PHP.

 AL2027 incorporates new versions of PHP during its lifetime. The package name is namespaced using a naming convention such as `php8.5`. Amazon Linux does not remove previous package versions from the repositories. If you need a previous PHP version, you can install an earlier version from the repositories. Note that an earlier version does not include the bug fixes and security fixes of a newer PHP version.

## Migrating from older PHP versions
<a name="php-migration"></a>

**Use the following migration documentation from the upstream PHP community:**
+ [Migrating from PHP 8.4.x to PHP 8.5.x](https://www.php.net/migration85) on the PHP website

## PHP modules in AL2027
<a name="php-modules"></a>

 AL2027 includes the following packages from the [PHP Extension Community Library (PECL)](https://pecl.php.net/) on the PECL website:
+ `php-pecl-redis6`
+ `php-pecl-apcu`
+ `php-pecl-msgpack`
+ `php-pecl-igbinary`
+ `php-pecl-memcached`
