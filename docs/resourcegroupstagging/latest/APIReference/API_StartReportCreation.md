---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_StartReportCreation.html
---

# StartReportCreation
<a name="API_StartReportCreation"></a>

Generates a report that lists all tagged resources in the accounts across your organization and tells whether each resource is compliant with the effective tag policy. Compliance data is refreshed daily. The report is generated asynchronously.

The generated report is saved to the following location:

 `s3://amzn-s3-demo-bucket/AwsTagPolicies/o-exampleorgid/YYYY-MM-ddTHH:mm:ssZ/report.csv`

For more information about evaluating resource compliance with tag policies, including the required permissions, review [Permissions for evaluating organization-wide compliance](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-permissions-org) in the *Tagging AWS Resources and Tag Editor* user guide.

You can call this operation only from the organization's management account and from the us-east-1 Region.

If the account associated with the identity used to call `StartReportCreation` is different from the account that owns the Amazon S3 bucket, there must be a bucket policy attached to the bucket to provide access. For more information, review [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS Resources and Tag Editor* user guide.

## Request Syntax
<a name="API_StartReportCreation_RequestSyntax"></a>

```
{
   "S3Bucket": "{{string}}"
}
```

## Request Parameters
<a name="API_StartReportCreation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [S3Bucket](#API_StartReportCreation_RequestSyntax) **   <a name="resourcegrouptagging-StartReportCreation-request-S3Bucket"></a>
The name of the Amazon S3 bucket where the report will be stored; for example:
 `amzn-s3-demo-bucket`
For more information on S3 bucket requirements, including an example bucket policy, see the example Amazon S3 bucket policy on this page.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9.-]*`
Required: Yes

## Response Elements
<a name="API_StartReportCreation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartReportCreation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
The request failed because the target of the operation is currently being modified by a different request. Try again later.
HTTP Status Code: 400

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
<a name="API_StartReportCreation_Examples"></a>

### Example
<a name="API_StartReportCreation_Example_1"></a>

This example illustrates one usage of StartReportCreation.

#### Sample Request
<a name="API_StartReportCreation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 20
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.StartReportCreation
X-Amz-Date: 20191201T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS

{
    "S3Bucket": "amzn-s3-demo-bucket"
}
```

#### Sample Response
<a name="API_StartReportCreation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestID: d3cf21f0-26db-11e7-a532-75e05382c8b1
Content-Type: application/x-amz-json-1.1
Date: Sun, 1 Dec 2019 21:45:25 GMT

{}
```

## See Also
<a name="API_StartReportCreation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/StartReportCreation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/StartReportCreation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/StartReportCreation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/StartReportCreation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/StartReportCreation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/StartReportCreation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/StartReportCreation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/StartReportCreation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/StartReportCreation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/StartReportCreation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resourcegroupstagging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
