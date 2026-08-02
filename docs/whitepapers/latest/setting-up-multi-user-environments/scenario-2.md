---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/scenario-2.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scenario 2: Limited user access to the AWS Management Console within a single account
<a name="scenario-2"></a>

 This scenario is excellent for users that require control of AWS resources, such as students in cloud computing or high performance computing (HPC) classes. With this scenario, users are given restricted access to the AWS services through their IAM credentials.

## Example
<a name="example-1"></a>

 Consider a class with 25 students. The administrator creates 25 IAM users using the AWS Management Console, AWS Command Line Interface, or APIs, and provides each student with their IAM credentials and a login URL for the AWS Management Console. The administrator also creates a permissions policy that can be attached to a user group or an individual user to allow or deny access to different services.

 Each student (IAM user) has access to resources and services as defined by the access control policies set by the administrator. Students can log in to the AWS Management Console to access different AWS services as defined the policy. For example, they could launch Amazon EC2 instances and store objects in [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) buckets.
