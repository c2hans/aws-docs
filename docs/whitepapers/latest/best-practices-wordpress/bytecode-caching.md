---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/bytecode-caching.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Bytecode caching
<a name="bytecode-caching"></a>

 Each time a PHP script is run, it gets parsed and compiled. By using a PHP bytecode cache, the output of the PHP compilation is stored in RAM so that the same script doesn’t have to be compiled again and again. This reduces the overhead related to executing PHP scripts, resulting in better performance and lower CPU requirements.

 A bytecode cache can be installed on any Lightsail instance that hosts WordPress and can greatly reduce its load. For PHP 5.5 and later, AWS recommends the use of [OPcache](http://php.net/manual/en/book.opcache.php), a bundled extension with that PHP version.

 Note that OPcache is enabled by default in the Bitnami WordPress Lightsail template, so no further action is required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
