---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-configs-multi.html
---

# Connecting to multiple AWS CloudHSM clusters with the JCE provider
<a name="java-lib-configs-multi"></a>

This configuration allows a single client instance to communicate to multiple AWS CloudHSM clusters. Compared to having a single instance only communicate with a single cluster, this can be a cost-savings feature for some use cases. The `CloudHsmProvider` class is AWS CloudHSM's implementation of [Java Security's Provider class](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/security/Provider.html). Each instance of this class represents a connection to your entire AWS CloudHSM cluster. You instantiate this class and add it to Java Security provider's list so that you can interact with it using standard JCE classes.

The following example instantiates this class and adds it to Java Security provider’s list:

```
if (Security.getProvider(CloudHsmProvider.PROVIDER_NAME) == null) {
    Security.addProvider(new CloudHsmProvider());
}
```

`CloudHsmProvider` can be configured in two ways:

1. Configure with file (default configuration)

1. Configure using code

The following topics describe these configurations, and how to connect to multiple clusters.

**Topics**
+ [Configure the AWS CloudHSM `CloudHsmProvider` class with a file (Default configuration)](java-lib-configs-default.md)
+ [Configure the AWS CloudHSM `CloudHsmProvider` class using code](java-lib-configs-using-code.md)
+ [Connect to multiple AWS CloudHSM clusters](java-lib-connecting-to-multiclusters.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
