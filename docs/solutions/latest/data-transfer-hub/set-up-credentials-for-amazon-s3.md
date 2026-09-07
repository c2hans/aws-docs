---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/set-up-credentials-for-amazon-s3.html
---

# Set up credentials for Amazon S3
<a name="set-up-credentials-for-amazon-s3"></a>

## Step 1: Create an IAM policy
<a name="step-1-create-an-iam-policy"></a>

1.  Open AWS Management Console.

1.  Choose IAM > Policy, and choose **Create Policy**.

1.  Create a policy. You can follow the example below to use IAM policy statement with minimum permissions, and change the `<your-bucket-name>` in the policy statement accordingly.

**Note**
 For S3 buckets in AWS China Regions, make sure you also change to use `arn:aws-cn:s3:::` instead of `arn:aws:s3:::`.

**Policy for source bucket**

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "dth",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource":[
                "arn:aws:s3:::<your-bucket-name>/*",
                "arn:aws:s3:::<your-bucket-name>"
            ]
        }
    ]
}
```

------

**Policy for destination bucket**

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "dth",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket",
                "s3:PutObjectAcl",
                "s3:AbortMultipartUpload",
                "s3:ListBucketMultipartUploads",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": [
                "arn:aws:s3:::<your-bucket-name>/*",
                "arn:aws:s3:::<your-bucket-name>"
            ]
        }
    ]
}
```

------

 To enable S3 Delete Event, you need to add "s3:DeleteObject" permission to the policy.

 Data Transfer Hub has native support for the S3 source bucket which enabled SSE-S3 and SSE-KMS. If your source bucket enabled *SSE-CMK*, please replace the source bucket policy with the policy [for S3 SSE-KMS](policy-for-s3-source-bucket-with-sse-cmk-enabled.md).

## Step 2: Create a user
<a name="step-2-create-a-user"></a>

1.  Open AWS Management Console.

1.  Choose IAM > User, and choose **Add User** to follow the wizard to create a user with credential.

1.  Specify a user name, for example, `dth-user`.

1.  For Access Type, select **Programmatic access** only and choose **Next: Permissions**.

1.  Select **Attach existing policies directly**, search and use the policy created in Step 1, and choose **Next: Tags**.

1.  Add tags if needed, and choose **Next: Review**.

1.  Review the user details, and choose **Create User**.

1.  Make sure you copied/saved the credential, and then choose **Close**.
![Success message for user creation with access key ID and secret access key displayed.](https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/user.png)
