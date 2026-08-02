---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-pipeline.html
---

# Understanding Amazon Chime SDK media pipeline creation
<a name="create-pipeline"></a>

You follow a multi-step process to create an Amazon Chime SDK media pipeline, and you can create several types of pipelines. The following list outlines the creation process and provide links to more information about creating the various types of pipelines.
+ Create an Amazon S3 bucket. You must create the bucket in the same AWS Region as the meeting. For more information, refer to [Creating an Amazon S3 bucket for Amazon Chime SDK media capture pipelines](create-s3-bucket.md).
+ Create a service-linked role named `AWSServiceRoleForAmazonChimeSDKMediaPipelines`. This allows media pipelines to access meetings on your behalf. For more information, refer to [Creating a service-linked role for Amazon Chime SDK media pipelines](create-pipeline-role.md).
+ Create an IAM role with sufficient permission to interact with the [ Amazon Chime SDK media pipeline APIs ](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Media_Pipelines.html). To create that role, we recommend adding the [AmazonChimeSDK](https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-chime-sdk) managed policy from the IAM console. The policy contains the necessary APIs.

  Your IAM role must also have permission to call the Amazon S3 [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html) API on all resources. The following example shows a typical policy for doing so.

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Action": "s3:GetBucketPolicy",
              "Effect": "Allow",
              "Resource": "*"
          }
      ]
  }
  ```

------

Once you have those items, see these topics for information on creating pipelines.
+ [Creating media capture pipelines for Amazon Chime SDK meetings](capture-pipe-config.md)
+ [Creating media concatenation pipelines for Amazon Chime SDK meetings](create-concat-pipe.md)
+ [Creating media live connector pipelines for Amazon Chime SDK meetings](connector-pipe-config.md)
+ [Creating media stream pipelines using the Amazon Chime SDK](create-media-stream-pipeline.md)
