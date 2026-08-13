---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/encryption-rest.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Data encryption at rest for Amazon WorkSpaces Thin Client
<a name="encryption-rest"></a>

Amazon WorkSpaces Thin Client provides encryption by default to protect sensitive customer data at rest by using AWS owned encryption keys.
+ **AWS owned keys ** — Amazon WorkSpaces Thin Client uses these keys by default to automatically encrypt personally identifiable data. You cannot view, manage, or use AWS owned keys or audit their use. However, you don't have to take any action or change any programs to protect the keys that encrypt your data. For more information, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the *AWS Key Management Service Developer Guide*.

Encryption of data at rest by default helps reduce the operational overhead and complexity involved in protecting sensitive data. At the same time, it enables you to build secure applications that meet strict encryption compliance and regulatory requirements.

While you can't disable this layer of encryption or select an alternate encryption type, you can add a second layer of encryption over the existing AWS owned encryption keys by choosing a customer managed key when you create your Thin Client Environment:
+ **Customer managed keys** — Amazon WorkSpaces Thin Client supports the use of a symmetric customer managed key that you create, own, and manage to add a second layer of encryption on the existing AWS owned encryption. Because you have full control of this layer of encryption, you can perform such tasks as the following:
  + Establishing and maintaining key policies
  + Establishing and maintaining IAM policies
  + Enabling and disabling key policies
  + Rotating key cryptographic material
  + Adding tags
  + Creating key aliases
  + Scheduling keys for deletion

