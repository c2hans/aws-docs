---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-external-prereqs.html
---

# Set up prerequisites for MSK Replicator with self-managed Apache Kafka clusters
<a name="msk-replicator-external-prereqs"></a>

## Create an IAM execution role
<a name="msk-replicator-external-iam-role"></a>

Create an IAM role with a trust policy for `kafka.amazonaws.com`. Attach the `AWSMSKReplicatorExecutionRole` managed policy. The managed policy grants the cluster-, topic-, and consumer-group-level Kafka permissions the Replicator needs, but it does *not* include AWS Secrets Manager or AWS KMS permissions, which are required for SASL/SCRAM authentication and CMK-encrypted credentials. For the inline policy snippets to add, see [Additional SER permissions for SASL/SCRAM, mTLS, and customer managed keys](msk-replicator-ser-additional-perms.md).

Example trust policy:

```
{
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "kafka.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }]
}
```

## Configure SASL/SCRAM user and ACL permissions
<a name="msk-replicator-external-scram"></a>

Create a dedicated SCRAM user on your self-managed Kafka cluster. The following ACL permissions are required:

1. Read, Describe on all topics

1. Read, Describe on all consumer groups

1. Describe on cluster resource

Example kafka-acls.sh commands:

```
# Grant Read and Describe on all topics
kafka-acls.sh --bootstrap-server <broker>:9092 \
  --add --allow-principal User:msk-replicator \
  --operation Read --operation Describe \
  --topic '*'

# Grant Read and Describe on all consumer groups
kafka-acls.sh --bootstrap-server <broker>:9092 \
  --add --allow-principal User:msk-replicator \
  --operation Read --operation Describe \
  --group '*'

# Grant Describe on cluster
kafka-acls.sh --bootstrap-server <broker>:9092 \
  --add --allow-principal User:msk-replicator \
  --operation Describe --cluster
```

## Configure mTLS on self-managed cluster
<a name="msk-replicator-external-mtls"></a>

Configure an SSL listener on your self-managed Kafka brokers with `ssl.client.auth=required`. The broker's truststore must contain the CA certificate that signed the client certificate you will use for MSK Replicator.

Grant ACL permissions to the Kafka principal derived from the client certificate's Distinguished Name (DN). The required permissions are: Read and Describe on all topics, Read and Describe on all consumer groups, and Describe on the cluster resource.

## Configure SSL on self-managed cluster
<a name="msk-replicator-external-ssl"></a>

Configure SSL listeners on your brokers. For publicly trusted certificates, no additional configuration is required. For private or self-signed certificates, include the full CA certificate chain in the secret stored in AWS Secrets Manager.

## Store credentials in AWS Secrets Manager
<a name="msk-replicator-external-secrets"></a>

Create a secret of type *Other* (not RDS/Redshift) in AWS Secrets Manager with the appropriate key-value pairs for your authentication type.

**For SASL/SCRAM:**

1. `username` — SCRAM username for the self-managed cluster

1. `password` — SCRAM password for the self-managed cluster

1. `certificate` — CA certificate chain (PEM format; required for private/self-signed certs)

**For mTLS:**

1. `certificate` — PEM-encoded client certificate chain

1. `privateKey` — PEM-encoded private key

1. `privateKeyPassword` — (Optional) Passphrase for the private key, required only for encrypted PKCS8 keys

## Configure network connectivity
<a name="msk-replicator-external-network"></a>

MSK Replicator requires network connectivity to your self-managed Kafka cluster. Supported options:
+ **AWS Site-to-Site VPN** — Connect on-premises networks to your VPC over the internet.
+ **AWS Direct Connect** — Establish a dedicated private network connection from your premises to AWS.

## Configure security groups
<a name="msk-replicator-external-security-groups"></a>

Ensure security groups allow traffic between MSK Replicator and the self-managed cluster on the port used by your authentication listener. Update both inbound rules on VPC security groups and outbound rules on the self-managed cluster firewall.
