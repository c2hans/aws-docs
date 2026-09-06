---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UsageReportSubscription.html
---

# UsageReportSubscription
<a name="API_UsageReportSubscription"></a>

Describes information about the usage report subscription.

## Contents
<a name="API_UsageReportSubscription_Contents"></a>

 ** LastGeneratedReportDate **   <a name="WorkSpacesApplications-Type-UsageReportSubscription-LastGeneratedReportDate"></a>
The time when the last usage report was generated.
Type: Timestamp
Required: No

 ** S3BucketName **   <a name="WorkSpacesApplications-Type-UsageReportSubscription-S3BucketName"></a>
The Amazon S3 bucket where generated reports are stored.
If you enabled on-instance session scripts and Amazon S3 logging for your session script configuration, WorkSpaces Applications created an S3 bucket to store the script output. The bucket is unique to your account and Region. When you enable usage reporting in this case, WorkSpaces Applications uses the same bucket to store your usage reports. If you haven't already enabled on-instance session scripts, when you enable usage reports, WorkSpaces Applications creates a new S3 bucket.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Schedule **   <a name="WorkSpacesApplications-Type-UsageReportSubscription-Schedule"></a>
The schedule for generating usage reports.
Type: String
Valid Values: `DAILY`
Required: No

 ** SubscriptionErrors **   <a name="WorkSpacesApplications-Type-UsageReportSubscription-SubscriptionErrors"></a>
The errors that were returned if usage reports couldn't be generated.
Type: Array of [LastReportGenerationExecutionError](API_LastReportGenerationExecutionError.md) objects
Required: No

## See Also
<a name="API_UsageReportSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UsageReportSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UsageReportSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UsageReportSubscription)
