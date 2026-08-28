---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-s3a-cse-kms.html
---

# Setup CSE-KMS
<a name="emr-s3a-cse-kms"></a>

You can enable client-side encryption using AWS KMS (CSE-KMS) in two primary scopes:
+ The first is cluster-wide configuration:

  ```
  [
    {
      "Classification":"core-site",
      "Properties": {
         "fs.s3a.encryption.algorithm": "CSE-KMS",
         "fs.s3a.encryption.key":"${KMS_KEY_ID}",
      }
    }
  ]
  ```
**Note**
If the AWS KMS key region is different than the S3 bucket/EMR region, you must set the following additional configuration: `fs.s3a.encryption.cse.kms.region=${KMS_REGION}`.
+ The second is job or application-specific configuration. CSE-KMS can be setup for a specific Spark application as follows:

  ```
  spark-submit --conf spark.hadoop.fs.s3a.encryption.algorithm=CSE-KMS --conf spark.hadoop.fs.s3a.encryption.key=${{{KMS_KEY_ID}}}
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
