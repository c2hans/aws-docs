---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsUploadObjects.html
---

# Upload an object to an S3 on Outposts bucket
<a name="S3OutpostsUploadObjects"></a>

Objects are the fundamental entities stored in Amazon S3 on Outposts. Every object is contained in a bucket. You must use access points to access any object in an Outpost bucket. When you specify the bucket for object operations, you use the access point Amazon Resource Name (ARN) or the access point alias. For more information about access point aliases, see [Using a bucket-style alias for your S3 on Outposts bucket access point](s3-outposts-access-points-alias.md).

The following example shows the ARN format for S3 on Outposts access points, which includes the AWS Region code for the Region that the Outpost is homed to, the AWS account ID, the Outpost ID, and the access point name:

```
arn:aws:s3-outposts:{{region}}:{{account-id}}:outpost/{{outpost-id}}/accesspoint/{{accesspoint-name}}
```

For more information about S3 on Outposts ARNs, see [Resource ARNs for S3 on Outposts](S3OutpostsIAM.md#S3OutpostsARN).

With Amazon S3 on Outposts, object data is always stored on the Outpost. When AWS installs an Outpost rack, your data stays local to your Outpost to meet data-residency requirements. Your objects never leave your Outpost and are not in an AWS Region. Because the AWS Management Console is hosted in-Region, you can't use the console to upload or manage objects in your Outpost. However, you can use the REST API, AWS Command Line Interface (AWS CLI), and AWS SDKs to upload and manage your objects through your access points.

The following AWS CLI and AWS SDK for Java examples show you how to upload an object to an S3 on Outposts bucket by using an access point.

------
#### [ AWS CLI ]

**Example**
The following example puts an object named `sample-object.xml` into an S3 on Outposts bucket (`s3-outposts:PutObject`) by using the AWS CLI. To use this command, replace each `{{user input placeholder}}` with your own information. For more information about this command, see [put-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html) in the *AWS CLI Reference*.

```
aws s3api put-object --bucket arn:aws:s3-outposts:{{Region}}:{{{{123456789012}}}}:outpost/{{op-01ac5d28a6a232904}}/accesspoint/{{example-outposts-access-point}} --key {{sample-object.xml}} --body {{sample-object.xml}}
```

------
#### [ SDK for Java ]

**Example**
For examples of how to upload an object to an S3 Outposts bucket with the AWS SDK for Java, see [PutObjectOnOutpost.java](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/outposts/PutObjectOnOutpost.java) in the *AWS SDK for Java 2.x Code Examples*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
