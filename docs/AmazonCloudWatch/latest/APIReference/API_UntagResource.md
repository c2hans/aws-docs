---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes one or more tags from the specified resource. Currently, alarms, dashboards, metric streams and Contributor Insights rules support tagging.

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

 ** ResourceARN **
The ARN of the CloudWatch resource that you're removing tags from.
The ARN format of an alarm is `arn:aws:cloudwatch:Region:account-id:alarm:alarm-name `
The ARN format of a Contributor Insights rule is `arn:aws:cloudwatch:Region:account-id:insight-rule/insight-rule-name `
The ARN format of a dashboard is `arn:aws:cloudwatch::account-id:dashboard/dashboard-name `
The ARN format of a metric stream is `arn:aws:cloudwatch:Region:account-id:metric-stream/metric-stream-name `
For more information about ARN format, see [ Resource Types Defined by Amazon CloudWatch](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies) in the *Amazon Web Services General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** TagKeys **
The list of tag keys to remove from the resource.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
More than one process tried to modify a resource at the same time.
HTTP Status Code: 429

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 409

 ** InternalServiceError **
Request processing has failed due to some unknown error, exception, or failure.
 ** Message **

HTTP Status Code: 500

 ** InvalidParameterValue **
The value of an input parameter is bad or out-of-range.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/UntagResource)
