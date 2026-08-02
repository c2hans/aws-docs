---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImageUsageReport.html
---

# CreateImageUsageReport
<a name="API_CreateImageUsageReport"></a>

Creates a report that shows how your image is used across other AWS accounts. The report provides visibility into which accounts are using the specified image, and how many resources (EC2 instances or launch templates) are referencing it.

For more information, see [View your AMI usage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/your-ec2-ami-usage.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateImageUsageReport_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AccountId.N**
The AWS account IDs to include in the report. To include all accounts, omit this parameter.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure idempotency of the request.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the image to report on.
Type: String
Required: Yes

 **ResourceType.N**
The resource types to include in the report.
Type: Array of [ImageUsageResourceTypeRequest](API_ImageUsageResourceTypeRequest.md) objects
Required: Yes

 **TagSpecification.N**
The tags to apply to the report on creation. The `ResourceType` must be set to `image-usage-report`; any other value will cause the report creation to fail.
To tag a report after it has been created, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html).
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateImageUsageReport_ResponseElements"></a>

The following elements are returned by the service.

 **reportId**
The ID of the report.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateImageUsageReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateImageUsageReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateImageUsageReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateImageUsageReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateImageUsageReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateImageUsageReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateImageUsageReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateImageUsageReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateImageUsageReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateImageUsageReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateImageUsageReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateImageUsageReport)
