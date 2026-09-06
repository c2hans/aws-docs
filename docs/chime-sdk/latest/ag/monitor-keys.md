---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/monitor-keys.html
---

# Monitoring encryption keys
<a name="monitor-keys"></a>

Amazon Chime SDK Voice Connectors send requests to AWS KMS, and you can track those requests in CloudTrail or CloudWatch logs.

------
#### [ CreateGrant ]

When you use a customer managed key to create a voice profile domain resource, the associated Voice Connector sends a `CreateGrant` request on your behalf to access the KMS key in your AWS account. The grant that the Voice Connector creates is specific to the resource associated with the customer managed key. The Voice Connector also uses the `RetireGrant` operation to remove a grant when you delete a resource.

The following example records a `CreateGrant` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "{{AROAIGDTESTANDEXAMPLE}}:{{Sampleuser01}}",
        "arn": "arn:aws:sts::{{111122223333}}:assumed-role/Admin/{{Sampleuser01}}",
        "accountId": "{{111122223333}}",
        "accessKeyId": "{{AKIAIOSFODNN7EXAMPLE3}}",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "{{AROAIGDTESTANDEXAMPLE}}:{{Sampleuser01}}",
                "arn": "arn:aws:sts::{{111122223333}}:assumed-role/Admin/{{Sampleuser01}}",
                "accountId": "{{111122223333}}",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "{{2021-04-22T17:02:00Z}}"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "{{2021-04-22T17:07:02Z}}",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "{{ExampleDesktop}}/1.0 (V1; OS)",
    "requestParameters": {
       "constraints": {
            "encryptionContextSubset": {
                "aws:chime:voice-profile-domain:arn": "arn:aws:chime:us-west-2:{{111122223333}}:voice-profile-domain/sample-domain-id"
            }
        },
        "retiringPrincipal": "chimevoiceconnector.region.amazonaws.com",
        "operations": [
            "GenerateDataKey",
            "Decrypt",
            "DescribeKey",
            "RetireGrant"
        ],
        "keyId": "arn:aws:kms:us-west-2:{{111122223333}}:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "granteePrincipal": "chimevoiceconnector.region.amazonaws.com",
        "retiringPrincipal": "chimevoiceconnector.region.amazonaws.com"
    },
    "responseElements": {
        "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE"
    },
    "requestID": "{{ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE}}",
    "eventID": "{{ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE}}",
    "readOnly": false,
    "resources": [
        {
            "accountId": "{{111122223333}}",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:{{111122223333}}:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "{{111122223333}}"
}
```

------
#### [ GenerateDataKey ]

When you create a voice profile domain and assign a customer managed key to the domain, the associated Voice Connector creates a unique data key to encrypt each speaker’s enrollment audio. The Voice Connector sends a `GenerateDataKey` request to AWS KMS that specifies the key for the resource.

The following example records a `GenerateDataKey` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "{{2021-04-22T17:07:02Z}}",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "{{ExampleDesktop}}/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "aws:chime:voice-profile-domain:arn": "arn:aws:chime:us-west-2:{{111122223333}}:{{voice-profile-domain}}/{{sample-domain-id}}"
        },
        "keySpec": "AES_256",
        "keyId": "arn:aws:kms:us-west-2:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-123456SAMPLE}}"
    },
    "responseElements": null,
    "requestID": "{{ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE}}",
    "eventID": "{{ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE}}",
    "readOnly": true,
    "resources": [
        {
            "accountId": "{{111122223333}}",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-123456SAMPLE}}"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "{{111122223333}}",
    "sharedEventID": "{{57f5dbee-16da-413e-979f-2c4c6663475e}}"
}
```

------
#### [ Decrypt ]

When a voice profile in a voice profile domain needs to have its voice print upgraded because of a newer voice recognition model, the associated Voice Connector calls the `Decrypt` operation to use the stored encrypted data key to access the encrypted data.

The following example records a `Decrypt` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "{{2021-10-12T23:59:34Z}}",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "{{ExampleDesktop}}/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "keyId": "arn:aws:kms:us-west-2:{{111122223333}}:key/44444444-3333-2222-1111-EXAMPLE11111",
            "encryptionContext": {
                "aws:chime:voice-profile-domain:arn": "arn:aws:chime:us-west-2:{{111122223333}}:{{voice-profile-domain}}/{{sample-domain-id}}"
            },
            "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
        },
        "responseElements": null,
        "requestID": "ed0fe4ab-305b-4388-8adf-7e8e3a4e80fe",
        "eventID": "31d0d7c6-ce5b-4caf-901f-025bf71241f6",
        "readOnly": true,
        "resources": [{
            "accountId": "{{111122223333}}",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:{{111122223333}}:key/{{00000000-1111-2222-3333-9999999999999}}"
        }],
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "{{111122223333}}",
        "sharedEventID": "{{35d58aa1-26b2-427a-908f-025bf71241f6}}",
        "eventCategory": "Management"
    }
```

------
#### [ DescribeKey ]

Voice Connectors use the `DescribeKey` operation to verify that the key associated with a voice profile domain exists in the account and Region.

The following example records a `DescribeKey` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "{{AROAIGDTESTANDEXAMPLE}}:{{Sampleuser01}}",
        "arn": "arn:aws:sts::{{111122223333}}:assumed-role/Admin/{{Sampleuser01}}",
        "accountId": "{{111122223333}}",
        "accessKeyId": "{{AKIAIOSFODNN7EXAMPLE3}}",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "{{AROAIGDTESTANDEXAMPLE}}:{{Sampleuser01}}",
                "arn": "arn:aws:sts::{{111122223333}}:assumed-role/Admin/{{Sampleuser01}}",
                "accountId": "{{111122223333}}",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "{{2021-04-22T17:02:00Z}}"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "{{2021-04-22T17:07:02Z}}",
    "eventSource": "kms.amazonaws.com",
    "eventName": "DescribeKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "{{ExampleDesktop}}/1.0 (V1; OS)",
    "requestParameters": {
        "keyId": "{{00dd0db0-0000-0000-ac00-b0c000SAMPLE}}"
    },
    "responseElements": null,
    "requestID": "{{ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE}}",
    "eventID": "{{ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE}}",
    "readOnly": true,
    "resources": [
        {
            "accountId": "{{111122223333}}",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-123456SAMPLE}}"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "{{111122223333}}"
}
```

------
