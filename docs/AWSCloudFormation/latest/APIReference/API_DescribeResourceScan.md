---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeResourceScan.html
---

# DescribeResourceScan
<a name="API_DescribeResourceScan"></a>

Describes details of a resource scan.

## Request Parameters
<a name="API_DescribeResourceScan_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceScanId **
The Amazon Resource Name (ARN) of the resource scan.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeResourceScan_ResponseElements"></a>

The following elements are returned by the service.

 ** EndTime **
The time that the resource scan was finished.
Type: Timestamp

 ** PercentageCompleted **
The percentage of the resource scan that has been completed.
Type: Double

 ** ResourceScanId **
The Amazon Resource Name (ARN) of the resource scan. The format is `arn:${Partition}:cloudformation:${Region}:${Account}:resourceScan/${Id}`. An example is `arn:aws:cloudformation:us-east-1:123456789012:resourceScan/f5b490f7-7ed4-428a-aa06-31ff25db0772 `.
Type: String

 ** ResourcesRead **
The number of resources that were read. This is only available for scans with a `Status` set to `COMPLETE`, `EXPIRED`, or `FAILED`.
This field may be 0 if the resource scan failed with a `ResourceScanLimitExceededException`.
Type: Integer

 ** ResourcesScanned **
The number of resources that were listed. This is only available for scans with a `Status` set to `COMPLETE`, `EXPIRED`, or `FAILED `.
Type: Integer

 **ResourceTypes.member.N**
The list of resource types for the specified scan. Resource types are only available for scans with a `Status` set to `COMPLETE` or `FAILED `.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.

 **ScanFilters.member.N**
The scan filters that were used.
Type: Array of [ScanFilter](API_ScanFilter.md) objects
Array Members: Fixed number of 1 item.

 ** StartTime **
The time that the resource scan was started.
Type: Timestamp

 ** Status **
Status of the resource scan.
 **IN\_PROGRESS**
The resource scan is still in progress.
 **COMPLETE**
The resource scan is complete.
 **EXPIRED**
The resource scan has expired.
 **FAILED**
The resource scan has failed.
Type: String
Valid Values: `IN_PROGRESS | FAILED | COMPLETE | EXPIRED`

 ** StatusReason **
The reason for the resource scan status, providing more information if a failure happened.
Type: String

## Errors
<a name="API_DescribeResourceScan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceScanNotFound **
The resource scan was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeResourceScan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeResourceScan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/DescribeResourceScan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeResourceScan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeResourceScan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeResourceScan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeResourceScan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeResourceScan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeResourceScan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeResourceScan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeResourceScan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
