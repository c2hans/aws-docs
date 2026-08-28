---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_database-migration-service_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS DMS examples using AWS CLI
<a name="cli_2_database-migration-service_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS DMS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `add-tags-to-resource`
<a name="database-migration-service_AddTagsToResource_cli_2_topic"></a>

The following code example shows how to use `add-tags-to-resource`.

**AWS CLI**
**To add tags to a resource**
The following `add-tags-to-resource` example adds tags to a replication instance.

```
aws dms add-tags-to-resource \
    --resource-arn {{arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE}} \
    --tags {{Key=Environment,Value=PROD}} {{Key=Project,Value=dbMigration}}
```
This command produces no output.
For more information, see [Tagging Resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [AddTagsToResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/add-tags-to-resource.html) in *AWS CLI Command Reference*.

### `cancel-metadata-model-conversion`
<a name="database-migration-service_CancelMetadataModelConversion_cli_2_topic"></a>

The following code example shows how to use `cancel-metadata-model-conversion`.

**AWS CLI**
**To cancel a metadata model conversion**
The following `cancel-metadata-model-conversion` example cancels a metadata model conversion operation.

```
aws dms cancel-metadata-model-conversion \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --request-identifier {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "Request": {
        "Status": "CANCELING",
        "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
    }
}
```
For more information, see [Converting database schemas](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-convert.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CancelMetadataModelConversion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/cancel-metadata-model-conversion.html) in *AWS CLI Command Reference*.

### `cancel-metadata-model-creation`
<a name="database-migration-service_CancelMetadataModelCreation_cli_2_topic"></a>

The following code example shows how to use `cancel-metadata-model-creation`.

**AWS CLI**
**To cancel a metadata model creation**
The following `cancel-metadata-model-creation` example cancels a metadata model creation operation.

```
aws dms cancel-metadata-model-creation \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --request-identifier {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "Request": {
        "Status": "CANCELING",
        "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
    }
}
```
For more information, see [Creating statement metadata models](https://docs.aws.amazon.com/dms/latest/userguide/sc-metadata-model.html#sc-metadata-model-creation) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CancelMetadataModelCreation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/cancel-metadata-model-creation.html) in *AWS CLI Command Reference*.

### `create-data-provider`
<a name="database-migration-service_CreateDataProvider_cli_2_topic"></a>

The following code example shows how to use `create-data-provider`.

**AWS CLI**
**Example 1: To create a Microsoft SQL Server data provider**
The following `create-data-provider` example creates a Microsoft SQL Server data provider.

```
aws dms create-data-provider \
    --data-provider-name {{example-data-provider}} \
    --engine {{sqlserver}} \
    --description {{"Example data provider for documentation"}} \
    --settings {{MicrosoftSqlServerSettings={ServerName=example-source-server.us-east-1.rds.amazonaws.com,Port=1433,DatabaseName=ExampleDatabase,SslMode=verify-full,CertificateArn=arn:aws:dms:us-east-1:123456789012:cert:EXAMPLEABCDEFGHIJKLMNOPQRS}}}
```
Output:

```
{
    "DataProvider": {
        "DataProviderName": "example-data-provider",
        "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "DataProviderCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "Description": "Example data provider for documentation",
        "Engine": "sqlserver",
        "Settings": {
            "MicrosoftSqlServerSettings": {
                "ServerName": "example-source-server.us-east-1.rds.amazonaws.com",
                "Port": 1433,
                "DatabaseName": "ExampleDatabase",
                "SslMode": "verify-full",
                "CertificateArn": "arn:aws:dms:us-east-1:123456789012:cert:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        }
    }
}
```
For more information, see [Working with data providers](https://docs.aws.amazon.com/dms/latest/userguide/data-providers.html) in the *AWS Database Migration Service User Guide*.
**Example 2: To create a virtual data provider**
The following `create-data-provider` example creates a virtual data provider, which doesn't require a connection to the database.

```
aws dms create-data-provider \
    --data-provider-name {{example-virtual-data-provider}} \
    --engine {{aurora-postgresql}} \
    --description {{"Example data provider for documentation"}} \
    --virtual \
    --settings {{PostgreSqlSettings={ServerName=virtual,Port=5432,DatabaseName=virtual,SslMode=none}}}
```
Output:

```
{
    "DataProvider": {
        "DataProviderName": "example-virtual-data-provider",
        "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "DataProviderCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "Description": "Example data provider for documentation",
        "Engine": "aurora-postgresql",
        "Virtual": true,
        "Settings": {
            "PostgreSqlSettings": {
                "ServerName": "virtual",
                "Port": 5432,
                "DatabaseName": "virtual",
                "SslMode": "none"
            }
        }
    }
}
```
For more information, see [Working with virtual data providers](https://docs.aws.amazon.com/dms/latest/userguide/virtual-data-provider.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CreateDataProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-data-provider.html) in *AWS CLI Command Reference*.

### `create-endpoint`
<a name="database-migration-service_CreateEndpoint_cli_2_topic"></a>

The following code example shows how to use `create-endpoint`.

**AWS CLI**
**To create an endpoint**
The following `create-endpoint` example creates an endpoint for an Amazon S3 source.

```
aws dms create-endpoint \
    --endpoint-type {{source}} \
    --engine-name {{s3}} \
    --endpoint-identifier {{src-endpoint}} \
    --s3-settings {{file://s3-settings.json}}
```
Contents of `s3-settings.json`:

```
{
    "BucketName":"my-corp-data",
    "BucketFolder":"sourcedata",
    "ServiceAccessRoleArn":"arn:aws:iam::123456789012:role/my-s3-access-role"
}
```
Output:

```
{
    "Endpoint": {
        "EndpointIdentifier": "src-endpoint",
        "EndpointType": "SOURCE",
        "EngineName": "s3",
        "EngineDisplayName": "Amazon S3",
        "ExtraConnectionAttributes": "bucketFolder=sourcedata;bucketName=my-corp-data;compressionType=NONE;csvDelimiter=,;csvRowDelimiter=\\n;",
        "Status": "active",
        "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:GUVAFG34EECUOJ6QVZ56DAHT3U",
        "SslMode": "none",
        "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role",
        "S3Settings": {
            "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role",
            "CsvRowDelimiter": "\\n",
            "CsvDelimiter": ",",
            "BucketFolder": "sourcedata",
            "BucketName": "my-corp-data",
            "CompressionType": "NONE",
            "EnableStatistics": true
        }
    }
}
```
For more information, see [Working with AWS DMS Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CreateEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html) in *AWS CLI Command Reference*.

### `create-event-subscription`
<a name="database-migration-service_CreateEventSubscription_cli_2_topic"></a>

The following code example shows how to use `create-event-subscription`.

**AWS CLI**
**To list event subscriptions**
The following `create-event-subscription` example creates an event subscription to an Amazon SNS topic (my-sns-topic).

```
aws dms create-event-subscription \
    --subscription-name {{my-dms-events}} \
    --sns-topic-arn {{arn:aws:sns:us-east-1:123456789012:my-sns-topic}}
```
Output:

```
{
    "EventSubscription": {
        "CustomerAwsId": "123456789012",
        "CustSubscriptionId": "my-dms-events",
        "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:my-sns-topic",
        "Status": "creating",
        "SubscriptionCreationTime": "2020-05-21 21:58:38.598",
        "Enabled": true
    }
}
```
For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CreateEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-event-subscription.html) in *AWS CLI Command Reference*.

### `create-instance-profile`
<a name="database-migration-service_CreateInstanceProfile_cli_2_topic"></a>

The following code example shows how to use `create-instance-profile`.

**AWS CLI**
**To create an instance profile**
The following `create-instance-profile` example creates an instance profile.

```
aws dms create-instance-profile \
    --instance-profile-name {{example-instance-profile}} \
    --description {{"Example instance profile for documentation"}} \
    --subnet-group-identifier {{example-replication-subnet-group}} \
    --vpc-security-groups {{"sg-0123456789abcdef0"}} \
    --kms-key-arn {{arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --network-type {{IPV4}} \
    --no-publicly-accessible
```
Output:

```
{
    "InstanceProfile": {
        "InstanceProfileArn": "arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "KmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "PubliclyAccessible": false,
        "NetworkType": "IPV4",
        "InstanceProfileName": "example-instance-profile",
        "Description": "Example instance profile for documentation",
        "InstanceProfileCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "SubnetGroupIdentifier": "example-replication-subnet-group",
        "VpcSecurityGroups": [
            "sg-0123456789abcdef0"
        ]
    }
}
```
For more information, see [Working with instance profiles](https://docs.aws.amazon.com/dms/latest/userguide/instance-profiles.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CreateInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-instance-profile.html) in *AWS CLI Command Reference*.

### `create-migration-project`
<a name="database-migration-service_CreateMigrationProject_cli_2_topic"></a>

The following code example shows how to use `create-migration-project`.

**AWS CLI**
**To create a migration project**
The following `create-migration-project` example creates a migration project.

```
aws dms create-migration-project \
    --migration-project-name {{example-migration-project}} \
    --description {{"Example migration project for documentation"}} \
    --source-data-provider-descriptors {{DataProviderIdentifier=arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS,SecretsManagerSecretId=arn:aws:secretsmanager:us-east-1:123456789012:secret:example-source-secret-A1B2C3,SecretsManagerAccessRoleArn=arn:aws:iam::123456789012:role/example-secrets-manager-role}} \
    --target-data-provider-descriptors {{DataProviderIdentifier=arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS,SecretsManagerSecretId=arn:aws:secretsmanager:us-east-1:123456789012:secret:example-target-secret-A1B2C3,SecretsManagerAccessRoleArn=arn:aws:iam::123456789012:role/example-secrets-manager-role}} \
    --instance-profile-identifier {{arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --transformation-rules '{{{"rules":[{"rule-type":"transformation","rule-id":"1","rule-name":"1","rule-target":"schema","rule-action":"rename","object-locator":{"schema-name":"ExampleSchema"},"value":"TargetSchema"}]}}}' \
    --schema-conversion-application-attributes {{S3BucketPath=s3://amzn-s3-demo-bucket,S3BucketRoleArn=arn:aws:iam::123456789012:role/example-s3-access-role}}
```
Output:

```
{
    "MigrationProject": {
        "MigrationProjectName": "example-migration-project",
        "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "MigrationProjectCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "SourceDataProviderDescriptors": [
            {
                "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:example-source-secret-A1B2C3",
                "SecretsManagerAccessRoleArn": "arn:aws:iam::123456789012:role/example-secrets-manager-role",
                "DataProviderName": "example-data-provider",
                "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        ],
        "TargetDataProviderDescriptors": [
            {
                "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:example-target-secret-A1B2C3",
                "SecretsManagerAccessRoleArn": "arn:aws:iam::123456789012:role/example-secrets-manager-role",
                "DataProviderName": "example-data-provider",
                "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        ],
        "InstanceProfileArn": "arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "InstanceProfileName": "example-instance-profile",
        "TransformationRules": "{\"rules\":[{\"rule-type\":\"transformation\",\"rule-id\":\"1\",\"rule-name\":\"1\",\"rule-target\":\"schema\",\"rule-action\":\"rename\",\"object-locator\":{\"schema-name\":\"ExampleSchema\"},\"value\":\"TargetSchema\"}]}",
        "Description": "Example migration project for documentation",
        "SchemaConversionApplicationAttributes": {
            "S3BucketPath": "s3://amzn-s3-demo-bucket",
            "S3BucketRoleArn": "arn:aws:iam::123456789012:role/example-s3-access-role"
        }
    }
}
```
For more information, see [Working with migration projects](https://docs.aws.amazon.com/dms/latest/userguide/migration-projects-create.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CreateMigrationProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-migration-project.html) in *AWS CLI Command Reference*.

### `create-replication-instance`
<a name="database-migration-service_CreateReplicationInstance_cli_2_topic"></a>

The following code example shows how to use `create-replication-instance`.

**AWS CLI**
**To create a replication instance**
The following `create-replication-instance` example creates a replication instance.

```
aws dms create-replication-instance \
    --replication-instance-identifier {{my-repl-instance}} \
    --replication-instance-class {{dms.t2.micro}} \
    --allocated-storage {{5}}
```
Output:

```
{
    "ReplicationInstance": {
        "ReplicationInstanceIdentifier": "my-repl-instance",
        "ReplicationInstanceClass": "dms.t2.micro",
        "ReplicationInstanceStatus": "creating",
        "AllocatedStorage": 5,
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-f839b688",
                "Status": "active"
            }
        ],
        "ReplicationSubnetGroup": {
            "ReplicationSubnetGroupIdentifier": "default",
            "ReplicationSubnetGroupDescription": "default",
            "VpcId": "vpc-136a4c6a",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-da327bf6",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-42599426",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1d"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-bac383e0",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1c"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-6746046b",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1f"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-d7c825e8",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1e"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-cbfff283",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1b"
                    },
                    "SubnetStatus": "Active"
                }
            ]
        },
        "PreferredMaintenanceWindow": "sat:12:35-sat:13:05",
        "PendingModifiedValues": {},
        "MultiAZ": false,
        "EngineVersion": "3.3.2",
        "AutoMinorVersionUpgrade": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/f7bc0f8e-1a3a-4ace-9faa-e8494fa3921a",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:ZK2VQBUWFDBAWHIXHAYG5G2PKY",
        "PubliclyAccessible": true
    }
}
```
For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CreateReplicationInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-instance.html) in *AWS CLI Command Reference*.

### `create-replication-subnet-group`
<a name="database-migration-service_CreateReplicationSubnetGroup_cli_2_topic"></a>

The following code example shows how to use `create-replication-subnet-group`.

**AWS CLI**
**To create a subnet group**
The following `create-replication-subnet-group` example creates a group consisting of 3 subnets.

```
aws dms create-replication-subnet-group \
    --replication-subnet-group-identifier {{my-subnet-group}} \
    --replication-subnet-group-description {{"my subnet group"}} \
    --subnet-ids {{subnet-da327bf6}} {{subnet-bac383e0}} {{subnet-d7c825e8}}
```
Output:

```
{
    "ReplicationSubnetGroup": {
        "ReplicationSubnetGroupIdentifier": "my-subnet-group",
        "ReplicationSubnetGroupDescription": "my subnet group",
        "VpcId": "vpc-136a4c6a",
        "SubnetGroupStatus": "Complete",
        "Subnets": [
            {
                "SubnetIdentifier": "subnet-da327bf6",
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1a"
                },
                "SubnetStatus": "Active"
            },
            {
                "SubnetIdentifier": "subnet-bac383e0",
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1c"
                },
                "SubnetStatus": "Active"
            },
            {
                "SubnetIdentifier": "subnet-d7c825e8",
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1e"
                },
                "SubnetStatus": "Active"
            }
        ]
    }
}
```
For more information, see [Setting Up a Network for a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CreateReplicationSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-subnet-group.html) in *AWS CLI Command Reference*.

### `create-replication-task`
<a name="database-migration-service_CreateReplicationTask_cli_2_topic"></a>

The following code example shows how to use `create-replication-task`.

**AWS CLI**
**To create a replication task**
The following `create-replication-task` example creates a replication task.

```
aws dms create-replication-task \
    --replication-task-identifier {{movedata}} \
    --source-endpoint-arn {{arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA}} \
    --target-endpoint-arn {{arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U}} \
    --replication-instance-arn {{$RI_ARN}} \
    --migration-type {{full-load}} \
    --table-mappings {{file://table-mappings.json}}
```
Contents of `table-mappings.json`:

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "prodrep",
                "table-name": "%"
            },
            "rule-action": "include",
            "filters": []
        }
    ]
}
```
Output:

```
{
    "ReplicationTask": {
        "ReplicationTaskIdentifier": "moveit2",
        "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "MigrationType": "full-load",
        "TableMappings": ...output omitted... ,
        "ReplicationTaskSettings": ...output omitted... ,
        "Status": "creating",
        "ReplicationTaskCreationDate": 1590524772.505,
        "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"
    }
}
```
For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CreateReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-task.html) in *AWS CLI Command Reference*.

### `delete-connection`
<a name="database-migration-service_DeleteConnection_cli_2_topic"></a>

The following code example shows how to use `delete-connection`.

**AWS CLI**
**To delete a connection**
The following `delete-connection` example disassociates an endpoint from a replication instance.

```
aws dms delete-connection \
    --endpoint-arn {{arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA}} \
    --replication-instance-arn {{arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE}}
