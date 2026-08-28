---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshotReturnCode.html
---

# DeleteSnapshotReturnCode
<a name="API_DeleteSnapshotReturnCode"></a>

The snapshot ID and its deletion result code.

## Contents
<a name="API_DeleteSnapshotReturnCode_Contents"></a>

 ** returnCode **
The result code from the snapshot deletion attempt. Possible values:
+  `success` - The snapshot was successfully deleted.
+  `skipped` - The snapshot was not deleted because it's associated with other AMIs.
+  `missing-permissions` - The snapshot was not deleted because the role lacks `DeleteSnapshot` permissions. For more information, see [How Amazon EBS works with IAM](https://docs.aws.amazon.com/ebs/latest/userguide/security_iam_service-with-iam.html).
+  `internal-error` - The snapshot was not deleted due to a server error.
+  `client-error` - The snapshot was not deleted due to a client configuration error.
For details about an error, check the `DeleteSnapshot` event in the CloudTrail event history. For more information, see [View event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-event-history.html) in the * AWS CloudTrail User Guide*.
Type: String
Valid Values: `success | skipped | missing-permissions | internal-error | client-error`
Required: No

 ** snapshotId **
The ID of the snapshot.
Type: String
Required: No

## See Also
<a name="API_DeleteSnapshotReturnCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteSnapshotReturnCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteSnapshotReturnCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteSnapshotReturnCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
