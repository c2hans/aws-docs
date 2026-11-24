---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-cluster-peers.html
---

# Creating a cluster peer

A cluster peer establishes a trust relationship between two ONTAP file systems or clusters so that they can replicate data with SnapMirror or cache data with FlexCache. A cluster peer is required before you can create an SVM peer or a SnapMirror relationship.

Cluster peering is mutual. Each cluster specifies the other cluster's inter-cluster IP addresses and the same passphrase, and the cluster peer stays pending until both sides are created. When you use the Amazon FSx console to peer with a file system in the same AWS account and AWS Region, Amazon FSx creates the cluster peer on both file systems for you. Otherwise, the administrator of the other cluster creates the matching cluster peer. You use AWS Secrets Manager to securely store and manage the peering passphrase. This approach eliminates the need to pass the passphrase in plaintext in commands, application code, or configuration files, strengthening your security posture.

## Before you begin
<a name="cluster-peer-prerequisites"></a>

Cluster peering fails if the two clusters can't communicate. Before you create a cluster peer, make sure that you meet the following network prerequisites:
+ The source and destination file systems are connected in the same VPC, or are in networks that are peered using Amazon VPC Peering, Transit Gateway, AWS Direct Connect or Site-to-Site VPN. For more information, see [Accessing data from within the AWS Cloud](supported-fsx-clients.md#access-environments) and [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) in the *Amazon VPC Peering Guide*.
+ For cluster peering and SnapMirror to function correctly, every inter-cluster LIF on each cluster must be able to communicate with every inter-cluster LIF on the other cluster. If you are peering with an on-premises ONTAP cluster, ensure that all inter-cluster LIFs on all nodes of the on-premises cluster have network connectivity (routing and firewall rules) to all inter-cluster LIFs on the FSx for ONTAP file system, and vice versa. For more information, see [Cluster peering prerequisites](https://docs.netapp.com/us-en/ontap/peering/prerequisites-cluster-peering-reference.html) on the NetApp website.
+ The VPC security group for the FSx for ONTAP file system allows the inbound and outbound traffic that cluster peering and SnapMirror require between the inter-cluster endpoints (LIFs). For the required rules, see [Creating a VPC security group](limit-access-security-groups.md#create-security-group).

## Creating the cluster peer passphrase
<a name="cluster-peer-passphrase-secret"></a>

Before you create a cluster peer, create a secret in AWS Secrets Manager that contains the peering passphrase. The secret is needed only to create a cluster peer. You can also use IAM policies to manage access to the secret. Create the secret in the same AWS Region as the file system.

### To create the cluster peer passphrase (AWS CLI)
<a name="cluster-peer-passphrase-secret-cli"></a>

The following example stores the passphrase as a secret and attaches a resource policy that allows Amazon FSx to read it for file systems in your AWS account. At the top of the example, set `SECRET_NAME` to a name for the secret and `KMS_KEY_ARN` to the ARN of the customer managed AWS KMS key that encrypts the secret. The key policy must grant Amazon FSx `kms:Decrypt`. Then copy and paste the whole example into your shell. The commands prompt for the passphrase so that it isn't saved in your shell history. Run the commands in the same AWS Region as the file system.

```
# Set a name for the secret
SECRET_NAME={{fsx-cluster-peer-passphrase}}

# Add your KMS key: the ARN of the customer managed key that encrypts the secret.
# The key policy must grant Amazon FSx kms:Decrypt.
KMS_KEY_ARN={{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}

# Look up your account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Enter the peering passphrase when prompted
read -rs -p "Passphrase: " PASSPHRASE; echo

# Create the secret
SECRET_ARN=$(aws secretsmanager create-secret \
    --name "$SECRET_NAME" \
    --secret-string "$PASSPHRASE" \
    --kms-key-id "$KMS_KEY_ARN" \
    --query ARN --output text)
unset PASSPHRASE

# Allow Amazon FSx to read the secret
aws secretsmanager put-resource-policy \
    --secret-id "$SECRET_ARN" \
    --resource-policy "{
      \"Version\": \"2012-10-17\",
      \"Statement\": [{
        \"Effect\": \"Allow\",
        \"Principal\": {\"Service\": \"fsx.amazonaws.com\"},
        \"Action\": \"secretsmanager:GetSecretValue\",
        \"Resource\": \"$SECRET_ARN\",
        \"Condition\": {
          \"StringEquals\": {\"aws:SourceAccount\": \"$ACCOUNT_ID\"}
        }
      }]
    }"

echo "Passphrase secret ARN: $SECRET_ARN"
```

(Optional) To allow only specific file systems to read the secret, add an `aws:SourceArn` condition with the ARNs of those file systems to the policy, for example `"ArnLike": {"aws:SourceArn": ["{{file-system-arn-1}}", "{{file-system-arn-2}}"]}`. If you add it, include both file systems when you peer two file systems in the same AWS account.

Your AWS KMS key policy must grant Amazon FSx `kms:Decrypt` so that Amazon FSx can decrypt the secret. Add the key policy statement shown in the console procedure to the key.

### To create the cluster peer passphrase (AWS Management Console)
<a name="cluster-peer-passphrase-secret-console"></a>

1. Open the [Secrets Manager console](https://console.aws.amazon.com/secretsmanager/), and then choose **Store a new secret**.

1. For **Secret type**, choose **Other type of secret**. Under **Key/value pairs**, choose **Plaintext**, and then enter only the peering passphrase. Use the same passphrase for the cluster peer on both clusters.

1. For **Encryption key**, choose the AWS KMS key that encrypts the secret. To use your own customer managed key, enter the ARN of the key. The key policy must grant Amazon FSx `kms:Decrypt`; see the last step of this procedure. Then choose **Next**.

1. For **Secret name**, enter a descriptive name that helps you find your secret later. (Optional) For **Description**, enter a description for the secret.

1. For **Resource permissions**, choose **Edit permissions**. Add the following policy to allow Amazon FSx to read the secret, and then choose **Save**. Replace {{111122223333}} with your AWS account ID.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "fsx.amazonaws.com"
               },
               "Action": "secretsmanager:GetSecretValue",
               "Resource": "*",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "{{111122223333}}"
                   }
               }
           }
       ]
   }
   ```

   (Optional) To allow only specific file systems to read the secret, add an `aws:SourceArn` condition with the ARNs of those file systems to the policy, for example `"ArnLike": {"aws:SourceArn": ["{{file-system-arn-1}}", "{{file-system-arn-2}}"]}`. If you add it, include both file systems when you peer two file systems in the same AWS account.

1. Choose **Next**, review the secret, and then choose **Store**.

1. If you use your own customer managed AWS KMS key, add the following statement to the key policy to grant Amazon FSx `kms:Decrypt` so that it can decrypt the secret. Replace {{us-east-1}} with the AWS Region of the secret, and {{111122223333}} with your AWS account ID.

   ```
   {
       "Sid": "Allow FSx to decrypt the cluster peer passphrase",
       "Effect": "Allow",
       "Principal": {
           "Service": "fsx.amazonaws.com"
       },
       "Action": "kms:Decrypt",
       "Resource": "*",
       "Condition": {
           "StringEquals": {
               "kms:ViaService": "secretsmanager.{{us-east-1}}.amazonaws.com",
               "aws:SourceAccount": "{{111122223333}}"
           }
       }
   }
   ```

## Creating the cluster peer relationship
<a name="create-cluster-peer-relationship"></a>

### To create a cluster peer (AWS Management Console)
<a name="create-a-cluster-peer-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, under **ONTAP**, choose **Cluster peers**. Then choose **Create cluster peer**.

1. In the **Cluster peer configuration** section, for **Local file system**, choose the file system that initiates the peer relationship.

1. For **Peer location**, do one of the following:
   + Choose **In this AWS account** if the peer file system is in the same AWS account. This lets you choose the **Peer file system region** and **Peer file system** from the dropdown menus. Amazon FSx resolves the peer file system's inter-cluster IP addresses for you.
   + Choose **In another AWS account or on premises** if the peer is an FSx for ONTAP file system in a different AWS account or an on-premises ONTAP cluster. Then enter the peer cluster name or file system ID, and the peer cluster's inter-cluster LIF IP addresses.

1. For **Passphrase secret ARN**, choose the Secrets Manager secret that contains the peering passphrase. The peer cluster must use the same passphrase. The secret must have a resource policy that grants the Amazon FSx service principal (`fsx.amazonaws.com`) permission to access it. For more information, see [Creating the cluster peer passphrase](#cluster-peer-passphrase-secret).

1. Choose **Create cluster peer**. If the peer is in this AWS account, Amazon FSx initiates the peering from the local file system and accepts it on the peer file system for you.

1. On the **Cluster peers** page, verify that the cluster peer's **Status** is **Available**. If the peer is in another AWS account or on premises, the status stays pending until you create the matching cluster peer on the other cluster.

### To create a cluster peer (AWS CLI)
<a name="create-a-cluster-peer-cli"></a>

1. Get the inter-cluster IP addresses of the other cluster. If the other cluster is an FSx for ONTAP file system, use the [describe-file-systems](https://docs.aws.amazon.com/cli/latest/reference/fsx/describe-file-systems.html) CLI command in the AWS account that owns it, as shown in the following example. If the other cluster is an on-premises ONTAP cluster, run the `network interface show -role intercluster` command on that cluster.

   ```
   aws fsx describe-file-systems \
         --file-system-ids {{fs-0fedcba9876543210}} \
         --query 'FileSystems[0].OntapConfiguration.Endpoints.Intercluster.IpAddresses'
   ```

1. Create a cluster peer on the first file system by using the **create-cluster-peer** command. For `--peer-addresses`, specify the inter-cluster IP addresses of the other cluster from the previous step. For `--allowed-svm-mode`, specify `ALL` to let every SVM on the file system form SVM peers over this cluster peer, `NONE` to allow none, or `SPECIFIED` with `--allowed-svm-ids` to allow only the SVMs that you list. This parameter is required in the AWS CLI.

   ```
   aws fsx create-cluster-peer \
         --file-system-id {{fs-0123456789abcdef0}} \
         --peer-addresses {{10.0.2.10}} {{10.0.2.11}} \
         --passphrase-secret-arn {{arn:aws:secretsmanager:us-east-1:111122223333:secret:fsx/cluster-peer/dr-passphrase-AbCdEf}} \
         --allowed-svm-mode ALL
   ```

1. Create the matching cluster peer on the other cluster, using the inter-cluster IP addresses of the first file system and a secret that contains the same passphrase. To get the first file system's inter-cluster IP addresses, use the **describe-file-systems** command as in step 1. If the other cluster is an FSx for ONTAP file system, run the **create-cluster-peer** command for that file system, in its AWS account. If the other cluster is an on-premises ONTAP cluster, run the ONTAP `cluster peer create` command on that cluster.

   ```
   aws fsx create-cluster-peer \
         --file-system-id {{fs-0fedcba9876543210}} \
         --peer-addresses {{10.0.1.10}} {{10.0.1.11}} \
         --passphrase-secret-arn {{arn:aws:secretsmanager:us-east-1:111122223333:secret:fsx/cluster-peer/dr-passphrase-AbCdEf}} \
         --allowed-svm-mode ALL
   ```

1. Use the **describe-cluster-peers** command to verify that the cluster peer's `Lifecycle` is `CREATED` and its `Status` is `available`.

### To create the matching cluster peer on the other cluster
<a name="create-matching-cluster-peer"></a>

If the peer is in another AWS account or on premises, create the matching cluster peer on the other cluster, using this file system's inter-cluster IP addresses and the same passphrase.
+ If the other file system is in another AWS account, repeat the instructions you followed on this page in that account.
+ If the other cluster is an on-premises ONTAP cluster, use the ONTAP CLI. Run the following command on that cluster, and enter the same passphrase when prompted.

  ```
  OnPrem-Cluster::> cluster peer create -address-family ipv4 -peer-addrs {{fsx_inter_1}},{{fsx_inter_2}}
  ```