```
Output:

```
{
    "Connection": {
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "Status": "deleting",
        "EndpointIdentifier": "src-database-1",
        "ReplicationInstanceIdentifier": "my-repl-instance"
    }
}
```
For more information, see [https://docs.aws.amazon.com/dms/latest/userguide/CHAP\_Endpoints.Creating.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DeleteConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-connection.html) in *AWS CLI Command Reference*.

### `delete-data-provider`
<a name="database-migration-service_DeleteDataProvider_cli_2_topic"></a>

The following code example shows how to use `delete-data-provider`.

**AWS CLI**
**To delete a data provider**
The following `delete-data-provider` example deletes a data provider identified by its ARN.

```
aws dms delete-data-provider \
    --data-provider-identifier {{arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS}}
```
Output:

```
{
    "DataProvider": {
        "DataProviderName": "example-data-provider",
        "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "DataProviderCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "Description": "Example data provider for documentation",
        "Engine": "sqlserver",
        "Settings": {
            "MicrosoftSqlServerSettings": {
                "ServerName": "example-source-server.us-east-1.rds.amazonaws.com",
                "Port": 1433,
                "DatabaseName": "ExampleDatabase",
                "SslMode": "verify-full",
                "CertificateArn": "arn:aws:dms:us-east-1:123456789012:cert:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        }
    }
}
```
For more information, see [Working with data providers](https://docs.aws.amazon.com/dms/latest/userguide/data-providers.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DeleteDataProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-data-provider.html) in *AWS CLI Command Reference*.

### `delete-endpoint`
<a name="database-migration-service_DeleteEndpoint_cli_2_topic"></a>

The following code example shows how to use `delete-endpoint`.

**AWS CLI**
**To delete an endpoint**
The following `delete-endpoint` example deletes an endpoint.

```
aws dms delete-endpoint \
    --endpoint-arn {{arn:aws:dms:us-east-1:123456789012:endpoint:OUJJVXO4XZ4CYTSEG5XGMN2R3Y}}
```
Output:

```
{
    "Endpoint": {
        "EndpointIdentifier": "src-endpoint",
        "EndpointType": "SOURCE",
        "EngineName": "s3",
        "EngineDisplayName": "Amazon S3",
        "ExtraConnectionAttributes": "bucketFolder=sourcedata;bucketName=my-corp-data;compressionType=NONE;csvDelimiter=,;csvRowDelimiter=\\n;",
        "Status": "deleting",
        "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:OUJJVXO4XZ4CYTSEG5XGMN2R3Y",
        "SslMode": "none",
        "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role",
        "S3Settings": {
            "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role",
            "CsvRowDelimiter": "\\n",
            "CsvDelimiter": ",",
            "BucketFolder": "sourcedata",
            "BucketName": "my-corp-data",
            "CompressionType": "NONE",
            "EnableStatistics": true
        }
    }
}
```
For more information, see [Working with AWS DMS Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DeleteEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-endpoint.html) in *AWS CLI Command Reference*.

### `delete-event-subscription`
<a name="database-migration-service_DeleteEventSubscription_cli_2_topic"></a>

The following code example shows how to use `delete-event-subscription`.

**AWS CLI**
**To delete an event subscription**
The following `delete-event-subscription` example deletes a subscription to an Amazon SNS topic.

```
aws dms delete-event-subscription \
    --subscription-name {{"my-dms-events"}}
```
Output:

```
{
    "EventSubscription": {
        "CustomerAwsId": "123456789012",
        "CustSubscriptionId": "my-dms-events",
        "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:my-sns-topic",
        "Status": "deleting",
        "SubscriptionCreationTime": "2020-05-21 21:58:38.598",
        "Enabled": true
    }
}
```
For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DeleteEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-event-subscription.html) in *AWS CLI Command Reference*.

### `delete-instance-profile`
<a name="database-migration-service_DeleteInstanceProfile_cli_2_topic"></a>

The following code example shows how to use `delete-instance-profile`.

**AWS CLI**
**To delete an instance profile**
The following `delete-instance-profile` example deletes an instance profile identified by its ARN.

```
aws dms delete-instance-profile \
    --instance-profile-identifier {{arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS}}
```
Output:

```
{
    "InstanceProfile": {
        "InstanceProfileArn": "arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "KmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "PubliclyAccessible": false,
        "NetworkType": "IPV4",
        "InstanceProfileName": "example-instance-profile",
        "Description": "Example instance profile for documentation",
        "InstanceProfileCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "SubnetGroupIdentifier": "example-replication-subnet-group",
        "VpcSecurityGroups": [
            "sg-0123456789abcdef0"
        ]
    }
}
```
For more information, see [Working with instance profiles](https://docs.aws.amazon.com/dms/latest/userguide/instance-profiles.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DeleteInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-instance-profile.html) in *AWS CLI Command Reference*.

### `delete-migration-project`
<a name="database-migration-service_DeleteMigrationProject_cli_2_topic"></a>

The following code example shows how to use `delete-migration-project`.

**AWS CLI**
**To delete a migration project**
The following `delete-migration-project` example deletes a migration project identified by its ARN.

```
aws dms delete-migration-project \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}}
```
Output:

```
{
    "MigrationProject": {
        "MigrationProjectName": "example-migration-project",
        "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "MigrationProjectCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "SourceDataProviderDescriptors": [
            {
                "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:example-source-secret-A1B2C3",
                "SecretsManagerAccessRoleArn": "arn:aws:iam::123456789012:role/example-secrets-manager-role",
                "DataProviderName": "example-data-provider",
                "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        ],
        "TargetDataProviderDescriptors": [
            {
                "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:example-target-secret-A1B2C3",
                "SecretsManagerAccessRoleArn": "arn:aws:iam::123456789012:role/example-secrets-manager-role",
                "DataProviderName": "example-data-provider",
                "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        ],
        "InstanceProfileArn": "arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "InstanceProfileName": "example-instance-profile",
        "TransformationRules": "{\"rules\":[{\"rule-type\":\"transformation\",\"rule-id\":\"1\",\"rule-name\":\"1\",\"rule-target\":\"schema\",\"rule-action\":\"rename\",\"object-locator\":{\"schema-name\":\"ExampleSchema\"},\"value\":\"TargetSchema\"}]}",
        "Description": "Example migration project for documentation",
        "SchemaConversionApplicationAttributes": {
            "S3BucketPath": "s3://amzn-s3-demo-bucket",
            "S3BucketRoleArn": "arn:aws:iam::123456789012:role/example-s3-access-role"
        }
    }
}
```
For more information, see [Working with migration projects](https://docs.aws.amazon.com/dms/latest/userguide/migration-projects-manage.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DeleteMigrationProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-migration-project.html) in *AWS CLI Command Reference*.

### `delete-replication-instance`
<a name="database-migration-service_DeleteReplicationInstance_cli_2_topic"></a>

The following code example shows how to use `delete-replication-instance`.

**AWS CLI**
**To delete a replication instance**
The following `delete-replication-instance` example deletes a replication instance.

```
aws dms delete-replication-instance \
    --replication-instance-arn {{arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE}}
```
Output:

```
{
    "ReplicationInstance": {
        "ReplicationInstanceIdentifier": "my-repl-instance",
        "ReplicationInstanceClass": "dms.t2.micro",
        "ReplicationInstanceStatus": "deleting",
        "AllocatedStorage": 5,
        "InstanceCreateTime": 1590011235.952,
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-f839b688",
                "Status": "active"
            }
        ],
        "AvailabilityZone": "us-east-1e",
        "ReplicationSubnetGroup": {
            "ReplicationSubnetGroupIdentifier": "default",
            "ReplicationSubnetGroupDescription": "default",
            "VpcId": "vpc-136a4c6a",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-da327bf6",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-42599426",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1d"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-bac383e0",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1c"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-6746046b",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1f"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-d7c825e8",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1e"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-cbfff283",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1b"
                    },
                    "SubnetStatus": "Active"
                }
            ]
        },
        "PreferredMaintenanceWindow": "wed:11:42-wed:12:12",
        "PendingModifiedValues": {},
        "MultiAZ": true,
        "EngineVersion": "3.3.2",
        "AutoMinorVersionUpgrade": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/f7bc0f8e-1a3a-4ace-9faa-e8494fa3921a",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "ReplicationInstancePublicIpAddress": "54.225.120.92",
        "ReplicationInstancePrivateIpAddress": "172.31.30.121",
        "ReplicationInstancePublicIpAddresses": [
            "54.225.120.92",
            "3.230.18.248"
        ],
        "ReplicationInstancePrivateIpAddresses": [
            "172.31.30.121",
            "172.31.75.90"
        ],
        "PubliclyAccessible": true,
        "SecondaryAvailabilityZone": "us-east-1b"
    }
}
```
For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DeleteReplicationInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-instance.html) in *AWS CLI Command Reference*.

### `delete-replication-subnet-group`
<a name="database-migration-service_DeleteReplicationSubnetGroup_cli_2_topic"></a>

The following code example shows how to use `delete-replication-subnet-group`.

**AWS CLI**
**To delete a subnet group**
The following `delete-replication-subnet-group` example deletes a subnet group.

```
aws dms delete-replication-subnet-group \
--replication-subnet-group-identifier {{my-subnet-group}}
```
Output:

```
(none)
```
For more information, see [Setting Up a Network for a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DeleteReplicationSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-subnet-group.html) in *AWS CLI Command Reference*.

### `delete-replication-task`
<a name="database-migration-service_DeleteReplicationTask_cli_2_topic"></a>

The following code example shows how to use `delete-replication-task`.

**AWS CLI**
**To delete a replication task**
The following `delete-replication-task` example deletes a replication task.

```
aws dms delete-replication-task \
    --replication-task-arn {{arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII}}
