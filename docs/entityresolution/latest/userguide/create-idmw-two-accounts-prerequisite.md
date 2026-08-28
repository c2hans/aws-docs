---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/create-idmw-two-accounts-prerequisite.html
---

# Prerequisites
<a name="create-idmw-two-accounts-prerequisite"></a>

Before you create an ID mapping workflow across two AWS accounts, you must first do the following:
+ Complete the tasks in [Set up AWS Entity Resolution](setting-up.md).
+ [Create an ID namespace source](create-id-namespace-source.md).
+ [Create an ID namespace target](create-id-namespace-target.md).
+ Acquire the ID namespace ARN if you are using an ID namespace source from another AWS account.
+ (**Provider services** only) Creating an ID mapping workflow across two AWS accounts requires permission for LiveRamp to access the S3 bucket and the AWS Key Management Service (AWS KMS) customer managed key.

  Before you create an ID mapping workflow across two AWS accounts with LiveRamp, add the following permission policy, which allows LiveRamp to access the S3 bucket and the customer managed key.

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [{
          "Effect": "Allow",
          "Principal": {
              "AWS": "arn:aws:iam::715724997226:root"
          },
          "Action": [
              "kms:Decrypt"
          ],
          "Resource": "arn:aws:kms:us-east-1:{{111122223333}}:key/key-id",
          "Condition": {
              "StringEquals": {
              "kms:ViaService": "s3.us-east-1.amazonaws.com"
              }
          }
      }]
  }
  ```

------

  In the preceding permissions policy, replace each {{<user input placeholder>}} with your own information.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-idmw-two-accounts-prerequisite.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