For more information, see [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the AWS Key Management Service Developer Guide.

The following table summarizes how Amazon WorkSpaces Thin Client encrypts personally identifiable data.

| Data type | AWS owned key encryption | Customer managed key encryption (Optional) |
| --- | --- | --- |
| Environment name<br />WorkSpaces Thin Client [Environment](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Environment.html) name | Enabled | Enabled |
| Device name<br />WorkSpaces Thin Client [Device](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Device.html) name | Enabled | Enabled |
|  User activity<br />WorkSpaces Thin Client [User](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Device.html) activity | Enabled | Enabled |
| Device settings<br />WorkSpaces Thin Client [Device](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Device.html) settings | Enabled | Enabled |
| Device creation tags<br />WorkSpaces Thin Client [Environment](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/device-user-activity.html) device creation tags | Enabled | Enabled |

**Note**
Amazon WorkSpaces Thin Client automatically enables encryption at rest by using AWS owned keys to protect personally identifiable data at no charge.
However, AWS KMS charges apply for using a customer managed key. For more information about pricing, see the [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).

## How Amazon WorkSpaces Thin Client uses AWS KMS
<a name="using-aws-kms"></a>

Amazon WorkSpaces Thin Client requires a key policy for you to use your customer managed key.

Amazon WorkSpaces Thin Client requires the key policy to use your customer managed key for the following internal operations:
+ Send [`GenerateDataKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) requests to AWS KMS to encrypt the data.
+ Send [`Decrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) requests to AWS KMS to decrypt the encrypted data.

You can remove the service's access to the customer managed key at any time. If you do, Amazon WorkSpaces Thin Client won't be able to access any of the data encrypted by the customer managed key, which affects operations that are dependent on that data. For example, if you attempt to [get environment details](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_GetEnvironment.html) that WorkSpaces Thin Client can't access, then the operation returns an `AccessDeniedException` error. Additionally, the WorkSpaces Thin Client device will not be able to use a WorkSpaces Thin Client Environment.

## Create a customer managed key
<a name="create-customer-managed-key"></a>

You can create a symmetric customer managed key by using the AWS Management Console or the AWS KMS API operations.

### To create a symmetric customer managed key
<a name="create-symmetric-customer-managed-key"></a>

Follow the steps for [Creating symmetric customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

### Key policy
<a name="key-policy"></a>

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see [Managing access to customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html#managing-access) in the [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

To use your customer managed key with your Amazon WorkSpaces Thin Client resources, the following API operations must be permitted in the key policy:
+ [`kms:DescribeKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) — Provides the customer managed key details so Amazon WorkSpaces Thin Client can validate the key.
+ [`kms:GenerateDataKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) — Allows using the customer managed key to encrypt the data.
+ [`kms:Decrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) — Allows using the customer managed key to decrypt the data.

The following are policy statement examples you can add for Amazon WorkSpaces Thin Client:

```
{
    "Statement":
    [
        {
            "Sid": "Allow access to principals authorized to use Amazon WorkSpaces Thin Client",
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": [
                "kms:DescribeKey",
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "thinclient.region.amazonaws.com",
                    "kms:CallerAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "Allow Amazon WorkSpaces Thin Client service to encrypt and decrypt data",
            "Effect": "Allow",
            "Principal": {"Service": "thinclient.amazonaws.com"},
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "aws:SourceArn":
                         "arn:aws:thinclient:region:111122223333:*",
                    "kms:EncryptionContext:aws:thinclient:arn":
                         "arn:aws:thinclient:region:111122223333:*"
                }
            }
        },
        {
            "Sid": "Allow access for key administrators",
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:iam::111122223333:root"},
            "Action": ["kms:*"],
            "Resource": "arn:aws:kms:region:111122223333:key/key_ID"
        },
        {
            "Sid": "Allow read-only access to key metadata to the account",
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:iam::111122223333:root"},
            "Action": [
                "kms:Describe*",
                "kms:Get*",
                "kms:List*"
            ],
            "Resource": "*"
        }
    ]
}
```

For more information about [specifying permissions in a policy](https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html#overview-policy-elements), see the [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

For more information about [ troubleshooting key access](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html#example-no-iam), see the [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

## Specifying a customer managed key for WorkSpaces Thin Client
<a name="specifying-customer-managed-key"></a>

You can specify a customer managed key as a second layer encryption for the following resources:
+ WorkSpaces Thin Client [Environment](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Environment.html)

When you create an Environment, you can specify the data key by providing a `kmsKeyArn`, which Amazon WorkSpaces Thin Client uses to encrypt the identifiable personal data.
+ `kmsKeyArn` — A key identifier for an AWS KMS customer managed key. Provide a key ARN.

When a new WorkSpaces Thin Client device is added to the WorkSpaces Thin Client [Environment](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Environment.html) encrypted with a customer managed key, the WorkSpaces Thin Client Device inherits the customer managed key setting from the WorkSpaces Thin Client Environment.

An [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) is an optional set of key-value pairs that contains additional contextual information about the data.

AWS KMS uses the encryption context as [additional authenticated data](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) to support authenticated encryption. When you include an encryption context in a request to encrypt data, AWS KMS binds the encryption context to the encrypted data. To decrypt data, include the same encryption context in the request.

### Amazon WorkSpaces Thin Client encryption context
<a name="thin-client-encryption-context"></a>

Amazon WorkSpaces Thin Client uses the same encryption context in all AWS KMS cryptographic operations, where the key is `aws:thinclient:arn` and the value is the Amazon Resource Name (ARN).

The following is the Environment encryption context:

```
"encryptionContext": {
    "aws:thinclient:arn": "arn:aws:thinclient:region:111122223333:environment/environment_ID"
}
```

The following is the Device encryption context:

```
"encryptionContext": {
    "aws:thinclient:arn": "arn:aws:thinclient:region:111122223333:device/device_ID"
}
```

### Using encryption context for monitoring
<a name="using-encryption-context-monitoring"></a>

When you use a symmetric customer managed key to encrypt your WorkSpaces Thin Client Environment and Device data, you can also use the encryption context in audit records and logs to identify how the customer managed key is being used. The encryption context also appears in [logs generated by AWS CloudTrail or Amazon CloudWatch Logs](https://docs.aws.amazon.com/location/latest/developerguide/encryption-at-rest.html#example-custom-encryption).

### Using encryption context to control access to your customer managed key
<a name="using-encryption-context-control-access"></a>

You can use the encryption context in key policies and IAM policies as conditions to control access to your symmetric customer managed key.

The following are example key policy statements to grant access to a customer managed key for a specific encryption context. The condition in this policy statement requires that the `kms:Decrypt` call has an encryption context constraint that specifies the encryption context.

```
{
    "Sid": "Enable Decrypt to access Thin Client Environment",
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::111122223333:role/ExampleReadOnlyRole"},
    "Action": "kms:Decrypt",
    "Resource": "*",
    "Condition": {
        "StringEquals": {"kms:EncryptionContext:aws:thinclient:arn": "arn:aws:thinclient:region:111122223333:environment/environment_ID"}
    }
}
```

## Monitoring your encryption keys for Amazon WorkSpaces Thin Client
<a name="monitoring-encryption-keys-for-thin-client"></a>

When you use an AWS KMS customer managed key with your Amazon WorkSpaces Thin Client resources, you can use AWS CloudTrail or Amazon CloudWatch Logs to track requests that Amazon WorkSpaces Thin Client sends to AWS KMS.

The following examples are AWS CloudTrail events for `DescribeKey`, `GenerateDataKey`, `Decrypt`, to monitor KMS operations called by Amazon WorkSpaces Thin Client to access data encrypted by your customer managed key:

In the following examples, you can see `encryptionContext` for the WorkSpaces Thin Client Environment. Similar CloudTrail events are recorded for the WorkSpaces Thin Client Device.

------
#### [ DescribeKey ]

Amazon WorkSpaces Thin Client uses the `DescribeKey` operation to verify the AWS KMS customer managed key.

The following example event records the `DescribeKey` operation:

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2024-04-08T13:43:33Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "thinclient.amazonaws.com"
    },
    "eventTime": "2024-04-08T13:44:22Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "DescribeKey",
    "awsRegion": "eu-west-1",
    "sourceIPAddress": "thinclient.amazonaws.com",
    "userAgent": "thinclient.amazonaws.com",
    "requestParameters": {"keyId": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"},
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

------
#### [ GenerateDataKey ]

Amazon WorkSpaces Thin Client uses the `GenerateDataKey` operation to encrypt data.

The following example event records the `GenerateDataKey` operation:

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2024-04-08T12:21:03Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "thinclient.amazonaws.com"
    },
    "eventTime": "2024-04-08T13:03:56Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "eu-west-1",
    "sourceIPAddress": "thinclient.amazonaws.com",
    "userAgent": "thinclient.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "encryptionContext": {
            "aws-crypto-public-key": "ABC123def4567890abc12345678/90dE/F123abcDEF+4567890abc123D+ef1==",
            "aws:thinclient:arn": "arn:aws:thinclient:eu-west-1:111122223333:environment/abcSAMPLE"
        },
        "numberOfBytes": 32
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "1234abcd-12ab-34cd-56ef-123456SAMPLE",
    "vpcEndpointId": "vpce-1234abcd567SAMPLE",
    "vpcEndpointAccountId": "thinclient.amazonaws.com",
    "eventCategory": "Management"
}
```

------
#### [ GenerateDataKey (by service) ]

When Amazon WorkSpaces Thin Client uses the `GenerateDataKey` saves Device information, the `GenerateDataKey` operation is used to encrypt the data.

The `GenerateDataKey` operation is allowed in KMS key policy statement with Sid "Allow Amazon WorkSpaces Thin Client service to encrypt and decrypt data".

The following example event records the GenerateDataKey operation:

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "thinclient.amazonaws.com"
    },
    "eventTime": "2024-04-08T13:03:56Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "eu-west-1",
    "sourceIPAddress": "thinclient.amazonaws.com",
    "userAgent": "thinclient.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "encryptionContext": {
            "aws-crypto-public-key": "ABC123def4567890abc12345678/90dE/F123abcDEF+4567890abc123D+ef1==",
            "aws:thinclient:arn": "arn:aws:thinclient:eu-west-1:111122223333:environment/abcSAMPLE"
        },
        "numberOfBytes": 32
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "1234abcd-12ab-34cd-56ef-123456SAMPLE",
    "vpcEndpointId": "vpce-1234abcd567SAMPLE",
    "vpcEndpointAccountId": "thinclient.amazonaws.com",
    "eventCategory": "Management"
}
```

------
#### [ Decrypt ]

Amazon WorkSpaces Thin Client uses the `Decrypt` operation to decrypt data.

The following example event records the `Decrypt` operation:

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2024-04-08T13:43:33Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "thinclient.amazonaws.com"
    },
    "eventTime": "2024-04-08T13:44:25Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "eu-west-1",
    "sourceIPAddress": "thinclient.amazonaws.com",
    "userAgent": "thinclient.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "encryptionContext": {
            "aws-crypto-public-key": "ABC123def4567890abc12345678/90dE/F123abcDEF+4567890abc123D+ef1==",
            "aws:thinclient:arn": "arn:aws:thinclient:eu-west-1:111122223333:environment/abcSAMPLE"
         },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "1234abcd-12ab-34cd-56ef-123456SAMPLE",
    "vpcEndpointId": "vpce-1234abcd567SAMPLE",
    "vpcEndpointAccountId": "thinclient.amazonaws.com",
    "eventCategory": "Management"
}
```