```
Output:

```
{
    "ReplicationTask": {
        "ReplicationTaskIdentifier": "moveit2",
        "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "MigrationType": "full-load",
        "TableMappings": ...output omitted...,
        "ReplicationTaskSettings": ...output omitted...,
        "Status": "deleting",
        "StopReason": "Stop Reason FULL_LOAD_ONLY_FINISHED",
        "ReplicationTaskCreationDate": 1590524772.505,
        "ReplicationTaskStartDate": 1590789988.677,
        "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"
    }
}
```
For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DeleteReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task.html) in *AWS CLI Command Reference*.

### `describe-account-attributes`
<a name="database-migration-service_DescribeAccountAttributes_cli_2_topic"></a>

The following code example shows how to use `describe-account-attributes`.

**AWS CLI**
**To describe account attributes**
The following `describe-account-attributes` example lists the attributes for your AWS account.

```
aws dms describe-account-attributes
```
Output:

```
{
    "AccountQuotas": [
        {
            "AccountQuotaName": "ReplicationInstances",
            "Used": 1,
            "Max": 20
        },
        {
            "AccountQuotaName": "AllocatedStorage",
            "Used": 5,
            "Max": 10000
        },

        ...remaining output omitted...

    ],
    "UniqueAccountIdentifier": "cqahfbfy5xee"
}
```
+  For API details, see [DescribeAccountAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-account-attributes.html) in *AWS CLI Command Reference*.

### `describe-certificates`
<a name="database-migration-service_DescribeCertificates_cli_2_topic"></a>

The following code example shows how to use `describe-certificates`.

**AWS CLI**
**To list the available certificates**
The following `describe-certificates` example lists the available certificates in your AWS account.

```
aws dms describe-certificates
```
Output:

```
{
    "Certificates": [
        {
            "CertificateIdentifier": "my-cert",
            "CertificateCreationDate": 1543259542.506,
            "CertificatePem": "-----BEGIN CERTIFICATE-----\nMIID9DCCAtygAwIBAgIBQjANBgkqhkiG9w0BAQ ...U"

            ... remaining output omittted ...

        }
    ]
}
```
For more information, see [Using SSL](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.SSL) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-certificates.html) in *AWS CLI Command Reference*.

### `describe-connections`
<a name="database-migration-service_DescribeConnections_cli_2_topic"></a>

The following code example shows how to use `describe-connections`.

**AWS CLI**
**To describe connections**
The following `describe-connections` example lists the connections that you have tested between a replication instance and an endpoint.

```
aws dms describe-connections
```
Output:

```
{
    "Connections": [
        {
            "Status": "successful",
            "ReplicationInstanceIdentifier": "test",
            "EndpointArn": "arn:aws:dms:us-east-arn:aws:dms:us-east-1:123456789012:endpoint:ZW5UAN6P4E77EC7YWHK4RZZ3BE",
            "EndpointIdentifier": "testsrc1",
            "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ"
        }
    ]
}
```
For more information, see [Creating Source and Target Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-connections.html) in *AWS CLI Command Reference*.

### `describe-conversion-configuration`
<a name="database-migration-service_DescribeConversionConfiguration_cli_2_topic"></a>

The following code example shows how to use `describe-conversion-configuration`.

**AWS CLI**
**To describe a conversion configuration**
The following `describe-conversion-configuration` example retrieves the conversion configuration for a migration project.

```
aws dms describe-conversion-configuration \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}}
```
Output:

```
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "ConversionConfiguration": "{\"Common project settings\":{\"ShowSeverityLevelInSql\":\"CRITICAL\",\"EnableGenAiConversion\":false},\"MSSQL_TO_AURORA_POSTGRESQL\":{\"ConvertProceduresToFunction\":true,\"UniqueIndexGeneration\":true,\"CaseSensitivityNames\":false},\"Conversion version\":{\"MSSQL_TO_AURORA_POSTGRESQL_target_engine_version\":\"15\"}}"
}
```
For more information, see [Specifying schema conversion settings](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-settings.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeConversionConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-conversion-configuration.html) in *AWS CLI Command Reference*.

### `describe-data-providers`
<a name="database-migration-service_DescribeDataProviders_cli_2_topic"></a>

The following code example shows how to use `describe-data-providers`.

**AWS CLI**
**To describe data providers**
The following `describe-data-providers` example retrieves the details of a data provider identified by its ARN.

```
aws dms describe-data-providers \
    --filters {{Name=data-provider-identifier,Values=arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS}}
```
Output:

```
{
    "DataProviders": [
        {
            "DataProviderName": "example-data-provider",
            "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "DataProviderCreationTime": "2026-01-09T12:30:00.000000+00:00",
            "Description": "Example data provider for documentation",
            "Engine": "sqlserver",
            "Settings": {
                "MicrosoftSqlServerSettings": {
                    "ServerName": "example-source-server.us-east-1.rds.amazonaws.com",
                    "Port": 1433,
                    "DatabaseName": "ExampleDatabase",
                    "SslMode": "verify-full",
                    "CertificateArn": "arn:aws:dms:us-east-1:123456789012:cert:EXAMPLEABCDEFGHIJKLMNOPQRS"
                }
            }
        }
    ]
}
```
For more information, see [Working with data providers](https://docs.aws.amazon.com/dms/latest/userguide/data-providers.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeDataProviders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-data-providers.html) in *AWS CLI Command Reference*.

### `describe-endpoint-types`
<a name="database-migration-service_DescribeEndpointTypes_cli_2_topic"></a>

The following code example shows how to use `describe-endpoint-types`.

**AWS CLI**
**To list the available endpoint types**
The following `describe-endpoint-types` example lists the MySQL endpoint types that are available.

```
aws dms describe-endpoint-types \
    --filters {{"Name=engine-name,Values=mysql"}}
