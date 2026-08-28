---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl.html
---

# GetEvidenceFileUploadUrl
<a name="API_GetEvidenceFileUploadUrl"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

Creates a presigned Amazon S3 URL that can be used to upload a file as manual evidence. For instructions on how to use this operation, see [Upload a file from your browser ](https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#how-to-upload-manual-evidence-files) in the * AWS Audit Manager User Guide*.

The following restrictions apply to this operation:
+ Maximum size of an individual evidence file: 100 MB
+ Number of daily manual evidence uploads per control: 100
+ Supported file formats: See [Supported file types for manual evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files) in the * AWS Audit Manager User Guide*

For more information about Audit Manager service restrictions, see [Quotas and restrictions for AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html).

## Request Syntax
<a name="API_GetEvidenceFileUploadUrl_RequestSyntax"></a>

```
GET /evidenceFileUploadUrl?fileName={{fileName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEvidenceFileUploadUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [fileName](#API_GetEvidenceFileUploadUrl_RequestSyntax) **   <a name="auditmanager-GetEvidenceFileUploadUrl-request-uri-fileName"></a>
The file that you want to upload. For a list of supported file formats, see [Supported file types for manual evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files) in the * AWS Audit Manager User Guide*.
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[^\/]*`
Required: Yes

## Request Body
<a name="API_GetEvidenceFileUploadUrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEvidenceFileUploadUrl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "evidenceFileName": "string",
   "uploadUrl": "string"
}
```

## Response Elements
<a name="API_GetEvidenceFileUploadUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [evidenceFileName](#API_GetEvidenceFileUploadUrl_ResponseSyntax) **   <a name="auditmanager-GetEvidenceFileUploadUrl-response-evidenceFileName"></a>
The name of the uploaded manual evidence file that the presigned URL was generated for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`

 ** [uploadUrl](#API_GetEvidenceFileUploadUrl_ResponseSyntax) **   <a name="auditmanager-GetEvidenceFileUploadUrl-response-uploadUrl"></a>
The presigned URL that was generated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`

## Errors
<a name="API_GetEvidenceFileUploadUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetEvidenceFileUploadUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetEvidenceFileUploadUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
