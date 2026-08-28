---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration.html
---

# Migrate from version 1.x to 2.x of the AWS SDK for Java
<a name="migration"></a>

The AWS SDK for Java 2.x is a major rewrite of the 1.x code base built on top of Java 8\+. It includes many updates, such as improved consistency, ease of use, and strongly enforced immutability. This section describes the major features that are new in version 2.x, and provides guidance on how to migrate your code to version 2.x from 1.x.

**Topics**
+ [What’s new in version 2](#migration-whats-new)
+ [Find applications using 1.x clients](migration-find-apps-using-v1.md)
+ [How to migrate](migration-howto.md)
+ [What's different between 1.x and 2.x](migration-whats-different.md)
+ [Use the SDK for Java 1.x and 2.x side-by-side](migration-side-by-side.md)

## What’s new in version 2
<a name="migration-whats-new"></a>
+ You can configure your own HTTP clients. See [HTTP transport configuration](http-configuration.md).
+ Async clients feature non-blocking I/O support and return `CompletableFuture` objects. See [Asynchronous programming](asynchronous.md).
+ Operations that return multiple pages have autopaginated responses. This way, you can focus your code on what to do with the response, without the need to check for and get subsequent pages. See [Pagination](pagination.md).
+ SDK start time performance for AWS Lambda functions is improved. See [SDK start time performance improvements](lambda-optimize-starttime.md).
+ Version 2.x supports a new shorthand method for creating requests.
**Example**

  ```
  dynamoDbClient.putItem(request -> request.tableName(TABLE))
  ```

For more details about the new features and to see specific code examples, refer to the other sections of this guide.
+  [Quick Start](get-started.md)
+  [Setting up](setup.md)
+  [Code examples for the AWS SDK for Java 2.x ](java_code_examples.md)
+  [Use the SDK](using.md)
+  [Security for the AWS SDK for Java](security.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
