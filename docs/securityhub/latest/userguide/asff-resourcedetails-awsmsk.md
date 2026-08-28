---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/asff-resourcedetails-awsmsk.html
---

# AwsMsk resources in ASFF
<a name="asff-resourcedetails-awsmsk"></a>

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsMsk` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

## AwsMskCluster
<a name="asff-resourcedetails-awsmskcluster"></a>

The `AwsMskCluster` object provides information about an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsMskCluster` object. To view descriptions of `AwsMskCluster` attributes, see [AwsMskClusterDetails](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsMskClusterDetails.html) in the *AWS Security Hub API Reference*.

**Example**

```
"AwsMskCluster": {
        "ClusterInfo": {
            "ClientAuthentication": {
                "Sasl": {
                    "Scram": {
                        "Enabled": true
                    },
                    "Iam": {
                        "Enabled": true
                    }
                },
                "Tls": {
                    "CertificateAuthorityArnList": [],
                    "Enabled": false
                },
                "Unauthenticated": {
                    "Enabled": false
                }
            },
            "ClusterName": "my-cluster",
            "CurrentVersion": "K2PWKAKR8XB7XF",
            "EncryptionInfo": {
                "EncryptionAtRest": {
                    "DataVolumeKMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
                },
                "EncryptionInTransit": {
                    "ClientBroker": "TLS",
                    "InCluster": true
                }
            },
            "EnhancedMonitoring": "PER_TOPIC_PER_BROKER",
            "NumberOfBrokerNodes": 3
        }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
