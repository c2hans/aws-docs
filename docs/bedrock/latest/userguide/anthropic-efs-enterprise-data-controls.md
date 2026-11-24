---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/anthropic-efs-enterprise-data-controls.html
---

# Enterprise Frontier Safeguards and Enterprise Data Controls on Amazon Bedrock (public preview)

This topic shows you how to set up Enterprise Frontier Safeguards (EFS) and Enterprise Data Controls (EDC) on Amazon Bedrock.

**Note**
EFS and EDC on Amazon Bedrock are in public preview. Their APIs, IAM action names, and endpoints can change before general availability. Review [Preview availability and limitations](#efs-edc-limitations) before you rely on it.

EFS and EDC are trusted access programs on Amazon Bedrock, available through the trusted access programs API (TAP API). With the TAP API, you can check your account's eligibility and enrollment status for programs. To learn more, see [Trusted access programs in Amazon Bedrock](trusted-access-programs.md).

Before you start:
+ Use a test account and send only test traffic. Don't send regulated data, such as PII or PHI.
+ Joining the preview turns zero data retention (ZDR) off for the accounts or projects you add, so their content is retained: in your own Amazon S3 bucket with EFS, or in Amazon-managed storage with EDC. Your other accounts keep ZDR.

## How it works
<a name="efs-edc-how-it-works"></a>

EFS and EDC apply to the covered models: Claude Fable, Claude Mythos, and Claude Opus 5.5 and Claude Sonnet 5.5 used through the Cyber Verification Program (CVP). See [Preview availability and limitations](#efs-edc-limitations).

Its parts are:

Your AWS KMS key and bucket
The bucket holds the retained content, and the key encrypts it.

Storage configuration
Tells Amazon Bedrock where retained content goes, either your own S3 bucket and KMS key or Amazon-managed storage. Amazon-managed storage requires EDC eligibility and isn't available to EFS-only accounts. You set it for each Region, for your organization, an account, or a project. The most specific one applies: project, then account, then organization.

Service principal
`bedrock.amazonaws.com`, the identity Amazon Bedrock uses to reach your key and bucket.

Data retention mode
An account setting that says whether Amazon Bedrock may retain content for safety review. EFS and EDC accounts use `aws_review`.

Case
A file that EFS writes to your bucket when automated review finds activity that appears to deliberately violate AWS's or Anthropic's terms of service or use policies. You review it and respond.

When you call a covered model:

1. Amazon Bedrock runs the request through Amazon Bedrock Runtime (`bedrock-runtime`). Inference is unchanged, and your code doesn't change.

1. Amazon Bedrock stores inputs and outputs. It writes the prompt and response to your bucket, encrypted with your key (EFS), or to Amazon-managed storage (EDC), usually within minutes. If your key or bucket has a failure, Amazon Bedrock can retry for up to 72 hours. For EFS, Amazon Bedrock stores retained content in the bucket configured for the Region you call (the source Region), even when cross-Region inference processes the request in another Region. Your bucket holds two kinds of records: readable copies of inputs and outputs in `transcripts/`, and encrypted records for safety review in `slab/` (with `slab-manifest/`, `media/`, and `verify/`), which you can't read.

1. Automated review runs in US East (N. Virginia) (`us-east-1`) and Europe (Ireland) (`eu-west-1`). In the public preview, it covers requests made through the US and EU geographic cross-Region inference profiles and the global cross-Region inference profile for covered models.

1. You review anything flagged. EFS opens a case in your bucket. See [Handle cases](#efs-edc-cases).

1. The content is deleted after 30 days in Amazon-managed storage, or under your bucket's lifecycle rules.

For more information about automated review and human review, see [Automated review and human review in Amazon Bedrock](automated-review-human-review.md).

## Choose where your data is stored
<a name="efs-edc-storage-choice"></a>

|  | Your own bucket | Amazon-managed storage |
| --- | --- | --- |
| Where it's stored | An S3 bucket in your account | A bucket that AWS runs |
| Who can access it | The Amazon Bedrock service principal, plus the people and services you allow in your policies | AWS |
| Encryption | Your KMS key | Managed by AWS. Your key isn't used. |
| What you see in AWS CloudTrail | Key use, and bucket access when CloudTrail data events are on | Nothing in your account |
| Cases | Arrive in your bucket for you to review and answer | You review cases. |
| What you manage | The key, the bucket, and their policies | Nothing, apart from reviewing cases |

## Charges
<a name="efs-edc-charges"></a>

AWS and Anthropic don't charge for EFS or EDC, and they don't change model pricing, behavior, or rate limits. You pay standard Amazon S3 and AWS KMS charges for your bucket and key. If your bucket is in a Region other than where automated review runs, you also pay S3 data transfer when review reads your content. For Amazon Bedrock pricing, see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/).

### Next steps
<a name="efs-edc-next-steps"></a>

1. [Get access to EFS and EDC](#efs-edc-get-access).

1. [Set up EFS and EDC](#efs-edc-setup), then call a covered model.

1. Set up your team to handle cases. See [Handle cases](#efs-edc-cases).

## Get access to EFS and EDC
<a name="efs-edc-get-access"></a>

To enroll in the EFS and EDC public preview, work with your AWS account representatives to submit a request. The preview is for customers already enrolled in EFS ZDR.

**To join the preview, request access for the organization, accounts, or projects you want to test with**

1. Provide your AWS account representatives the scope you want (organization, account, or project) and the identifiers for that scope:
   + Organization or account: the 12-digit AWS account ID
   + Project (if applicable): the Amazon Bedrock runtime project ARN

1. AWS turns on data retention for the accounts or projects you listed, and confirms through your account representatives. For EFS-only accounts, Amazon Bedrock refuses calls to covered models until you save a storage configuration with your own bucket, so finish [Set up EFS and EDC](#efs-edc-setup) before you call a covered model.

1. Go on to [Set up EFS and EDC](#efs-edc-setup).

**Important**
Eligible EFS customers can use current Claude Fable models and existing CVP models with ZDR for internal use through at least June 30, 2027.

### Leave the preview
<a name="efs-edc-leave-preview"></a>

To move accounts or projects back to ZDR, ask your AWS account representatives. AWS turns ZDR back on for you.

## Set up EFS and EDC
<a name="efs-edc-setup"></a>

This walkthrough sets up EFS for one account: it creates your key and bucket, lets Amazon Bedrock access them, saves your storage configuration, and sets your retention mode. Do the steps in order, in each Region where you call the covered models. For an organization or project configuration, the policies and permissions differ: see [Organization and project configurations](#efs-edc-org-project). If your account is eligible for EDC and you want Amazon-managed storage instead, skip Steps 1 and 2, and in Step 4 save `{"storageDestination": "amazon_managed"}`.

### Values you provide
<a name="efs-edc-values"></a>

In the policies and commands in this topic, replace each value in angle brackets with your own.

`{{<account-id>}}`
Your 12-digit AWS account ID

`{{<region>}}`
The Region where you call the covered models, such as `us-east-1`

`{{<profile-name>}}`
Your AWS CLI profile

`{{<bucket-name>}}`
The name of your S3 bucket

`{{<key-arn>}}`
The full ARN of your KMS key, not an alias

`{{<project-arn>}}`
Your Amazon Bedrock project ARN (project configurations only)

`{{<topic-arn>}}`
Your Amazon SNS topic ARN (case alerts only)

| What | What it's for |
| --- | --- |
| KMS key | Encrypts the content Amazon Bedrock keeps in your bucket |
| S3 bucket | Stores the content in your account |
| Caller policy | Lets the role you work as save the storage configuration |
| Storage configuration | Tells Amazon Bedrock to use your key and bucket |

### Prerequisites
<a name="efs-edc-prerequisites"></a>
+ Your account is in the EFS and EDC preview.
+ AWS CLI version 2.35 or later, and curl with `--aws-sigv4`.
+ An IAM role that can create KMS keys, S3 buckets, and IAM policies.
+ Access to a covered model in Amazon Bedrock.

### Configure AWS credentials and Region
<a name="efs-edc-credentials"></a>

```bash
export AWS_PROFILE={{<profile-name>}}
export AWS_REGION={{<region>}}
export AWS_PAGER=""
aws sts get-caller-identity
```

Check that the account in the output is the one you're setting up. `AWS_PAGER=""` stops the CLI from opening a pager.

### Step 1: Create the KMS key
<a name="efs-edc-step1-key"></a>

1. Open the AWS KMS console in the Region where you'll call the covered models, and choose **Create key**.

1. Choose **Symmetric** and **Encrypt and decrypt**. Keep **Single-Region key**.

1. Replace the default key policy with the following policy. Replace the values in angle brackets (see [Values you provide](#efs-edc-values)). The first statement keeps your account in control of the key. The second lets Amazon Bedrock use the key directly, and the third lets Amazon Bedrock's writes through Amazon S3 use it.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AccountRootAdministersTheKey",
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::{{<account-id>}}:root"
         },
         "Action": "kms:*",
         "Resource": "*"
       },
       {
         "Sid": "AllowBedrockDataRetentionCMEK",
         "Effect": "Allow",
         "Principal": {
           "Service": "bedrock.amazonaws.com"
         },
         "Action": [
           "kms:DescribeKey",
           "kms:Encrypt",
           "kms:Decrypt",
           "kms:GenerateDataKey"
         ],
         "Resource": "{{<key-arn>}}",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{<account-id>}}"
           }
         }
       },
       {
         "Sid": "AllowBedrockRetentionBucketSSEKMS",
         "Effect": "Allow",
         "Principal": {
           "Service": "bedrock.amazonaws.com"
         },
         "Action": [
           "kms:GenerateDataKey",
           "kms:Decrypt"
         ],
         "Resource": "{{<key-arn>}}",
         "Condition": {
           "StringEqualsIfExists": {
             "aws:SourceAccount": "{{<account-id>}}"
           },
           "StringLike": {
             "kms:ViaService": "s3.*.amazonaws.com",
             "kms:EncryptionContext:aws:s3:arn": [
               "arn:aws:s3:::{{<bucket-name>}}",
               "arn:aws:s3:::{{<bucket-name>}}/*"
             ]
           }
         }
       }
     ]
   }
   ```

   The `aws:SourceAccount` condition means Amazon Bedrock can use this key only for your account's data. These policies are for an account configuration. For a project or organization configuration, see [Organization and project configurations](#efs-edc-org-project) for the conditions to add.

1. Turn on automatic key rotation, create the key, and copy its ARN.

**Important**
If you disable this key or schedule it for deletion, nobody can read the content it protects, and Amazon Bedrock removes access to covered models for that account after 24 hours.

### Step 2: Create the bucket
<a name="efs-edc-step2-bucket"></a>

For the preview, we recommend you test with your own bucket.

1. Open the Amazon S3 console and create a general purpose bucket in the same Region as the key. Don't use dots in the name.

1. Use these settings:

<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>Object Ownership</td><td>Bucket owner enforced</td></tr>
  <tr><td>Block Public Access</td><td>All four settings on</td></tr>
  <tr><td>Bucket Versioning</td><td>Enabled</td></tr>
  <tr><td>Default encryption</td><td>SSE-KMS with your key from Step 1, with Bucket Key enabled</td></tr>
  <tr><td>Object Lock, Requester Pays</td><td>Off</td></tr>
  <tr><td>Replication, storage class transitions</td><td>None</td></tr>
  <tr><td>Lifecycle rules</td><td>Only the rules in <a href="#efs-edc-lifecycle">Bucket lifecycle rules</a></td></tr>
</tbody>
</table>

1. Add this bucket policy. Replace the values in angle brackets.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AllowBedrockDataRetentionObjects",
         "Effect": "Allow",
         "Principal": {
           "Service": "bedrock.amazonaws.com"
         },
         "Action": [
           "s3:PutObject",
           "s3:GetObject",
           "s3:GetObjectVersion",
           "s3:DeleteObject",
           "s3:DeleteObjectVersion",
           "s3:AbortMultipartUpload",
           "s3:ListMultipartUploadParts",
           "s3:GetObjectAttributes",
           "s3:GetObjectVersionAttributes"
         ],
         "Resource": "arn:aws:s3:::{{<bucket-name>}}/*",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{<account-id>}}"
           }
         }
       },
       {
         "Sid": "AllowBedrockDataRetentionBucket",
         "Effect": "Allow",
         "Principal": {
           "Service": "bedrock.amazonaws.com"
         },
         "Action": [
           "s3:ListBucket",
           "s3:ListBucketVersions",
           "s3:GetBucketLocation",
           "s3:GetBucketVersioning",
           "s3:GetLifecycleConfiguration",
           "s3:GetEncryptionConfiguration",
           "s3:GetBucketPublicAccessBlock",
           "s3:GetBucketOwnershipControls",
           "s3:GetBucketObjectLockConfiguration",
           "s3:GetBucketRequestPayment",
           "s3:GetReplicationConfiguration",
           "s3:GetMetricsConfiguration",
           "s3:GetInventoryConfiguration",
           "s3:GetBucketPolicy",
           "s3:ListBucketMultipartUploads",
           "s3:GetIntelligentTieringConfiguration",
           "s3:GetBucketTagging"
         ],
         "Resource": "arn:aws:s3:::{{<bucket-name>}}",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{<account-id>}}"
           }
         }
       },
       {
         "Sid": "NobodyHardDeletesRecordVersions",
         "Effect": "Deny",
         "Principal": "*",
         "Action": "s3:DeleteObjectVersion",
         "Resource": [
           "arn:aws:s3:::{{<bucket-name>}}/slab/*",
           "arn:aws:s3:::{{<bucket-name>}}/slab-manifest/*",
           "arn:aws:s3:::{{<bucket-name>}}/safeguards-data/slab/*",
           "arn:aws:s3:::{{<bucket-name>}}/safeguards-data/slab-manifest/*",
           "arn:aws:s3:::{{<bucket-name>}}/safeguards-data/derived_slab/*",
           "arn:aws:s3:::{{<bucket-name>}}/transcripts/*"
         ]
       },
       {
         "Sid": "RequireTls",
         "Effect": "Deny",
         "Principal": "*",
         "Action": "s3:*",
         "Resource": [
           "arn:aws:s3:::{{<bucket-name>}}",
           "arn:aws:s3:::{{<bucket-name>}}/*"
         ],
         "Condition": {
           "Bool": {
             "aws:SecureTransport": "false"
           }
         }
       },
       {
         "Sid": "DenyUploadsWithOtherEncryption",
         "Effect": "Deny",
         "Principal": "*",
         "Action": "s3:PutObject",
         "Resource": "arn:aws:s3:::{{<bucket-name>}}/*",
         "Condition": {
           "Null": {
             "s3:x-amz-server-side-encryption": "false"
           },
           "StringNotEquals": {
             "s3:x-amz-server-side-encryption": "aws:kms"
           }
         }
       },
       {
         "Sid": "DenyUploadsNamingAnotherKey",
         "Effect": "Deny",
         "Principal": "*",
         "Action": "s3:PutObject",
         "Resource": "arn:aws:s3:::{{<bucket-name>}}/*",
         "Condition": {
           "Null": {
             "s3:x-amz-server-side-encryption-aws-kms-key-id": "false"
           },
           "StringNotEquals": {
             "s3:x-amz-server-side-encryption-aws-kms-key-id": "{{<key-arn>}}"
           }
         }
       },
       {
         "Sid": "DenySseCUploads",
         "Effect": "Deny",
         "Principal": "*",
         "Action": "s3:PutObject",
         "Resource": "arn:aws:s3:::{{<bucket-name>}}/*",
         "Condition": {
           "Null": {
             "s3:x-amz-server-side-encryption-customer-algorithm": "false"
           }
         }
       }
     ]
   }
   ```

   The first two statements let Amazon Bedrock read and write retained content to the bucket, and check your bucket's settings when you save your configuration. The rest are required: nobody, including Amazon Bedrock, can permanently delete retained records; requests without TLS are refused; and uploads can't name another encryption type, another KMS key, or customer-provided keys (SSE-C). Don't give Amazon Bedrock broader access than this, or Amazon Bedrock refuses to save the configuration.

1. To see Amazon Bedrock's access to your objects, turn on CloudTrail data events for the bucket.

1. Add the lifecycle rules in [Bucket lifecycle rules](#efs-edc-lifecycle).

### Step 3: Give your role permission to save the configuration
<a name="efs-edc-step3-caller"></a>

Attach this policy to the role you'll use in Steps 4 and 5. When you save, Amazon Bedrock checks that your role can use the key and bucket. If the key or bucket is in another account, its policy must also allow your role.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageRetentionStorageAndMode",
      "Effect": "Allow",
      "Action": [
        "bedrock:PutAccountDataRetentionStorage",
        "bedrock:GetAccountDataRetentionStorage",
        "bedrock:DeleteAccountDataRetentionStorage",
        "bedrock:GetAccountDataRetention",
        "bedrock:PutAccountDataRetention"
      ],
      "Resource": "*"
    },
    {
      "Sid": "UseTheKey",
      "Effect": "Allow",
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "{{<key-arn>}}"
    },
    {
      "Sid": "UseTheBucket",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::{{<bucket-name>}}/*"
    }
  ]
}
```

### Step 4: Save your storage configuration
<a name="efs-edc-step4-storage"></a>

```bash
efs() {
  local method=$1 route=$2; shift 2
  eval "$(aws configure export-credentials --format env)"
  curl -sS -X "$method" --aws-sigv4 "aws:amz:${AWS_REGION}:bedrock" \
    --user "${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}" \
    -H "x-amz-security-token: ${AWS_SESSION_TOKEN}" \
    -H "content-type: application/json" "$@" \
    "https://bedrock.${AWS_REGION}.amazonaws.com${route}"
}
efs PUT /v1/data_retention/storage/anthropic -d '{
  "storageDestination": "customer_managed",
  "storageConfiguration": {
    "kmsKeyArn":     "{{<key-arn>}}",
    "s3BucketArn":   "arn:aws:s3:::{{<bucket-name>}}",
    "s3BucketOwner": "{{<account-id>}}"
  }
}'
```

The bucket and key must be in the Region where you save the configuration, so each Region needs its own bucket and key. Run this step once in each Region where you call the covered models, with `AWS_REGION` set to that Region.

Use the key ARN, not an alias, and the plain bucket ARN, without a prefix. Before it saves, Amazon Bedrock checks your role's access, its own access, encryption, and your source conditions. It writes empty test files under `amazon-bedrock-retention-storage-validation/` and then deletes them. If any check fails, nothing is saved. A successful save returns `active` for the key and the bucket:

```json
{
  "scope": "account",
  "modelProvider": "anthropic",
  "storageDestination": "customer_managed",
  "storageConfiguration": {
    "kmsKeyArn": "{{<key-arn>}}",
    "s3BucketArn": "arn:aws:s3:::{{<bucket-name>}}",
    "s3BucketOwner": "{{<account-id>}}"
  },
  "updatedAt": "2026-11-19T17:00:00Z",
  "kmsKeyStatus": "active",
  "s3BucketStatus": "active"
}
```

**Note**
`active` means Amazon Bedrock could use your key and bucket when you saved the configuration. It doesn't guarantee they'll stay usable. Use every setting from Step 2, and don't change them afterward.

### Step 5: Set your data retention mode
<a name="efs-edc-step5-mode"></a>

Set the mode to `aws_review` in each Region where you call the covered models. For accounts in EFS or EDC, AWS's reviewers don't review your content: anything flagged goes to you as a case. Choosing a mode doesn't make your account eligible for EFS. See [Data retention](data-retention.md).

```bash
efs GET /data-retention
efs PUT /data-retention -d '{"mode": "aws_review"}'
```

**Important**
The mode applies to every Amazon Bedrock call in the account in that Region, not only to EFS or EDC.

### Check your setup
<a name="efs-edc-check-setup"></a>

1. Run `efs GET /v1/data_retention/storage/anthropic` and check that `kmsKeyStatus` and `s3BucketStatus` are `active`.

1. Call a covered model through Amazon Bedrock.

1. In CloudTrail, look for `GenerateDataKey`, `Decrypt`, `DescribeKey`, and `Encrypt` calls on your key by the service principal. Expect about one `GenerateDataKey` a day.

1. If you have a bucket, look for objects under `slab/`. They usually appear within minutes, or up to 72 hours if Amazon Bedrock has to retry.

If something looks wrong, see [Troubleshooting](#efs-edc-troubleshooting).

## Handle cases
<a name="efs-edc-cases"></a>

Each case is a new file in the `review-cases/` folder of your S3 bucket. Check this folder at least once a day, or set an alert (see [Get alerted when a case arrives](#efs-edc-case-alerts)). Notices, such as a reminder to respond, arrive in the same bucket, in `review-notices/`.

### How cases work
<a name="efs-edc-how-cases-work"></a>

1. Transcripts arrive. Amazon Bedrock writes retained requests and responses to `transcripts/`, whether or not there's a case.

1. When automated review flags potentially unsafe activity, a case file appears in `review-cases/`. It lists each flagged request and points to its transcript in `transcripts/`.

1. You review it with your own access, and investigate whether there's a violation of AWS's or Anthropic's terms of service or use policies.

1. You respond with a file in `review-responses/`.

1. EFS reads your response. About once an hour, it checks for responses to your open cases.

1. The case closes after a valid response, or when the 7-day review window ends.

| Folder in your bucket | What's in it |
| --- | --- |
| transcripts/ | Retained copies of your requests and responses |
| review-cases/ | One file per case. Amazon Bedrock creates it, and updates it when the case closes. |
| review-responses/ | Your responses. Amazon Bedrock reads only files named after your open cases. |
| review-notices/ | Reminders, for example when a case is still unanswered. Each kind of notice is a fixed sentence. |

Don't move or edit case files, because Amazon Bedrock updates each case's status in place. Transcripts are readable files under your bucket's SSE-KMS encryption. They expire after up to 30 days, so copy any you must keep. Transcripts don't yet support Amazon Bedrock Guardrails masking or blocking: they store responses as they were before guardrails ran.

### Get alerted when a case arrives
<a name="efs-edc-case-alerts"></a>

EFS doesn't send email. To route new cases to your intake, add an S3 Event Notification on `review-cases/`. This example sends each new or updated case file to an Amazon SNS topic, which can email your security operations center (SOC) or feed your ticketing system:

```bash
aws s3api put-bucket-notification-configuration --bucket {{<bucket-name>}} \
  --notification-configuration '{
    "TopicConfigurations": [{
      "TopicArn": "{{<topic-arn>}}",
      "Events": ["s3:ObjectCreated:*"],
      "Filter": { "Key": { "FilterRules": [
        { "Name": "prefix", "Value": "review-cases/" } ] } }
    }]
  }'
```

The topic's access policy must allow `s3.amazonaws.com` to publish, with `aws:SourceArn` set to your bucket. You can also use CloudTrail data events with Amazon EventBridge, or an AWS Lambda function that opens a ticket.

### What a case tells you
<a name="efs-edc-case-contents"></a>

Each case contains a case ID, the policy categories, the project, and a list of flagged inference requests. Each entry has an `item_id`, which identifies one flagged request, and an `object_key`, which points to that request's transcript in your bucket. The case also shows its status, and when it was last updated.

### Route a case to the right team
<a name="efs-edc-case-routing"></a>

How you route cases is up to your own process. The policy categories, the project, and the request IDs help. To find the user behind a flagged request, match its request ID to your own logs. Cases, transcripts, and responses are in separate folders, so you can use IAM permissions to give people access to one folder and not another. Access is by folder, not by case.

### Give your reviewers access
<a name="efs-edc-reviewer-access"></a>

Give this policy only to the people who review cases, because transcripts contain your users' prompts and responses. It lets them read cases, transcripts, and notices, and write responses. We recommend that you use a policy according to your individual compliance requirements.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadCasesAndTranscripts",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": [
        "arn:aws:s3:::{{<bucket-name>}}/transcripts/*",
        "arn:aws:s3:::{{<bucket-name>}}/review-cases/*",
        "arn:aws:s3:::{{<bucket-name>}}/review-notices/*"
      ]
    },
    {
      "Sid": "WriteResponses",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::{{<bucket-name>}}/review-responses/*"
    },
    {
      "Sid": "ListCaseFolders",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::{{<bucket-name>}}",
      "Condition": {
        "StringLike": {
          "s3:prefix": [
            "transcripts/*",
            "review-cases/*",
            "review-responses/*",
            "review-notices/*"
          ]
        }
      }
    },
    {
      "Sid": "UseTheKey",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "{{<key-arn>}}"
    }
  ]
}
```

Respond within 7 calendar days of the case arriving in your bucket.

### Respond to a case
<a name="efs-edc-respond"></a>

Investigate whether there's a violation of AWS's or Anthropic's terms of service or use policies, then write one file, `review-responses/{{<case id>}}.json`. The file states `violation` or `no_violation`, meaning whether you found evidence of a violation. For a `violation`, list which of the case's policy categories apply, or `other`. For `no_violation`, use an empty list. The first valid response that Amazon Bedrock reads is final.

Respond within 7 calendar days of the case arriving. If you don't, Amazon Bedrock may stop serving your requests. In certain cases, requests may stop being served before the 7 days end.

### Know when a case is closed
<a name="efs-edc-case-closed"></a>

When Amazon Bedrock accepts your response, the case status changes to `closed`, with the reason `responded`. If it stays open, correct your file and write it again. Closed with `window_ended` means the 7-day review window ended without a valid response, not that the matter is cleared. Repeatedly not responding can lead to account suspension.

### Escalate a case
<a name="efs-edc-escalate"></a>

If you need more information about a case, or think it's wrong, contact AWS Support or your AWS account team with the case ID and your account ID.

## Manage storage for organizations, accounts, and projects
<a name="efs-edc-scopes"></a>

You set your key and storage for each Region, at organization, account, or project scope. An organization configuration is automatically inherited by every account in the organization, and an account can override it with its own configuration.

The most specific configuration wins. Within a Region, and within the scope of your approval, Amazon Bedrock checks for a configuration in this order and uses the first one it finds:

1. Project: the configuration for the project named in the request.

1. Account: the configuration for the account that made the request.

1. Organization: the configuration for the account's organization.

For example, if your organization saves a configuration with one bucket, and one account saves its own configuration with a different bucket, that account's content goes to its own bucket. Every other account in the organization uses the organization's bucket.

**Note**
How configurations combine across organization, account, and project scope may change during the preview. We'll update this topic when it does.

| Scope | What it covers |
| --- | --- |
| Organization | Every account in your organization in AWS Organizations, in one Region. Save it from the management account or a delegated administrator for Amazon Bedrock. |
| Account | One account, in one Region |
| Project | One Amazon Bedrock project in your account, in one Region. Use projects to keep separate storage for separate workloads. Up to 10,000 projects per account are supported in the public preview. |

To change a configuration, save it again. Each save replaces the whole configuration, and Amazon Bedrock switches to the new key or bucket within 24 hours of saving the new configuration, often sooner. Content already stored stays where it is until it expires, so keep your old key and bucket for 40 days. To delete a configuration, run `efs DELETE /v1/data_retention/storage/anthropic`. Amazon Bedrock then uses the next configuration that applies. Deleting a configuration doesn't delete your S3 objects or your key.

## Security and access control
<a name="efs-edc-security"></a>

### Shared responsibility
<a name="efs-edc-shared-responsibility"></a>

| AWS | You |
| --- | --- |
| Encrypts retained content with your key and stores it in your bucket, if you have one | Keep the key enabled and the policies in place |
| Reaches your key and bucket only as the service principal, for your account | Scope your policies to your account, and review CloudTrail |
| Checks your key and bucket when you save a configuration | Keep the required bucket settings and lifecycle rules |
| Opens cases in your bucket | Review and respond to cases |

### If Amazon Bedrock loses access
<a name="efs-edc-lost-access"></a>

Amazon Bedrock fails closed. If it can't use your key or bucket for 24 hours, it stops serving the covered models for the organization, account, or project and Region that use that configuration. Amazon Bedrock also stops serving the covered models if you delete retained content early or loosen the required bucket settings.

### Audit
<a name="efs-edc-audit"></a>

CloudTrail shows the service principal for every use of your key, and for bucket access when data events are on.

### Organization policies
<a name="efs-edc-org-policies"></a>
+ A resource control policy (RCP) that blocks AWS services unless the source is your organization allows Amazon Bedrock, because Amazon Bedrock sends your account as the source.
+ If your key or bucket policy blocks requests by IP address or VPC, add an exception for AWS services (`aws:PrincipalIsAWSService`). Otherwise Amazon Bedrock is blocked, and Amazon Bedrock stops serving the covered models.
+ If an RCP or service control policy (SCP) denies S3 or KMS access from outside your organization unless `aws:PrincipalIsAWSService` is `true`, check that it allows the service principal. If it doesn't, saving the storage configuration fails with missing access on the key, and your CloudTrail shows no denied calls.
+ If you limit AWS KMS to certain Regions, include the key's Region.
+ Don't limit your key to use through S3 only (`kms:ViaService`). Amazon Bedrock and the role that saves the configuration also call the key directly, so a policy that allows only S3 calls blocks them.
+ Don't require an encryption header on uploads. Amazon Bedrock relies on your bucket's default encryption, so your bucket policy must allow uploads without the header.

## Preview availability and limitations
<a name="efs-edc-limitations"></a>

| Area | In this preview |
| --- | --- |
| How to join | See [Get access to EFS and EDC](#efs-edc-get-access) |
| Covered models |  +  Claude Fable 5, Claude Fable 5.1, and Claude Fable 5.2 <br />+  Claude Mythos 5, Claude Mythos 5.1, and Claude Mythos 5.2 <br />+  Claude Opus 5.5 and Claude Sonnet 5.5 when used through CVP   |
| Regions | See [Supported Regions](#efs-edc-regions) |
| APIs | Requests through Amazon Bedrock Runtime (bedrock-runtime). |
| Projects | Up to 10,000 projects per account. This limit changes at general availability. |
| Console | Not available. |
| Which configuration applies | The storage APIs return what's saved at each scope. |
| Bucket in another account | Supported. Set s3BucketOwner, and allow your role in that account's bucket. |
| Policy condition keys | Not available. You can't yet use an SCP to require a retention mode or storage destination. We welcome feedback on what you want to enforce. |

## Troubleshooting
<a name="efs-edc-troubleshooting"></a>

| What you see | What to do |
| --- | --- |
| ConflictException (HTTP 400) when you save | Your account isn't in the preview yet. Confirm with your AWS account representatives that it was added. |
| HTTP 400 about the key | Check that it's a full, single-Region, symmetric key ARN in the same Region, that it's enabled, and that its policy matches [Step 1: Create the KMS key](#efs-edc-step1-key). |
| HTTP 400 about the bucket | Check the settings and policy in [Step 2: Create the bucket](#efs-edc-step2-bucket), including the lifecycle rules (see [Bucket lifecycle rules](#efs-edc-lifecycle)). |
| Saving fails with missing access on the key | Check that your role can use the key and bucket ([Step 3: Give your role permission to save the configuration](#efs-edc-step3-caller)), that the key policy matches [Step 1: Create the KMS key](#efs-edc-step1-key), and that no RCP or SCP blocks the service principal ([Organization policies](#efs-edc-org-policies)). |
| kmsKeyStatus or s3BucketStatus isn't active | A policy, organization policy, or the key's state changed. Fix it within 24 hours, or Amazon Bedrock stops serving the covered models. |
| Calls to covered models fail | The mode isn't aws\_review, or Amazon Bedrock stopped serving the models after 24 hours without key or bucket access. |
| No files in the bucket | Check that both statuses are active and that you called a covered model. |

When you contact AWS Support, include your account ID, the Region, the time and request ID, and the output of `efs GET /v1/data_retention/storage/anthropic`.

## Clean up resources
<a name="efs-edc-cleanup"></a>

1. Leave the preview. See [Leave the preview](#efs-edc-leave-preview).

1. Delete your storage configuration in each Region: `efs DELETE /v1/data_retention/storage/anthropic`.

1. Keep the key and bucket for at least 40 days, so that content already stored can still be read until it expires.

1. Then delete the bucket, and schedule the key for deletion. Once the key is deleted, any data encrypted with it can't be decrypted.

## Organization and project configurations
<a name="efs-edc-org-project"></a>

The walkthrough in [Set up EFS and EDC](#efs-edc-setup) configures one account. For an organization or a project, use the same steps with these differences.

| Scope | Source condition in key and bucket policies | Caller permissions | Storage path |
| --- | --- | --- | --- |
| Account | aws:SourceAccount with your account ID | bedrock:\*AccountDataRetentionStorage | /v1/data\_retention/storage/anthropic |
| Organization | aws:SourceOrgID with your organization ID, not a member account ID | bedrock:\*OrganizationDataRetentionStorage, plus organizations:DescribeOrganization on \*. A delegated administrator also needs organizations:ListDelegatedAdministrators on \*. | /v1/data\_retention/organization-storage/anthropic |
| Project | aws:SourceAccount, plus aws:SourceArn with the project ARN | bedrock:\*ProjectDataRetentionStorage on the project ARN | /v1/projects/{projectIdentifier}/data\_retention/storage/anthropic |

For a project configuration, add the project ARN to the `Condition` block of each statement that allows `bedrock.amazonaws.com`:

```json
"ArnEquals": {
  "aws:SourceArn": "{{<project-arn>}}"
}
```

In the key policy's `AllowBedrockRetentionBucketSSEKMS` statement, use `ArnEqualsIfExists` instead of `ArnEquals`.

For an organization configuration, replace `aws:SourceAccount` with `aws:SourceOrgID` and your organization ID in the same statements.

Organization prerequisites: your organization must have all features enabled, and you save the configuration from the management account or a delegated administrator for Amazon Bedrock.

### Use projects
<a name="efs-edc-use-projects"></a>

Create a project with `POST /projects` on the Amazon Bedrock control plane, then save a storage configuration for it at `/v1/projects/{projectIdentifier}/data_retention/storage/anthropic`. To send a request through a project, pass the project ID or ARN with your request. Requests that don't name a project use your account or organization configuration.

Your IAM policy must allow the model call on the project ARN as well as the model. In the key and bucket policies, add `aws:SourceArn` with the project ARN. Archived projects can't be used for inference or changed.

## Bucket lifecycle rules
<a name="efs-edc-lifecycle"></a>

Use only these lifecycle rules on your bucket. Other lifecycle rules, such as rules that expire objects sooner or transition storage classes, can make Amazon Bedrock's checks fail. Save the rules as `lifecycle.json`:

```json
{
  "Rules": [
    {
      "ID": "efs-slab-noncurrent-expiry",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "slab/"
      },
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 3
      }
    },
    {
      "ID": "efs-media-noncurrent-expiry",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "media/"
      },
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 3
      }
    },
    {
      "ID": "efs-safeguards-slab-noncurrent-expiry",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "safeguards-data/slab/"
      },
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 3
      }
    },
    {
      "ID": "efs-safeguards-media-noncurrent-expiry",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "safeguards-data/media/"
      },
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 3
      }
    },
    {
      "ID": "efs-abort-incomplete-multipart",
      "Status": "Enabled",
      "Filter": {
        "Prefix": ""
      },
      "AbortIncompleteMultipartUpload": {
        "DaysAfterInitiation": 7
      }
    },
    {
      "ID": "efs-expire-delete-markers",
      "Status": "Enabled",
      "Filter": {
        "Prefix": ""
      },
      "Expiration": {
        "ExpiredObjectDeleteMarker": true
      }
    },
    {
      "ID": "efs-review-summaries-expiry",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "review-summaries/"
      },
      "Expiration": {
        "Days": 30
      },
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 3
      }
    },
    {
      "ID": "efs-transcripts-expiry",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "transcripts/"
      },
      "Expiration": {
        "Days": 30
      },
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 3
      }
    }
  ]
}
```

Then apply them to your bucket:

```bash
aws s3api put-bucket-lifecycle-configuration --bucket {{<bucket-name>}} \
  --lifecycle-configuration file://lifecycle.json
```

These rules expire noncurrent versions of retained records after 3 days, expire transcripts and review summaries after 30 days, abort incomplete multipart uploads after 7 days, and remove expired delete markers.

## Supported Regions
<a name="efs-edc-regions"></a>

Automated review runs in US East (N. Virginia) (`us-east-1`) and Europe (Ireland) (`eu-west-1`). In the public preview, EFS and EDC apply to covered model requests made through the US and EU geographic cross-Region inference profiles and the global cross-Region inference profile.
