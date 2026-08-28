---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/using-kms-keys-for-encryption.html
---

# Enabling object level server-side encryption with AWS KMS key
<a name="using-kms-keys-for-encryption"></a>

Media Capture Pipeline and Media Concatenation Pipeline can use AWS Key Management Service (AWS KMS) customer managed keys to enable server-side encryption (SSE) for individual objects in an Amazon S3 bucket. To configure this, you must use the [CreateMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html) API call. The Media Concatenation Pipeline will use the server-side encryption parameters from the associated Media Capture Pipeline.

To enable SSE for individual objects (object-level SSE) using your AWS KMS customer managed key, you must provide the `SseAwsKeyManagementParams` structure and the `SinkIamRoleArn` during the [CreateMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html) API call:

1. Use the `AwsKmsKeyId` parameter in the `SseAwsKeyManagementParams` structure to specify the AWS KMS key. You can specify the key ID using the key's ID, ARN, or alias.

1. Use the `SinkIamRoleArn` parameter to specify the IAM role to access the AWS KMS key and the sink Amazon S3 bucket.

1. Optionally, you can use the `AwsKmsEncryptionContext` parameter in the `SseAwsKeyManagementParams` structure to specify the encryption context to be used along with AWS KMS key artifacts for enhanced security.

**Note**
The `AwsKmsKeyId` and `SinkIamRoleArn` parameters are co-dependent. When both are present and valid, the Media Capture Pipeline will assume the role and place each artifact into the specified Amazon S3 bucket-sink with the specified AWS KMS key. The [CreateMediaConcatenationPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaConcatenationPipeline.html) API call doesn’t have new parameters but will use the aforementioned parameters if specified. If you plan on concatenating artifacts, ensure your resources configuration is set as described in the following [Configuration](#using-kms-keys-for-encryption-config) section, and are persistent over time.

## Configuration
<a name="using-kms-keys-for-encryption-config"></a>

The `SinkIamRoleArn` must have the same permissions and access as the principal to put artifacts into the Amazon S3 bucket. For more information about the expected default permissions in the Amazon S3 bucket, see [Creating an Amazon S3 bucket for Amazon Chime SDK Media Capture Pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-s3-bucket.html). To enable SSE for individual objects, your Amazon S3 bucket must allow the IAM role specified using the `SinkIamRoleArn` to perform the same set of actions you would expect from the calling IAM identity. You can achieve this by adding the following principal to your Amazon S3 bucket permission policy.

```
...
"Principal": {
    ...
    "AWS": "arn:aws:iam::{{<YOUR_ACCOUNT_ID>}};:role/{{<SINK_IAM_ROLE_NAME>}}"
    ...
},
...
```

The `AwsKmsKeyId` should point to a key that permits the `SinkIamRoleArn` to perform `GenerateDataKey`. If Media Concatenation Pipeline is going to be used, the AWS KMS key should also permit the use of the `Decrypt` action. See the following example.

**Note**
The resource is set to use wildcard `“*”`, which in this context of a AWS KMS key policy signifies “itself”.

```
{
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::{{<YOUR_ACCOUNT_ID>}}:role/{{<YOUR_CUSTOMER_ROLE_ID>}}"
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "*"
}
```

The `SinkIamRoleArn` role must have a trust relationship allowing the service to assume it. See the following example.

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "mediapipelines.chime.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "{{<YOUR_ACCOUNT_ID>}}"
        },
        "ArnLike": {
            "aws:SourceArn": "arn:aws:chime:*:{{<YOUR_ACCOUNT_ID>}}:*"
        }
    }
}
```

The `SinkIamRoleArn` should have the following minimum permissions policy for Media Capture Pipeline. See the following example.

```
{
    "Effect": "Allow",
    "Action": "kms:GenerateDataKey",
    "Resource": "arn:aws:kms:{{<KMS_KEY_REGION>}}:{{<KMS_KEY_ACCOUNT_ID>}}:key/{{<MS_KEY_ID>}}",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "{{<YOUR_ACCOUNT_ID>}}"
        },
        "ArnLike": {
            "aws:SourceArn": "arn:aws:chime:*:{{<YOUR_ACCOUNT_ID>}}:*"
        }
    }
},
{
    "Effect": "Allow",
    "Action": ["s3:PutObject", "s3:PutObjectAcl"],
    "Resource": "arn:aws:s3:::{{<YOUR_DEDICATED_KMS_BUCKET_ID>}}/*",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "{{<YOUR_ACCOUNT_ID>}}"
        },
        "ArnLike": {
            "aws:SourceArn": "arn:aws:chime:*:{{<YOUR_ACCOUNT_ID>}}:*"
        }
    }
}
```

Additionally, the caller must be allowed to pass `SinkIamRoleArn` to the service. In cases when the caller doesn’t have such permission it should be added explicitly. See the following example.

```
{
    "Effect": "Allow",
    "Action": "iam:PassRole",
    "Resource": "{{<SINK_IAM_ROLE_ARN>}}",
    "Condition": {
        "ArnLike": {
            "iam:AssociatedResourceArn": "arn:aws:chime:*:{{<YOUR_ACCOUNT_ID>}}:media-pipeline/*"
        },
        "StringEquals": {
            "iam:PassedToService": "mediapipelines.chime.amazonaws.com"
        }
    }
}
```

## Media concatenation implementation
<a name="media-concatenation-implementatoin"></a>

If you plan on using Media Concatenation Pipeline after Media Capture, see [Building an Amazon Chime SDK media concatenation pipeline](create-concat-pipe-steps.md) to understand the required permissions. To make the pipeline work with the AWS KMS key for object-level SSE, the `SinkIamRoleArn` permissions (allowed actions) must be expanded for the AWS KMS key and Amazon S3 bucket. See the following example.

```
...
{
    ...
    {
        ...
        "Action": ["kms:GenerateDataKey","kms:Decrypt"]
        "Resource": "arn:aws:kms:{{<KMS_KEY_REGION>}}:{{<KMS_KEY_ACCOUNT_ID>}}:key/{{<KMS_KEY_ID>}}",
        ...
    }
    ...
    {
        "Action": [ "s3:PutObject", "s3:PutObjectAcl", "s3:GetObject", "s3:ListBucket"],
        "Resource": "arn:aws:s3:::{{<YOUR_DEDICATED_KMS_BUCKET_ID>}}/*",
    }
    ...
}
...
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
