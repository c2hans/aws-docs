---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/configure-the-solution.html
---

# Configure the guidance
<a name="configure-the-solution"></a>

This section describes the various options that you configure for your use case while deploying Apache Druid in your AWS account.

The following table lists the configuration, setting, and if the configuration is mandatory before you deploy the guidance in your AWS account.

| Configuration | Setting | Default value | Mandatory/Optional |
| --- | --- | --- | --- |
|  [Amazon Machine Images (AMI)](#amazon-machine-images-ami)  |  `customAmi`  | Latest Amazon Linux 2 AMI | Optional |
|  [Data retention policy](#data-retention-policy)  |  `retainData`  | true | Optional |
|  [Network](#network)  |  |  | Optional |
| \* VPC CIDR Range |  `vpcCidr`  | 10.0.0.0/16 | Optional |
| \* VPC ID |  `vpcId`  | N/A | Optional |
| \* Application Load Balancer |  `internetFacing`  | true | Optional |
| \* Bastion host |  `bastionHost`  | false | Optional |
|  [Druid domain](#druid-domain)  |  |  | Optional |
| \* Route53 hosted zone |  `route53HostedZoneName`, and `route53HostedZoneId`  | N/A | Optional |
| \* Druid domain |  `druidDomain`  | N/A | Optional |
| \* TLS certificate |  `tlsCertificateArn`  | N/A | Optional |
|  [FIPS 140-2](#fips-140-2)  |  `useFipsEndpoint`  | false | Optional |
|  [Identity provider](#identity-provider)  |  `oidcIdpConfig`  | N/A | Optional |
|  [Druid configuration](#druid-basic-configuration)  |  |  | Mandatory |
| \* Version |  `druidVersion`  |  | Mandatory |
| \* Cluster name |  `druidClusterName`  |  | Mandatory |
| \* Operation platform |  `druidOperationPlatform`  |  | Mandatory |
| \* Custom IAM policy list |  `druidInstanceIamPolicyArns`  | N/A | Optional |
| \* Query concurrency rate limit |  `druidConcurrentQueryLimit`  | 100 | Optional |
| \* Extensions |  `druidExtensions`  |  | Mandatory |
| \* Common runtime properties |  `druidCommonRuntimeConfig`  | N/A | Optional |
| \* Retention rules |  `druidRetentionRules`  |  | Optional |
|  [Druid metadata store](#druid-metadata-store)  |  `druidMetadataStoreConfig`  | Amazon Aurora PostgreSQL Serverless | Mandatory |
|  [Druid deep storage](#druid-deep-storage)  |  `druidDeepStorageConfig`  |  | Mandatory |
|  [Druid EC2 configuration](#druid-ec2-configuration)  |  |  |  **Mandatory** (if the druidOperationPlatform is EC2) |
| \* Auto scaling group |  `<Druid node type>`  |  | Mandatory |
| \* Rolling update policy |  `rollingUpdatePolicy`  | N/A | Optional |
| \* Auto scaling policy | ` autoScalingPolicy ` | N/A | Optional |
| \* Runtime configuration |  `runtimeConfig`  | N/A | Optional |
|  [Druid EKS configuration](#druid-eks-configuration)  |  |  |  **Mandatory** (if the druidOperationPlatform is EKS) |
| \* EKS cluster configuration |  `druidEksConfig`  |  | Mandatory |
| \* EC2 capacity provider configuration |  `<nodeGroupName>`  |  |  **Mandatory** (if capacityProviderType is EC2) |
| \* Fargate capacity provider configuration |  `<druidProcessName>`  |  |  **Mandatory** (if capacityProviderType is Fargate) |

## Amazon Machine Images (AMI)
<a name="amazon-machine-images-ami"></a>

By default, the `EC2` hosting option provisions EC2 instances with Amazon Linux 2.

To override this, specify the `customAmi` object in the `cdk.json` file. This object should provide the AMI name and owners' account IDs or the alias that cdk would use to perform an AMI lookup. Depending on the instance types utilized in the cluster, provide the corresponding AMI for **arm64** (Graviton instances) or **amd64** (x86-based instance types).

**Note**
The guidance has been tested with Amazon Linux, Ubuntu 20.04 LTS and Ubuntu 22.04 LTS.

```
"customAmi": {
    "arm64": {
        "name": "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-arm64-server*",
        "owners": ["amazon"]
    },
    "amd64": {
        "name": "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server*",
        "owners": ["amazon"]
    }
},
```

## Data retention policy
<a name="data-retention-policy"></a>

By default, all the guidance data (S3 buckets, Aurora DB instances, Aurora DB snapshots etc.) is retained when you uninstall the guidance.

To remove this data, in the configuration file, set the retainData flag to false. You are liable for the service charges when guidance data is retained in the default configuration.

```
"retainData": false,
```

## Network
<a name="network"></a>

 **Virtual Private Cloud (VPC)**
+ VPC CIDR Range: By default, the guidance creates a new VPC for deployment with 10.120.0.0/16 as the default CIDR range. You can override this using this configuration:

```
"vpcCidr": "x.x.x.x/x",
```
+ VPC ID: You can deploy to an existing VPC. To do this, use the following configuration option:

```
"vpcId": "vpc-xxxxxxxxxxxxxxxxx"
```

 **Application Load Balancer setting**

The guidance will provision an ALB to route requests to Druid query instances. It supports both internet facing and private options as follows.

```
"internetFacing": true,
```

The default setting creates a private Application Load Balancer (ALB). To access this private ALB, you can either use an AWS VPN or SSH tunneling via a bastion host. However, if the `internetFacing`` parameter is set to true, the ALB will be publicly available. In such an instance, use the AWS WAF (Web Application Firewall) with your ALB to allow or block requests based on rules in a web access control list (web ACL).

 **Bastion Host**

You can launch a bastion host in the public subnet using this configuration, which facilitates the access to the hosts and services running in private and isolated subnets.

```
"bastionHost": true,
```

## Druid domain
<a name="druid-domain"></a>

This guidance can integrate with Amazon Route 53 to automate the creation of domains, streamlining access to the Druid web console and API endpoints.

With the following Route 53 configuration, this guidance automatically creates a Route53 domain using the specified druidDomain in the supplied hosted zone. Additionally, this guidance creates a certificate in the AWS Certificate Manager (ACM) and associates it with the Application Load Balancer (ALB) to enable secure HTTPS communication.
+ Route 53 hosted zone configuration

```
"route53HostedZoneName": "<The hosted zone name in Route 53. eg. example.com>",

"route53HostedZoneId": "<The hosted zone ID in Route 53. eg. Z03935053V8YUTYYYEXXX>",
```
+ Druid domain configuration

```
"druidDomain": "<A full domain address. eg. druid.example.com>"
```

**Note**
If none of these configurations are set up, the guidance assigns a generic Application Load Balancer (ALB) domain name for your Druid cluster which will expose HTTP protocol only. You have the flexibility to set up the domain outside of the guidance. In such a case, you must configure the TLS certificate and the `druidDomain` to facilitate secure HTTPS access to the Druid cluster after the domain has been successfully set up.
+ TLS certificate configuration

```
"tlsCertificateArn": "<The ARN of ACM certificate>"
```

## FIPS 140-2
<a name="fips-140-2"></a>

The Federal Information Processing Standard ([FIPS](https://aws.amazon.com/compliance/fips/) ) Publication 140-2 is a US and Canadian government standard that specifies the security requirements for cryptographic modules that protect sensitive information.

**Note**
FIPSEndpoints are only available in North American (NA) Regions.

If you want to use FIPS 140-2 validated cryptographic modules, you can set this using this configuration:

```
"useFipsEndpoint": true,
```

## Identity provider
<a name="identity-provider"></a>

By default, this guidance activates basic authentication, enabling access to the Druid web console and API through a username and password. Additionally, you can use user access federation through a third-party identity provider (IdP) that supports OpenID Connect (OIDC) authentication. If you have an existing enterprise Identity Provider, you can integrate it using this CDK configuration.

```
"oidcIdpConfig": {
    "clientId": "<OIDC IDP client ID>",
    "clientSecretArn": "<The ARN of the secret in AWS secret manager which stores the client secret and cookiePassphrase.>",
    "discoveryURI": "<OIDC IDP client discovery URI. e.g. https://dev-pkaccwqn.us.auth0.com/.well-known/openid-configuration>",
    "groupClaimName": "<OIDC claim name that contains the group name list that the user belongs to>",
    "groupRoleMappings": {
        "<groupName>": ["<roleName>", ...],
    }
}
```

The OIDC group mapping facilitates the integration of Role-Based Access Control (RBAC). Users authenticate through an OIDC identity provider, and their group information is extracted from the ID token. This information is then mapped to the corresponding RBAC roles within Druid, governing users' access to resources based on their external OIDC group memberships. This integration ensures that access privileges in Druid align with the user roles defined in the OIDC identity provider. It consists of the following two fields:
+  `groupClaimName`: <the OIDC claim name in the ID token that contains the group membership list that the user belongs to.>
+  `groupRoleMappings`: <it defines a mapping mechanism that associates OIDC groups with specific RBAC roles in Druid>

The client secret consists of the following two fields:
+  `clientSecret`: <the secret code for the OIDC IdP client, which is typically generated by the OIDC IdP.>
+  `cookiePassphrase`: <a password that uses a mix of letters and numbers in plain text form.>

Example: Identity provider configuration to federate through Amazon Cognito.

```
"oidcIdpConfig": {
     "clientId": "<OIDC IDP client ID>",
     "clientSecretArn": "arn:aws:secretsmanager:<region>:<account>:secret:<secret-name>-<random-6-characters>",
     "discoveryURI": "https://cognito-idp.<region>.amazonaws.com/<user pool id>/.well-known/openid-configuration",
     "groupClaimName": "cognito:groups",
     "groupRoleMappings": {
          "developers": ["administrator"],
          "scrum-masters": ["read"]
         }
     }
```

**Note**
You must configure the redirect URI on the IDP side as `https://<druid_domain>/druid-ext/druid-oidc/callback`.

## Druid basic configuration
<a name="druid-basic-configuration"></a>

### Version
<a name="version"></a>

Apache Druid release version (eg. 30.0.0) that you want to run. We recommend using the latest stable [Druid version](https://code.amazon.com/packages/Apjsb-druid-swift/trees/mainline#https://druid.apache).

```
"druidVersion": "30.0.0",
```

### Cluster name
<a name="cluster-name"></a>

A sequence of ASCII characters that uniquely identifies each Druid cluster. If there are multiple deployments, make sure that you have an unique cluster name for each cluster. The cluster name is appended to the CloudFormation stack name.

```
"druidClusterName": "dev",
```

### Operation platform
<a name="operation-platform"></a>

The intended computing service for hosting a Druid cluster currently has two options available:
+ EC2: The guidance will be deployed on Amazon EC2 hosts. For more information on how to configure Druid EC2, refer to the [Druid EC2 configuration](#druid-ec2-configuration) section.

```
"druidOperationPlatform": "ec2",
```
+ EKS: The guidance will be deployed on Amazon EKS.

### Custom IAM policy list (optional)
<a name="custom-iam-policy-list-optional"></a>

By default, this guidance creates an IAM role that gives Druid components the minimum permissions to function. You can extend this role with additional permissions by using the following configuration:

```
"druidInstanceIamPolicyArns": ["The ARN of custom IAM policy"...]
```

### Query concurrency rate limit (optional)
<a name="query-concurrency-rate-limit-optional"></a>

The maximum number of concurrent queries that the Druid cluster can handle. The default value is 100.
+ This parameter sets `druid.broker.http.numConnections` on the broker nodes and `druid.server.http.numThreads` on the historical nodes.
+ In a cluster with 2 broker nodes and the default value of 100, the `druid.server.http.numThreads` parameter on the historical nodes will be set to 100, while the `druid.broker.http.numConnections` parameter on the broker nodes will be set to 50. This configuration ensures that the `druid.server.http.numThreads` value must be equal to or higher than the sum of `druid.broker.http.numConnections` across all the Brokers in the cluster.

To customize this default configuration, you can override the values using the following configuration:

```
"druidConcurrentQueryLimit": number
```

### Extensions
<a name="extensions"></a>

A list of Druid extensions to load into the cluster. To load the core extensions for Druid, you can modify the list by adding or removing extensions from it.

**Note**
It is the customer’s responsibility to ensure the extension’s security, performance, and compatibility. To uphold a robust security posture, we strongly advise consistently monitoring for new releases and promptly applying updates, thereby proactively addressing and mitigating any potential vulnerabilities.

To load any custom extensions that you have developed in-house, make sure that the artifacts for those extensions (such as Java JAR files) are also copied into the `source/lib/docker/extensions` folder. To reduce the configuration overhead, the guidance will automatically incorporate the extensions to the user provided extension list:
+ druid-oidc
+ druid-cloudwatch
+ druid-basic-security
+ druid-s3-extensions
+ postgresql-metadata-storage, and
+ simple-client-sslcontext.

 **Druid extensions example**

```
"druidExtensions": [
    "druid-hdfs-storage",
    "druid-kafka-indexing-service",
    "druid-kinesis-indexing-service",
    "druid-avro-extensions",
    "druid-parquet-extensions",
    "druid-protobuf-extensions",
    "druid-orc-extensions"
],
```

### Common runtime properties(optional)
<a name="common-runtime-propertiesoptional"></a>

By default, the guidance features a common.runtime.properties file located within the `source/lib/uploads/config/_common` directory, to cater to the majority of the use cases. However, you can customize and override the settings in this file using the CDK configuration as needed.

Druid common runtime customization configuration example:

```
"druidCommonRuntimeConfig": {
     "druid.startup.logging.logProperties": false
     }
```

### Retention rules (optional)
<a name="retention-rules-optional"></a>

The data retention policies specify which data to retain and which data to drop from the cluster. The rule chain is evaluated from top to bottom, with the default rule chain always added at the bottom. For more information, refer to the [Using rules to drop and retain data guide](https://druid.apache.org/docs/latest/operations/rule-configuration.html).

Alternatively, you can use the Druid API or the Druid Web Console to configure the retention rules for Druid.

 **Druid retention rules example**

```
"druidRetentionRules": [
          {
          "type": "loadByPeriod",
          "period": "P1M",
          "includeFuture": true,
          "tieredReplicants": {
              "hot": 3,
              "_default_tier": 1
              }
          },
          {
          "type": "loadForever",
          "tieredReplicants": {
             "hot": 1,
             "_default_tier": 1
              }
          }
]
```

## Druid metadata store
<a name="druid-metadata-store"></a>

In the default configuration, this guidance sets up an Amazon Aurora Serverless v1 cluster, using the PostgreSQL-compatible engine as the metadata store for Druid. If you prefer to use an Amazon Aurora cluster as the metadata store, connect to an existing PostgreSQL database, or create the metadata store from a snapshot, you can customize the configuration by applying the following settings:

```
"druidMetadataStoreConfig": {
        // Metadata store type. Acceptable values include aurora, aurora_serverless, or custom.
        "metadataStoreType": "<aurora | aurora_serverless | custom>",

        // The metadata store configuration differs based on the chosen type of metadata store.
        "metadataStoreConfig": {
        },

        // Optional. The configuration for the backup plan determines the frequency and retention policy for the database snapshots.
        "backupPlanConfig" {

        // The cron expression which defines the snapshot frequency. E.g. cron(0 10 * * ? *) which runs at 10:00 am (UTC) every day.
        "scheduleExpression": "<cron expression>",

        // Number of days that the snapshot will be kept
        "deleteAfterDays": number
        }
}
```

### Create a new Aurora metadata store (recommended)
<a name="create-a-new-aurora-metadata-store-recommended"></a>

This section provides instructions for creating a new Aurora metadata store.

```
"druidMetadataStoreConfig": {
      "metadataStoreType": "aurora",
      "metadataStoreConfig": {
          // Optional. Aurora DB instance class type. eg. t3.large
         "rdsInstanceType": string,
          // Optional. Number of DB instances. Default is 2.
         "rdsInstanceCount": number,
         // Optional. The parameter group name for DB instance.
         "rdsParameterGroupName": string,
         // Optional. Aurora PostgreSQL engine version. The default version is 13.6. Please be aware that updating the version of your existing RDS instance will not result in data migration.
         "rdsEngineVersion": string
         }
      }
```

Example configuration to create a new Aurora metadata store:

```
"druidMetadataStoreConfig": {
     "metadataStoreType": "aurora",
     "metadataStoreConfig": {
          "rdsInstanceType": "t3.large",
          "rdsInstanceCount": 2,
          "rdsParameterGroupName":
          "aurora-postgresql13",
          "rdsEngineVersion": "13.6"
          }
     }
```

### Create a new Aurora metadata store from a snapshot
<a name="create-a-new-aurora-metadata-store-from-a-snapshot"></a>

This section provides instructions on how to create a new Aurora metadata store from a snapshot.

**Note**
The guidance will try to create two magic users, specifically `admin` and `druid_system`, to run internal operations if these users don’t exist in the snapshot. If these users already exist in the snapshot, generate a secret in AWS Secrets Manager that includes both the username and password, and then proceed to integrate it into the metadata store configuration. If the secrets are encrypted by a KMS key, ensure that the KMS key permits access from AWS Secrets Manager to enable decryption of the secret.

```
"druidMetadataStoreConfig": {
    "metadataStoreType": "aurora",
    "metadataStoreConfig": {
        // Optional. Aurora DB instance class type. eg. t3.large
        "rdsInstanceType": string,

        // Optional. Number of DB instances. Default is 2.
        "rdsInstanceCount": number,

        // The ARN of RDS snapshot
        "rdsSnapshotArn": string,

        // Optional. The ARN of KMS key which is used to encrypt the database. Required if the storage is encrypted with a KMS key.
        "rdsSnapshotEncryptionKeyArn": string,

        // Optional. Required if the snapshot contains 'druid_system' user.
        "druidInternalUserSecretArn": "<The ARN of secret which stores username and password of the druid_system user >",

        // Optional. Required if the snapshot contains 'admin' user.
        "druidAdminUserSecretArn": "<The ARN of secret which stores username and password of the admin user >",

        // Optional. The parameter group name for DB instance.
        "rdsParameterGroupName": string,

        // Optional. Aurora PostgreSQL engine version. The default version is 13.6. Please be aware that updating the version of your existing RDS instance will not result in data migration.
        "rdsEngineVersion": string
    }
}
```

Example configuration to create a metadata store from snapshot:

```
"druidMetadataStoreConfig": {
    "metadataStoreType": "aurora",
    "metadataStoreConfig": {
        "rdsInstanceType": "t3.large",
        "rdsInstanceCount": 2,
        "rdsSnapshotArn": "arn:aws:rds:<region>:<account-id>:cluster-snapshot:<snapshort-name>",
        "rdsSnapshotEncryptionKeyArn": "arn:aws:kms:<region>:<account-id>:key/<key-id>",
        "druidInternalUserSecretArn": "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-id>",
        "druidAdminUserSecretArn": "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-id>",
        "rdsParameterGroupName": "aurora-postgresql13",
        "rdsEngineVersion": "13.6"
    }
}
```

### Use your own PostgreSQL database for metadata store
<a name="use-your-own-postgresql-database-for-metadata-store"></a>

This section explains how to use your own PostgreSQL database for the metadata store.

**Note**
By default, this guidance will enforce TLS for the database connectivity. If you’re using non-public certificates, you must ensure the non-public certificates can be validated by the Druid system.

```
"druidMetadataStoreConfig": {
    "metadataStoreType": "custom",
    "metadataStoreConfig": {
        // The endpoint address of database
        "databaseUri": string,

        // Optional. The listening port of database. Default to be 5432.
        "databasePort": number,

        // Optional. Database name. Default to be DruidMetadata.
        "databaseName": string,

        // The ARN of secret in secrets manager which stores the administrative username and password in JSON format
        // The secret must contain fields namely "username" and "password"
        "databaseSecretArn": string
    }
}
```

Example configuration to connect to an external metadata store:

```
"druidMetadataStoreConfig": {
    "metadataStoreType": "custom",
    "metadataStoreConfig": {
        "databaseUri": "druidec2stack-dev296-druidmetadataconstructaurorac-xxx.cluster-xxx.us-east-1.rds.amazonaws.com",
        "databasePort": 5432,
        "databaseName": "DruidMetadata",
        "databaseSecretArn": "arn:aws:secretsmanager:<region>:<account>:secret:<secret-id>"
    }
}
```

## Druid deep storage
<a name="druid-deep-storage"></a>

By default, this guidance will set up a bucket in Amazon S3 for deep storage. To use your own bucket for deep storage, you can override this default configuration using the following configuration:

```
"druidDeepStorageConfig": {
    // The ARN of S3 bucket to be used as deep storage
    "bucketArn": string,
    // The bucket prefix to be used to store segments
    "bucketPrefix": string,
    // Optional when using SSE-S3. The KMS key to be used to encrypt the data.
    "bucketEncryptionKeyArn": string
}
```

Example deep storage configuration:

```
"druidDeepStorageConfig": {
    "bucketArn": "arn:aws:s3:::<bucket-id>",
    "bucketPrefix": "druid/segments",
    "bucketEncryptionKeyArn": "arn:aws:kms:<region>:<account-id>:key/<key-id>"
}
```

## Druid EC2 configuration
<a name="druid-ec2-configuration"></a>

### Auto scaling group configuration
<a name="auto-scaling-group-configuration"></a>

This section provides instructions and details about the Auto scaling group configuration for a variety of Druid node types, including master, query, data, historical, middleManager, and ZooKeeper.

This guidance also fully supports the [service tiering](https://druid.apache.org/docs/latest/operations/mixed-workloads/) functionalities provided by Druid, offering enhanced resource management and optimization. The service tiering feature allows you to create distinct groups of Historicals and Brokers, each responsible for managing queries based on the segments and resource requirements of the query.

It covers the following fields for each node type:

```
// Druid node type. Valid values include data, master, query, and zookeeper. In case of service tiering, it also supports data_<tier>, historical_<tier>, middleManager_<tier>

"<Druid node type>": {
      // Minimum number of EC2 instances in the auto scaling group
      "minNodes": number,

      // Optional, maximum number of EC2 instances in the auto scaling group
      "maxNodes": number,

      // Optional. EBS volume size in GB for the root file system of EC2 instance.
      "rootVolumeSize": number,

      // Optional. The size of EBS volume (GB) utilized for segment caching on historical node. Required if not using storage optimized instance types.
      "segmentCacheVolumeSize": number,

      // EC2 instance type. eg. m5.2xlarge.
      "instanceType": string

      }
```

### Rolling update policy (optional)
<a name="rolling-update-policy-optional"></a>

A rolling update is a deployment strategy that incrementally replaces previous versions of an application with new versions of an application by completely replacing the infrastructure on which the application is running.

It minimizes the impact on application availability and ensures a smooth transition to the new version.

The guidance operates on a default process of sequentially replacing the Druid EC2 instances in a specific order: data, query, and master. This replacement process involves stopping the previous instance initially, followed by the creation of a new instance.

Once the new instance is confirmed to be in a healthy state, the process proceeds to replace the next instance in the specified order. In the event that an instance is deemed unhealthy during the update process, the system will initiate a rollback to the previous version.

You can customize and override the batch size using the following configuration:

```
// Optional. The rollingUpdatePolicy defines how an Auto Scaling group resource is updated.
"rollingUpdatePolicy": {
    // Optional. Number of instances that is going to be replaced in each batch. Default 1.
    "maxBatchSize": number
},
```

### Auto scaling policy (optional)
<a name="auto-scaling-policy-optional"></a>

An Auto scaling policy consists of predefined rules and parameters that dictate how the scaling process should occur. These rules are defined by the user based on specific metrics, such as CPU utilization, network traffic, or application-specific performance metrics. In addition to dynamic auto scaling based on Scalable metrics, it also offers schedule-based auto scaling.

```
"autoScalingPolicy": {
    "cpuUtilisationPercent": number between [1, 100],
    "schedulePolicies": [
        {
            // A UTC timestamp represented by a cron expression.
            // eg. "0 5 * * *" means 5:00 AM in UTC time
            "scheduleExpression": "<cron expression>",
            "minNodes": number,
            "maxNodes": number
        }
    ]
}
```

### Runtime configuration (optional)
<a name="runtime-configuration-optional"></a>

The guidance comes pre-configured with Druid, which suits most use cases. You can customize the Druid configuration (runtime.properties) using the following settings:

```
"runtimeConfig": {
    // Druid process type depending on the node type. Valid values include coordinator, overlord, middleManager, historical, router, and broker.
    "<Druid process type>": {
        // The key name of Druid configuration item. eg. druid.server.http.numThreads
        "<druid configuration key>": "<druid configuration value>"
        ...
    },
}
```

Runtime configuration customization example:

```
"runtimeConfig": {
    "historical": {
        "druid.server.http.numThreads": 300
    },
    "middleManager": {
        "druid.server.http.numThreads": 200
    }
}
```

Druid EC2 configuration example

```
"druidEc2Config": {
    "master": {
        "minNodes": 2,
        "maxNodes": 2,
        "rootVolumeSize": 50,
        "instanceType": "m5.2xlarge"
    },
    "query": {
        "minNodes": 2,
        "maxNodes": 3,
        "rootVolumeSize": 50,
        "instanceType": "m5.2xlarge",
        "autoScalingPolicy": {
            "cpuUtilisationPercent": 60
        }
    },
    "data": {
        "minNodes": 3,
        "maxNodes": 3,
        "rootVolumeSize": 200,
        "segmentCacheVolumeSize": 500,
        "instanceType": "m5d.2xlarge"
    },
    "zookeeper": {
        "minNodes": 3,
        "maxNodes": 3,
        "rootVolumeSize": 50,
        "instanceType": "m6g.xlarge"
    }
}
```

Example: Druid deployment using EC2 for a medium profile

```
{
    "vpcCidr": "xx.xxx.0.0/16",
    "route53HostedZoneName": "<route53 hosted zone name>",
    "route53HostedZoneId": "<route 53 hosted zone ID>",
    "druidDomain": "<Domain where Druid is hosted>",
    "internetFacing": true,
    "druidClusterName": "ec2",
    "druidVersion": "30.0.0",
    "druidOperationPlatform": "ec2",
    "retainData": true,
    "druidExtensions": [
        "druid-hdfs-storage",
        "druid-kafka-indexing-service",
        "druid-datasketches",
        "druid-s3-extensions",
        "postgresql-metadata-storage",
        "druid-kinesis-indexing-service",
        "druid-avro-extensions",
        "druid-parquet-extensions",
        "druid-protobuf-extensions",
        "druid-cloudwatch",
        "druid-orc-extensions",
        "druid-basic-security",
        "druid-pac4j",
        "simple-client-sslcontext"
    ],
        "druidEc2Config": {
            "master": {
                "minNodes": 3,
                "maxNodes": 3,
                "rootVolumeSize": 50,
                "instanceType": "m6g.xlarge"
            },
            "query": {
                "minNodes": 3,
                "maxNodes": 3,
                "rootVolumeSize": 50,
                "instanceType": "m6g.xlarge"
            },
            "data": {
                "minNodes": 3,
                "maxNodes": 3,
                "rootVolumeSize": 200,
                "segmentCacheVolumeSize": 500,
                "instanceType": "m6g.2xlarge"
            },
            "zookeeper": {
                "minNodes": 3,
                "maxNodes": 3,
                "instanceType": "t4g.medium"
            }
        },
        "druidMetadataStoreConfig": {
            "metadataStoreType": "aurora",
            "metadataStoreConfig": {
                "rdsInstanceType": "t3.medium",
                "rdsInstanceCount": 3
            }
        }
}
```

You can find more configuration examples about EC2 configuration in the `source/quickstart` directory.

## Druid EKS configuration
<a name="druid-eks-configuration"></a>

The guidance will set up a new Amazon EKS cluster to serve as the hosting environment for Druid.

This section provides instructions on the configuration for the EKS cluster, including node group settings, involves the provisioning of four distinct node groups during deployment: master, query, data, and zookeeper.

### EKS cluster configuration
<a name="eks-cluster-configuration"></a>

```
"druidEksConfig": {
    // Kubernetes API server endpoint access. Valid values include PUBLIC, PRIVATE, and PUBLIC_AND_PRIVATE
    "endpointAccess": "PUBLIC",

    // The ARN of IAM role for the EKS cluster master
    "clusterMasterPrincipalArn": "<the ARN of IAM role for the cluster master>",

    // The underlying capacity provider for the EKS cluster. Valid values include ec2 and fargate.
    "capacityProviderType": "<ec2 or fargate>",

    // The capacity provider configuration. It differs based on the chosen capacity provider.
    "capacityProviderConfig": {
    }
}
```

### EC2 capacity provider configuration
<a name="ec2-capacity-provider-configuration"></a>

This is required if `capacityProviderType` is ec2.

```
// Node group name, valid values include master, query, data, and zookeeper. In case of service tiering, data_<tier> is also supported.

"<nodeGroupName>": {
    // Minimum number of EC2 instances in the node group
    "minNodes": number,

    // Optional. Maximum number of EC2 instances in the node group
    "maxNodes": number,

    // Optional. EBS volume size in GB for the root file system of EC2 instance.
    "rootVolumeSize": number,

    // EBS volume size in GB. Persistent volume for middleManager pods. Only required for middleManager pods.
    "taskCacheVolumeSize": number,

    // EBS volume size in GB. Persistent volume for historical pods. Only required for historical pods.
    "segmentCacheVolumeSize": number,

    // EC2 instance type for the node group.
    "instanceType": string
},
```

### Fargate capacity provider configuration
<a name="fargate-capacity-provider-configuration"></a>

This is required if `capacityProviderType` is Fargate.

```
// Druid process name, valid values include coordinator, overlord, middleManager, historical, router, broker, and zookeeper.

"<druidProcessName>": {
    // Minimum number of kubernetes pods
    "minNodes": number,

    // Optional. Maximum number of kubernetes pods
    "maxNodes": number,

    // Number of vCPUs to assign to each pod. eg. 2 means 2 vCPUs.
    "cpu": number,

    // The amount of memory to assign to each pod. eg. 4Gi means 4GB memory.
    "memory": string
}
```

 **Druid EKS configuration example (EC2 capacity provider)**

```
"druidEksConfig": {
    "endpointAccess": "PUBLIC",
    "clusterMasterPrincipalArn": "arn:aws:iam::<account id>:role/<role name>",
    "capacityProviderType": "ec2",
    "capacityProviderConfig": {
        "master": {
            "minNodes": 2,
            "maxNodes": 2,
            "rootVolumeSize": 50,
            "instanceType": "m5.2xlarge"
        },
        "query": {
            "minNodes": 2,
            "maxNodes": 2,
            "rootVolumeSize": 50,
            "instanceType": "m5.2xlarge"
        },
        "data": {
            "minNodes": 3,
            "maxNodes": 3,
            "rootVolumeSize": 50,
            "taskCacheVolumeSize": 300,
            "segmentCacheVolumeSize": 500,
            "instanceType": "m5.2xlarge"
        },
        "zookeeper": {
            "minNodes": 3,
            "maxNodes": 3,
            "rootVolumeSize": 50,
            "instanceType": "m5.large"
        }
    }
}
```

Example: Druid deployment using EKS for a medium profile

```
{
    "vpcCidr": "xx.xxx.0.0/16",
    "route53HostedZoneName": "<route53 hosted zone name>",
    "route53HostedZoneId": "<route 53 hosted zone ID>",
    "druidDomain": "<Domain where Druid is hosted>",
    "internetFacing": true,
    "druidClusterName": "eks",
    "retainData": false,
    "druidVersion": "30.0.0",
    "druidOperationPlatform": "eks",
    "druidExtensions": [
        "druid-hdfs-storage",
        "druid-kafka-indexing-service",
        "druid-datasketches",
        "druid-s3-extensions",
        "postgresql-metadata-storage",
        "druid-kinesis-indexing-service",
        "druid-avro-extensions",
        "druid-parquet-extensions",
        "druid-protobuf-extensions",
        "druid-cloudwatch",
        "druid-orc-extensions",
        "druid-basic-security",
        "druid-pac4j"
    ],
    "druidEksConfig": {
        "endpointAccess": "PUBLIC",
        "clusterMasterPrincipalArn": "arn:aws:iam::<account id>:role/<role name>",
        "capacityProviderType": "ec2",
        "capacityProviderConfig": {

"master": {
                    "minNodes": 3,
                    "maxNodes": 3,
                    "instanceType": "m5.xlarge"
                },
                "query": {
                    "minNodes": 3,
                    "maxNodes": 3,
                    "instanceType": "m5.xlarge"
                },
                "data": {
                    "minNodes": 3,
                    "maxNodes": 3,
                    "taskCacheVolumeSize": 300,
                    "segmentCacheVolumeSize": 500,
                    "instanceType": "m5.large"
                },
                "zookeeper": {
                    "minNodes": 3,
                    "maxNodes": 3,
                    "rootVolumeSize": 50,
                    "instanceType": "t3.medium"
                }
            }
        },
        "druidMetadataStoreConfig": {
            "metadataStoreType": "aurora",
            "metadataStoreConfig": {
                "rdsInstanceType": "t3.medium",
                "rdsInstanceCount": 3
            }
    }
}
```

Example: Druid configuration using EKS and Fargate, for a medium profile

```
{
    "vpcCidr": "xx.xxx.0.0/16",
    "route53HostedZoneName": "<route53 hosted zone name>",
    "route53HostedZoneId": "<route 53 hosted zone ID>",
    "druidDomain": "<Domain where Druid is hosted>",
    "internetFacing": true,
    "druidVersion": "27.0.0",
    "druidClusterName": "fargate",
    "druidOperationPlatform": "eks",
    "retainData": false,
    "druidExtensions": [
        "druid-hdfs-storage",
        "druid-kafka-indexing-service",
        "druid-datasketches",
        "druid-s3-extensions",
        "postgresql-metadata-storage",
        "druid-kinesis-indexing-service",
        "druid-avro-extensions",
        "druid-parquet-extensions",
        "druid-protobuf-extensions",
        "druid-cloudwatch",
        "druid-orc-extensions",
        "druid-basic-security",
        "druid-pac4j"
    ],

"druidEksConfig": {
            "endpointAccess": "PUBLIC",
            "clusterMasterPrincipalArn": "arn:aws:iam::<account id>:role/<role name>",
            "capacityProviderType": "fargate",
            "capacityProviderConfig": {
                "historical": {
                    "minNodes": 3,
                    "maxNodes": 3,
                    "cpu": 4,
                    "memory": "16Gi"
                },
                "middleManager": {
                    "minNodes": 3,
                    "maxNodes": 3,
                    "cpu": 4,
                    "memory": "16Gi"
                },
                "broker": {
                    "minNodes": 3,
                    "maxNodes": 3,
                    "cpu": 2,
                    "memory": "8Gi"
                },
                "router": {
                    "minNodes": 3,
                    "maxNodes": 3,
                    "cpu": 2,
                    "memory": "8Gi"
                },
                "coordinator": {
                    "minNodes": 1,
                    "maxNodes": 1,
                    "cpu": 2,
                    "memory": "8Gi"
                },
                "overlord": {
                    "minNodes": 1,
                    "maxNodes": 1,
                    "cpu": 2,
                    "memory": "8Gi"
                },
                "zookeeper": {
                    "minNodes": 3,
                    "maxNodes": 3,
                    "cpu": 2,
                    "memory": "4Gi"
                }
            }
        },
        "druidMetadataStoreConfig": {
            "metadataStoreType": "aurora",
            "metadataStoreConfig": {
                "rdsInstanceType": "t3.medium",
                "rdsInstanceCount": 3
            }
    }
}
```

You can find more examples about EKS configuration in the `source/quickstart` directory.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
