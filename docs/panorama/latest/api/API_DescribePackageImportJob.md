---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_DescribePackageImportJob.html
---

# DescribePackageImportJob
<a name="API_DescribePackageImportJob"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns information about a package import job.

## Request Syntax
<a name="API_DescribePackageImportJob_RequestSyntax"></a>

```
GET /packages/import-jobs/{{JobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePackageImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobId](#API_DescribePackageImportJob_RequestSyntax) **   <a name="panorama-DescribePackageImportJob-request-uri-JobId"></a>
The job's ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

## Request Body
<a name="API_DescribePackageImportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePackageImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ClientToken": "string",
   "CreatedTime": number,
   "InputConfig": {
      "PackageVersionInputConfig": {
         "S3Location": {
            "BucketName": "string",
            "ObjectKey": "string",
            "Region": "string"
         }
      }
   },
   "JobId": "string",
   "JobTags": [
      {
         "ResourceType": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ],
   "JobType": "string",
   "LastUpdatedTime": number,
   "Output": {
      "OutputS3Location": {
         "BucketName": "string",
         "ObjectKey": "string"
      },
      "PackageId": "string",
      "PackageVersion": "string",
      "PatchVersion": "string"
   },
   "OutputConfig": {
      "PackageVersionOutputConfig": {
         "MarkLatest": boolean,
         "PackageName": "string",
         "PackageVersion": "string"
      }
   },
   "Status": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_DescribePackageImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientToken](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-ClientToken"></a>
The job's client token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [CreatedTime](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-CreatedTime"></a>
When the job was created.
Type: Timestamp

 ** [InputConfig](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-InputConfig"></a>
The job's input config.
Type: [PackageImportJobInputConfig](API_PackageImportJobInputConfig.md) object

 ** [JobId](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-JobId"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [JobTags](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-JobTags"></a>
The job's tags.
Type: Array of [JobResourceTags](API_JobResourceTags.md) objects

 ** [JobType](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-JobType"></a>
The job's type.
Type: String
Valid Values: `NODE_PACKAGE_VERSION | MARKETPLACE_NODE_PACKAGE_VERSION`

 ** [LastUpdatedTime](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-LastUpdatedTime"></a>
When the job was updated.
Type: Timestamp

 ** [Output](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-Output"></a>
The job's output.
Type: [PackageImportJobOutput](API_PackageImportJobOutput.md) object

 ** [OutputConfig](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-OutputConfig"></a>
The job's output config.
Type: [PackageImportJobOutputConfig](API_PackageImportJobOutputConfig.md) object

 ** [Status](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-Status"></a>
The job's status.
Type: String
Valid Values: `PENDING | SUCCEEDED | FAILED`

 ** [StatusMessage](#API_DescribePackageImportJob_ResponseSyntax) **   <a name="panorama-DescribePackageImportJob-response-StatusMessage"></a>
The job's status message.
Type: String

## Errors
<a name="API_DescribePackageImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** ConflictException **
The target resource is in use.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_DescribePackageImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/DescribePackageImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/DescribePackageImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/DescribePackageImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/DescribePackageImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/DescribePackageImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/DescribePackageImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/DescribePackageImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/DescribePackageImportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/DescribePackageImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/DescribePackageImportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
