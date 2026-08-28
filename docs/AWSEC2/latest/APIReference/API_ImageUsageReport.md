---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageUsageReport.html
---

# ImageUsageReport
<a name="API_ImageUsageReport"></a>

The configuration and status of an image usage report.

## Contents
<a name="API_ImageUsageReport_Contents"></a>

 ** AccountIdSet.N **
The IDs of the AWS accounts that were specified when the report was created.
Type: Array of strings
Required: No

 ** creationTime **
The date and time when the report was created.
Type: Timestamp
Required: No

 ** expirationTime **
The date and time when Amazon EC2 will delete the report (30 days after the report was created).
Type: Timestamp
Required: No

 ** imageId **
The ID of the image that was specified when the report was created.
Type: String
Required: No

 ** reportId **
The ID of the report.
Type: String
Required: No

 ** ResourceTypeSet.N **
The resource types that were specified when the report was created.
Type: Array of [ImageUsageResourceType](API_ImageUsageResourceType.md) objects
Required: No

 ** state **
The current state of the report. Possible values:
+  `available` - The report is available to view.
+  `pending` - The report is being created and not available to view.
+  `error` - The report could not be created.
Type: String
Required: No

 ** stateReason **
Provides additional details when the report is in an `error` state.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the report.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ImageUsageReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageUsageReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageUsageReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageUsageReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
