---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_S3Action.html
---

# S3Action
<a name="API_S3Action"></a>

Describes an action to write data to an Amazon S3 bucket.

## Contents
<a name="API_S3Action_Contents"></a>

 ** bucketName **   <a name="iot-Type-S3Action-bucketName"></a>
The Amazon S3 bucket.
Type: String
Required: Yes

 ** key **   <a name="iot-Type-S3Action-key"></a>
The object key. For more information, see [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html).
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-S3Action-roleArn"></a>
The ARN of the IAM role that grants access.
Type: String
Required: Yes

 ** cannedAcl **   <a name="iot-Type-S3Action-cannedAcl"></a>
The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see [S3 canned ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl).
Type: String
Valid Values: `private | public-read | public-read-write | aws-exec-read | authenticated-read | bucket-owner-read | bucket-owner-full-control | log-delivery-write`
Required: No

## See Also
<a name="API_S3Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/S3Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/S3Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/S3Action)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
