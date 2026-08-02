---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-howto.html
---

# How to migrate your code from AWS SDK for Java 1.x to 2.x
<a name="migration-howto"></a>

You can migrate your existing SDK for Java 1.x applications in a couple ways.

1. Automated approach by using the [migration tool](migration-tool.md).

1. [Manual approach](migration-steps.md) by incrementally replacing 1.x imports with 2.x imports.

We recommend that you start by using the migration tool. It automates much of the routine, replacement work from 1.x to 2.x code.

Since the tool [doesn't migrate all features](migration-tool.md#migration-tool-limitations), you'll need to search for remaining v1 code after running the tool. When you find code that the tool didn't migrate, follow the [step-by-step instructions](migration-steps.md) (manual approach) and use the [migration guide articles](migration-whats-different.md) to finish the migration.

**Topics**
+ [Migration tool](migration-tool.md)
+ [Step-by-step instructions](migration-steps.md)
