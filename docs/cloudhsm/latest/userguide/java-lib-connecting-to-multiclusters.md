---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-connecting-to-multiclusters.html
---

# Connect to multiple AWS CloudHSM clusters
<a name="java-lib-connecting-to-multiclusters"></a>

Each `CloudHsmProvider` represents a connection to your AWS CloudHSM Cluster. If you want to talk to another cluster from the same application, you can create another object of `CloudHsmProvider` with configurations for your other cluster and you can interact with this other cluster either using the provider object or using the provider name, as shown in the following example.

**Example**

```
CloudHsmProviderConfig config = CloudHsmProviderConfig.builder()
                                    .withCluster(
                                        CloudHsmCluster.builder()
                                            .withHsmCAFilePath(hsmCAFilePath)
                                            .withClusterUniqueIdentifier("CloudHsmCluster1")
        .withServer(CloudHsmServer.builder().withHostIP(hostName).build())
                        .build())
        .build();
CloudHsmProvider provider1 = new CloudHsmProvider(config);

if (Security.getProvider(provider1.getName()) == null) {
    Security.addProvider(provider1);
}

CloudHsmProviderConfig config2 = CloudHsmProviderConfig.builder()
                                    .withCluster(
                                        CloudHsmCluster.builder()
                                            .withHsmCAFilePath(hsmCAFilePath2)
                                            .withClusterUniqueIdentifier("CloudHsmCluster2")
        .withServer(CloudHsmServer.builder().withHostIP(hostName2).build())
                        .build())
        .build();
CloudHsmProvider provider2 = new CloudHsmProvider(config2);

if (Security.getProvider(provider2.getName()) == null) {
    Security.addProvider(provider2);
}
```

Once you have configured both the providers (both the clusters) above, you can interact with them either using the provider object or using the provider name.

Expanding upon this example that shows how to talk to `cluster1`, you could use the following sample for a AES/GCM/NoPadding operation:

```
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", provider1);
```

And in the same application to do "AES" Key generation on the second cluster using the provider name, you could also use the following sample:

```
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", provider2.getName());
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