```
Output:

```
{
    "SupportedEndpointTypes": [
        {
            "EngineName": "mysql",
            "SupportsCDC": true,
            "EndpointType": "source",
            "EngineDisplayName": "MySQL"
        },
        {
            "EngineName": "mysql",
            "SupportsCDC": true,
            "EndpointType": "target",
            "EngineDisplayName": "MySQL"
        }
    ]
}
```
For more information, see Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP\_Endpoints.html>`\_\_ in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeEndpointTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-endpoint-types.html) in *AWS CLI Command Reference*.

### `describe-endpoints`
<a name="database-migration-service_DescribeEndpoints_cli_2_topic"></a>

The following code example shows how to use `describe-endpoints`.

**AWS CLI**
**To describe endpoints**
The following `describe-endpoints` example lists the endpoints in your AWS account.

```
aws dms describe-endpoints
```
Output:

```
{
    "Endpoints": [
        {
            "Username": "dms",
            "Status": "active",
            "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:SF2WOFLWYWKVEOHID2EKLP3SJI",
            "ServerName": "ec2-52-32-48-61.us-west-2.compute.amazonaws.com",
            "EndpointType": "SOURCE",
            "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/94d5c4e7-4e4c-44be-b58a-c8da7adf57cd",
            "DatabaseName": "test",
            "EngineName": "mysql",
            "EndpointIdentifier": "pri100",
            "Port": 8193
        },
        {
            "Username": "admin",
            "Status": "active",
            "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:TJJZCIH3CJ24TJRU4VC32WEWFR",
            "ServerName": "test.example.com",
            "EndpointType": "SOURCE",
            "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/2431021b-1cf2-a2d4-77b2-59a9e4bce323",
            "DatabaseName": "EMPL",
            "EngineName": "oracle",
            "EndpointIdentifier": "test",
            "Port": 1521
        }
    ]
}
```
For more information, see [Working with AWS DMS Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-endpoints.html) in *AWS CLI Command Reference*.

### `describe-event-categories`
<a name="database-migration-service_DescribeEventCategories_cli_2_topic"></a>

The following code example shows how to use `describe-event-categories`.

**AWS CLI**
**To describe event categories**
The following `describe-event-categories` example lists the available event categories.

```
aws dms describe-event-categories
```
Output:

```
{
    "EventCategoryGroupList": [
        {
            "SourceType": "replication-instance",
            "EventCategories": [
                "low storage",
                "configuration change",
                "maintenance",
                "deletion",
                "creation",
                "failover",
                "failure"
            ]
        },
        {
            "SourceType": "replication-task",
            "EventCategories": [
                "configuration change",
                "state change",
                "deletion",
                "creation",
                "failure"
            ]
        }
    ]
}
```
For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeEventCategories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-event-categories.html) in *AWS CLI Command Reference*.

### `describe-event-subscriptions`
<a name="database-migration-service_DescribeEventSubscriptions_cli_2_topic"></a>

The following code example shows how to use `describe-event-subscriptions`.

**AWS CLI**
**To describe event subscriptions**
The following `describe-event-subscriptions` example lists the event subscriptions to an Amazon SNS topic.

```
aws dms describe-event-subscriptions
```
Output:

```
{
    "EventSubscriptionsList": [
        {
            "CustomerAwsId": "123456789012",
            "CustSubscriptionId": "my-dms-events",
            "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:my-sns-topic",
            "Status": "deleting",
            "SubscriptionCreationTime": "2020-05-21 22:28:51.924",
            "Enabled": true
        }
    ]
}
```
For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeEventSubscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-event-subscriptions.html) in *AWS CLI Command Reference*.

### `describe-events`
<a name="database-migration-service_DescribeEvents_cli_2_topic"></a>

The following code example shows how to use `describe-events`.

**AWS CLI**
**To list DMS events**
The following `describe-events` example lists the events that originated from a replication instance.

```
aws dms describe-events \
    --source-type {{"replication-instance"}}
```
Output:

```
{
    "Events": [
        {
            "SourceIdentifier": "my-repl-instance",
            "SourceType": "replication-instance",
            "Message": "Replication application shutdown",
            "EventCategories": [],
            "Date": 1590771645.776
        }
    ]
}
```
For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-events.html) in *AWS CLI Command Reference*.

### `describe-extension-pack-associations`
<a name="database-migration-service_DescribeExtensionPackAssociations_cli_2_topic"></a>

The following code example shows how to use `describe-extension-pack-associations`.

**AWS CLI**
**To describe extension pack associations**
The following `describe-extension-pack-associations` example retrieves the status of operations that apply an extension pack to the target database, identified by their request IDs.

```
aws dms describe-extension-pack-associations \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --filters {{Name=request-id,Values=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,a1b2c3d4-5678-90ab-cdef-EXAMPLE22222,a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
Output:

```
{
    "Requests": [
        {
            "Status": "SUCCESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
        },
        {
            "Status": "IN_PROGRESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Progress": {
                "ProgressPercent": 50.0,
                "ProgressStep": "IN_PROGRESS"
            }
        },
        {
            "Status": "FAILED",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Error": {
                "defaultErrorDetails": {
                    "Message": "The database user in your target secret does not have sufficient privileges. Grant the required privileges and try again."
                }
            }
        }
    ]
}
```
For more information, see [Using extension packs](https://docs.aws.amazon.com/dms/latest/userguide/extension-pack.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeExtensionPackAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-extension-pack-associations.html) in *AWS CLI Command Reference*.

### `describe-instance-profiles`
<a name="database-migration-service_DescribeInstanceProfiles_cli_2_topic"></a>

The following code example shows how to use `describe-instance-profiles`.

**AWS CLI**
**To describe instance profiles**
The following `describe-instance-profiles` example retrieves the details of an instance profile identified by its ARN.

```
aws dms describe-instance-profiles \
    --filters {{Name=instance-profile-identifier,Values=arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS}}
