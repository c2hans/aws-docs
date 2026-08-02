---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/regional-boundary-enforcement.html
---

# Regional boundary enforcement
<a name="regional-boundary-enforcement"></a>

## Control objective
<a name="control-objective.4858afe1-8071-54f8-9613-2aa6d7cbe121"></a>

***Network perimeter**** – My identities can access resources only from expected networks*

AI workloads often have data residency requirements that mandate processing within specific geographic regions. Implement controls that prevent cross-region data flows and ensure model invocations occur only in approved regions by applying this service control policy (SCP) at the organization or OU level to enforce regional boundaries for all Amazon Bedrock operations:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RestrictToApprovedRegions",
      "Effect": "Deny",
      "Action": "bedrock:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": [
            "us-east-1",
            "us-west-2",
            "eu-west-1"
          ]
        }
      }
    },
    {
      "Sid": "DataResidencyCompliance",
      "Effect": "Deny",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:CreateCustomModel"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/DataResidency": "EU"
        },
        "StringNotEquals": {
          "aws:RequestedRegion": [
            "eu-west-1",
            "eu-central-1"
          ]
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **RestrictToApprovedRegions** – Blocks all Amazon Bedrock operations outside approved regions (`us-east-1`, `us-west-2`, `eu-west-1`).
+ **DataResidencyCompliance** – Ensures EU data residency compliance by restricting EU-tagged operations to EU regions only.

### Cross-region replication restrictions (Amazon S3 bucket policy):
<a name="cross-region-replication-restrictions-bucket-policy"></a>

Prevent cross-region replication of training data by attaching this policy to Amazon S3 buckets containing Amazon Bedrock training data:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PreventCrossRegionReplication",
      "Effect": "Deny",
      "Action": [
        "s3:ReplicateObject",
        "s3:ReplicateDelete"
      ],
      "Resource": "arn:aws:s3:::bedrock-*/*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-repl-context": "SAME_REGION"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **PreventCrossRegionReplication** – Blocks Amazon S3 cross-region replication for Amazon Bedrock data buckets to maintain data residency.
