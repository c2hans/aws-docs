---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-s3.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Create an S3 Stack
<a name="gui-ex-create-s3"></a>

Launch an S3 bucket. The S3 bucket is where you upload the application bundle you created.

REQUIRED DATA:
+ `VPC-ID`: This value determines where your S3 Bucket will be, this should be the same as the previously used VPC.
+ `AccessControl`: Pre-set AccessControl list (ACL) options are `Private`, and `PublicRead`. For more information, see [Amazon Simple Storage Service Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl).
+ `BucketName`: This value sets the S3 Bucket name, you use it to upload your application bundle. It must be unique across the region of the account and cannot include upper-case letters. Including your account ID as part of the BucketName is not a requirement but makes it easier to identify the bucket later. To see what S3 bucket names exist in the account, go to the Amazon S3 Console for your account.

1. On the **Create RFC** page, select the category **Deployment**, subcategory **Advanced Stack Components**, item **S3 storage**, and click **Create**.

   You can leave the default parameter option at **Basic** to accept the defaults as described. To set different values, choose **Advanced**.
**Note**
The bucket deployed with this change type allows full read/write access to the whole account, new change types may be needed to allow more restricted access permissions.

   ```
   Subject:              S3-Bucket-RFC
   BucketName:           {{ACCOUNT_ID-codedeploy-bundles}}
   AccessControl:        {{Private}}

   VpcId:                {{VPC_ID}}
   Name:                 S3BucketForWP
   ```

1. Click **Submit** when finished.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