```
Output:

```
{
    "InstanceProfiles": [
        {
            "InstanceProfileArn": "arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "KmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "PubliclyAccessible": false,
            "NetworkType": "IPV4",
            "InstanceProfileName": "example-instance-profile",
            "Description": "Example instance profile for documentation",
            "InstanceProfileCreationTime": "2026-01-09T12:30:00.000000+00:00",
            "SubnetGroupIdentifier": "example-replication-subnet-group",
            "VpcSecurityGroups": [
                "sg-0123456789abcdef0"
            ]
        }
    ]
}
```
For more information, see [Working with instance profiles](https://docs.aws.amazon.com/dms/latest/userguide/instance-profiles.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeInstanceProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-instance-profiles.html) in *AWS CLI Command Reference*.

### `describe-metadata-model-assessments`
<a name="database-migration-service_DescribeMetadataModelAssessments_cli_2_topic"></a>

The following code example shows how to use `describe-metadata-model-assessments`.

**AWS CLI**
**To describe metadata model assessments**
The following `describe-metadata-model-assessments` example retrieves the status of metadata model assessment operations identified by their request IDs.

```
aws dms describe-metadata-model-assessments \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --filters {{Name=request-id,Values=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,a1b2c3d4-5678-90ab-cdef-EXAMPLE22222,a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
Output:

```
{
    "Requests": [
        {
            "Status": "SUCCESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
        },
        {
            "Status": "IN_PROGRESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Progress": {
                "ProgressPercent": 50.0,
                "TotalObjects": 100,
                "ProgressStep": "ANALYZING",
                "ProcessedObject": {
                    "Name": "ExampleTable",
                    "Type": "table",
                    "EndpointType": "SOURCE"
                }
            }
        },
        {
            "Status": "FAILED",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Error": {
                "defaultErrorDetails": {
                    "Message": "No objects were found according to the specified selection rules. Please review your selection rules and try again."
                }
            }
        }
    ]
}
```
For more information, see [Creating database migration assessment reports](https://docs.aws.amazon.com/dms/latest/userguide/assessment-reports.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeMetadataModelAssessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-metadata-model-assessments.html) in *AWS CLI Command Reference*.

### `describe-metadata-model-children`
<a name="database-migration-service_DescribeMetadataModelChildren_cli_2_topic"></a>

The following code example shows how to use `describe-metadata-model-children`.

**AWS CLI**
**To describe metadata model children**
The following `describe-metadata-model-children` example retrieves the child metadata models of the `ExampleSchema` schema from the source metadata tree.

```
aws dms describe-metadata-model-children \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"}, "rule-action": "explicit"}]}}}' \
    --origin {{SOURCE}}
```
Output:

```
{
    "MetadataModelChildren": [
        {
            "MetadataModelName": "Tables",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\", \"category-name\": \"Tables\"}, \"rule-action\": \"explicit\"}]}"
        },
        {
            "MetadataModelName": "Views",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"2\", \"rule-name\": \"2\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\", \"category-name\": \"Views\"}, \"rule-action\": \"explicit\"}]}"
        },
        {
            "MetadataModelName": "Functions",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"3\", \"rule-name\": \"3\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\", \"category-name\": \"Functions\"}, \"rule-action\": \"explicit\"}]}"
        },
        {
            "MetadataModelName": "Sequences",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"4\", \"rule-name\": \"4\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\", \"category-name\": \"Sequences\"}, \"rule-action\": \"explicit\"}]}"
        }
    ]
}
```
For more information, see [Navigating the metadata model tree](https://docs.aws.amazon.com/dms/latest/userguide/sc-metadata-model.html#sc-metadata-model-navigating) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeMetadataModelChildren](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-metadata-model-children.html) in *AWS CLI Command Reference*.

### `describe-metadata-model-conversions`
<a name="database-migration-service_DescribeMetadataModelConversions_cli_2_topic"></a>

The following code example shows how to use `describe-metadata-model-conversions`.

**AWS CLI**
**To describe metadata model conversions**
The following `describe-metadata-model-conversions` example retrieves the status of metadata model conversion operations identified by their request IDs.

```
aws dms describe-metadata-model-conversions \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --filters {{Name=request-id,Values=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,a1b2c3d4-5678-90ab-cdef-EXAMPLE22222,a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
Output:

```
{
    "Requests": [
        {
            "Status": "SUCCESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
        },
        {
            "Status": "IN_PROGRESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Progress": {
                "ProgressPercent": 50.0,
                "TotalObjects": 100,
                "ProgressStep": "CONVERTING",
                "ProcessedObject": {
                    "Name": "ExampleTable",
                    "Type": "table",
                    "EndpointType": "SOURCE"
                }
            }
        },
        {
            "Status": "FAILED",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Error": {
                "defaultErrorDetails": {
                    "Message": "No objects were found according to the specified selection rules. Please review your selection rules and try again."
                }
            }
        }
    ]
}
```
For more information, see [Converting database schemas](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-convert.html#schema-conversion-convert-steps) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeMetadataModelConversions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-metadata-model-conversions.html) in *AWS CLI Command Reference*.

### `describe-metadata-model-creations`
<a name="database-migration-service_DescribeMetadataModelCreations_cli_2_topic"></a>

The following code example shows how to use `describe-metadata-model-creations`.

**AWS CLI**
**To describe metadata model creations**
The following `describe-metadata-model-creations` example retrieves the status of metadata model creation operations identified by their request IDs.

```
aws dms describe-metadata-model-creations \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --filters {{Name=request-id,Values=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,a1b2c3d4-5678-90ab-cdef-EXAMPLE22222,a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
Output:

```
{
    "Requests": [
        {
            "Status": "SUCCESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
        },
        {
            "Status": "IN_PROGRESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
        },
        {
            "Status": "FAILED",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Error": {
                "defaultErrorDetails": {
                    "Message": "No objects were found according to the specified selection rules. Please review your selection rules and try again."
                }
            }
        }
    ]
}
```
For more information, see [Creating statement metadata models](https://docs.aws.amazon.com/dms/latest/userguide/sc-metadata-model.html#sc-metadata-model-creation) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeMetadataModelCreations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-metadata-model-creations.html) in *AWS CLI Command Reference*.

### `describe-metadata-model-exports-as-script`
<a name="database-migration-service_DescribeMetadataModelExportsAsScript_cli_2_topic"></a>

The following code example shows how to use `describe-metadata-model-exports-as-script`.

**AWS CLI**
**To describe metadata model exports as script**
The following `describe-metadata-model-exports-as-script` example retrieves the status of operations that export metadata models as data definition language (DDL) scripts, identified by their request IDs.

```
aws dms describe-metadata-model-exports-as-script \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --filters {{Name=request-id,Values=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,a1b2c3d4-5678-90ab-cdef-EXAMPLE22222,a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
Output:

```
{
    "Requests": [
        {
            "Status": "SUCCESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "ExportSqlDetails": {
                "S3ObjectKey": "s3://amzn-s3-demo-bucket/example-migration-project/ExampleScript.zip",
                "ObjectURL": "https://amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com/example-migration-project/ExampleScript.zip"
            }
        },
        {
            "Status": "IN_PROGRESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Progress": {
                "ProgressPercent": 50.0,
                "TotalObjects": 100,
                "ProgressStep": "IN_PROGRESS",
                "ProcessedObject": {
                    "EndpointType": "TARGET"
                }
            }
        },
        {
            "Status": "FAILED",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Error": {
                "defaultErrorDetails": {
                    "Message": "No objects were found according to the specified selection rules. Please review your selection rules and try again."
                }
            }
        }
    ]
}
```
For more information, see [Saving your converted code to a SQL file](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-save-apply.html#schema-conversion-save) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeMetadataModelExportsAsScript](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-metadata-model-exports-as-script.html) in *AWS CLI Command Reference*.

### `describe-metadata-model-exports-to-target`
<a name="database-migration-service_DescribeMetadataModelExportsToTarget_cli_2_topic"></a>

The following code example shows how to use `describe-metadata-model-exports-to-target`.

**AWS CLI**
**To describe metadata model exports to target**
The following `describe-metadata-model-exports-to-target` example retrieves the status of operations that export converted metadata models to the target database, identified by their request IDs.

```
aws dms describe-metadata-model-exports-to-target \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --filters {{Name=request-id,Values=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,a1b2c3d4-5678-90ab-cdef-EXAMPLE22222,a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
Output:

```
{
    "Requests": [
        {
            "Status": "SUCCESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
        },
        {
            "Status": "IN_PROGRESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Progress": {
                "ProgressPercent": 50.0,
                "TotalObjects": 100,
                "ProgressStep": "APPLYING",
                "ProcessedObject": {
                    "EndpointType": "TARGET"
                }
            }
        },
        {
            "Status": "FAILED",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Error": {
                "defaultErrorDetails": {
                    "Message": "No objects were found according to the specified selection rules. Please review your selection rules and try again."
                }
            }
        }
    ]
}
```
For more information, see [Applying your converted code](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-save-apply.html#schema-conversion-apply) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeMetadataModelExportsToTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-metadata-model-exports-to-target.html) in *AWS CLI Command Reference*.

### `describe-metadata-model-imports`
<a name="database-migration-service_DescribeMetadataModelImports_cli_2_topic"></a>

The following code example shows how to use `describe-metadata-model-imports`.

**AWS CLI**
**To describe metadata model imports**
The following `describe-metadata-model-imports` example retrieves the status of metadata import operations identified by their request IDs.

```
aws dms describe-metadata-model-imports \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --filters {{Name=request-id,Values=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,a1b2c3d4-5678-90ab-cdef-EXAMPLE22222,a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
Output:

```
{
    "Requests": [
        {
            "Status": "SUCCESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
        },
        {
            "Status": "IN_PROGRESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Progress": {
                "ProgressPercent": 50.0,
                "TotalObjects": 100,
                "ProgressStep": "IN_PROGRESS",
                "ProcessedObject": {
                    "EndpointType": "SOURCE"
                }
            }
        },
        {
            "Status": "FAILED",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Error": {
                "defaultErrorDetails": {
                    "Message": "No objects were found according to the specified selection rules. Please review your selection rules and try again."
                }
            }
        }
    ]
}
```
For more information, see [Navigating the metadata model tree](https://docs.aws.amazon.com/dms/latest/userguide/sc-metadata-model.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeMetadataModelImports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-metadata-model-imports.html) in *AWS CLI Command Reference*.

### `describe-metadata-model`
<a name="database-migration-service_DescribeMetadataModel_cli_2_topic"></a>

The following code example shows how to use `describe-metadata-model`.

**AWS CLI**
**To describe a metadata model**
The following `describe-metadata-model` example retrieves detailed information about the `ExampleTable` table in the `ExampleSchema` schema from the source metadata tree, including its SQL definition and references to the corresponding converted metadata models in the target database.

```
aws dms describe-metadata-model \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema", "table-name": "ExampleTable"}, "rule-action": "explicit"}]}}}' \
    --origin {{SOURCE}}
```
Output:

```
{
    "MetadataModelName": "ExampleTable",
    "MetadataModelType": "table",
    "TargetMetadataModels": [
        {
            "MetadataModelName": "exampletable",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-target-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"exampleschema\", \"table-name\": \"exampletable\"}, \"rule-action\": \"explicit\"}]}"
        }
    ],
    "Definition": "CREATE TABLE ExampleTable (ExampleColumn INTEGER NOT NULL);"
}
```
For more information, see [Navigating the metadata model tree](https://docs.aws.amazon.com/dms/latest/userguide/sc-metadata-model.html#sc-metadata-model-navigating) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeMetadataModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-metadata-model.html) in *AWS CLI Command Reference*.

### `describe-migration-projects`
<a name="database-migration-service_DescribeMigrationProjects_cli_2_topic"></a>

The following code example shows how to use `describe-migration-projects`.

**AWS CLI**
**To describe migration projects**
The following `describe-migration-projects` example retrieves the details of a migration project identified by its ARN.

```
aws dms describe-migration-projects \
    --filters {{Name=migration-project-identifier,Values=arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}}
```
Output:

```
{
    "MigrationProjects": [
        {
            "MigrationProjectName": "example-migration-project",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "MigrationProjectCreationTime": "2026-01-09T12:30:00.000000+00:00",
            "SourceDataProviderDescriptors": [
                {
                    "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:example-source-secret-A1B2C3",
                    "SecretsManagerAccessRoleArn": "arn:aws:iam::123456789012:role/example-secrets-manager-role",
                    "DataProviderName": "example-data-provider",
                    "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
                }
            ],
            "TargetDataProviderDescriptors": [
                {
                    "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:example-target-secret-A1B2C3",
                    "SecretsManagerAccessRoleArn": "arn:aws:iam::123456789012:role/example-secrets-manager-role",
                    "DataProviderName": "example-data-provider",
                    "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
                }
            ],
            "InstanceProfileArn": "arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "InstanceProfileName": "example-instance-profile",
            "TransformationRules": "{\"rules\":[{\"rule-type\":\"transformation\",\"rule-id\":\"1\",\"rule-name\":\"1\",\"rule-target\":\"schema\",\"rule-action\":\"rename\",\"object-locator\":{\"schema-name\":\"ExampleSchema\"},\"value\":\"TargetSchema\"}]}",
            "Description": "Example migration project for documentation",
            "SchemaConversionApplicationAttributes": {
                "S3BucketPath": "s3://amzn-s3-demo-bucket",
                "S3BucketRoleArn": "arn:aws:iam::123456789012:role/example-s3-access-role"
            }
        }
    ]
}
```
For more information, see [Working with migration projects](https://docs.aws.amazon.com/dms/latest/userguide/migration-projects.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeMigrationProjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-migration-projects.html) in *AWS CLI Command Reference*.

### `describe-orderable-replication-instances`
<a name="database-migration-service_DescribeOrderableReplicationInstances_cli_2_topic"></a>

The following code example shows how to use `describe-orderable-replication-instances`.

**AWS CLI**
**To describe orderable replication instances**
The following `describe-orderable-replication-instances` example lists replication instance types that you can order.

```
aws dms describe-orderable-replication-instances
```
Output:

```
{
    "OrderableReplicationInstances": [
        {
            "EngineVersion": "3.3.2",
            "ReplicationInstanceClass": "dms.c4.2xlarge",
            "StorageType": "gp2",
            "MinAllocatedStorage": 5,
            "MaxAllocatedStorage": 6144,
            "DefaultAllocatedStorage": 100,
            "IncludedAllocatedStorage": 100,
            "AvailabilityZones": [
                "us-east-1a",
                "us-east-1b",
                "us-east-1c",
                "us-east-1d",
                "us-east-1e",
                "us-east-1f"
            ]
        },
        {
            "EngineVersion": "3.3.2",
            "ReplicationInstanceClass": "dms.c4.4xlarge",
            "StorageType": "gp2",
            "MinAllocatedStorage": 5,
            "MaxAllocatedStorage": 6144,
            "DefaultAllocatedStorage": 100,
            "IncludedAllocatedStorage": 100,
            "AvailabilityZones": [
                "us-east-1a",
                "us-east-1b",
                "us-east-1c",
                "us-east-1d",
                "us-east-1e",
                "us-east-1f"
            ]
        },

        ...remaining output omitted...

    }
```
For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeOrderableReplicationInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-orderable-replication-instances.html) in *AWS CLI Command Reference*.

### `describe-refresh-schemas-status`
<a name="database-migration-service_DescribeRefreshSchemasStatus_cli_2_topic"></a>

The following code example shows how to use `describe-refresh-schemas-status`.

**AWS CLI**
**To list the refresh status for an endpoint**
The following `describe-refresh-schemas-status` example returns the status of a previous refresh request.

```
aws dms describe-refresh-schemas-status \
    --endpoint-arn {{arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA}}
```
Output:

```
{
    "RefreshSchemasStatus": {
        "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "Status": "successful",
        "LastRefreshDate": 1590786544.605
    }
}
```
+  For API details, see [DescribeRefreshSchemasStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-refresh-schemas-status.html) in *AWS CLI Command Reference*.

### `describe-replication-instances`
<a name="database-migration-service_DescribeReplicationInstances_cli_2_topic"></a>

The following code example shows how to use `describe-replication-instances`.

**AWS CLI**
**To describe replication instances**
The following `describe-replication-instances` example lists the replication instances in your AWS account.

```
aws dms describe-replication-instances
```
Output:

```
{
    "ReplicationInstances": [
        {
            "ReplicationInstanceIdentifier": "my-repl-instance",
            "ReplicationInstanceClass": "dms.t2.micro",
            "ReplicationInstanceStatus": "available",
            "AllocatedStorage": 5,
            "InstanceCreateTime": 1590011235.952,
            "VpcSecurityGroups": [
                {
                    "VpcSecurityGroupId": "sg-f839b688",
                    "Status": "active"
                }
            ],
            "AvailabilityZone": "us-east-1e",
            "ReplicationSubnetGroup": {
                "ReplicationSubnetGroupIdentifier": "default",
                "ReplicationSubnetGroupDescription": "default",
                "VpcId": "vpc-136a4c6a",
                "SubnetGroupStatus": "Complete",
                "Subnets": [
                    {
                        "SubnetIdentifier": "subnet-da327bf6",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1a"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-42599426",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1d"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-bac383e0",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1c"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-6746046b",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1f"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-d7c825e8",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1e"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-cbfff283",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1b"
                        },
                        "SubnetStatus": "Active"
                    }
                ]
            },
            "PreferredMaintenanceWindow": "wed:11:42-wed:12:12",
            "PendingModifiedValues": {
                "MultiAZ": true
            },
            "MultiAZ": false,
            "EngineVersion": "3.3.2",
            "AutoMinorVersionUpgrade": true,
            "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/f7bc0f8e-1a3a-4ace-9faa-e8494fa3921a",
            "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
            "ReplicationInstancePublicIpAddress": "3.230.18.248",
            "ReplicationInstancePrivateIpAddress": "172.31.75.90",
            "ReplicationInstancePublicIpAddresses": [
                "3.230.18.248"
            ],
            "ReplicationInstancePrivateIpAddresses": [
                "172.31.75.90"
            ],
            "PubliclyAccessible": true,
            "FreeUntil": 1590194829.267
        }
    ]
}
```
For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeReplicationInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-instances.html) in *AWS CLI Command Reference*.

### `describe-replication-subnet-groups`
<a name="database-migration-service_DescribeReplicationSubnetGroups_cli_2_topic"></a>

The following code example shows how to use `describe-replication-subnet-groups`.

**AWS CLI**
**To display the available subnet groups**
The following `describe-replication-subnet-groups` example lists the available subnet groups.

```
aws dms describe-replication-subnet-groups \
    --filter {{"Name=replication-subnet-group-id,Values=my-subnet-group"}}
```
Output:

```
{
    "ReplicationSubnetGroups": [
        {
            "ReplicationSubnetGroupIdentifier": "my-subnet-group",
            "ReplicationSubnetGroupDescription": "my subnet group",
            "VpcId": "vpc-136a4c6a",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-da327bf6",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-bac383e0",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1c"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-d7c825e8",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1e"
                    },
                    "SubnetStatus": "Active"
                }
            ]
        }
    ]
}
```
For more information, see [Setting Up a Network for a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeReplicationSubnetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-subnet-groups.html) in *AWS CLI Command Reference*.

### `describe-replication-task-assessment-results`
<a name="database-migration-service_DescribeReplicationTaskAssessmentResults_cli_2_topic"></a>

The following code example shows how to use `describe-replication-task-assessment-results`.

**AWS CLI**
**To list the results of replication task assessmentss**
The following `describe-replication-task-assessment-results` example lists the results of a prior task assesssment.

```
aws dms describe-replication-task-assessment-results
```
Output:

```
{
    "ReplicationTaskAssessmentResults": [
        {
            "ReplicationTaskIdentifier": "moveit2",
            "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII",
            "ReplicationTaskLastAssessmentDate": 1590790230.0,
            "AssessmentStatus": "No issues found",
            "AssessmentResultsFile": "moveit2/2020-05-29-22-10"
        }
    ]
}
```
For more information, see [Creating a Task Assessment Report](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeReplicationTaskAssessmentResults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-task-assessment-results.html) in *AWS CLI Command Reference*.

### `describe-replication-tasks`
<a name="database-migration-service_DescribeReplicationTasks_cli_2_topic"></a>

The following code example shows how to use `describe-replication-tasks`.

**AWS CLI**
**To describe a replication task**
The following `describe-replication-tasks` example describes current replication tasks.

```
aws dms describe-replication-tasks
```
Output:

```
{
    "ReplicationTasks": [
        {
            "ReplicationTaskIdentifier": "moveit2",
            "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
            "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U",
            "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
            "MigrationType": "full-load",
            "TableMappings": ...output omitted... ,
            "ReplicationTaskSettings": ...output omitted... ,
            "Status": "stopped",
            "StopReason": "Stop Reason FULL_LOAD_ONLY_FINISHED",
            "ReplicationTaskCreationDate": 1590524772.505,
            "ReplicationTaskStartDate": 1590619805.212,
            "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII",
            "ReplicationTaskStats": {
                "FullLoadProgressPercent": 100,
                "ElapsedTimeMillis": 0,
                "TablesLoaded": 0,
                "TablesLoading": 0,
                "TablesQueued": 0,
                "TablesErrored": 0,
                "FreshStartDate": 1590619811.528,
                "StartDate": 1590619811.528,
                "StopDate": 1590619842.068
            }
        }
    ]
}
```
For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeReplicationTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-tasks.html) in *AWS CLI Command Reference*.

### `describe-schemas`
<a name="database-migration-service_DescribeSchemas_cli_2_topic"></a>

The following code example shows how to use `describe-schemas`.

**AWS CLI**
**To describe database schemas**
The following `describe-schemas` example lists the available tables at an endpoint.

```
aws dms describe-schemas \
    --endpoint-arn {{"arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA"}}
```
Output:

```
{
    "Schemas": [
        "prodrep"
    ]
}
```
For more information, see [This is the topic title](https://link.to.the/topic/page) in the *AWS Database Migration Service User Guide*.
+  For API details, see [DescribeSchemas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-schemas.html) in *AWS CLI Command Reference*.

### `export-metadata-model-assessment`
<a name="database-migration-service_ExportMetadataModelAssessment_cli_2_topic"></a>

The following code example shows how to use `export-metadata-model-assessment`.

**AWS CLI**
**To export a conversion assessment report**
The following `export-metadata-model-assessment` example exports a conversion assessment report for all objects in the `ExampleSchema` schema.

```
aws dms export-metadata-model-assessment \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"}, "rule-action": "explicit"}]}}}' \
    --file-name {{example-assessment-report}} \
    --assessment-report-types {{pdf}} {{csv}}
```
Output:

```
{
    "PdfReport": {
        "S3ObjectKey": "example-migration-project/example-assessment-report.pdf",
        "ObjectURL": "https://amzn-s3-demo-bucket.s3.amazonaws.com/example-migration-project/example-assessment-report.pdf"
    },
    "CsvReport": {
        "S3ObjectKey": "example-migration-project/example-assessment-report.zip",
        "ObjectURL": "https://amzn-s3-demo-bucket.s3.amazonaws.com/example-migration-project/example-assessment-report.zip"
    }
}
```
For more information, see [Creating database migration assessment reports](https://docs.aws.amazon.com/dms/latest/userguide/assessment-reports.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ExportMetadataModelAssessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/export-metadata-model-assessment.html) in *AWS CLI Command Reference*.

### `get-target-selection-rules`
<a name="database-migration-service_GetTargetSelectionRules_cli_2_topic"></a>

The following code example shows how to use `get-target-selection-rules`.

**AWS CLI**
**To convert source selection rules to target selection rules**
The following `get-target-selection-rules` example converts source selection rules that select the `ExampleTable` table in the `ExampleSchema` schema into target selection rules that reference its converted counterpart.

```
aws dms get-target-selection-rules \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "database-name": "ExampleDatabase", "schema-name": "ExampleSchema", "table-name": "ExampleTable"}, "rule-action": "explicit"}]}}}'
```
Output:

```
{
    "TargetSelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-target-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"exampledatabase_exampleschema\", \"table-name\": \"exampletable\"}, \"rule-action\": \"explicit\"}]}"
}
```
For more information, see [Using selection rules](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [GetTargetSelectionRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/get-target-selection-rules.html) in *AWS CLI Command Reference*.

### `list-tags-for-resource`
<a name="database-migration-service_ListTagsForResource_cli_2_topic"></a>

The following code example shows how to use `list-tags-for-resource`.

**AWS CLI**
**To list the tags for a resource**
The following `list-tags-for-resource` example lists the tags for a replication instance.

```
aws dms list-tags-for-resource \
    --resource-arn {{arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE}}
