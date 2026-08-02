---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.html
---

# DescribeReportCreation
<a name="API_DescribeReportCreation"></a>

Describes the status of the `StartReportCreation` operation.

You can call this operation only from the organization's management account and from the us-east-1 Region.

## Response Syntax
<a name="API_DescribeReportCreation_ResponseSyntax"></a>

```
{
   "ErrorMessage": "string",
   "S3Location": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeReportCreation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ErrorMessage](#API_DescribeReportCreation_ResponseSyntax) **   <a name="resourcegrouptagging-DescribeReportCreation-response-ErrorMessage"></a>
Details of the common errors that all operations return.
Type: String

 ** [S3Location](#API_DescribeReportCreation_ResponseSyntax) **   <a name="resourcegrouptagging-DescribeReportCreation-response-S3Location"></a>
The path to the Amazon S3 bucket where the report was stored on creation.
Type: String

 ** [Status](#API_DescribeReportCreation_ResponseSyntax) **   <a name="resourcegrouptagging-DescribeReportCreation-response-Status"></a>
Reports the status of the operation.
The operation status can be one of the following:
+  `RUNNING` - Report creation is in progress.
+  `SUCCEEDED` - Report creation is complete. You can open the report from the Amazon S3 bucket that you specified when you ran `StartReportCreation`.
+  `FAILED` - Report creation timed out or the Amazon S3 bucket is not accessible.
+  `NO REPORT` - No report was generated in the last 90 days.
Type: String

## Errors
<a name="API_DescribeReportCreation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConstraintViolationException **
The request failed because performing the operation would violate a constraint.
Some of the reasons in the following list might not apply to this specific operation.
+ You must meet the prerequisites for using tag policies. For information, see [Prerequisites and permissions](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-prereqs) in the *Tagging AWS resources and Tag Editor* user guide.
+ You must enable the tag policies service principal (`tagpolicies.tag.amazonaws.com`) to integrate with AWS Organizations For information, see [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html).
+ You must have a tag policy attached to the organization root, an OU, or an account.
HTTP Status Code: 400

 ** InternalServiceException **
The request processing failed because of an unknown error, exception, or failure. You can retry the request.
HTTP Status Code: 500

 ** InvalidParameterException **
The request failed because of one of the following reasons:
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide.
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** ThrottledException **
The request failed because it exceeded the allowed frequency of submitted requests.
HTTP Status Code: 400

## Examples
<a name="API_DescribeReportCreation_Examples"></a>

### Example
<a name="API_DescribeReportCreation_Example_1"></a>

This example illustrates one usage of DescribeReportCreation.

#### Sample Request
<a name="API_DescribeReportCreation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 20
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.DescribeReportCreation
X-Amz-Date: 20191201T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS

{}
```

#### Sample Response
<a name="API_DescribeReportCreation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestID: d3cf21f0-26db-11e7-a532-75e05382c8b1
Content-Type: application/x-amz-json-1.1
Date: Sun, 1 Dec 2019 21:45:25 GMT

{
    "ErrorMessage":null,
    "S3Location":"s3://amzn-s3-demo-bucket/AwsTagPolicies/o-exampleorgid/2019-12-01-T21:45:24Z/report.csv",
    "Status":"SUCCEEDED"
}
```

## See Also
<a name="API_DescribeReportCreation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/DescribeReportCreation)
