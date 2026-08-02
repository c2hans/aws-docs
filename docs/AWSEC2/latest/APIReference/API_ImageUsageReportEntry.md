---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageUsageReportEntry.html
---

# ImageUsageReportEntry
<a name="API_ImageUsageReportEntry"></a>

A single entry in an image usage report, detailing how an image is being used by a specific AWS account and resource type.

## Contents
<a name="API_ImageUsageReportEntry_Contents"></a>

 ** accountId **
The ID of the account that uses the image.
Type: String
Required: No

 ** imageId **
The ID of the image.
Type: String
Required: No

 ** reportCreationTime **
The date and time the report creation was initiated.
Type: Timestamp
Required: No

 ** reportId **
The ID of the report.
Type: String
Required: No

 ** resourceType **
The type of resource (`ec2:Instance` or `ec2:LaunchTemplate`).
Type: String
Required: No

 ** usageCount **
The number of times resources of this type reference this image in the account.
Type: Long
Required: No

## See Also
<a name="API_ImageUsageReportEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageUsageReportEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageUsageReportEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageUsageReportEntry)