------
#### [ Decrypt (by service) ]

When WorkSpaces Thin Client Device accesses Environment or Device information, the `Decrypt` operation is used to decrypt the data. The `Decrypt` operation is allowed in KMS key policy statement with Sid "Allow Amazon WorkSpaces Thin Client service to encrypt and decrypt data".

The following example event records the `Decrypt` operation, authorized through a `Grant`:

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "thinclient.amazonaws.com"
    },
    "eventTime": "2024-04-08T13:44:25Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "eu-west-1",
    "sourceIPAddress": "thinclient.amazonaws.com",
    "userAgent": "thinclient.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "encryptionContext": {
            "aws-crypto-public-key": "ABC123def4567890abc12345678/90dE/F123abcDEF+4567890abc123D+ef1==",
            "aws:thinclient:arn": "arn:aws:thinclient:eu-west-1:111122223333:environment/abcSAMPLE"
         },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "1234abcd-12ab-34cd-56ef-123456SAMPLE",
    "vpcEndpointId": "vpce-1234abcd567SAMPLE",
    "vpcEndpointAccountId": "thinclient.amazonaws.com",
    "eventCategory": "Management"
}
```

------

## Learn More
<a name="learn-more"></a>

The following resources provide more information about data encryption at rest:
+ For more information about [AWS Key Management Service basic concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), see the [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).
+ For more information about [Security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html), see the [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).
