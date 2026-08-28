---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-maven.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Using Maven
<a name="packages-maven"></a>

The Maven repository format is used by many different languages, including Java, Kotlin, Scala, and Clojure. It's supported by many different build tools, including Maven, Gradle, Scala SBT, Apache Ivy, and Leiningen.

We have tested and confirmed compatibility with CodeCatalyst for the following versions:
+ Latest **Maven** version: 3.6.3.
+ Latest **Gradle** version: 6.4.1. Version 5.5.1 has also been tested.

**Topics**
+ [Configuring and using Gradle Groovy](packages-maven-gradle.md)
+ [Configuring and using mvn](packages-maven-mvn.md)
+ [Publishing packages with curl](packages-maven-curl.md)
+ [Using Maven checksums and snapshots](packages-maven-checksums-snapshots.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
