---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/client-creation-defaults.html
---

# Client creation defaults
<a name="client-creation-defaults"></a>

In version 2.x, the following changes have been made to the default client creation logic.
+ The default credential provider chain for S3 no longer includes anonymous credentials. You must manually specify anonymous access to S3 by using the `AnonymousCredentialsProvider`.
+ The following environment variables related to default client creation are different.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/client-creation-defaults.html)
+ The following system properties related to default client creation are different.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/client-creation-defaults.html)
+ Version 2.x does not support the following system properties.
+
[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/client-creation-defaults.html)
+ Loading Region configuration from a custom `endpoints.json` file is no longer supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