```
Output:

```
{
    "TagList": [
        {
            "Key": "Project",
            "Value": "dbMigration"
        },
        {
            "Key": "Environment",
            "Value": "PROD"
        }
    ]
}
```
For more information, see [Tagging Resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/list-tags-for-resource.html) in *AWS CLI Command Reference*.

### `modify-conversion-configuration`
<a name="database-migration-service_ModifyConversionConfiguration_cli_2_topic"></a>

The following code example shows how to use `modify-conversion-configuration`.

**AWS CLI**
**To modify a conversion configuration**
The following `modify-conversion-configuration` example enables generative AI assisted conversion and updates a conversion path setting for a migration project.

```
aws dms modify-conversion-configuration \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --conversion-configuration '{{{"Common project settings":{"EnableGenAiConversion":true},"MSSQL_TO_AURORA_POSTGRESQL":{"ConvertProceduresToFunction":false}}}}'
```
Output:

```
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
}
```
For more information, see [Specifying schema conversion settings](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-settings.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ModifyConversionConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-conversion-configuration.html) in *AWS CLI Command Reference*.

### `modify-data-provider`
<a name="database-migration-service_ModifyDataProvider_cli_2_topic"></a>

The following code example shows how to use `modify-data-provider`.

**AWS CLI**
**To modify a data provider**
The following `modify-data-provider` example updates the description and server name of a data provider.

```
aws dms modify-data-provider \
    --data-provider-identifier {{arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --description {{"Updated data provider description"}} \
    --engine {{sqlserver}} \
    --settings {{MicrosoftSqlServerSettings={ServerName=new-source-server.us-east-1.rds.amazonaws.com}}}
```
Output:

```
{
    "DataProvider": {
        "DataProviderName": "example-data-provider",
        "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "DataProviderCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "Description": "Updated data provider description",
        "Engine": "sqlserver",
        "Settings": {
            "MicrosoftSqlServerSettings": {
                "ServerName": "new-source-server.us-east-1.rds.amazonaws.com",
                "Port": 1433,
                "DatabaseName": "ExampleDatabase",
                "SslMode": "verify-full",
                "CertificateArn": "arn:aws:dms:us-east-1:123456789012:cert:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        }
    }
}
```
For more information, see [Working with data providers](https://docs.aws.amazon.com/dms/latest/userguide/data-providers.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ModifyDataProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-data-provider.html) in *AWS CLI Command Reference*.

### `modify-endpoint`
<a name="database-migration-service_ModifyEndpoint_cli_2_topic"></a>

The following code example shows how to use `modify-endpoint`.

**AWS CLI**
**To modify an endpoint**
The following `modify-endpoint` example adds an extra connection attribute to an endpoint.

```
aws dms modify-endpoint \
    --endpoint-arn {{"arn:aws:dms:us-east-1:123456789012:endpoint:GUVAFG34EECUOJ6QVZ56DAHT3U"}} \
    --extra-connection-attributes {{"compressionType=GZIP"}}
```
Output:

```
{
    "Endpoint": {
        "EndpointIdentifier": "src-endpoint",
        "EndpointType": "SOURCE",
        "EngineName": "s3",
        "EngineDisplayName": "Amazon S3",
        "ExtraConnectionAttributes": "compressionType=GZIP;csvDelimiter=,;csvRowDelimiter=\\n;",
        "Status": "active",
        "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:GUVAFG34EECUOJ6QVZ56DAHT3U",
        "SslMode": "none",
        "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role",
        "S3Settings": {
            "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role",
            "CsvRowDelimiter": "\\n",
            "CsvDelimiter": ",",
            "BucketFolder": "",
            "BucketName": "",
            "CompressionType": "GZIP",
            "EnableStatistics": true
        }
    }
}
```
For more information, see Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP\_Endpoints.html>`\_\_ in the *AWS Database Migration Service User Guide*.
+  For API details, see [ModifyEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-endpoint.html) in *AWS CLI Command Reference*.

### `modify-event-subscription`
<a name="database-migration-service_ModifyEventSubscription_cli_2_topic"></a>

The following code example shows how to use `modify-event-subscription`.

**AWS CLI**
**To modify an event subscription**
The following `modify-event-subscription` example changes the source type of an event subscription.

```
aws dms modify-event-subscription \
    --subscription-name {{"my-dms-events"}} \
    --source-type {{replication-task}}
```
Output:

```
{
    "EventSubscription": {
        "CustomerAwsId": "123456789012",
        "CustSubscriptionId": "my-dms-events",
        "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:my-sns-topic",
        "Status": "modifying",
        "SubscriptionCreationTime": "2020-05-29 17:04:40.262",
        "SourceType": "replication-task",
        "Enabled": true
    }
}
```
For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ModifyEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-event-subscription.html) in *AWS CLI Command Reference*.

### `modify-instance-profile`
<a name="database-migration-service_ModifyInstanceProfile_cli_2_topic"></a>

The following code example shows how to use `modify-instance-profile`.

**AWS CLI**
**To modify an instance profile**
The following `modify-instance-profile` example updates the description and network type of an instance profile.

```
aws dms modify-instance-profile \
    --instance-profile-identifier {{arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --description {{"Updated instance profile description"}} \
    --network-type {{DUAL}}
```
Output:

```
{
    "InstanceProfile": {
        "InstanceProfileArn": "arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "KmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "PubliclyAccessible": false,
        "NetworkType": "DUAL",
        "InstanceProfileName": "example-instance-profile",
        "Description": "Updated instance profile description",
        "InstanceProfileCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "SubnetGroupIdentifier": "example-replication-subnet-group",
        "VpcSecurityGroups": [
            "sg-0123456789abcdef0"
        ]
    }
}
```
For more information, see [Working with instance profiles](https://docs.aws.amazon.com/dms/latest/userguide/instance-profiles.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ModifyInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-instance-profile.html) in *AWS CLI Command Reference*.

### `modify-migration-project`
<a name="database-migration-service_ModifyMigrationProject_cli_2_topic"></a>

The following code example shows how to use `modify-migration-project`.

**AWS CLI**
**To modify a migration project**
The following `modify-migration-project` example updates the source data provider and description of a migration project.

```
aws dms modify-migration-project \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --description {{"Updated migration project description"}} \
    --source-data-provider-descriptors {{DataProviderIdentifier=arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS}}
```
Output:

```
{
    "MigrationProject": {
        "MigrationProjectName": "example-migration-project",
        "MigrationProjectArn": "arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "MigrationProjectCreationTime": "2026-01-09T12:30:00.000000+00:00",
        "SourceDataProviderDescriptors": [
            {
                "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:example-source-secret-A1B2C3",
                "SecretsManagerAccessRoleArn": "arn:aws:iam::123456789012:role/example-secrets-manager-role",
                "DataProviderName": "example-data-provider",
                "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        ],
        "TargetDataProviderDescriptors": [
            {
                "SecretsManagerSecretId": "arn:aws:secretsmanager:us-east-1:123456789012:secret:example-target-secret-A1B2C3",
                "SecretsManagerAccessRoleArn": "arn:aws:iam::123456789012:role/example-secrets-manager-role",
                "DataProviderName": "example-data-provider",
                "DataProviderArn": "arn:aws:dms:us-east-1:123456789012:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS"
            }
        ],
        "InstanceProfileArn": "arn:aws:dms:us-east-1:123456789012:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS",
        "InstanceProfileName": "example-instance-profile",
        "TransformationRules": "{\"rules\":[{\"rule-type\":\"transformation\",\"rule-id\":\"1\",\"rule-name\":\"1\",\"rule-target\":\"schema\",\"rule-action\":\"rename\",\"object-locator\":{\"schema-name\":\"ExampleSchema\"},\"value\":\"TargetSchema\"}]}",
        "Description": "Updated migration project description",
        "SchemaConversionApplicationAttributes": {
            "S3BucketPath": "s3://amzn-s3-demo-bucket",
            "S3BucketRoleArn": "arn:aws:iam::123456789012:role/example-s3-access-role"
        }
    }
}
```
For more information, see [Working with migration projects](https://docs.aws.amazon.com/dms/latest/userguide/migration-projects-manage.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ModifyMigrationProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-migration-project.html) in *AWS CLI Command Reference*.

### `modify-replication-instance`
<a name="database-migration-service_ModifyReplicationInstance_cli_2_topic"></a>

The following code example shows how to use `modify-replication-instance`.

**AWS CLI**
**To modify a replication instance**
The following `modify-replication-instance` example modifies a replication instance so that it uses a Multi-AZ deployment.

```
aws dms modify-replication-instance \
     --replication-instance-arn {{arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE}} \
     --multi-az
```
Output:

```
{
    "ReplicationInstance": {
        "ReplicationInstanceIdentifier": "my-repl-instance",
        "ReplicationInstanceClass": "dms.t2.micro",
        "ReplicationInstanceStatus": "available",
        "AllocatedStorage": 5,
        "InstanceCreateTime": 1590011235.952,

        ...output omitted...

        "PendingModifiedValues": {
            "MultiAZ": true
        },
        "MultiAZ": false,
        "EngineVersion": "3.3.2",
        "AutoMinorVersionUpgrade": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/f7bc0f8e-1a3a-4ace-9faa-e8494fa3921a",

        ...output omitted...

    }
}
```
For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ModifyReplicationInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-instance.html) in *AWS CLI Command Reference*.

### `modify-replication-subnet-group`
<a name="database-migration-service_ModifyReplicationSubnetGroup_cli_2_topic"></a>

The following code example shows how to use `modify-replication-subnet-group`.

**AWS CLI**
**To modify a subnet group**
The following `modify-replication-subnet-group` example changes the lists of subnets associated with a subnet group.

```
aws dms modify-replication-subnet-group \
    --replication-subnet-group-identifier {{my-subnet-group}} \
    --subnet-id {{subnet-da327bf6}} {{subnet-bac383e0}}
```
Output:

```
{
    "ReplicationSubnetGroup": {
        "ReplicationSubnetGroupIdentifier": "my-subnet-group",
        "ReplicationSubnetGroupDescription": "my subnet group",
        "VpcId": "vpc-136a4c6a",
        "SubnetGroupStatus": "Complete",
        "Subnets": [
            {
                "SubnetIdentifier": "subnet-da327bf6",
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1a"
                },
                "SubnetStatus": "Active"
            },
            {
                "SubnetIdentifier": "subnet-bac383e0",
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1c"
                },
                "SubnetStatus": "Active"
            }
        ]
    }
}
```
For more information, see [Setting Up a Network for a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ModifyReplicationSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-subnet-group.html) in *AWS CLI Command Reference*.

### `modify-replication-task`
<a name="database-migration-service_ModifyReplicationTask_cli_2_topic"></a>

The following code example shows how to use `modify-replication-task`.

**AWS CLI**
**To modify a replication task**
The following `modify-replication-task` example changes the table mappings for a task.

```
aws dms modify-replication-task \
    --replication-task-arn {{"arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"}} \
    --table-mappings {{file://table-mappings.json}}
```
Contents of `table-mappings.json`:

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "prodrep",
                "table-name": "ACCT_%"
            },
            "rule-action": "include",
            "filters": []
        }
    ]
}
```
Output:

```
{
    "ReplicationTask": {
        "ReplicationTaskIdentifier": "moveit2",
        "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "MigrationType": "full-load",
        "TableMappings": ...output omitted...,
        "ReplicationTaskSettings": ...output omitted...,
        "Status": "modifying",
        "StopReason": "Stop Reason FULL_LOAD_ONLY_FINISHED",
        "ReplicationTaskCreationDate": 1590524772.505,
        "ReplicationTaskStartDate": 1590789424.653,
        "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"
    }
}
```
For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [ModifyReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-task.html) in *AWS CLI Command Reference*.

### `reboot-replication-instance`
<a name="database-migration-service_RebootReplicationInstance_cli_2_topic"></a>

The following code example shows how to use `reboot-replication-instance`.

**AWS CLI**
**To reboot a replication instance**
The following `reboot-replication-instance` example reboots a replication instance.

```
aws dms reboot-replication-instance \
    --replication-instance-arn {{arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE}}
