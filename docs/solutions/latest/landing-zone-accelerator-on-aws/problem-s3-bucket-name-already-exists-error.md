---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-s3-bucket-name-already-exists-error.html
---

# Problem: "S3 bucket name already exists" error
<a name="problem-s3-bucket-name-already-exists-error"></a>

This solution creates Amazon S3 buckets during deployment. Some of these buckets (such as those deployed along with the [Centralized logging](centralized-logging.md) infrastructure) are mandatory. Others (such as the report destination buckets created for Cost and Usage Reports and AWS Audit Manager) deploy based on your defined configuration.

**Note**
By default, Amazon S3 buckets deployed by CloudFormation have a [deletion policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) that’s set to retain the resources. Landing Zone Accelerator on AWS uses this default policy so that you can deactivate a service that the solution previously managed and still preserve your data stored in Amazon S3.

Scenarios that can cause this error include:

1. If you deactivate a solution-managed service and then reactivate it later.

1. If you uninstall the solution and then reinstall it later into the same environment.

These errors result from a standard naming convention for Amazon S3 buckets that this solution deploys. Because Amazon S3 bucket names must be globally unique, you receive an error message if the previous Amazon S3 buckets were not deleted. The following is an example, with `aws-accelerator-<SERVICE>-<ACCOUNT_ID>-<REGION> ` representing the bucket name:

 `AWSAccelerator-<STACK_NAME>- <ACCOUNT_ID>-<REGION> ` failed: Error: The stack named AWSAccelerator-` <STACK_NAME>- <ACCOUNT_ID>-<REGION> ` failed creation, it may need to be manually deleted from the AWS console: ROLLBACK\_COMPLETE: aws-accelerator-` <SERVICE>- <ACCOUNT_ID>-<REGION> ` already exists.

## Resolution
<a name="resolution-5"></a>

Complete the following steps when this error occurs:

1. If you want to retain the data, make a local copy or [copy the data to another Amazon S3 bucket](https://aws.amazon.com/premiumsupport/knowledge-center/move-objects-s3-bucket/) in your account.

1. Delete the solution-created Amazon S3 bucket that’s causing the conflict.

1.  [Retry](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-retry.html) the failing **AWSAccelerator-Pipeline** stage.
