---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/scheduled-replication.html
---

# Replicating your data using NetApp SnapMirror

You can use NetApp SnapMirror to schedule periodic replication of your FSx for ONTAP file system to or from another file system or an on-premises ONTAP cluster.

NetApp SnapMirror replicates data efficiently. After the initial transfer, it transfers only the blocks that have changed, so you get high data availability and fast data replication across ONTAP systems. Replication can be scheduled as frequently as every 5 minutes, although intervals should be carefully chosen based on RPOs (Recovery Point Objectives), RTOs (Recovery Time Objectives), and performance considerations.

When you replicate data to NetApp storage systems and continually update the secondary data, your data is kept current and remains available whenever you need it. No external replication servers are required. For more information about using NetApp SnapMirror to replicate your data, see [Learn about NetApp Replication](https://docs.netapp.com/us-en/data-services-replication/concept-replication.html) in the *NetApp Console documentation*.

## How SnapMirror replication works
<a name="how-snapmirror-works"></a>

SnapMirror replicates data at the volume level, from a source volume to a destination volume. The destination is a data protection (DP) volume, which is read-only while the relationship is active. The source volume can be on another FSx for ONTAP file system or on an on-premises ONTAP cluster.

A SnapMirror relationship connects the source volume and the destination volume. The relationship is always created on, and owned by, the destination file system. Before you can create a relationship between two volumes, the file systems or clusters must be peered, and then the source and destination SVMs must be peered:
+ *Cluster peer* – Establishes trust between the two file systems or clusters. For more information, see [Creating a cluster peer](creating-cluster-peers.md).
+ *SVM peer* – Authorizes replication between the source SVM and the destination SVM. For more information, see [Creating an SVM peer](creating-svm-peers.md).

When you create a relationship, SnapMirror performs an initial (baseline) transfer of the source volume's data. After that, SnapMirror transfers changes on a transfer schedule of your choosing, for example hourly or daily. Each SnapMirror relationship has a SnapMirror policy, which determines the snapshots that are transferred and how many are retained on the destination volume. For more information, see [Creating a SnapMirror policy](creating-snapmirror-policies.md).

**Note**
There are two types of SnapMirror replication: Volume-level SnapMirror and SVM Disaster Recovery (SVMDR). Only volume-level SnapMirror replication is supported by FSx for ONTAP. Synchronous SnapMirror, including StrictSync, is not supported.

## Using the Amazon FSx console to schedule replication
<a name="replication-fsx-console"></a>

Amazon FSx simplifies setting up a SnapMirror relationship between FSx for ONTAP volumes in the same AWS account and AWS Region. **Replicate volume** is the simplest way to get started. You specify the destination file system, storage virtual machine (SVM), transfer schedule, and peering passphrase, and **Replicate volume** creates the SnapMirror relationship and a DP destination volume for you. It reuses an existing cluster peer and SVM peer between the file systems, or creates them if they don't exist. **Replicate volume** uses the default settings for other configuration options.

**To replicate a volume within the same AWS account and AWS Region (console)**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, choose **Volumes**, and then choose the volume that you want to replicate. From **Actions**, choose **Replicate volume**. The **Replicate volume** page appears.

1. Choose the **Destination file system** and **Destination storage virtual machine** that you want to replicate the volume to from the dropdown menus. For **Transfer schedule**, choose how often to transfer data from the source volume to the destination volume.

1. For **Passphrase secret ARN**, choose an AWS Secrets Manager secret that contains a passphrase. Amazon FSx uses the passphrase to create the cluster peer between the two file systems. The secret is needed only to create a cluster peer. If a cluster peer already exists between the two file systems, Amazon FSx reuses it. For more information, see [Creating the cluster peer passphrase](creating-cluster-peers.md#cluster-peer-passphrase-secret).

1. (Optional) To view the default settings, expand **Configuration details**. By default, the destination volume has the same size and tiering policy as the source volume, and the relationship uses the `MirrorAllSnapshots` policy, which replicates every snapshot on the source volume. The **Modifiable after creation** column shows which settings you can change after you create the relationship.

1. Choose **Start replication**. Amazon FSx creates a cluster peer, an SVM peer, a DP volume on the destination SVM, and a SnapMirror relationship, and then starts the initial (baseline) transfer. If a cluster peer or SVM peer between the file systems already exists, Amazon FSx reuses it.

**To replicate a volume across AWS Regions or AWS accounts, or with an on-premises ONTAP cluster (console)**

If the other file system is in another AWS account, or the other cluster is on premises, its administrator also needs to create a matching cluster peer.

1. [Create the cluster peer passphrase](creating-cluster-peers.md#cluster-peer-passphrase-secret) as a Secrets Manager secret, which both clusters use to authenticate the cluster peer.

1. [Create a cluster peer](creating-cluster-peers.md) to establish trust between the two file systems or clusters.

1. [Create an SVM peer](creating-svm-peers.md) to authorize replication between the source SVM and the destination SVM.

1. (Optional) [Create a custom SnapMirror policy](creating-snapmirror-policies.md) if you need different retention or a different transfer schedule than the default policy.

1. [Create a DP volume](creating-volumes.md) on the destination file system to receive the replicated data.

1. [Create a SnapMirror relationship](creating-snapmirror-relationships.md) on the destination file system between the source volume and the DP volume, which starts the initial (baseline) transfer.

## Using the AWS CLI to schedule replication
<a name="replication-fsx-cli"></a>

The following example replicates a volume from one FSx for ONTAP file system to another file system in the same AWS account and Region. You provide the source volume ID, the destination volume ID, and the transfer schedule. The example looks up the file systems, SVMs, and inter-cluster IP addresses for you. It runs every step in order: it creates the cluster peer passphrase secret with a random passphrase, creates the cluster peer on both file systems, creates the SVM peer, creates the SnapMirror relationship, and then reports progress until the initial (baseline) transfer completes.

Before you run the example, make sure that you have a data protection (DP) volume on the destination file system. If you don't have one, [create a DP volume](creating-volumes.md). You also need a customer managed AWS KMS key to encrypt the cluster peer passphrase secret, with a key policy that grants Amazon FSx `kms:Decrypt`. For more information, see [Creating the cluster peer passphrase](creating-cluster-peers.md#cluster-peer-passphrase-secret).

To replicate between AWS accounts or with an on-premises ONTAP cluster, run the cluster peer and SVM peer steps on each side separately. For more information, see [Creating a cluster peer](creating-cluster-peers.md) and [Creating an SVM peer](creating-svm-peers.md).

```
# Replace these values
SRC_VOL={{fsvol-0123456789abcdef0}}      # Source volume ID
DST_VOL={{fsvol-0fedcba9876543210}}      # Destination volume ID. It must be a data protection (DP) volume.
SCHEDULE={{hourly}}                      # Transfer schedule
# Add your KMS key: the ARN of the customer managed key that encrypts the cluster peer passphrase secret.
# The key policy must grant Amazon FSx kms:Decrypt.
KMS_KEY_ARN={{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}

# Look up the source file system, SVM, and volume name
read SRC_FS SRC_SVM SRC_VOL_NAME <<< "$(aws fsx describe-volumes --volume-ids $SRC_VOL \
    --query 'Volumes[0].[FileSystemId,OntapConfiguration.StorageVirtualMachineId,Name]' --output text)"
SRC_SVM_NAME=$(aws fsx describe-storage-virtual-machines --storage-virtual-machine-ids $SRC_SVM \
    --query 'StorageVirtualMachines[0].Name' --output text)

# Look up the destination file system and SVM
read DST_FS DST_SVM <<< "$(aws fsx describe-volumes --volume-ids $DST_VOL \
    --query 'Volumes[0].[FileSystemId,OntapConfiguration.StorageVirtualMachineId]' --output text)"

# Look up the inter-cluster IP addresses and your account ID
SRC_IPS=$(aws fsx describe-file-systems --file-system-ids $SRC_FS \
    --query 'FileSystems[0].OntapConfiguration.Endpoints.Intercluster.IpAddresses' --output text)
DST_IPS=$(aws fsx describe-file-systems --file-system-ids $DST_FS \
    --query 'FileSystems[0].OntapConfiguration.Endpoints.Intercluster.IpAddresses' --output text)
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# 1. Create the cluster peer passphrase secret with a random passphrase, readable by FSx in your account
SECRET_ARN=$(aws secretsmanager create-secret --name fsx-cluster-peer-$SRC_FS-$DST_FS \
    --secret-string "$(aws secretsmanager get-random-password --password-length 32 --exclude-punctuation \
        --query RandomPassword --output text)" \
    --kms-key-id "$KMS_KEY_ARN" \
    --query ARN --output text)
aws secretsmanager put-resource-policy --secret-id "$SECRET_ARN" --resource-policy "{
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
# Give the resource policy time to take effect before FSx checks access to the secret
sleep 15

# 2. Create the cluster peer on both file systems
DST_PEER_ID=$(aws fsx create-cluster-peer --file-system-id $DST_FS --peer-addresses $SRC_IPS \
    --passphrase-secret-arn "$SECRET_ARN" --allowed-svm-mode ALL \
    --query 'ClusterPeer.ClusterPeerId' --output text)
SRC_PEER_ID=$(aws fsx create-cluster-peer --file-system-id $SRC_FS --peer-addresses $DST_IPS \
    --passphrase-secret-arn "$SECRET_ARN" --allowed-svm-mode ALL \
    --query 'ClusterPeer.ClusterPeerId' --output text)

# Wait until both cluster peers are created and available. The SVM peer in step 3 relies on the source
# cluster peer, which preauthorizes the destination SVM.
for PEER_ID in $DST_PEER_ID $SRC_PEER_ID; do
  while true; do
    read LIFECYCLE STATUS <<< "$(aws fsx describe-cluster-peers --cluster-peer-ids $PEER_ID \
        --query 'ClusterPeers[0].[Lifecycle,Status]' --output text)"
    [ "$LIFECYCLE" = "FAILED" ] && { echo "Cluster peer $PEER_ID failed"; exit 1; }
    [ "$LIFECYCLE" = "CREATED" ] && [ "$STATUS" = "available" ] && break
    sleep 30
  done
done
SRC_CLUSTER_NAME=$(aws fsx describe-cluster-peers --cluster-peer-ids $DST_PEER_ID \
    --query 'ClusterPeers[0].PeerClusterName' --output text)

# 3. Create the SVM peer from the destination SVM
#    If the source and destination SVMs have the same name, FSx rejects the SVM peer. In that case, add
#    --peer-svm-alias with a different name, and use the alias instead of $SRC_SVM_NAME in step 4.
SVM_PEER_ID=$(aws fsx create-storage-virtual-machine-peer --storage-virtual-machine-id $DST_SVM \
    --peer-svm-name $SRC_SVM_NAME --peer-cluster-name "$SRC_CLUSTER_NAME" --applications SNAPMIRROR \
    --query 'StorageVirtualMachinePeer.StorageVirtualMachinePeerId' --output text)

# Wait until the SVM peer is peered
while true; do
  read LIFECYCLE STATE <<< "$(aws fsx describe-storage-virtual-machine-peers \
      --storage-virtual-machine-peer-ids $SVM_PEER_ID \
      --query 'StorageVirtualMachinePeers[0].[Lifecycle,State]' --output text)"
  { [ "$LIFECYCLE" = "FAILED" ] || [ "$STATE" = "REJECTED" ]; } && { echo "SVM peer $SVM_PEER_ID failed"; exit 1; }
  [ "$STATE" = "PEERED" ] && break
  sleep 15
done

# 4. Create the SnapMirror relationship on the destination file system
aws fsx create-snapmirror-relationship \
    --source Path=$SRC_SVM_NAME:$SRC_VOL_NAME \
    --destination VolumeId=$DST_VOL \
    --transfer-schedule $SCHEDULE

# 5. Print the relationship's progress every 30 seconds until the baseline transfer completes
while true; do
  read LIFECYCLE STATE TRANSFER BYTES HEALTHY <<< "$(aws fsx describe-snapmirror-relationships \
      --filters Name=destination-volume-id,Values=$DST_VOL \
      --query 'SnapmirrorRelationships[0].[Lifecycle,State,TransferState.State,TransferState.BytesTransferred,Healthy]' \
      --output text)"
  echo "$(date +%T) Lifecycle=$LIFECYCLE State=$STATE Transfer=$TRANSFER BytesTransferred=$BYTES Healthy=$HEALTHY"
  if [ "$STATE" = "SNAPMIRRORED" ] || [ "$LIFECYCLE" = "FAILED" ]; then break; fi
  sleep 30
done
```

Because the example creates the cluster peers with `--allowed-svm-mode ALL`, you don't need to accept the SVM peer on the source file system. When the state is `SNAPMIRRORED`, the baseline transfer is complete and later transfers run on the schedule that you chose.

## Using NetApp Console to schedule replication
<a name="replication-snapmirror"></a>

You can use NetApp Console to set up replication with SnapMirror on your FSx for ONTAP file system. For more information, see [Set up data replication in NetApp Replication](https://docs.netapp.com/us-en/cloud-manager-replication/task-replicating-data.html) in the *NetApp Console documentation*.

## Using the ONTAP CLI to schedule replication
<a name="replication-ontap-cli"></a>

You can use the ONTAP CLI to configure scheduled volume replication. For information, see [ Managing SnapMirror volume replication](https://docs.netapp.com/us-en/ontap/data-protection/snapmirror-replication-workflow-concept.html) in the *NetApp ONTAP Documentation Center*.