```
Output:

```
{
    "ReplicationInstance": {
        "ReplicationInstanceIdentifier": "my-repl-instance",
        "ReplicationInstanceClass": "dms.t2.micro",
        "ReplicationInstanceStatus": "rebooting",
        "AllocatedStorage": 5,
        "InstanceCreateTime": 1590011235.952,
    ... output omitted ...
    }
}
```
For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [RebootReplicationInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/reboot-replication-instance.html) in *AWS CLI Command Reference*.

### `refresh-schemas`
<a name="database-migration-service_RefreshSchemas_cli_2_topic"></a>

The following code example shows how to use `refresh-schemas`.

**AWS CLI**
**To refresh database schemas**
The following `refresh-schemas` example requests that AWS DMS refresh the list of schemas at an endpoint.

```
aws dms refresh-schemas \
    --replication-instance-arn {{arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE}} \
    --endpoint-arn {{"arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA"}}
```
Output:

```
{
    "RefreshSchemasStatus": {
        "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "Status": "refreshing",
        "LastRefreshDate": 1590019949.103
    }
}
```
+  For API details, see [RefreshSchemas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/refresh-schemas.html) in *AWS CLI Command Reference*.

### `reload-tables`
<a name="database-migration-service_ReloadTables_cli_2_topic"></a>

The following code example shows how to use `reload-tables`.

**AWS CLI**
**To refresh the list of tables available at an endpoint**
The following `reload-tables` example reloads the list of available tables at an endpoint.

```
aws dms reload-tables \
    --replication-task-arn {{"arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"}} \
    --tables-to-reload {{"SchemaName=prodrep,TableName=ACCT_BAL"}}
