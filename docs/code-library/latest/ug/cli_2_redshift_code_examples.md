---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_redshift_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Redshift examples using AWS CLI
<a name="cli_2_redshift_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Redshift.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `accept-reserved-node-exchange`
<a name="redshift_AcceptReservedNodeExchange_cli_2_topic"></a>

The following code example shows how to use `accept-reserved-node-exchange`.

**AWS CLI**
**To accept reserved node exchange**
The following `accept-reserved-node-exchange` example accepts exchange of a DC1 reserved node for a DC2 reserved node.

```
aws redshift accept-reserved-node-exchange \
    --reserved-node-id {{12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE}} \
    --target-reserved-node-offering-id {{12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE}}
```
Output:

```
{
    "ExchangedReservedNode": {
        "ReservedNodeId": "12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE",
        "ReservedNodeOfferingId": "12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE",
        "NodeType": "dc2.large",
        "StartTime": "2019-12-06T21:17:26Z",
        "Duration": 31536000,
        "FixedPrice": 0.0,
        "UsagePrice": 0.0,
        "CurrencyCode": "USD",
        "NodeCount": 1,
        "State": "exchanging",
        "OfferingType": "All Upfront",
        "RecurringCharges": [
            {
                "RecurringChargeAmount": 0.0,
                "RecurringChargeFrequency": "Hourly"
            }
        ],
        "ReservedNodeOfferingType": "Regular"
    }
}
```
For more information, see [Upgrading Reserved Nodes With the AWS CLI](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-offering-console.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [AcceptReservedNodeExchange](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/accept-reserved-node-exchange.html) in *AWS CLI Command Reference*.

### `authorize-cluster-security-group-ingress`
<a name="redshift_AuthorizeClusterSecurityGroupIngress_cli_2_topic"></a>

The following code example shows how to use `authorize-cluster-security-group-ingress`.

**AWS CLI**
**Example 1: To authorize access to an EC2 security group**
The following `authorize-cluster-security-group-ingress` example authorizes access to a named Amazon EC2 security group.

```
aws redshift authorize-cluster-security-group-ingress \
    --cluster-security-group-name {{mysecuritygroup}} \
    --ec2-security-group-name {{myec2securitygroup}} \
    --ec2-security-group-owner-id {{123456789012}}
```
Output:

```
{
    "ClusterSecurityGroup": {
        "ClusterSecurityGroupName": "mysecuritygroup",
        "Description": "This is my cluster security group",
        "EC2SecurityGroups": [
            {
                "Status": "authorizing",
                "EC2SecurityGroupName": "myec2securitygroup",
                "EC2SecurityGroupOwnerId": "123456789012",
                "Tags": []
            }
        ],
        "IPRanges": [],
        "Tags": []
    }
}
```
For more information, see [Infrastructure security in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/security-network-isolation.html) in the *Amazon Redshift Management Guide*.
**Example 2: To authorize access to a CIDR range**
The following `authorize-cluster-security-group-ingress` example authorizes access to a CIDR range.

```
aws redshift authorize-cluster-security-group-ingress \
    --cluster-security-group-name {{mysecuritygroup}} \
    --cidrip {{192.168.100.100/32}}
```
Output:

```
{
    "ClusterSecurityGroup": {
        "ClusterSecurityGroupName": "mysecuritygroup",
        "Description": "This is my cluster security group",
        "EC2SecurityGroups": [],
        "IPRanges": [
            {
                "Status": "authorizing",
                "CIDRIP": "192.168.100.100/32",
                "Tags": []
            }
        ],
        "Tags": []
    }
}
```
For more information, see [Infrastructure security in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/security-network-isolation.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [AuthorizeClusterSecurityGroupIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-cluster-security-group-ingress.html) in *AWS CLI Command Reference*.

### `authorize-snapshot-access`
<a name="redshift_AuthorizeSnapshotAccess_cli_2_topic"></a>

The following code example shows how to use `authorize-snapshot-access`.

**AWS CLI**
**To authorize an AWS account to restore a snapshot**
The following `authorize-snapshot-access` example authorizes the AWS account `123456789111` to restore the snapshot `my-snapshot-id`. By default, the output is in JSON format.

```
aws redshift authorize-snapshot-access \
    --snapshot-id {{my-snapshot-id}} \
    --account-with-restore-access {{123456789111}}
```
Output:

```
{
    "Snapshot": {
        "Status": "available",
        "SnapshotCreateTime": "2013-07-17T22:04:18.947Z",
        "EstimatedSecondsToCompletion": 0,
        "AvailabilityZone": "us-west-2a",
        "ClusterVersion": "1.0",
        "MasterUsername": "adminuser",
        "Encrypted": false,
        "OwnerAccount": "123456789012",
        "BackupProgressInMegaBytes": 11.0,
        "ElapsedTimeInSeconds": 0,
        "DBName": "dev",
        "CurrentBackupRateInMegaBytesPerSecond": 0.1534,
        "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
        "ActualIncrementalBackupSizeInMegaBytes": 11.0,
        "SnapshotType": "manual",
        "NodeType": "dw.hs1.xlarge",
        "ClusterIdentifier": "mycluster",
        "TotalBackupSizeInMegaBytes": 20.0,
        "Port": 5439,
        "NumberOfNodes": 2,
        "SnapshotIdentifier": "my-snapshot-id"
    }
}
```
For more information, see [Sharing a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-share-snapshot.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [AuthorizeSnapshotAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-snapshot-access.html) in *AWS CLI Command Reference*.

### `batch-delete-cluster-snapshots`
<a name="redshift_BatchDeleteClusterSnapshots_cli_2_topic"></a>

The following code example shows how to use `batch-delete-cluster-snapshots`.

**AWS CLI**
**To delete a set of cluster snapshots**
The following `batch-delete-cluster-snapshots` example deletes a set of manual cluster snapshots.

```
aws redshift batch-delete-cluster-snapshots \
    --identifiers {{SnapshotIdentifier=mycluster-2019-11-06-14-12}} {{SnapshotIdentifier=mycluster-2019-11-06-14-20}}
```
Output:

```
{
    "Resources": [
        "mycluster-2019-11-06-14-12",
        "mycluster-2019-11-06-14-20"
    ]
}
```
For more information, see [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [BatchDeleteClusterSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/batch-delete-cluster-snapshots.html) in *AWS CLI Command Reference*.

### `batch-modify-cluster-snapshots`
<a name="redshift_BatchModifyClusterSnapshots_cli_2_topic"></a>

The following code example shows how to use `batch-modify-cluster-snapshots`.

**AWS CLI**
**To modify a set of cluster snapshots**
The following `batch-modify-cluster-snapshots` example modifies the settings for a set of cluster snapshots.

```
aws redshift batch-modify-cluster-snapshots \
    --snapshot-identifier-list {{mycluster-2019-11-06-16-31}} {{mycluster-2019-11-06-16-32}} \
    --manual-snapshot-retention-period {{30}}
```
Output:

```
{
    "Resources": [
        "mycluster-2019-11-06-16-31",
        "mycluster-2019-11-06-16-32"
    ],
    "Errors": []
}
```
For more information, see [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [BatchModifyClusterSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/batch-modify-cluster-snapshots.html) in *AWS CLI Command Reference*.

### `cancel-resize`
<a name="redshift_CancelResize_cli_2_topic"></a>

The following code example shows how to use `cancel-resize`.

**AWS CLI**
**To cancel resize of a cluster**
The following `cancel-resize` example cancels a classic resize operation for a cluster.

```
aws redshift cancel-resize \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "TargetNodeType": "dc2.large",
    "TargetNumberOfNodes": 2,
    "TargetClusterType": "multi-node",
    "Status": "CANCELLING",
    "ResizeType": "ClassicResize",
    "TargetEncryptionType": "NONE"
}
```
For more information, see [Resizing a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/resizing-cluster.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [CancelResize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/cancel-resize.html) in *AWS CLI Command Reference*.

### `copy-cluster-snapshot`
<a name="redshift_CopyClusterSnapshot_cli_2_topic"></a>

The following code example shows how to use `copy-cluster-snapshot`.

**AWS CLI**
**To copy a cluster snapshot**
The following `copy-cluster-snapshot` example creates a copy of the automated snapshot `cm:examplecluster-2013-01-22-19-27-58` named `my-saved-snapshot-copy`. By default, the output is in JSON format.

```
aws redshift copy-cluster-snapshot \
    --source-snapshot-identifier {{cm:examplecluster-2013-01-22-19-27-58}} \
    --target-snapshot-identifier {{my-saved-snapshot-copy}}
```
Output:

```
{
    "Snapshot": {
        "Status": "available",
        "SnapshotCreateTime": "2013-01-22T19:27:58.931Z",
        "AvailabilityZone": "us-west-2c",
        "ClusterVersion": "1.0",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "ClusterCreateTime": "2013-01-22T19:23:59.368Z",
        "SnapshotType": "manual",
        "NodeType": "dw.hs1.xlarge",
        "ClusterIdentifier": "examplecluster",
        "Port": 5439,
        "NumberOfNodes": 2,
        "SnapshotIdentifier": "my-saved-snapshot-copy"
    }
}
```
For more information, see [Copying an automated snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-copy.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [CopyClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/copy-cluster-snapshot.html) in *AWS CLI Command Reference*.

### `create-cluster-parameter-group`
<a name="redshift_CreateClusterParameterGroup_cli_2_topic"></a>

The following code example shows how to use `create-cluster-parameter-group`.

**AWS CLI**
**To create a cluster parameter group**
The following `create-cluster-parameter-group` example creates a new cluster parameter group.

```
aws redshift create-cluster-parameter-group \
    --parameter-group-name {{myclusterparametergroup}} \
    --parameter-group-family {{redshift-1.0}} \
    --description {{"My first cluster parameter group"}}
```
Output:

```
{
    "ClusterParameterGroup": {
        "ParameterGroupFamily": "redshift-1.0",
        "Description": "My first cluster parameter group",
        "ParameterGroupName": "myclusterparametergroup"
    }
}
```
For more information, see [Amazon Redshift parameter groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [CreateClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-parameter-group.html) in *AWS CLI Command Reference*.

### `create-cluster-security-group`
<a name="redshift_CreateClusterSecurityGroup_cli_2_topic"></a>

The following code example shows how to use `create-cluster-security-group`.

**AWS CLI**
**To create a cluster security group**
The following `create-cluster-security-group` example creates a new cluster security group. By default, the output is in JSON format.

```
aws redshift create-cluster-security-group \
    --cluster-security-group-name {{mysecuritygroup}} \
    --description {{"This is my cluster security group"}}
```
Output:

```
{
    "ClusterSecurityGroup": {
        "ClusterSecurityGroupName": "mysecuritygroup",
        "Description": "This is my cluster security group",
        "EC2SecurityGroups": [],
        "IPRanges": [],
        "Tags": []
    }
}
```
You can also obtain the same information in text format using the `--output text` option.

```
aws redshift create-cluster-security-group \
    --cluster-security-group-name {{mysecuritygroup}} \
    --description {{"This is my cluster security group"}} \
    --output {{text}}
```
Output:

```
This is my cluster security group   123456789012    mysecuritygroup
```
For more information, see [Infrastructure security in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/security-network-isolation.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [CreateClusterSecurityGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-security-group.html) in *AWS CLI Command Reference*.

### `create-cluster-snapshot`
<a name="redshift_CreateClusterSnapshot_cli_2_topic"></a>

The following code example shows how to use `create-cluster-snapshot`.

**AWS CLI**
**To create a cluster snapshot**
The following `create-cluster-snapshot` example creates a new cluster snapshot. By default, the output is in JSON format.

```
aws redshift create-cluster-snapshot \
    --cluster-identifier {{mycluster}} \
    --snapshot-identifier {{my-snapshot-id}}
```
Output:

```
{
    "Snapshot": {
        "Status": "creating",
        "SnapshotCreateTime": "2013-01-22T22:20:33.548Z",
        "AvailabilityZone": "us-west-2a",
        "ClusterVersion": "1.0",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
        "SnapshotType": "manual",
        "NodeType": "dw.hs1.xlarge",
        "ClusterIdentifier": "mycluster",
        "Port": 5439,
        "NumberOfNodes": 2,
        "SnapshotIdentifier": "my-snapshot-id"
    }
}
```
For more information, see [Creating a manual snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-create.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [CreateClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-snapshot.html) in *AWS CLI Command Reference*.

### `create-cluster-subnet-group`
<a name="redshift_CreateClusterSubnetGroup_cli_2_topic"></a>

The following code example shows how to use `create-cluster-subnet-group`.

**AWS CLI**
**To create a cluster subnet group**
The following `create-cluster-subnet-group` example creates a new cluster subnet group.

```
aws redshift create-cluster-subnet-group \
    --cluster-subnet-group-name {{mysubnetgroup}} \
    --description {{"My subnet group"}} \
    --subnet-ids {{subnet-763fdd1c}}
```
Output:

```
{
    "ClusterSubnetGroup": {
        "Subnets": [
            {
                "SubnetStatus": "Active",
                "SubnetIdentifier": "subnet-763fdd1c",
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2a"
                }
            } ],
        "VpcId": "vpc-7e3fdd14",
        "SubnetGroupStatus": "Complete",
        "Description": "My subnet group",
        "ClusterSubnetGroupName": "mysubnetgroup"
    }
}
```
For more information, see [Subnets for Redshift resources](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [CreateClusterSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-subnet-group.html) in *AWS CLI Command Reference*.

### `create-cluster`
<a name="redshift_CreateCluster_cli_2_topic"></a>

The following code example shows how to use `create-cluster`.

**AWS CLI**
**To create a cluster with minimal parameters**
The following `create-cluster` example creates a cluster with the minimal set of parameters. By default, the output is in JSON format.

```
aws redshift create-cluster \
    --node-type {{dw.hs1.xlarge}} \
    --number-of-nodes {{2}} \
    --master-username {{adminuser}} \
    --master-user-password {{TopSecret1}} \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "Cluster": {
        "NodeType": "dw.hs1.xlarge",
        "ClusterVersion": "1.0",
        "PubliclyAccessible": true,
        "MasterUsername": "adminuser",
        "ClusterParameterGroups": [
            {
                "ParameterApplyStatus": "in-sync",
                "ParameterGroupName": "default.redshift-1.0"
        } ],
        "ClusterSecurityGroups": [
            {
                "Status": "active",
                "ClusterSecurityGroupName": "default"
        } ],
        "AllowVersionUpgrade": true,
        "VpcSecurityGroups": [],
        "PreferredMaintenanceWindow": "sat:03:30-sat:04:00",
        "AutomatedSnapshotRetentionPeriod": 1,
        "ClusterStatus": "creating",
        "ClusterIdentifier": "mycluster",
        "DBName": "dev",
        "NumberOfNodes": 2,
        "PendingModifiedValues": {
            "MasterUserPassword": "****"
        }
    }
}
```
For more information, see [Creating a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/create-cluster.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [CreateCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster.html) in *AWS CLI Command Reference*.

### `create-event-subscription`
<a name="redshift_CreateEventSubscription_cli_2_topic"></a>

The following code example shows how to use `create-event-subscription`.

**AWS CLI**
**To create a notification subscription for an event**
The following `create-event-subscription` example creates an event notification subscription.

```
aws redshift create-event-subscription \
    --subscription-name {{mysubscription}} \
    --sns-topic-arn {{arn:aws:sns:us-west-2:123456789012:MySNStopic}} \
    --source-type {{cluster}} \
    --source-ids {{mycluster}}
```
Output:

```
{
        "EventSubscription": {
        "CustomerAwsId": "123456789012",
        "CustSubscriptionId": "mysubscription",
        "SnsTopicArn": "arn:aws:sns:us-west-2:123456789012:MySNStopic",
        "Status": "active",
        "SubscriptionCreationTime": "2019-12-09T20:05:19.365Z",
        "SourceType": "cluster",
        "SourceIdsList": [
            "mycluster"
        ],
        "EventCategoriesList": [],
        "Severity": "INFO",
        "Enabled": true,
        "Tags": []
    }
}
```
For more information, see [Subscribing to Amazon Redshift Event Notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [CreateEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-event-subscription.html) in *AWS CLI Command Reference*.

### `create-hsm-client-certificate`
<a name="redshift_CreateHsmClientCertificate_cli_2_topic"></a>

The following code example shows how to use `create-hsm-client-certificate`.

**AWS CLI**
**To create an HSM client certificate**
The following `create-hsm-client-certificate` example generates an HSM client certificate that a cluster can use to connect to an HSM.

```
aws redshift create-hsm-client-certificate \
    --hsm-client-certificate-identifier {{myhsmclientcert}}
```
Output:

```
{
    "HsmClientCertificate": {
        "HsmClientCertificateIdentifier": "myhsmclientcert",
        "HsmClientCertificatePublicKey": "-----BEGIN CERTIFICATE-----\nMIICiEXAMPLECQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC\nVVMxCzAJBgNVBAgTEXAMPLEwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6\nb24xFDASBgNVBAsTC0lBTSBDb25EXAMPLEIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd\nBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb2EXAMPLETEwNDI1MjA0NTIxWhcN\nMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBEXAMPLEMRAwDgYD\nEXAMPLETZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z\nb2xlMRIwEAEXAMPLEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt\nYXpvbi5jb20wgZ8wDQYJKEXAMPLEAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ\n21uUSfwfEvySWtC2XADZ4nB+BLYgVIk6EXAMPLE3G93vUEIO3IyNoH/f0wYK8m9T\nrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugEXAMPLEzZswY6786m86gpE\nIbb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEEXAMPLEEAtCu4\nnUhVVxYUEXAMPLEh8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb\nFFBjvSfpJIlJ00zbhNYS5f6GEXAMPLEl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb\nNYiytVbZPQUQ5Yaxu2jXnimvw3rEXAMPLE=\n-----END CERTIFICATE-----\n",
        "Tags": []
    }
}
```
For more information, see [Amazon Redshift API Permissions Reference](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [CreateHsmClientCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-hsm-client-certificate.html) in *AWS CLI Command Reference*.

### `create-hsm-configuration`
<a name="redshift_CreateHsmConfiguration_cli_2_topic"></a>

The following code example shows how to use `create-hsm-configuration`.

**AWS CLI**
**To create an HSM configuration**
The following `create-hsm-configuration` example creates the specified HSM configuration that contains information required by a cluster to store and use database encryption keys in a hardware security module (HSM).

```
aws redshift create-hsm-configuration \
    --hsm-configuration-identifier {{myhsmconnection}} \
    --description {{"My HSM connection"}} \
    --hsm-ip-address {{192.0.2.09}} \
    --hsm-partition-name {{myhsmpartition}} \
    --hsm-partition-password {{A1b2c3d4}} \
    --hsm-server-public-certificate {{myhsmclientcert}}
```
Output:

```
{
    "HsmConfiguration": {
        "HsmConfigurationIdentifier": "myhsmconnection",
        "Description": "My HSM connection",
        "HsmIpAddress": "192.0.2.09",
        "HsmPartitionName": "myhsmpartition",
        "Tags": []
    }
}
```
For more information, see [Amazon Redshift database encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [CreateHsmConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-hsm-configuration.html) in *AWS CLI Command Reference*.

### `create-snapshot-copy-grant`
<a name="redshift_CreateSnapshotCopyGrant_cli_2_topic"></a>

The following code example shows how to use `create-snapshot-copy-grant`.

**AWS CLI**
**To create a snapshot copy grant**
The following `create-snapshot-copy-grant` example creates a snapshot copy grant and encrypts copied snapshots in a destination AWS Region.

```
aws redshift create-snapshot-copy-grant \
    --snapshot-copy-grant-name {{mysnapshotcopygrantname}}
```
Output:

```
{
    "SnapshotCopyGrant": {
        "SnapshotCopyGrantName": "mysnapshotcopygrantname",
        "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY",
        "Tags": []
    }
}
```
For more information, see [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [CreateSnapshotCopyGrant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-copy-grant.html) in *AWS CLI Command Reference*.

### `create-snapshot-schedule`
<a name="redshift_CreateSnapshotSchedule_cli_2_topic"></a>

The following code example shows how to use `create-snapshot-schedule`.

**AWS CLI**
**To create snapshot schedule**
The following `create-snapshot-schedule` example creates a snapshot schedule with the specified description and a rate of every 12 hours.

```
aws redshift create-snapshot-schedule \
    --schedule-definitions {{"rate(12 hours)"}} \
    --schedule-identifier {{mysnapshotschedule}} \
    --schedule-description {{"My schedule description"}}
```
Output:

```
{
    "ScheduleDefinitions": [
        "rate(12 hours)"
    ],
    "ScheduleIdentifier": "mysnapshotschedule",
    "ScheduleDescription": "My schedule description",
    "Tags": []
}
```
For more information, see [Automated Snapshot Schedules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#automated-snapshot-schedules) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [CreateSnapshotSchedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-schedule.html) in *AWS CLI Command Reference*.

### `create-tags`
<a name="redshift_CreateTags_cli_2_topic"></a>

The following code example shows how to use `create-tags`.

**AWS CLI**
**To create tags for a cluster**
The following `create-tags` example adds the specified tag key/value pair to the specified cluster.

```
aws redshift create-tags \
    --resource-name {{arn:aws:redshift:us-west-2:123456789012:cluster:mycluster}} \
    --tags "Key"="mytags","Value"="tag1"
```
This command produces no output.
For more information, see [Tagging Resources in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-tagging.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [CreateTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-tags.html) in *AWS CLI Command Reference*.

### `delete-cluster-parameter-group`
<a name="redshift_DeleteClusterParameterGroup_cli_2_topic"></a>

The following code example shows how to use `delete-cluster-parameter-group`.

**AWS CLI**
**To delete a cluster parameter group**
The following `delete-cluster-parameter-group` example deletes a cluster parameter group.

```
aws redshift delete-cluster-parameter-group \
    --parameter-group-name {{myclusterparametergroup}}
```
This command produces no output.
For more information, see [Amazon Redshift parameter groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DeleteClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-parameter-group.html) in *AWS CLI Command Reference*.

### `delete-cluster-security-group`
<a name="redshift_DeleteClusterSecurityGroup_cli_2_topic"></a>

The following code example shows how to use `delete-cluster-security-group`.

**AWS CLI**
**To delete a cluster security group**
The following `delete-cluster-security-group` example deletes a cluster security group.

```
aws redshift delete-cluster-security-group \
    --cluster-security-group-name {{mysecuritygroup}}
```
This command produces no output.
For more information, see [Infrastructure security in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/security-network-isolation.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DeleteClusterSecurityGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-security-group.html) in *AWS CLI Command Reference*.

### `delete-cluster-snapshot`
<a name="redshift_DeleteClusterSnapshot_cli_2_topic"></a>

The following code example shows how to use `delete-cluster-snapshot`.

**AWS CLI**
**To delete a cluster snapshot**
The following `delete-cluster-snapshot` example deletes a cluster snapshot.

```
aws redshift delete-cluster-snapshot \
    --snapshot-identifier {{my-snapshot-id}}
```
Output:

```
{
    "Snapshot": {
        "SnapshotIdentifier": "my-snapshot-id",
        "ClusterIdentifier": "mycluster",
        "SnapshotCreateTime": "2013-01-22T22:20:33.548Z",
        "Status": "deleted",
        "Port": 5439,
        "AvailabilityZone": "us-west-2a",
        "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
        "MasterUsername": "adminuser",
        "ClusterVersion": "1.0",
        "SnapshotType": "manual",
        "NodeType": "dc2.large",
        "NumberOfNodes": 2,
        "DBName": "dev",
        "Encrypted": false,
        "EncryptedWithHSM": false,
        "OwnerAccount": "123456789012",
        "TotalBackupSizeInMegaBytes": 20.0,
        "ActualIncrementalBackupSizeInMegaBytes": 20.0,
        "BackupProgressInMegaBytes": 20.0,
        "CurrentBackupRateInMegaBytesPerSecond": 0.0,
        "EstimatedSecondsToCompletion": -1,
        "ElapsedTimeInSeconds": 0,
        "Tags": [],
        "EnhancedVpcRouting": false,
        "MaintenanceTrackName": "current",
        "ManualSnapshotRetentionPeriod": -1
    }
}
```
For more information, see [Deleting a manual snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-delete.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DeleteClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-snapshot.html) in *AWS CLI Command Reference*.

### `delete-cluster-subnet-group`
<a name="redshift_DeleteClusterSubnetGroup_cli_2_topic"></a>

The following code example shows how to use `delete-cluster-subnet-group`.

**AWS CLI**
**To delete a cluster subnet group**
The following `delete-cluster-subnet-group` example deletes a cluster subnet group.

```
aws redshift delete-cluster-subnet-group \
    --cluster-subnet-group-name {{mysubnetgroup}}
```
This command produces no output.
For more information, see [Subnets for Redshift resources](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DeleteClusterSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-subnet-group.html) in *AWS CLI Command Reference*.

### `delete-cluster`
<a name="redshift_DeleteCluster_cli_2_topic"></a>

The following code example shows how to use `delete-cluster`.

**AWS CLI**
**Example 1: To delete a cluster with no final cluster snapshot**
The following `delete-cluster` example deletes a cluster, forcing data deletion so no final cluster snapshot is created.

```
aws redshift delete-cluster \
    --cluster-identifier {{mycluster}} \
    --skip-final-cluster-snapshot
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "deleting",
        "ClusterAvailabilityStatus": "Modifying",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.c1a2b3c4d5e6.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-23T21:42:51.430Z",
        "AutomatedSnapshotRetentionPeriod": 1,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-0a1b2c3d4e5f6a7b8",
                "Status": "active"
            }
        ],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "ClusterSubnetGroupName": "default",
        "VpcId": "vpc-0a1b2c3d4e5f6a7b8",
        "AvailabilityZone": "us-west-2a",
        "PreferredMaintenanceWindow": "sat:03:30-sat:04:00",
        "PendingModifiedValues": {},
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 2,
        "PubliclyAccessible": false,
        "Encrypted": false,
        "Tags": [],
        "EnhancedVpcRouting": false,
        "IamRoles": [],
        "MaintenanceTrackName": "current",
        "DeferredMaintenanceWindows": [],
        "NextMaintenanceWindowStartTime": "2019-12-28T03:30:00Z"
    }
}
```
For more information, see [Shutting down and deleting a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-mgmt-shutdown-delete-cluster.html) in the *Amazon Redshift Management Guide*.
**Example 2: To delete a cluster, allowing a final cluster snapshot**
The following `delete-cluster` example deletes a cluster, but specifies a final cluster snapshot.

```
aws redshift delete-cluster \
    --cluster-identifier {{mycluster}} \
    --final-cluster-snapshot-identifier {{myfinalsnapshot}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "deleting",
        "ClusterAvailabilityStatus": "Modifying",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.c1a2b3c4d5e6.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-23T21:42:51.430Z",
        "AutomatedSnapshotRetentionPeriod": 1,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-0a1b2c3d4e5f6a7b8",
                "Status": "active"
            }
        ],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "ClusterSubnetGroupName": "default",
        "VpcId": "vpc-0a1b2c3d4e5f6a7b8",
        "AvailabilityZone": "us-west-2a",
        "PreferredMaintenanceWindow": "sat:03:30-sat:04:00",
        "PendingModifiedValues": {},
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 2,
        "PubliclyAccessible": false,
        "Encrypted": false,
        "Tags": [],
        "EnhancedVpcRouting": false,
        "IamRoles": [],
        "MaintenanceTrackName": "current",
        "DeferredMaintenanceWindows": [],
        "NextMaintenanceWindowStartTime": "2019-12-28T03:30:00Z"
    }
}
```
For more information, see [Shutting down and deleting a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-mgmt-shutdown-delete-cluster.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DeleteCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster.html) in *AWS CLI Command Reference*.

### `delete-event-subscription`
<a name="redshift_DeleteEventSubscription_cli_2_topic"></a>

The following code example shows how to use `delete-event-subscription`.

**AWS CLI**
**To delete event subscription**
The following `delete-event-subscription` example deletes the specified event notification subscription.

```
aws redshift delete-event-subscription \
    --subscription-name {{mysubscription}}
```
This command produces no output.
For more information, see [Subscribing to Amazon Redshift Event Notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DeleteEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-event-subscription.html) in *AWS CLI Command Reference*.

### `delete-hsm-client-certificate`
<a name="redshift_DeleteHsmClientCertificate_cli_2_topic"></a>

The following code example shows how to use `delete-hsm-client-certificate`.

**AWS CLI**
**To delete HSM client certificate**
The following `delete-hsm-client-certificate` example deletes an HSM client certificate.

```
aws redshift delete-hsm-client-certificate \
    --hsm-client-certificate-identifier {{myhsmclientcert}}
```
This command produces no output.
For more information, see [Amazon Redshift API Permissions Reference](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DeleteHsmClientCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-client-certificate.html) in *AWS CLI Command Reference*.

### `delete-hsm-configuration`
<a name="redshift_DeleteHsmConfiguration_cli_2_topic"></a>

The following code example shows how to use `delete-hsm-configuration`.

**AWS CLI**
**To delete an HSM configuration**
The following `delete-hsm-configuration` example deletes the specified HSM configuration from the current AWS account.

```
aws redshift delete-hsm-configuration \
    --hsm-configuration-identifier {{myhsmconnection}}
```
This command produces no output.
For more information, see [Amazon Redshift database encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DeleteHsmConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-configuration.html) in *AWS CLI Command Reference*.

### `delete-scheduled-action`
<a name="redshift_DeleteScheduledAction_cli_2_topic"></a>

The following code example shows how to use `delete-scheduled-action`.

**AWS CLI**
**To delete scheduled action**
The following `delete-scheduled-action` example deletes the specified scheduled action.

```
aws redshift delete-scheduled-action \
    --scheduled-action-name {{myscheduledaction}}
```
This command produces no output.
For more information, see [Scheduling a resize](https://docs.aws.amazon.com/redshift/latest/mgmt/resizing-cluster.html#rs-restore-resize-overview-schedule) in the *Amazon Redshift Management Guide*.
+  For API details, see [DeleteScheduledAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-scheduled-action.html) in *AWS CLI Command Reference*.

### `delete-snapshot-copy-grant`
<a name="redshift_DeleteSnapshotCopyGrant_cli_2_topic"></a>

The following code example shows how to use `delete-snapshot-copy-grant`.

**AWS CLI**
**To delete snapshot copy grant**
The following `delete-snapshot-copy-grant` example deletes the specified snapshot copy grant.

```
aws redshift delete-snapshot-copy-grant \
    --snapshot-copy-grant-name {{mysnapshotcopygrantname}}
```
This command produces no output.
For more information, see [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DeleteSnapshotCopyGrant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-snapshot-copy-grant.html) in *AWS CLI Command Reference*.

### `delete-snapshot-schedule`
<a name="redshift_DeleteSnapshotSchedule_cli_2_topic"></a>

The following code example shows how to use `delete-snapshot-schedule`.

**AWS CLI**
**To delete snapshot schedule**
The following `delete-snapshot-schedule` example deletes the specified snapshot schedule. You must disassociate clusters before deleting the schedule.

```
aws redshift delete-snapshot-schedule \
    --schedule-identifier {{mysnapshotschedule}}
```
This command produces no output.
For more information, see [Automated Snapshot Schedules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#automated-snapshot-schedules) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DeleteSnapshotSchedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-snapshot-schedule.html) in *AWS CLI Command Reference*.

### `delete-tags`
<a name="redshift_DeleteTags_cli_2_topic"></a>

The following code example shows how to use `delete-tags`.

**AWS CLI**
**To delete tags from a cluster**
The following `delete-tags` example deletes the tags with the specified key names from the specified cluster.

```
aws redshift delete-tags \
    --resource-name {{arn:aws:redshift:us-west-2:123456789012:cluster:mycluster}} \
    --tag-keys {{"clustertagkey"}} {{"clustertagvalue"}}
```
This command produces no output.
For more information, see [Tagging Resources in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-tagging.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DeleteTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-tags.html) in *AWS CLI Command Reference*.

### `describe-account-attributes`
<a name="redshift_DescribeAccountAttributes_cli_2_topic"></a>

The following code example shows how to use `describe-account-attributes`.

**AWS CLI**
**To describe attributes of an AWS account**
The following `describe-account-attributes` example displays the attributes attached to the calling AWS account.

```
aws redshift describe-account-attributes
```
Output:

```
{
    "AccountAttributes": [
        {
            "AttributeName": "max-defer-maintenance-duration",
            "AttributeValues": [
                {
                    "AttributeValue": "45"
                }
            ]
        }
    ]
}
```
For more information, see [Considerations for using Amazon Redshift provisioned clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-considerations.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeAccountAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-account-attributes.html) in *AWS CLI Command Reference*.

### `describe-cluster-db-revisions`
<a name="redshift_DescribeClusterDbRevisions_cli_2_topic"></a>

The following code example shows how to use `describe-cluster-db-revisions`.

**AWS CLI**
**To describe DB revisions for a cluster**
The following `describe-cluster-db-revisions` example displays the details of an array of `ClusterDbRevision` objects for the specified cluster.

```
aws redshift describe-cluster-db-revisions \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "ClusterDbRevisions": [
        {
            "ClusterIdentifier": "mycluster",
            "CurrentDatabaseRevision": "11420",
            "DatabaseRevisionReleaseDate": "2019-11-22T16:43:49.597Z",
            "RevisionTargets": []
        }
    ]
}
```
For more information, see [Cluster versions for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeClusterDbRevisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-db-revisions.html) in *AWS CLI Command Reference*.

### `describe-cluster-parameter-groups`
<a name="redshift_DescribeClusterParameterGroups_cli_2_topic"></a>

The following code example shows how to use `describe-cluster-parameter-groups`.

**AWS CLI**
**To get a description of all cluster parameter groups**
The following `describe-cluster-parameter-groups` example returns a description of all cluster parameter groups for the account, with column headers. By default, the output is in JSON format.

```
aws redshift describe-cluster-parameter-groups
```
Output:

```
{
    "ParameterGroups": [
        {
            "ParameterGroupFamily": "redshift-1.0",
            "Description": "My first cluster parameter group",
            "ParameterGroupName": "myclusterparametergroup"
        }
    ]
}
```
You can also obtain the same information in text format using the `--output text` option.

```
aws redshift describe-cluster-parameter-groups \
    --output {{text}}
```
Output:

```
redshift-1.0        My first cluster parameter group        myclusterparametergroup
```
For more information, see [Amazon Redshift parameter groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeClusterParameterGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-parameter-groups.html) in *AWS CLI Command Reference*.

### `describe-cluster-parameters`
<a name="redshift_DescribeClusterParameters_cli_2_topic"></a>

The following code example shows how to use `describe-cluster-parameters`.

**AWS CLI**
**To retrieve the parameters for a specified cluster parameter group**
The following `describe-cluster-parameters` example retrieves the parameters for the named parameter group. By default, the output is in JSON format.

```
aws redshift describe-cluster-parameters \
    --parameter-group-name {{myclusterparametergroup}}
```
Output:

```
{
    "Parameters": [
        {
            "Description": "Sets the display format for date and time values.",
            "DataType": "string",
            "IsModifiable": true,
            "Source": "engine-default",
            "ParameterValue": "ISO, MDY",
            "ParameterName": "datestyle"
        },
        {
            "Description": "Sets the number of digits displayed for floating-point values",
            "DataType": "integer",
            "IsModifiable": true,
            "AllowedValues": "-15-2",
            "Source": "engine-default",
            "ParameterValue": "0",
            "ParameterName": "extra_float_digits"
        }
    ]
}
```
You can also obtain the same information in text format using the `--output text` option.

```
aws redshift describe-cluster-parameters \
    --parameter-group-name {{myclusterparametergroup}} \
    --output {{text}}
```
Output:

```
RESPONSEMETADATA    a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
Sets the display format for date and time values.   string  True    engine-default  ISO, MDY        datestyle
Sets the number of digits displayed for floating-point values       integer True    -15-2   engine-default  0       extra_float_digits
This parameter applies a user-defined label to a group of queries that are run during the same session..    string  True    engine-default  default query_group
require ssl for all databaseconnections     boolean True    true,false      engine-default  false   require_ssl
Sets the schema search order for names that are not schema-qualified.       string  True    engine-default  $user, public   search_path
Aborts any statement that takes over the specified number of milliseconds.  integer True    engine-default  0       statement_timeout
wlm json configuration      string  True    engine-default  \[{"query_concurrency":5}]      wlm_json_configuration
```
For more information, see [Amazon Redshift parameter groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeClusterParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-parameters.html) in *AWS CLI Command Reference*.

### `describe-cluster-security-groups`
<a name="redshift_DescribeClusterSecurityGroups_cli_2_topic"></a>

The following code example shows how to use `describe-cluster-security-groups`.

**AWS CLI**
**To get a description of all cluster security groups**
The following `describe-cluster-security-groups` example returns a description of all cluster security groups for the account. By default, the output is in JSON format.

```
aws redshift describe-cluster-security-groups
```
Output:

```
{
    "ClusterSecurityGroups": [
        {
            "Description": "default",
            "ClusterSecurityGroupName": "default",
            "EC2SecurityGroups": [],
            "IPRanges": [
                {
                    "Status": "authorized",
                    "CIDRIP": "0.0.0.0/0"
                }
            ]
        },
        {
            "Description": "This is my cluster security group",
            "ClusterSecurityGroupName": "mysecuritygroup",
            "EC2SecurityGroups": [],
            "IPRanges": []
        }
    ]
}
```
For more information, see [Infrastructure security in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/security-network-isolation.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeClusterSecurityGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-security-groups.html) in *AWS CLI Command Reference*.

### `describe-cluster-snapshots`
<a name="redshift_DescribeClusterSnapshots_cli_2_topic"></a>

The following code example shows how to use `describe-cluster-snapshots`.

**AWS CLI**
**To get a description of all cluster snapshots**
The following `describe-cluster-snapshots` example returns a description of all cluster snapshots for the account. By default, the output is in JSON format.

```
aws redshift describe-cluster-snapshots
```
Output:

```
{
    "Snapshots": [
        {
            "Status": "available",
            "SnapshotCreateTime": "2013-07-17T22:02:22.852Z",
            "EstimatedSecondsToCompletion": -1,
            "AvailabilityZone": "us-west-2a",
            "ClusterVersion": "1.0",
            "MasterUsername": "adminuser",
            "Encrypted": false,
            "OwnerAccount": "123456789012",
            "BackupProgressInMegaBytes": 20.0,
            "ElapsedTimeInSeconds": 0,
            "DBName": "dev",
            "CurrentBackupRateInMegaBytesPerSecond": 0.0,
            "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
            "ActualIncrementalBackupSizeInMegaBytes": 20.0,
            "SnapshotType": "automated",
            "NodeType": "dw.hs1.xlarge",
            "ClusterIdentifier": "mycluster",
            "Port": 5439,
            "TotalBackupSizeInMegaBytes": 20.0,
            "NumberOfNodes": 2,
            "SnapshotIdentifier": "cm:mycluster-2013-01-22-22-04-18"
        },
        {
            "EstimatedSecondsToCompletion": 0,
            "OwnerAccount": "123456789012",
            "CurrentBackupRateInMegaBytesPerSecond": 0.1534,
            "ActualIncrementalBackupSizeInMegaBytes": 11.0,
            "NumberOfNodes": 2,
            "Status": "available",
            "ClusterVersion": "1.0",
            "MasterUsername": "adminuser",
            "AccountsWithRestoreAccess": [
                {
                    "AccountId": "123456789111"
            } ],
            "TotalBackupSizeInMegaBytes": 20.0,
            "DBName": "dev",
            "BackupProgressInMegaBytes": 11.0,
            "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
            "ElapsedTimeInSeconds": 0,
            "ClusterIdentifier": "mycluster",
            "SnapshotCreateTime": "2013-07-17T22:04:18.947Z",
            "AvailabilityZone": "us-west-2a",
            "NodeType": "dw.hs1.xlarge",
            "Encrypted": false,
            "SnapshotType": "manual",
            "Port": 5439,
            "SnapshotIdentifier": "my-snapshot-id"
    } ]
}
```
For more information, see [Amazon Redshift snapshots and backups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeClusterSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-snapshots.html) in *AWS CLI Command Reference*.

### `describe-cluster-subnet-groups`
<a name="redshift_DescribeClusterSubnetGroups_cli_2_topic"></a>

The following code example shows how to use `describe-cluster-subnet-groups`.

**AWS CLI**
**To get a description of all cluster subnet groups**
The following `describe-cluster-subnet-groups` example returns a description of all cluster subnet groups. By default, the output is in JSON format.

```
aws redshift describe-cluster-subnet-groups
```
Output:

```
{
    "ClusterSubnetGroups": [
        {
            "Subnets": [
                {
                    "SubnetStatus": "Active",
                    "SubnetIdentifier": "subnet-763fdd1c",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2a"
                    }
                }
            ],
            "VpcId": "vpc-7e3fdd14",
            "SubnetGroupStatus": "Complete",
            "Description": "My subnet group",
            "ClusterSubnetGroupName": "mysubnetgroup"
        }
    ]
}
```
For more information, see [Subnets for Redshift resources](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeClusterSubnetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-subnet-groups.html) in *AWS CLI Command Reference*.

### `describe-cluster-tracks`
<a name="redshift_DescribeClusterTracks_cli_2_topic"></a>

The following code example shows how to use `describe-cluster-tracks`.

**AWS CLI**
**To describe cluster tracks**
The following `describe-cluster-tracks` example displays details of the available maintenance tracks.

```
aws redshift describe-cluster-tracks \
    --maintenance-track-name {{current}}
```
Output:

```
{
    "MaintenanceTracks": [
        {
            "MaintenanceTrackName": "current",
            "DatabaseVersion": "1.0.11420",
            "UpdateTargets": [
                {
                    "MaintenanceTrackName": "preview_features",
                    "DatabaseVersion": "1.0.11746",
                    "SupportedOperations": [
                        {
                            "OperationName": "restore-from-cluster-snapshot"
                        }
                    ]
                },
                {
                    "MaintenanceTrackName": "trailing",
                    "DatabaseVersion": "1.0.11116",
                    "SupportedOperations": [
                        {
                            "OperationName": "restore-from-cluster-snapshot"
                        },
                        {
                            "OperationName": "modify-cluster"
                        }
                    ]
                }
            ]
        }
    ]
}
```
For more information, see [Choosing Cluster Maintenance Tracks](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeClusterTracks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-tracks.html) in *AWS CLI Command Reference*.

### `describe-cluster-versions`
<a name="redshift_DescribeClusterVersions_cli_2_topic"></a>

The following code example shows how to use `describe-cluster-versions`.

**AWS CLI**
**To get a description of all cluster versions**
The following `describe-cluster-versions` example returns a description of all cluster versions. By default, the output is in JSON format.

```
aws redshift describe-cluster-versions
```
Output:

```
{
    "ClusterVersions": [
        {
            "ClusterVersion": "1.0",
            "Description": "Initial release",
            "ClusterParameterGroupFamily": "redshift-1.0"
        } ]
}
```
For more information, see [Cluster versions for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeClusterVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-versions.html) in *AWS CLI Command Reference*.

### `describe-clusters`
<a name="redshift_DescribeClusters_cli_2_topic"></a>

The following code example shows how to use `describe-clusters`.

**AWS CLI**
**To get a description of all clusters**
The following `describe-clusters` example returns a description of all clusters for the account. By default, the output is in JSON format.

```
aws redshift describe-clusters
```
Output:

```
{
    "Clusters": [
        {
            "NodeType": "dw.hs1.xlarge",
            "Endpoint": {
                "Port": 5439,
                "Address": "mycluster.coqoarplqhsn.us-west-2.redshift.amazonaws.com"
            },
            "ClusterVersion": "1.0",
            "PubliclyAccessible": true,
            "MasterUsername": "adminuser",
            "ClusterParameterGroups": [
                {
                    "ParameterApplyStatus": "in-sync",
                    "ParameterGroupName": "default.redshift-1.0"
            } ],
            "ClusterSecurityGroups": [
                {
                    "Status": "active",
                    "ClusterSecurityGroupName": "default"
            } ],
            "AllowVersionUpgrade": true,
            "VpcSecurityGroups": [],
            "AvailabilityZone": "us-west-2a",
            "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
            "PreferredMaintenanceWindow": "sat:03:30-sat:04:00",
            "AutomatedSnapshotRetentionPeriod": 1,
            "ClusterStatus": "available",
            "ClusterIdentifier": "mycluster",
            "DBName": "dev",
            "NumberOfNodes": 2,
            "PendingModifiedValues": {}
    } ]
}
```
You can also obtain the same information in text format using the `--output text` option.

```
aws redshift describe-clusters \
    --output {{text}}
```
Output:

```
dw.hs1.xlarge       1.0     true    adminuser       True    us-west-2a      2013-01-22T21:59:29.559Z        sat:03:30-sat:04:00     1       available       mycluster       dev     2
ENDPOINT    5439    mycluster.coqoarplqhsn.us-west-2.redshift.amazonaws.com
in-sync     default.redshift-1.0
active      default
PENDINGMODIFIEDVALUES
```
For more information, see [Amazon Redshift provisioned clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-clusters.html) in *AWS CLI Command Reference*.

### `describe-default-cluster-parameters`
<a name="redshift_DescribeDefaultClusterParameters_cli_2_topic"></a>

The following code example shows how to use `describe-default-cluster-parameters`.

**AWS CLI**
**To get a description of default cluster parameters**
The following `describe-default-cluster-parameters` example returns a description of the default cluster parameters for the `redshift-1.0` family. By default, the output is in JSON format.

```
aws redshift describe-default-cluster-parameters \
    --parameter-group-family {{redshift-1.0}}
```
Output:

```
{
    "DefaultClusterParameters": {
        "ParameterGroupFamily": "redshift-1.0",
        "Parameters": [
            {
                "Description": "Sets the display format for date and time values.",
                "DataType": "string",
                "IsModifiable": true,
                "Source": "engine-default",
                "ParameterValue": "ISO, MDY",
                "ParameterName": "datestyle"
            },
            {
                "Description": "Sets the number of digits displayed for floating-point values",
                "DataType": "integer",
                "IsModifiable": true,
                "AllowedValues": "-15-2",
                "Source": "engine-default",
                "ParameterValue": "0",
                "ParameterName": "extra_float_digits"
            }
        ]
    }
}
```
To see a list of valid parameter group families, use the `describe-cluster-parameter-groups` command.
For more information, see [Amazon Redshift parameter groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeDefaultClusterParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-default-cluster-parameters.html) in *AWS CLI Command Reference*.

### `describe-event-categories`
<a name="redshift_DescribeEventCategories_cli_2_topic"></a>

The following code example shows how to use `describe-event-categories`.

**AWS CLI**
**To describe event categories for a cluster**
The following `describe-event-categories` example displays details for the event categories for a cluster.

```
aws redshift describe-event-categories \
    --source-type {{cluster}}
```
Output:

```
{
    "EventCategoriesMapList": [
        {
            "SourceType": "cluster",
            "Events": [
                {
                    "EventId": "REDSHIFT-EVENT-2000",
                    "EventCategories": [
                        "management"
                    ],
                    "EventDescription": "Cluster <cluster name> created at <time in UTC>.",
                    "Severity": "INFO"
                },
                {
                    "EventId": "REDSHIFT-EVENT-2001",
                    "EventCategories": [
                        "management"
                    ],
                    "EventDescription": "Cluster <cluster name> deleted at <time in UTC>.",
                    "Severity": "INFO"
                },
                {
                    "EventId": "REDSHIFT-EVENT-3625",
                    "EventCategories": [
                        "monitoring"
                    ],
                    "EventDescription": "The cluster <cluster name> can't be resumed with its previous elastic network interface <ENI id>. We will allocate a new elastic network interface and associate it with the cluster node.",
                    "Severity": "INFO"
                }
            ]
        }
    ]
}
```
For more information, see [Amazon Redshift provisioned cluster event notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeEventCategories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-event-categories.html) in *AWS CLI Command Reference*.

### `describe-event-subscriptions`
<a name="redshift_DescribeEventSubscriptions_cli_2_topic"></a>

The following code example shows how to use `describe-event-subscriptions`.

**AWS CLI**
**To describe event subscriptions**
The following `describe-event-subscriptions` example displays event notification subscriptions for the specified subscription.

```
aws redshift describe-event-subscriptions \
    --subscription-name {{mysubscription}}
```
Output:

```
{
    "EventSubscriptionsList": [
        {
            "CustomerAwsId": "123456789012",
            "CustSubscriptionId": "mysubscription",
            "SnsTopicArn": "arn:aws:sns:us-west-2:123456789012:MySNStopic",
            "Status": "active",
            "SubscriptionCreationTime": "2019-12-09T21:50:21.332Z",
            "SourceIdsList": [],
            "EventCategoriesList": [
                "management"
            ],
            "Severity": "ERROR",
            "Enabled": true,
            "Tags": []
        }
    ]
}
```
For more information, see [Subscribing to Amazon Redshift Event Notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeEventSubscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-event-subscriptions.html) in *AWS CLI Command Reference*.

### `describe-events`
<a name="redshift_DescribeEvents_cli_2_topic"></a>

The following code example shows how to use `describe-events`.

**AWS CLI**
**To describe all events**
The following `describe-events` example returns all events. By default, the output is in JSON format.

```
aws redshift describe-events
```
Output:

```
{
    "Events": [
        {
            "Date": "2013-01-22T19:17:03.640Z",
            "SourceIdentifier": "myclusterparametergroup",
            "Message": "Cluster parameter group myclusterparametergroup has been created.",
            "SourceType": "cluster-parameter-group"
        }
    ]
}
```
You can also obtain the same information in text format using the `--output text` option.

```
aws redshift describe-events \
    --output {{text}}
```
Output:

```
2013-01-22T19:17:03.640Z    myclusterparametergroup Cluster parameter group myclusterparametergroup has been created.       cluster-parameter-group
```
For more information, see [Amazon Redshift events](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-events.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-events.html) in *AWS CLI Command Reference*.

### `describe-hsm-client-certificates`
<a name="redshift_DescribeHsmClientCertificates_cli_2_topic"></a>

The following code example shows how to use `describe-hsm-client-certificates`.

**AWS CLI**
**To describe HSM client certificates**
The following `describe-hsm-client-certificates` example displays details for the specified HSM client certificate.

```
aws redshift describe-hsm-client-certificates \
    --hsm-client-certificate-identifier {{myhsmclientcert}}
```
Output:

```
{
    "HsmClientCertificates": [
        {
        "HsmClientCertificateIdentifier": "myhsmclientcert",
        "HsmClientCertificatePublicKey": "-----BEGIN CERTIFICATE-----\nEXAMPLECAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC\nVVMxCzAJBgNVBAEXAMPLERAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6\nb24xFDASBgNVBAsTC0lBTSBDb25zEXAMPLEwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd\nBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhEXAMPLEDI1MjA0EXAMPLEN\nEXAMPLE0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD\nVQQHEwdTZWF0dGEXAMPLEQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z\nb2xlMRIwEAYDVQQDEwlUZXN0Q2lsEXAMPLEdBgkqhkiG9w0BCQEWEG5vb25lQGFt\nYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIEXAMPLEMaK0dn+a4GmWIWJ\n21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T\nrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY67EXAMPLEE\nEXAMPLEZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4\nnUhVVxYUntneD9EXAMPLE6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb\nFFBjvSfpJIlJ00zbhNYS5f6GuoEDEXAMPLEBHjJnyp378OD8uTs7fLvjx79LjSTb\nNYiytVbZPQUQ5Yaxu2jXnimvw3rEXAMPLE=\n-----END CERTIFICATE-----\n",
        "Tags": []
        }
    ]
}
```
For more information, see [Amazon Redshift API Permissions Reference](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeHsmClientCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-client-certificates.html) in *AWS CLI Command Reference*.

### `describe-hsm-configurations`
<a name="redshift_DescribeHsmConfigurations_cli_2_topic"></a>

The following code example shows how to use `describe-hsm-configurations`.

**AWS CLI**
**To describe HSM configurations**
The following `describe-hsm-configurations` example displays details for the available HSM configurations for the calling AWS account.

```
aws redshift describe-hsm-configurations \
    --hsm-configuration-identifier {{myhsmconnection}}
```
Output:

```
{
    "HsmConfigurations": [
        {
            "HsmConfigurationIdentifier": "myhsmconnection",
            "Description": "My HSM connection",
            "HsmIpAddress": "192.0.2.09",
            "HsmPartitionName": "myhsmpartition",
            "Tags": []
        }
    ]
}
```
For more information, see [Encryption using hardware security modules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeHsmConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-configurations.html) in *AWS CLI Command Reference*.

### `describe-logging-status`
<a name="redshift_DescribeLoggingStatus_cli_2_topic"></a>

The following code example shows how to use `describe-logging-status`.

**AWS CLI**
**To describe logging status for a cluster**
The following `describe-logging-status` example displays whether information, such as queries and connection attempts, is being logged for a cluster.

```
aws redshift describe-logging-status \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "LoggingEnabled": false
}
```
For more information, see [Database Audit Logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeLoggingStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-logging-status.html) in *AWS CLI Command Reference*.

### `describe-node-configuration-options`
<a name="redshift_DescribeNodeConfigurationOptions_cli_2_topic"></a>

The following code example shows how to use `describe-node-configuration-options`.

**AWS CLI**
**To describe node configuration options**
The following `describe-node-configuration-options` example displays the properties of possible node configurations such as node type, number of nodes, and disk usage for the specified cluster snapshot.

```
aws redshift describe-node-configuration-options \
    --action-type {{restore-cluster}} \
    --snapshot-identifier {{rs:mycluster-2019-12-09-16-42-43}}
```
Output:

```
{
    "NodeConfigurationOptionList": [
        {
            "NodeType": "dc2.large",
            "NumberOfNodes": 2,
            "EstimatedDiskUtilizationPercent": 19.61
        },
        {
            "NodeType": "dc2.large",
            "NumberOfNodes": 4,
            "EstimatedDiskUtilizationPercent": 9.96
        },
        {
            "NodeType": "ds2.xlarge",
            "NumberOfNodes": 2,
            "EstimatedDiskUtilizationPercent": 1.53
        },
        {
            "NodeType": "ds2.xlarge",
            "NumberOfNodes": 4,
            "EstimatedDiskUtilizationPercent": 0.78
        }
    ]
}
```
For more information, see [Purchasing Amazon Redshift Reserved Nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeNodeConfigurationOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-node-configuration-options.html) in *AWS CLI Command Reference*.

### `describe-orderable-cluster-options`
<a name="redshift_DescribeOrderableClusterOptions_cli_2_topic"></a>

The following code example shows how to use `describe-orderable-cluster-options`.

**AWS CLI**
**To describe all orderable cluster options**
The following `describe-orderable-cluster-options` example returns descriptions of all orderable cluster options. By default, the output is in JSON format.

```
aws redshift describe-orderable-cluster-options
```
Output:

```
{
    "OrderableClusterOptions": [
        {
            "NodeType": "dw.hs1.8xlarge",
            "AvailabilityZones": [
                { "Name": "us-west-2a" },
                { "Name": "us-west-2b" },
                { "Name": "us-west-2c" } ],
            "ClusterVersion": "1.0",
            "ClusterType": "multi-node"
        },
        {
            "NodeType": "dw.hs1.xlarge",
            "AvailabilityZones": [
                { "Name": "us-west-2a" },
                { "Name": "us-west-2b" },
                { "Name": "us-west-2c" } ],
            "ClusterVersion": "1.0",
            "ClusterType": "multi-node"
        },
        {
            "NodeType": "dw.hs1.xlarge",
            "AvailabilityZones": [
                { "Name": "us-west-2a" },
                { "Name": "us-west-2b" },
                { "Name": "us-west-2c" } ],
            "ClusterVersion": "1.0",
            "ClusterType": "single-node"
        } ]
}
```
You can also obtain the same information in text format using the `--output text` option.

```
aws redshift describe-orderable-cluster-options \
    --output {{text}}
```
Output:

```
dw.hs1.8xlarge      1.0     multi-node
us-west-2a
us-west-2b
us-west-2c
dw.hs1.xlarge       1.0     multi-node
us-west-2a
us-west-2b
us-west-2c
dw.hs1.xlarge       1.0     single-node
us-west-2a
us-west-2b
us-west-2c
```
For more information, see [Amazon Redshift provisioned clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeOrderableClusterOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-orderable-cluster-options.html) in *AWS CLI Command Reference*.

### `describe-reserved-node-offerings`
<a name="redshift_DescribeReservedNodeOfferings_cli_2_topic"></a>

The following code example shows how to use `describe-reserved-node-offerings`.

**AWS CLI**
**To describe reserved node offerings**
The following `describe-reserved-node-offerings` example shows all of the reserved node offerings that are available for purchase.

```
aws redshift describe-reserved-node-offerings
```
Output:

```
{
    "ReservedNodeOfferings": [
        {
            "OfferingType": "Heavy Utilization",
            "FixedPrice": 3000.0,
            "NodeType": "dw.hs1.xlarge",
            "UsagePrice": 0.0,
            "RecurringCharges": [
                {
                    "RecurringChargeAmount": 0.114,
                    "RecurringChargeFrequency": "Hourly"
            } ],
            "Duration": 31536000,
            "ReservedNodeOfferingId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        {
            "OfferingType": "Heavy Utilization",
            "FixedPrice": 24000.0,
            "NodeType": "dw.hs1.8xlarge",
            "UsagePrice": 0.0,
            "RecurringCharges": [
                {
                    "RecurringChargeAmount": 0.912,
                    "RecurringChargeFrequency": "Hourly"
            } ],
            "Duration": 31536000,
            "ReservedNodeOfferingId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
    ]
}
```
If you want to purchase a reserved node offering, you can call `purchase-reserved-node-offering` using a valid *ReservedNodeOfferingId*.
For more information, see [Reserved nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeReservedNodeOfferings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-reserved-node-offerings.html) in *AWS CLI Command Reference*.

### `describe-reserved-nodes`
<a name="redshift_DescribeReservedNodes_cli_2_topic"></a>

The following code example shows how to use `describe-reserved-nodes`.

**AWS CLI**
**To describe reserved nodes**
The following `describe-reserved-nodes` example shows a reserved node offering that has been purchased.

```
aws redshift describe-reserved-nodes
```
Output:

```
{
    "ReservedNodes": [
        {
            "OfferingType": "Heavy Utilization",
            "FixedPrice": 3000.0,
            "NodeType": "dw.hs1.xlarge",
            "ReservedNodeId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "UsagePrice": 0.0,
            "RecurringCharges": [
                {
                    "RecurringChargeAmount": 0.21,
                    "RecurringChargeFrequency": "Hourly"
                } ],
            "NodeCount": 1,
            "State": "payment-pending",
            "StartTime": "2013-02-13T17:08:39.051Z",
            "Duration": 31536000,
            "ReservedNodeOfferingId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
        }
    ]
}
```
For more information, see [Reserved nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeReservedNodes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-reserved-nodes.html) in *AWS CLI Command Reference*.

### `describe-resize`
<a name="redshift_DescribeResize_cli_2_topic"></a>

The following code example shows how to use `describe-resize`.

**AWS CLI**
**To describe a resize**
The following `describe-resize` example describes the latest resize of a cluster. The request was for 3 nodes of type `dw.hs1.8xlarge`.

```
aws redshift describe-resize \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "Status": "NONE",
    "TargetClusterType": "multi-node",
    "TargetNodeType": "dw.hs1.8xlarge",
    "TargetNumberOfNodes": 3
}
```
For more information, see [Resizing a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/resizing-cluster.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeResize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-resize.html) in *AWS CLI Command Reference*.

### `describe-scheduled-actions`
<a name="redshift_DescribeScheduledActions_cli_2_topic"></a>

The following code example shows how to use `describe-scheduled-actions`.

**AWS CLI**
**To describe scheduled actions**
The following `describe-scheduled-actions` example displays details for any currently scheduled actions.

```
aws redshift describe-scheduled-actions
```
Output:

```
{
    "ScheduledActions": [
        {
            "ScheduledActionName": "resizecluster",
            "TargetAction": {
                "ResizeCluster": {
                    "ClusterIdentifier": "mycluster",
                    "NumberOfNodes": 4,
                    "Classic": false
                }
            },
            "Schedule": "at(2019-12-10T00:07:00)",
            "IamRole": "arn:aws:iam::123456789012:role/myRedshiftRole",
            "State": "ACTIVE",
            "NextInvocations": [
                "2019-12-10T00:07:00Z"
            ]
        }
    ]
}
```
For more information, see [Scheduling a resize](https://docs.aws.amazon.com/redshift/latest/mgmt/resizing-cluster.html#rs-restore-resize-overview-schedule) in the *Amazon Redshift Management Guide*.
+  For API details, see [DescribeScheduledActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-scheduled-actions.html) in *AWS CLI Command Reference*.

### `describe-snapshot-copy-grants`
<a name="redshift_DescribeSnapshotCopyGrants_cli_2_topic"></a>

The following code example shows how to use `describe-snapshot-copy-grants`.

**AWS CLI**
**To describe snapshot copy grants**
The following `describe-snapshot-copy-grants` example displays details for the specified cluster snapshot copy grant.

```
aws redshift describe-snapshot-copy-grants \
    --snapshot-copy-grant-name {{mysnapshotcopygrantname}}
```
Output:

```
{
    "SnapshotCopyGrants": [
        {
            "SnapshotCopyGrantName": "mysnapshotcopygrantname",
            "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY",
            "Tags": []
        }
    ]
}
```
For more information, see [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeSnapshotCopyGrants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-copy-grants.html) in *AWS CLI Command Reference*.

### `describe-snapshot-schedules`
<a name="redshift_DescribeSnapshotSchedules_cli_2_topic"></a>

The following code example shows how to use `describe-snapshot-schedules`.

**AWS CLI**
**To describe snapshot schedules**
The following `describe-snapshot-schedules` example displays details for the specified cluster snapshot schedule.

```
aws redshift describe-snapshot-schedules \
    --cluster-identifier {{mycluster}} \
    --schedule-identifier {{mysnapshotschedule}}
```
Output:

```
{
    "SnapshotSchedules": [
        {
            "ScheduleDefinitions": [
                "rate(12 hours)"
            ],
            "ScheduleIdentifier": "mysnapshotschedule",
            "ScheduleDescription": "My schedule description",
            "Tags": [],
            "AssociatedClusterCount": 1,
            "AssociatedClusters": [
                {
                    "ClusterIdentifier": "mycluster",
                    "ScheduleAssociationState": "ACTIVE"
                }
            ]
        }
    ]
}
```
For more information, see [Automated Snapshot Schedules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#automated-snapshot-schedules) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeSnapshotSchedules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-schedules.html) in *AWS CLI Command Reference*.

### `describe-storage`
<a name="redshift_DescribeStorage_cli_2_topic"></a>

The following code example shows how to use `describe-storage`.

**AWS CLI**
**To describe storage**
The following `describe-storage` example displays details about the backup storage and provisional storage sizes for the account.

```
aws redshift describe-storage
```
Output:

```
{
    "TotalBackupSizeInMegaBytes": 193149.0,
    "TotalProvisionedStorageInMegaBytes": 655360.0
}
```
For more information, see [Managing Snapshot Storage](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#managing-snapshot-storage) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeStorage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-storage.html) in *AWS CLI Command Reference*.

### `describe-table-restore-status`
<a name="redshift_DescribeTableRestoreStatus_cli_2_topic"></a>

The following code example shows how to use `describe-table-restore-status`.

**AWS CLI**
**To describe status of table restore requests from a cluster snapshot**
The following `describe-table-restore-status` example displays details for table restore requests made for the specified cluster.

```
aws redshift describe-table-restore-status \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "TableRestoreStatusDetails": [
        {
            "TableRestoreRequestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "Status": "IN_PROGRESS",
            "RequestTime": "2019-12-27T18:22:12.257Z",
            "ClusterIdentifier": "mycluster",
            "SnapshotIdentifier": "mysnapshotid",
            "SourceDatabaseName": "dev",
            "SourceSchemaName": "public",
            "SourceTableName": "mytable",
            "TargetDatabaseName": "dev",
            "TargetSchemaName": "public",
            "NewTableName": "mytable-clone"
        }
    ]
}
```
For more information, see [Restoring a Table from a Snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-table-from-snapshot.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeTableRestoreStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-table-restore-status.html) in *AWS CLI Command Reference*.

### `describe-tags`
<a name="redshift_DescribeTags_cli_2_topic"></a>

The following code example shows how to use `describe-tags`.

**AWS CLI**
**To describe tags**
The following `describe-tags` example displays the resources the specified cluster associated with the specified tag names and values.

```
aws redshift describe-tags \
    --resource-name {{arn:aws:redshift:us-west-2:123456789012:cluster:mycluster}} \
    --tag-keys {{clustertagkey}} \
    --tag-values {{clustertagvalue}}
```
Output:

```
{
    "TaggedResources": [
        {
            "Tag": {
                "Key": "clustertagkey",
                "Value": "clustertagvalue"
            },
            "ResourceName": "arn:aws:redshift:us-west-2:123456789012:cluster:mycluster",
            "ResourceType": "cluster"
        }
    ]
}
```
For more information, see [Tagging Resources in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-tagging.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-tags.html) in *AWS CLI Command Reference*.

### `disable-snapshot-copy`
<a name="redshift_DisableSnapshotCopy_cli_2_topic"></a>

The following code example shows how to use `disable-snapshot-copy`.

**AWS CLI**
**To disable snapshot copy for a cluster**
The following `disable-snapshot-copy` example disables the automatic copy of a snapshot for the specified cluster.

```
aws redshift disable-snapshot-copy \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "available",
        "ClusterAvailabilityStatus": "Available",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-05T18:44:36.991Z",
        "AutomatedSnapshotRetentionPeriod": 3,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sh-i9b431cd",
                "Status": "active"
            }
        ],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "ClusterSubnetGroupName": "default",
        "VpcId": "vpc-b1fel7t9",
        "AvailabilityZone": "us-west-2f",
        "PreferredMaintenanceWindow": "sat:16:00-sat:16:30",
        "PendingModifiedValues": {
            "NodeType": "dc2.large",
            "NumberOfNodes": 2,
            "ClusterType": "multi-node"
        },
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 4,
        "PubliclyAccessible": false,
        "Encrypted": false,
        "Tags": [
            {
                "Key": "mytags",
                "Value": "tag1"
            }
        ],
        "EnhancedVpcRouting": false,
        "IamRoles": [
            {
                "IamRoleArn": "arn:aws:iam::123456789012:role/myRedshiftRole",
                "ApplyStatus": "in-sync"
            }
        ],
        "MaintenanceTrackName": "current",
        "DeferredMaintenanceWindows": [],
        "ExpectedNextSnapshotScheduleTime": "2019-12-10T04:42:43.390Z",
        "ExpectedNextSnapshotScheduleTimeStatus": "OnTrack",
        "NextMaintenanceWindowStartTime": "2019-12-14T16:00:00Z"
    }
}
```
For more information, see [Copying Snapshots to Another AWS Region](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [DisableSnapshotCopy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/disable-snapshot-copy.html) in *AWS CLI Command Reference*.

### `enable-snapshot-copy`
<a name="redshift_EnableSnapshotCopy_cli_2_topic"></a>

The following code example shows how to use `enable-snapshot-copy`.

**AWS CLI**
**To enable snapshot copy for a cluster**
The following `enable-snapshot-copy` example enables the automatic copy of a snapshot for the specified cluster.

```
aws redshift enable-snapshot-copy \
    --cluster-identifier {{mycluster}} \
    --destination-region {{us-west-1}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "available",
        "ClusterAvailabilityStatus": "Available",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-05T18:44:36.991Z",
        "AutomatedSnapshotRetentionPeriod": 3,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sh-f4c731cd",
                "Status": "active"
            }
        ],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "ClusterSubnetGroupName": "default",
        "VpcId": "vpc-b1ael7t9",
        "AvailabilityZone": "us-west-2f",
        "PreferredMaintenanceWindow": "sat:16:00-sat:16:30",
        "PendingModifiedValues": {
            "NodeType": "dc2.large",
            "NumberOfNodes": 2,
            "ClusterType": "multi-node"
        },
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 4,
        "PubliclyAccessible": false,
        "Encrypted": false,
        "ClusterSnapshotCopyStatus": {
            "DestinationRegion": "us-west-1",
            "RetentionPeriod": 7,
            "ManualSnapshotRetentionPeriod": -1
        },
        "Tags": [
            {
                "Key": "mytags",
                "Value": "tag1"
            }
        ],
        "EnhancedVpcRouting": false,
        "IamRoles": [
            {
                "IamRoleArn": "arn:aws:iam::123456789012:role/myRedshiftRole",
                "ApplyStatus": "in-sync"
            }
        ],
        "MaintenanceTrackName": "current",
        "DeferredMaintenanceWindows": [],
        "ExpectedNextSnapshotScheduleTime": "2019-12-10T04:42:43.390Z",
        "ExpectedNextSnapshotScheduleTimeStatus": "OnTrack",
        "NextMaintenanceWindowStartTime": "2019-12-14T16:00:00Z"
    }
}
```
For more information, see [Copying Snapshots to Another AWS Region](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [EnableSnapshotCopy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/enable-snapshot-copy.html) in *AWS CLI Command Reference*.

### `get-cluster-credentials`
<a name="redshift_GetClusterCredentials_cli_2_topic"></a>

The following code example shows how to use `get-cluster-credentials`.

**AWS CLI**
**To get cluster credentials for an AWS account**
The following `get-cluster-credentials` example retrieves temporary credentials that enable access to an Amazon Redshift database.

```
aws redshift get-cluster-credentials \
    --db-user {{adminuser}} \
    --db-name {{dev}} \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "DbUser": "IAM:adminuser",
    "DbPassword": "AMAFUyyuros/QjxPTtgzcsuQsqzIasdzJEN04aCtWDzXx1O9d6UmpkBtvEeqFly/EXAMPLE==",
    "Expiration": "2019-12-10T17:25:05.770Z"
}
```
For more information, see [Generating IAM Database Credentials Using the Amazon Redshift CLI or API](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-iam-credentials-cli-api.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [GetClusterCredentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-cluster-credentials.html) in *AWS CLI Command Reference*.

### `get-reserved-node-exchange-offerings`
<a name="redshift_GetReservedNodeExchangeOfferings_cli_2_topic"></a>

The following code example shows how to use `get-reserved-node-exchange-offerings`.

**AWS CLI**
**To get reserved node exchange offerings**
The following `get-reserved-node-exchange-offerings` example retrieves an array of `DC2` `ReservedNodeOfferings` that match the specified `DC1` reserved node.

```
aws redshift get-reserved-node-exchange-offerings \
    --reserved-node-id {{12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE}}
```
Output:

```
{
    "ReservedNodeOfferings": [
        {
            "ReservedNodeOfferingId": "12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE",
            "NodeType": "dc2.large",
            "Duration": 31536000,
            "FixedPrice": 0.0,
            "UsagePrice": 0.0,
            "CurrencyCode": "USD",
            "OfferingType": "All Upfront",
            "RecurringCharges": [
                {
                    "RecurringChargeAmount": 0.0,
                    "RecurringChargeFrequency": "Hourly"
                }
            ],
            "ReservedNodeOfferingType": "Regular"
        }
    ]
}
```
For more information, see [Upgrading Reserved Nodes With the AWS CLI](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-offering-console.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [GetReservedNodeExchangeOfferings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-reserved-node-exchange-offerings.html) in *AWS CLI Command Reference*.

### `modify-cluster-iam-roles`
<a name="redshift_ModifyClusterIamRoles_cli_2_topic"></a>

The following code example shows how to use `modify-cluster-iam-roles`.

**AWS CLI**
**To modify the IAM role for a cluster**
The following `modify-cluster-iam-roles` example removes the specified AWS IAM role from the specified cluster.

```
aws redshift modify-cluster-iam-roles \
    --cluster-identifier {{mycluster}} \
    --remove-iam-roles {{arn:aws:iam::123456789012:role/myRedshiftRole}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "available",
        "ClusterAvailabilityStatus": "Available",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-05T18:44:36.991Z",
        "AutomatedSnapshotRetentionPeriod": 3,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sh-f9b731sd",
                "Status": "active"
            }
        ],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "ClusterSubnetGroupName": "default",
        "VpcId": "vpc-b2fal7t9",
        "AvailabilityZone": "us-west-2f",
        "PreferredMaintenanceWindow": "sat:16:00-sat:16:30",
        "PendingModifiedValues": {
            "NodeType": "dc2.large",
            "NumberOfNodes": 2,
            "ClusterType": "multi-node"
        },
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 4,
        "PubliclyAccessible": false,
        "Encrypted": false,
        "Tags": [
            {
                "Key": "mytags",
                "Value": "tag1"
            }
        ],
        "EnhancedVpcRouting": false,
        "IamRoles": [],
        "MaintenanceTrackName": "current",
        "DeferredMaintenanceWindows": [],
        "ExpectedNextSnapshotScheduleTime": "2019-12-11T04:42:55.631Z",
        "ExpectedNextSnapshotScheduleTimeStatus": "OnTrack",
        "NextMaintenanceWindowStartTime": "2019-12-14T16:00:00Z"
    }
}
```
For more information, see [Using Identity-Based Policies (IAM Policies) for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [ModifyClusterIamRoles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-iam-roles.html) in *AWS CLI Command Reference*.

### `modify-cluster-maintenance`
<a name="redshift_ModifyClusterMaintenance_cli_2_topic"></a>

The following code example shows how to use `modify-cluster-maintenance`.

**AWS CLI**
**To modify cluster maintenance**
The following `modify-cluster-maintenance` example defers the maintenance of the specified cluster by 30 days.

```
aws redshift modify-cluster-maintenance \
    --cluster-identifier {{mycluster}} \
    --defer-maintenance \
    --defer-maintenance-duration {{30}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "available",
        "ClusterAvailabilityStatus": "Available",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-05T18:44:36.991Z",
        "AutomatedSnapshotRetentionPeriod": 3,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sh-a1a123ab",
                "Status": "active"
            }
        ],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "ClusterSubnetGroupName": "default",
        "VpcId": "vpc-b1ael7t9",
        "AvailabilityZone": "us-west-2f",
        "PreferredMaintenanceWindow": "sat:16:00-sat:16:30",
        "PendingModifiedValues": {
            "NodeType": "dc2.large",
            "NumberOfNodes": 2,
            "ClusterType": "multi-node"
        },
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 4,
        "PubliclyAccessible": false,
        "Encrypted": false,
        "Tags": [
            {
                "Key": "mytags",
                "Value": "tag1"
            }
        ],
        "EnhancedVpcRouting": false,
        "IamRoles": [],
        "MaintenanceTrackName": "current",
        "DeferredMaintenanceWindows": [
            {
                "DeferMaintenanceIdentifier": "dfm-mUdVIfFcT1B4SGhw6fyF",
                "DeferMaintenanceStartTime": "2019-12-10T18:18:39.354Z",
                "DeferMaintenanceEndTime": "2020-01-09T18:18:39.354Z"
            }
        ],
        "ExpectedNextSnapshotScheduleTime": "2019-12-11T04:42:55.631Z",
        "ExpectedNextSnapshotScheduleTimeStatus": "OnTrack",
        "NextMaintenanceWindowStartTime": "2020-01-11T16:00:00Z"
    }
}
```
For more information, see [Cluster Maintenance](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [ModifyClusterMaintenance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-maintenance.html) in *AWS CLI Command Reference*.

### `modify-cluster-parameter-group`
<a name="redshift_ModifyClusterParameterGroup_cli_2_topic"></a>

The following code example shows how to use `modify-cluster-parameter-group`.

**AWS CLI**
**To modify a parameter in a parameter group**
The following `modify-cluster-parameter-group` example modifies the *wlm\_json\_configuration* parameter for workload management. It accepts the parameters from a file that contains the JSON contents shown below.

```
aws redshift modify-cluster-parameter-group \
    --parameter-group-name {{myclusterparametergroup}} \
    --parameters {{file://modify_pg.json}}
```
Contents of `modify_pg.json`:

```
[
    {
        "ParameterName": "wlm_json_configuration",
        "ParameterValue": "[{\"user_group\":\"example_user_group1\",\"query_group\": \"example_query_group1\", \"query_concurrency\":7},{\"query_concurrency\":5}]"
    }
]
```
Output:

```
{
    "ParameterGroupStatus": "Your parameter group has been updated but changes won't get applied until you reboot the associated Clusters.",
    "ParameterGroupName": "myclusterparametergroup"
}
```
For more information, see [Modifying a parameter group](https://docs.aws.amazon.com/redshift/latest/mgmt/parameter-group-modify.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [ModifyClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-parameter-group.html) in *AWS CLI Command Reference*.

### `modify-cluster-snapshot-schedule`
<a name="redshift_ModifyClusterSnapshotSchedule_cli_2_topic"></a>

The following code example shows how to use `modify-cluster-snapshot-schedule`.

**AWS CLI**
**To modify cluster snapshot schedule**
The following `modify-cluster-snapshot-schedule` example removes the specified snapshot schedule from the specified cluster.

```
aws redshift modify-cluster-snapshot-schedule \
    --cluster-identifier {{mycluster}} \
    --schedule-identifier {{mysnapshotschedule}} \
    --disassociate-schedule
```
This command produces no output.
For more information, see [Automated Snapshot Schedules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#automated-snapshot-schedules) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [ModifyClusterSnapshotSchedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot-schedule.html) in *AWS CLI Command Reference*.

### `modify-cluster-snapshot`
<a name="redshift_ModifyClusterSnapshot_cli_2_topic"></a>

The following code example shows how to use `modify-cluster-snapshot`.

**AWS CLI**
**To modify cluster snapshot**
The following `modify-cluster-snapshot` example sets the manual retention period setting for the specified cluster snapshot to value of 10 days.

```
aws redshift modify-cluster-snapshot \
    --snapshot-identifier {{mycluster-2019-11-06-16-32}} \
    --manual-snapshot-retention-period {{10}}
```
Output:

```
{
    "Snapshot": {
        "SnapshotIdentifier": "mycluster-2019-11-06-16-32",
        "ClusterIdentifier": "mycluster",
        "SnapshotCreateTime": "2019-12-07T00:34:05.633Z",
        "Status": "available",
        "Port": 5439,
        "AvailabilityZone": "us-west-2f",
        "ClusterCreateTime": "2019-12-05T18:44:36.991Z",
        "MasterUsername": "adminuser",
        "ClusterVersion": "1.0",
        "SnapshotType": "manual",
        "NodeType": "dc2.large",
        "NumberOfNodes": 2,
        "DBName": "dev",
        "VpcId": "vpc-b1cel7t9",
        "Encrypted": false,
        "EncryptedWithHSM": false,
        "OwnerAccount": "123456789012",
        "TotalBackupSizeInMegaBytes": 64384.0,
        "ActualIncrementalBackupSizeInMegaBytes": 24.0,
        "BackupProgressInMegaBytes": 24.0,
        "CurrentBackupRateInMegaBytesPerSecond": 13.0011,
        "EstimatedSecondsToCompletion": 0,
        "ElapsedTimeInSeconds": 1,
        "Tags": [
            {
                "Key": "mytagkey",
                "Value": "mytagvalue"
            }
        ],
        "EnhancedVpcRouting": false,
        "MaintenanceTrackName": "current",
        "ManualSnapshotRetentionPeriod": 10,
        "ManualSnapshotRemainingDays": 6,
        "SnapshotRetentionStartTime": "2019-12-07T00:34:07.479Z"
    }
}
```
For more information, see [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [ModifyClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot.html) in *AWS CLI Command Reference*.

### `modify-cluster-subnet-group`
<a name="redshift_ModifyClusterSubnetGroup_cli_2_topic"></a>

The following code example shows how to use `modify-cluster-subnet-group`.

**AWS CLI**
**To modify the subnets in a cluster subnet group**
The following `modify-cluster-subnet-group` example modifies the list of subnets in a cluster subnet group. By default, the output is in JSON format.

```
aws redshift modify-cluster-subnet-group \
    --cluster-subnet-group-name {{mysubnetgroup}} \
    --subnet-ids {{subnet-763fdd1}} {{subnet-ac830e9}}
```
Output:

```
{
    "ClusterSubnetGroup":
    {
        "Subnets": [
            {
                "SubnetStatus": "Active",
                "SubnetIdentifier": "subnet-763fdd1c",
                "SubnetAvailabilityZone":
                    { "Name": "us-west-2a" }
            },
            {
                "SubnetStatus": "Active",
                "SubnetIdentifier": "subnet-ac830e9",
                "SubnetAvailabilityZone":
                    { "Name": "us-west-2b" }
            } ],
        "VpcId": "vpc-7e3fdd14",
        "SubnetGroupStatus": "Complete",
        "Description": "My subnet group",
        "ClusterSubnetGroupName": "mysubnetgroup"
    }
}
```
For more information, see [Modifying a cluster subnet group](https://docs.aws.amazon.com/redshift/latest/mgmt/modify-cluster-subnet-group.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [ModifyClusterSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-subnet-group.html) in *AWS CLI Command Reference*.

### `modify-cluster`
<a name="redshift_ModifyCluster_cli_2_topic"></a>

The following code example shows how to use `modify-cluster`.

**AWS CLI**
**Example 1: To associate a security group with a cluster**
The following `modify-cluster` example associates a cluster security group with the specified cluster.

```
aws redshift modify-cluster \
    --cluster-identifier {{mycluster}} \
    --cluster-security-groups {{mysecuritygroup}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "available",
        "ClusterAvailabilityStatus": "Available",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-02T22:45:07.890Z",
        "AutomatedSnapshotRetentionPeriod": 1,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [
            {
                "ClusterSecurityGroupName": "default",
                "Status": "removing"
            },
            {
                "ClusterSecurityGroupName": "mysecuritygroup",
                "Status": "adding"
            }
        ],
        "VpcSecurityGroups": [],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "AvailabilityZone": "us-west-2a",
        "PreferredMaintenanceWindow": "sat:03:30-sat:04:00",
        "PendingModifiedValues": {},
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 2,
        "PubliclyAccessible": true,
        "Encrypted": false,
        "Tags": [],
        "EnhancedVpcRouting": false,
        "IamRoles": [],
        "MaintenanceTrackName": "current"
    }
}
```
For more information, see [Modifying a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/modify-cluster.html) in the *Amazon Redshift Management Guide*.
**Example 2: To modify the maintenance window for a cluster**
The following `modify-cluster` example changes the weekly preferred maintenance window for a cluster to be the minimum four hour window starting Sundays at 11:15 PM, and ending Mondays at 3:15 AM.

```
aws redshift modify-cluster \
    --cluster-identifier {{mycluster}} \
    --preferred-maintenance-window {{Sun:23:15-Mon:03:15}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "available",
        "ClusterAvailabilityStatus": "Available",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-02T22:45:07.890Z",
        "AutomatedSnapshotRetentionPeriod": 1,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [
            {
                "ClusterSecurityGroupName": "default",
                "Status": "active"
            }
        ],
        "VpcSecurityGroups": [],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "AvailabilityZone": "us-west-2a",
        "PreferredMaintenanceWindow": "sun:23:15-mon:03:15",
        "PendingModifiedValues": {},
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 2,
        "PubliclyAccessible": true,
        "Encrypted": false,
        "Tags": [],
        "EnhancedVpcRouting": false,
        "IamRoles": [],
        "MaintenanceTrackName": "current"
    }
}
```
For more information, see [Maintenance windows](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-considerations.html#rs-maintenance-windows) in the *Amazon Redshift Management Guide*.
**Example 3: To change the master password for the cluster**
The following `modify-cluster` example changes the master password for a cluster.

```
aws redshift modify-cluster \
    --cluster-identifier {{mycluster}} \
    --master-user-password {{A1b2c3d4}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "available",
        "ClusterAvailabilityStatus": "Available",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-02T22:45:07.890Z",
        "AutomatedSnapshotRetentionPeriod": 1,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [
            {
                "ClusterSecurityGroupName": "default",
                "Status": "active"
            }
        ],
        "VpcSecurityGroups": [],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "AvailabilityZone": "us-west-2a",
        "PreferredMaintenanceWindow": "sat:03:30-sat:04:00",
        "PendingModifiedValues": {
            "MasterUserPassword": "****"
        },
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 2,
        "PubliclyAccessible": true,
        "Encrypted": false,
        "Tags": [],
        "EnhancedVpcRouting": false,
        "IamRoles": [],
        "MaintenanceTrackName": "current"
    }
}
```
For more information, see [Modifying a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/modify-cluster.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [ModifyCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster.html) in *AWS CLI Command Reference*.

### `modify-event-subscription`
<a name="redshift_ModifyEventSubscription_cli_2_topic"></a>

The following code example shows how to use `modify-event-subscription`.

**AWS CLI**
**To modify event subscription**
The following `modify-event-subscription` example disables the specified event notification subscription.

```
aws redshift modify-event-subscription \
    --subscription-name {{mysubscription}} \
    --no-enabled
```
Output:

```
{
    "EventSubscription": {
        "CustomerAwsId": "123456789012",
        "CustSubscriptionId": "mysubscription",
        "SnsTopicArn": "arn:aws:sns:us-west-2:123456789012:MySNStopic",
        "Status": "active",
        "SubscriptionCreationTime": "2019-12-09T21:50:21.332Z",
        "SourceIdsList": [],
        "EventCategoriesList": [
            "management"
        ],
        "Severity": "ERROR",
        "Enabled": false,
        "Tags": []
    }
}
```
For more information, see [Subscribing to Amazon Redshift Event Notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [ModifyEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-event-subscription.html) in *AWS CLI Command Reference*.

### `modify-scheduled-action`
<a name="redshift_ModifyScheduledAction_cli_2_topic"></a>

The following code example shows how to use `modify-scheduled-action`.

**AWS CLI**
**To modify scheduled action**
The following `modify-scheduled-action` example adds a description to the specified existing scheduled action.

```
aws redshift modify-scheduled-action \
    --scheduled-action-name {{myscheduledaction}} \
    --scheduled-action-description {{"My scheduled action"}}
```
Output:

```
{
    "ScheduledActionName": "myscheduledaction",
    "TargetAction": {
        "ResizeCluster": {
            "ClusterIdentifier": "mycluster",
            "NumberOfNodes": 2,
            "Classic": false
        }
    },
    "Schedule": "at(2019-12-25T00:00:00)",
    "IamRole": "arn:aws:iam::123456789012:role/myRedshiftRole",
    "ScheduledActionDescription": "My scheduled action",
    "State": "ACTIVE",
    "NextInvocations": [
        "2019-12-25T00:00:00Z"
    ]
}
```
For more information, see [Scheduling a resize](https://docs.aws.amazon.com/redshift/latest/mgmt/resizing-cluster.html#rs-restore-resize-overview-schedule) in the *Amazon Redshift Management Guide*.
+  For API details, see [ModifyScheduledAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-scheduled-action.html) in *AWS CLI Command Reference*.

### `modify-snapshot-copy-retention-period`
<a name="redshift_ModifySnapshotCopyRetentionPeriod_cli_2_topic"></a>

The following code example shows how to use `modify-snapshot-copy-retention-period`.

**AWS CLI**
**To modify snapshot copy retention period**
The following `modify-snapshot-copy-retention-period` example modifies the number of days to retain snapshots for the specified cluster in the destination AWS Region after they are copied from the source AWS Region.

```
aws redshift modify-snapshot-copy-retention-period \
    --cluster-identifier {{mycluster}} \
    --retention-period {{15}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "available",
        "ClusterAvailabilityStatus": "Available",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-05T18:44:36.991Z",
        "AutomatedSnapshotRetentionPeriod": 3,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sh-a1a123ab",
                "Status": "active"
            }
        ],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "ClusterSubnetGroupName": "default",
        "VpcId": "vpc-b1fet7t9",
        "AvailabilityZone": "us-west-2f",
        "PreferredMaintenanceWindow": "sat:16:00-sat:16:30",
        "PendingModifiedValues": {
            "NodeType": "dc2.large",
            "NumberOfNodes": 2,
            "ClusterType": "multi-node"
        },
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 4,
        "PubliclyAccessible": false,
        "Encrypted": false,
        "ClusterSnapshotCopyStatus": {
            "DestinationRegion": "us-west-1",
            "RetentionPeriod": 15,
            "ManualSnapshotRetentionPeriod": -1
        },
        "Tags": [
            {
                "Key": "mytags",
                "Value": "tag1"
            }
        ],
        "EnhancedVpcRouting": false,
        "IamRoles": [],
        "MaintenanceTrackName": "current",
        "DeferredMaintenanceWindows": [
            {
                "DeferMaintenanceIdentifier": "dfm-mUdVSfDcT1F4SGhw6fyF",
                "DeferMaintenanceStartTime": "2019-12-10T18:18:39.354Z",
                "DeferMaintenanceEndTime": "2020-01-09T18:18:39.354Z"
            }
        ],
        "NextMaintenanceWindowStartTime": "2020-01-11T16:00:00Z"
    }
}
```
For more information, see [Snapshot Schedule Format](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#working-with-snapshot-scheduling) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [ModifySnapshotCopyRetentionPeriod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-copy-retention-period.html) in *AWS CLI Command Reference*.

### `modify-snapshot-schedule`
<a name="redshift_ModifySnapshotSchedule_cli_2_topic"></a>

The following code example shows how to use `modify-snapshot-schedule`.

**AWS CLI**
**To modify snapshot schedule**
The following `modify-snapshot-schedule` example modifies the rate of the specified snapshot schedule to every 10 hours.

```
aws redshift modify-snapshot-schedule \
    --schedule-identifier {{mysnapshotschedule}} \
    --schedule-definitions {{"rate(10 hours)"}}
```
Output:

```
{
    "ScheduleDefinitions": [
        "rate(10 hours)"
    ],
    "ScheduleIdentifier": "mysnapshotschedule",
    "ScheduleDescription": "My schedule description",
    "Tags": []
}
```
For more information, see [Snapshot Schedule Format](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#working-with-snapshot-scheduling) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [ModifySnapshotSchedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-schedule.html) in *AWS CLI Command Reference*.

### `purchase-reserved-node-offering`
<a name="redshift_PurchaseReservedNodeOffering_cli_2_topic"></a>

The following code example shows how to use `purchase-reserved-node-offering`.

**AWS CLI**
**To purchase a reserved node**
The following `purchase-reserved-node-offering` example purchases a reserved node offering. The `reserved-node-offering-id` is obtained by calling `describe-reserved-node-offerings`.

```
aws redshift purchase-reserved-node-offering \
    --reserved-node-offering-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "ReservedNode": {
        "OfferingType": "Heavy Utilization",
        "FixedPrice": 3000.0,
        "NodeType": "dw.hs1.xlarge",
        "ReservedNodeId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "UsagePrice": 0.0,
        "RecurringCharges": [
            {
                "RecurringChargeAmount": 0.114,
                "RecurringChargeFrequency": "Hourly"
            }
        ],
        "NodeCount": 1,
        "State": "payment-pending",
        "StartTime": "2013-02-13T17:08:39.051Z",
        "Duration": 31536000,
        "ReservedNodeOfferingId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
}
```
For more information, see [Purchasing a reserved node](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-offering-console.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [PurchaseReservedNodeOffering](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/purchase-reserved-node-offering.html) in *AWS CLI Command Reference*.

### `reboot-cluster`
<a name="redshift_RebootCluster_cli_2_topic"></a>

The following code example shows how to use `reboot-cluster`.

**AWS CLI**
**To reboot a cluster**
The following `reboot-cluster` example reboots a cluster. By default, the output is in JSON format.

```
aws redshift reboot-cluster \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "Cluster": {
        "NodeType": "dw.hs1.xlarge",
        "Endpoint": {
            "Port": 5439,
            "Address": "mycluster.coqoarplqhsn.us-west-2.redshift.amazonaws.com"
        },
        "ClusterVersion": "1.0",
        "PubliclyAccessible": true,
        "MasterUsername": "adminuser",
        "ClusterParameterGroups": [
            {
                "ParameterApplyStatus": "in-sync",
                "ParameterGroupName": "default.redshift-1.0"
            }
        ],
        "ClusterSecurityGroups": [
            {
                "Status": "active",
                "ClusterSecurityGroupName": "default"
            }
        ],
        "AllowVersionUpgrade": true,
        "VpcSecurityGroups": [],
        "AvailabilityZone": "us-west-2a",
        "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
        "PreferredMaintenanceWindow": "sun:23:15-mon:03:15",
        "AutomatedSnapshotRetentionPeriod": 1,
        "ClusterStatus": "rebooting",
        "ClusterIdentifier": "mycluster",
        "DBName": "dev",
        "NumberOfNodes": 2,
        "PendingModifiedValues": {}
    }
}
```
For more information, see [Rebooting a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/reboot-cluster.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [RebootCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reboot-cluster.html) in *AWS CLI Command Reference*.

### `reset-cluster-parameter-group`
<a name="redshift_ResetClusterParameterGroup_cli_2_topic"></a>

The following code example shows how to use `reset-cluster-parameter-group`.

**AWS CLI**
**To reset parameters in a parameter group**
The following `reset-cluster-parameter-group` example resets all of the parameters in a parameter group.

```
aws redshift reset-cluster-parameter-group \
    --parameter-group-name {{myclusterparametergroup}} \
    --reset-all-parameters
```
Output:

```
{
    "ParameterGroupName": "myclusterparametergroup",
    "ParameterGroupStatus": "Your parameter group has been updated but changes won't get applied until you reboot the associated Clusters."
}
```
For more information, see [Amazon Redshift parameter groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [ResetClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reset-cluster-parameter-group.html) in *AWS CLI Command Reference*.

### `resize-cluster`
<a name="redshift_ResizeCluster_cli_2_topic"></a>

The following code example shows how to use `resize-cluster`.

**AWS CLI**
**To resize cluster**
The following `resize-cluster` example resizes the specified cluster.

```
aws redshift resize-cluster \
    --cluster-identifier {{mycluster}} \
    --cluster-type {{multi-node}} \
    --node-type {{dc2.large}} \
    --number-of-nodes {{6}} \
    --classic
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "resizing",
        "ClusterAvailabilityStatus": "Modifying",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-05T18:44:36.991Z",
        "AutomatedSnapshotRetentionPeriod": 3,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sh-a1a123ab",
                "Status": "active"
            }
        ],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "ClusterSubnetGroupName": "default",
        "VpcId": "vpc-a1abc1a1",
        "AvailabilityZone": "us-west-2f",
        "PreferredMaintenanceWindow": "sat:16:00-sat:16:30",
        "PendingModifiedValues": {
            "NodeType": "dc2.large",
            "NumberOfNodes": 6,
            "ClusterType": "multi-node"
        },
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 4,
        "PubliclyAccessible": false,
        "Encrypted": false,
        "Tags": [
            {
                "Key": "mytags",
                "Value": "tag1"
            }
        ],
        "EnhancedVpcRouting": false,
        "IamRoles": [],
        "MaintenanceTrackName": "current",
        "DeferredMaintenanceWindows": [
            {
                "DeferMaintenanceIdentifier": "dfm-mUdVCfDcT1B4SGhw6fyF",
                "DeferMaintenanceStartTime": "2019-12-10T18:18:39.354Z",
                "DeferMaintenanceEndTime": "2020-01-09T18:18:39.354Z"
            }
        ],
        "NextMaintenanceWindowStartTime": "2020-01-11T16:00:00Z",
        "ResizeInfo": {
            "ResizeType": "ClassicResize",
            "AllowCancelResize": true
        }
    }
}
```
For more information, see [Resizing a Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [ResizeCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resize-cluster.html) in *AWS CLI Command Reference*.

### `restore-from-cluster-snapshot`
<a name="redshift_RestoreFromClusterSnapshot_cli_2_topic"></a>

The following code example shows how to use `restore-from-cluster-snapshot`.

**AWS CLI**
**To restore a cluster from a snapshot**
The following `restore-from-cluster-snapshot` example restores a cluster from a snapshot.

```
aws redshift restore-from-cluster-snapshot \
    --cluster-identifier {{mycluster-clone}} \
    --snapshot-identifier {{my-snapshot-id}}
```
Output:

```
{
    "Cluster": {
        "NodeType": "dw.hs1.xlarge",
        "ClusterVersion": "1.0",
        "PubliclyAccessible": true,
        "MasterUsername": "adminuser",
        "ClusterParameterGroups": [
            {
                "ParameterApplyStatus": "in-sync",
                "ParameterGroupName": "default.redshift-1.0"
            }
        ],
        "ClusterSecurityGroups": [
            {
                "Status": "active",
                "ClusterSecurityGroupName": "default"
            }
        ],
        "AllowVersionUpgrade": true,
        "VpcSecurityGroups": [],
        "PreferredMaintenanceWindow": "sun:23:15-mon:03:15",
        "AutomatedSnapshotRetentionPeriod": 1,
        "ClusterStatus": "creating",
        "ClusterIdentifier": "mycluster-clone",
        "DBName": "dev",
        "NumberOfNodes": 2,
        "PendingModifiedValues": {}
    }
}
```
For more information, see [Restoring a cluster from a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html) in the *Amazon Redshift Management Guide*.
+  For API details, see [RestoreFromClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-from-cluster-snapshot.html) in *AWS CLI Command Reference*.

### `restore-table-from-cluster-snapshot`
<a name="redshift_RestoreTableFromClusterSnapshot_cli_2_topic"></a>

The following code example shows how to use `restore-table-from-cluster-snapshot`.

**AWS CLI**
**To restore table from a cluster snapshot**
The following `restore-table-from-cluster-snapshot` example creates a new table from the specified table in the specified cluster snapshot.

```
aws redshift restore-table-from-cluster-snapshot \
    --cluster-identifier {{mycluster}} \
    --snapshot-identifier {{mycluster-2019-11-19-16-17}} \
    --source-database-name {{dev}} \
    --source-schema-name {{public}} \
    --source-table-name {{mytable}} \
    --target-database-name {{dev}} \
    --target-schema-name {{public}} \
    --new-table-name {{mytable-clone}}
```
Output:

```
{
    "TableRestoreStatus": {
        "TableRestoreRequestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "Status": "PENDING",
        "RequestTime": "2019-12-20T00:20:16.402Z",
        "ClusterIdentifier": "mycluster",
        "SnapshotIdentifier": "mycluster-2019-11-19-16-17",
        "SourceDatabaseName": "dev",
        "SourceSchemaName": "public",
        "SourceTableName": "mytable",
        "TargetDatabaseName": "dev",
        "TargetSchemaName": "public",
        "NewTableName": "mytable-clone"
    }
}
```
For more information, see [Restoring a Table from a Snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-table-from-snapshot.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [RestoreTableFromClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-table-from-cluster-snapshot.html) in *AWS CLI Command Reference*.

### `revoke-cluster-security-group-ingress`
<a name="redshift_RevokeClusterSecurityGroupIngress_cli_2_topic"></a>

The following code example shows how to use `revoke-cluster-security-group-ingress`.

**AWS CLI**
**Example 1: To revoke access from an EC2 security group**
The following `revoke-cluster-security-group-ingress` example revokes access to a named Amazon EC2 security group.

```
aws redshift revoke-cluster-security-group-ingress \
    --cluster-security-group-name {{mysecuritygroup}} \
    --ec2-security-group-name {{myec2securitygroup}} \
    --ec2-security-group-owner-id {{123456789012}}
```
Output:

```
{
    "ClusterSecurityGroup": {
        "ClusterSecurityGroupName": "mysecuritygroup",
        "Description": "This is my cluster security group",
        "EC2SecurityGroups": [],
        "IPRanges": [],
        "Tags": []
    }
}
```
For more information, see [Configuring security group communication settings for an Amazon Redshift cluster or an Amazon Redshift Serverless workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-security-group-public-private.html) in the *Amazon Redshift Cluster Management Guide*.
**Example 2: To revoke access to a CIDR range**
The following `revoke-cluster-security-group-ingress` example revokes access to a CIDR range.

```
aws redshift revoke-cluster-security-group-ingress \
    --cluster-security-group-name {{mysecuritygroup}} \
    --cidrip {{192.168.100.100/32}}
```
Output:

```
{
    "ClusterSecurityGroup": {
        "ClusterSecurityGroupName": "mysecuritygroup",
        "Description": "This is my cluster security group",
        "EC2SecurityGroups": [],
        "IPRanges": [],
        "Tags": []
    }
}
```
For more information, see [Configuring security group communication settings for an Amazon Redshift cluster or an Amazon Redshift Serverless workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-security-group-public-private.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [RevokeClusterSecurityGroupIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/revoke-cluster-security-group-ingress.html) in *AWS CLI Command Reference*.

### `revoke-snapshot-access`
<a name="redshift_RevokeSnapshotAccess_cli_2_topic"></a>

The following code example shows how to use `revoke-snapshot-access`.

**AWS CLI**
**To revoke the authorization of an AWS account to restore a snapshot**
The following `revoke-snapshot-access` example revokes the authorization of the AWS account `123456789111` to restore the snapshot `my-snapshot-id`. By default, the output is in JSON format.

```
aws redshift revoke-snapshot-access \
    --snapshot-id {{my-snapshot-id}} \
    --account-with-restore-access {{123456789111}}
```
Output:

```
{
    "Snapshot": {
        "Status": "available",
        "SnapshotCreateTime": "2013-07-17T22:04:18.947Z",
        "EstimatedSecondsToCompletion": 0,
        "AvailabilityZone": "us-west-2a",
        "ClusterVersion": "1.0",
        "MasterUsername": "adminuser",
        "Encrypted": false,
        "OwnerAccount": "123456789012",
        "BackupProgressInMegaBytes": 11.0,
        "ElapsedTimeInSeconds": 0,
        "DBName": "dev",
        "CurrentBackupRateInMegaBytesPerSecond": 0.1534,
        "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
        "ActualIncrementalBackupSizeInMegaBytes": 11.0,
        "SnapshotType": "manual",
        "NodeType": "dw.hs1.xlarge",
        "ClusterIdentifier": "mycluster",
        "TotalBackupSizeInMegaBytes": 20.0,
        "Port": 5439,
        "NumberOfNodes": 2,
        "SnapshotIdentifier": "my-snapshot-id"
    }
}
```
For more information, see [Amazon Redshift snapshots and backups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [RevokeSnapshotAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/revoke-snapshot-access.html) in *AWS CLI Command Reference*.

### `rotate-encryption-key`
<a name="redshift_RotateEncryptionKey_cli_2_topic"></a>

The following code example shows how to use `rotate-encryption-key`.

**AWS CLI**
**To rotate encryption key for a cluster**
The following `rotate-encryption-key` example rotates the encryption key for the specified cluster.

```
aws redshift rotate-encryption-key \
    --cluster-identifier {{mycluster}}
```
Output:

```
{
    "Cluster": {
        "ClusterIdentifier": "mycluster",
        "NodeType": "dc2.large",
        "ClusterStatus": "rotating-keys",
        "ClusterAvailabilityStatus": "Modifying",
        "MasterUsername": "adminuser",
        "DBName": "dev",
        "Endpoint": {
            "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com",
            "Port": 5439
        },
        "ClusterCreateTime": "2019-12-10T19:25:45.886Z",
        "AutomatedSnapshotRetentionPeriod": 30,
        "ManualSnapshotRetentionPeriod": -1,
        "ClusterSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sh-a1a123ab",
                "Status": "active"
            }
        ],
        "ClusterParameterGroups": [
            {
                "ParameterGroupName": "default.redshift-1.0",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "ClusterSubnetGroupName": "default",
        "VpcId": "vpc-a1abc1a1",
        "AvailabilityZone": "us-west-2a",
        "PreferredMaintenanceWindow": "sat:16:00-sat:16:30",
        "PendingModifiedValues": {},
        "ClusterVersion": "1.0",
        "AllowVersionUpgrade": true,
        "NumberOfNodes": 2,
        "PubliclyAccessible": false,
        "Encrypted": true,
        "Tags": [],
        "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY",
        "EnhancedVpcRouting": false,
        "IamRoles": [
            {
                "IamRoleArn": "arn:aws:iam::123456789012:role/myRedshiftRole",
                "ApplyStatus": "in-sync"
            }
        ],
        "MaintenanceTrackName": "current",
        "DeferredMaintenanceWindows": [],
        "NextMaintenanceWindowStartTime": "2019-12-14T16:00:00Z"
    }
}
```
For more information, see [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Cluster Management Guide*.
+  For API details, see [RotateEncryptionKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/rotate-encryption-key.html) in *AWS CLI Command Reference*.
