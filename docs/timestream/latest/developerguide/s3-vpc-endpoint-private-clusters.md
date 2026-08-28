---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/s3-vpc-endpoint-private-clusters.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Configure S3 VPC Endpoint for Private Clusters
<a name="s3-vpc-endpoint-private-clusters"></a>

When deploying private clusters, you must configure an S3 VPC endpoint with appropriate permissions to ensure cluster resources can access required S3 buckets.

**Note**
The S3 endpoint should preferably be associated with a VPC that hosts only Timestream for InfluxDB private databases.

**Note**
Shared VPCs are not currently supported for Timestream for InfluxDB 3.

## Prerequisites
<a name="s3-endpoint-prerequisites"></a>
+ A VPC with private subnets configured for your cluster
+ Appropriate IAM permissions to create and modify VPC endpoints

## Required S3 Endpoint Policy
<a name="required-s3-endpoint-policy"></a>

Your S3 VPC endpoint requires a policy that grants sufficient access for cluster operations. The following example provides full S3 access through the endpoint:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "FullAccess",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

------

## Configuration Steps
<a name="s3-endpoint-configuration-steps"></a>

1. Navigate to the VPC console and select **Endpoints**

1. Choose your S3 endpoint or create a new one

1. In the **Policy** tab, replace the existing policy with the example above

1. Save your changes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