```
Output:

```
{
    "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"
}
```
+  For API details, see [ReloadTables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/reload-tables.html) in *AWS CLI Command Reference*.

### `remove-tags-from-resource`
<a name="database-migration-service_RemoveTagsFromResource_cli_2_topic"></a>

The following code example shows how to use `remove-tags-from-resource`.

**AWS CLI**
**To remove tags from a replication instance**
The following `remove-tags-from-resource` example removes tags from a replication instance.

```
aws dms remove-tags-from-resource \
    --resource-arn {{arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE}} \
    --tag-keys {{Environment}} {{Project}}
```
This command produces no output.
For more information, see [Tagging Resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [RemoveTagsFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/remove-tags-from-resource.html) in *AWS CLI Command Reference*.

### `start-extension-pack-association`
<a name="database-migration-service_StartExtensionPackAssociation_cli_2_topic"></a>

The following code example shows how to use `start-extension-pack-association`.

**AWS CLI**
**To apply an extension pack to the target database**
The following `start-extension-pack-association` example queues the application of an extension pack to the target database.

```
aws dms start-extension-pack-association \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}}
```
Output:

```
{
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Using extension packs](https://docs.aws.amazon.com/dms/latest/userguide/extension-pack.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StartExtensionPackAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-extension-pack-association.html) in *AWS CLI Command Reference*.

### `start-metadata-model-assessment`
<a name="database-migration-service_StartMetadataModelAssessment_cli_2_topic"></a>

The following code example shows how to use `start-metadata-model-assessment`.

**AWS CLI**
**To assess all objects in a schema**
The following `start-metadata-model-assessment` example queues an assessment of the conversion complexity for all objects in the `ExampleSchema` schema.

```
aws dms start-metadata-model-assessment \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}}}'
```
Output:

```
{
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Creating database migration assessment reports](https://docs.aws.amazon.com/dms/latest/userguide/assessment-reports.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StartMetadataModelAssessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-metadata-model-assessment.html) in *AWS CLI Command Reference*.

### `start-metadata-model-conversion`
<a name="database-migration-service_StartMetadataModelConversion_cli_2_topic"></a>

The following code example shows how to use `start-metadata-model-conversion`.

**AWS CLI**
**To convert all objects in a schema**
The following `start-metadata-model-conversion` example queues a conversion of all objects in the `ExampleSchema` schema to the target database format.

```
aws dms start-metadata-model-conversion \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}}}'
```
Output:

```
{
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Converting database schemas](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-convert.html#schema-conversion-convert-steps) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StartMetadataModelConversion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-metadata-model-conversion.html) in *AWS CLI Command Reference*.

### `start-metadata-model-creation`
<a name="database-migration-service_StartMetadataModelCreation_cli_2_topic"></a>

The following code example shows how to use `start-metadata-model-creation`.

**AWS CLI**
**To create a metadata model for a SQL statement**
The following `start-metadata-model-creation` example queues the creation of a metadata model for a SQL statement. The selection rule specifies the schema where the metadata model is placed, and `--metadata-model-name` provides a unique identifier for use in subsequent operations.

```
aws dms start-metadata-model-creation \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "database-name": "ExampleDatabase", "schema-name": "ExampleSchema"}, "rule-action": "explicit"}]}}}' \
    --metadata-model-name {{ExampleStatement}} \
    --properties StatementProperties={Definition="SELECT * FROM ExampleTable;"}
```
Output:

```
{
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Creating statement metadata models](https://docs.aws.amazon.com/dms/latest/userguide/sc-metadata-model.html#sc-metadata-model-creation) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StartMetadataModelCreation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-metadata-model-creation.html) in *AWS CLI Command Reference*.

### `start-metadata-model-export-as-script`
<a name="database-migration-service_StartMetadataModelExportAsScript_cli_2_topic"></a>

The following code example shows how to use `start-metadata-model-export-as-script`.

**AWS CLI**
**To export converted metadata models as DDL scripts**
The following `start-metadata-model-export-as-script` example queues an export of converted metadata models for all objects in the `ExampleSchema` schema as data definition language (DDL) scripts to the Amazon S3 bucket associated with the migration project.

```
aws dms start-metadata-model-export-as-script \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-target-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}}}' \
    --origin {{TARGET}} \
    --file-name {{ExampleScript}}
```
Output:

```
{
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Saving your converted code to a SQL file](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-save-apply.html#schema-conversion-save) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StartMetadataModelExportAsScript](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-metadata-model-export-as-script.html) in *AWS CLI Command Reference*.

### `start-metadata-model-export-to-target`
<a name="database-migration-service_StartMetadataModelExportToTarget_cli_2_topic"></a>

The following code example shows how to use `start-metadata-model-export-to-target`.

**AWS CLI**
**To export converted metadata models to the target database**
The following `start-metadata-model-export-to-target` example queues an export of converted metadata models for all objects in the `ExampleSchema` schema to the target database.

```
aws dms start-metadata-model-export-to-target \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-target-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}}}' \
    --overwrite-extension-pack
```
Output:

```
{
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Applying your converted code](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-save-apply.html#schema-conversion-apply) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StartMetadataModelExportToTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-metadata-model-export-to-target.html) in *AWS CLI Command Reference*.

### `start-metadata-model-import`
<a name="database-migration-service_StartMetadataModelImport_cli_2_topic"></a>

The following code example shows how to use `start-metadata-model-import`.

**AWS CLI**
**To import metadata from the source database**
The following `start-metadata-model-import` example queues a metadata import for all objects in the `ExampleSchema` schema from the source database.

```
aws dms start-metadata-model-import \
    --migration-project-identifier {{arn:aws:dms:us-east-1:123456789012:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS}} \
    --selection-rules '{{{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}}}' \
    --origin {{SOURCE}} \
    --no-refresh
```
Output:

```
{
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Navigating the metadata model tree](https://docs.aws.amazon.com/dms/latest/userguide/sc-metadata-model.html#sc-metadata-model-navigating) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StartMetadataModelImport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-metadata-model-import.html) in *AWS CLI Command Reference*.

### `start-replication-task-assessment`
<a name="database-migration-service_StartReplicationTaskAssessment_cli_2_topic"></a>

The following code example shows how to use `start-replication-task-assessment`.

**AWS CLI**
**To start a task assessment**
The following `start-replication-task-assessment` example starts a replication task assessment.

```
aws dms start-replication-task-assessment \
    --replication-task-arn {{arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII}}
```
Output:

```
{
    "ReplicationTask": {
        "ReplicationTaskIdentifier": "moveit2",
        "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "MigrationType": "full-load",
        "TableMappings": ...output omitted...,
        "ReplicationTaskSettings": ...output omitted...,
        "Status": "testing",
        "StopReason": "Stop Reason FULL_LOAD_ONLY_FINISHED",
        "ReplicationTaskCreationDate": 1590524772.505,
        "ReplicationTaskStartDate": 1590789988.677,
        "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"
    }
}
```
For more information, see [Creating a Task Assessment Report](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StartReplicationTaskAssessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task-assessment.html) in *AWS CLI Command Reference*.

### `start-replication-task`
<a name="database-migration-service_StartReplicationTask_cli_2_topic"></a>

The following code example shows how to use `start-replication-task`.

**AWS CLI**
**To start a replication task**
The following `command-name` example lists the available widgets in your AWS account.

```
aws dms start-replication-task \
    --replication-task-arn {{arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII}} \
    --start-replication-task-type {{reload-target}}
```
Output:

```
{
    "ReplicationTask": {
        "ReplicationTaskIdentifier": "moveit2",
        "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "MigrationType": "full-load",
        "TableMappings": ...output omitted... ,
        "ReplicationTaskSettings": ...output omitted... ,
        "Status": "starting",
        "ReplicationTaskCreationDate": 1590524772.505,
        "ReplicationTaskStartDate": 1590619805.212,
        "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"
    }
}
```
For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StartReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task.html) in *AWS CLI Command Reference*.

### `stop-replication-task`
<a name="database-migration-service_StopReplicationTask_cli_2_topic"></a>

The following code example shows how to use `stop-replication-task`.

**AWS CLI**
**To stop a task**
The following `stop-replication-task` example stops a task.

```
aws dms stop-replication-task \
    --replication-task-arn {{arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII}}
```
Output:

```
{
    "ReplicationTask": {
        "ReplicationTaskIdentifier": "moveit2",
        "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "MigrationType": "full-load",
        "TableMappings": ...output omitted...,
        "ReplicationTaskSettings": ...output omitted...,
        "Status": "stopping",
        "ReplicationTaskCreationDate": 1590524772.505,
        "ReplicationTaskStartDate": 1590789424.653,
        "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"
    }
}
```
For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [StopReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/stop-replication-task.html) in *AWS CLI Command Reference*.

### `test-connection`
<a name="database-migration-service_TestConnection_cli_2_topic"></a>

The following code example shows how to use `test-connection`.

**AWS CLI**
**To test a connection to an endpoint**
The following `test-connection` example tests whether an endpoint can be accessed from a replication instance.

```
aws dms test-connection \
    --replication-instance-arn {{arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE}} \
    --endpoint-arn {{arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA}}
```
Output:

```
{
    "Connection": {
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "Status": "testing",
        "EndpointIdentifier": "src-database-1",
        "ReplicationInstanceIdentifier": "my-repl-instance"
    }
}
```
For more information, see [Creating source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [TestConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/test-connection.html) in *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
