---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartImportFileEnrichment.html
---

# StartImportFileEnrichment
<a name="API_StartImportFileEnrichment"></a>

Starts an import file enrichment job to process and enrich network migration import files with additional metadata and IP assignment strategies.

## Request Syntax
<a name="API_StartImportFileEnrichment_RequestSyntax"></a>

```
POST /network-migration/StartImportFileEnrichment HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "ipAssignmentStrategy": "{{string}}",
   "s3BucketSource": {
      "s3Bucket": "{{string}}",
      "s3BucketOwner": "{{string}}",
      "s3Key": "{{string}}"
   },
   "s3BucketTarget": {
      "s3Bucket": "{{string}}",
      "s3BucketOwner": "{{string}}",
      "s3Key": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartImportFileEnrichment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartImportFileEnrichment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartImportFileEnrichment_RequestSyntax) **   <a name="mgn-StartImportFileEnrichment-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [ipAssignmentStrategy](#API_StartImportFileEnrichment_RequestSyntax) **   <a name="mgn-StartImportFileEnrichment-request-ipAssignmentStrategy"></a>
The IP assignment strategy to use when enriching the import file. Can be STATIC or DYNAMIC.
Type: String
Valid Values: `STATIC | DYNAMIC`
Required: No

 ** [s3BucketSource](#API_StartImportFileEnrichment_RequestSyntax) **   <a name="mgn-StartImportFileEnrichment-request-s3BucketSource"></a>
The S3 configuration specifying the source location of the import file to be enriched.
Type: [EnrichmentSourceS3Configuration](API_EnrichmentSourceS3Configuration.md) object
Required: Yes

 ** [s3BucketTarget](#API_StartImportFileEnrichment_RequestSyntax) **   <a name="mgn-StartImportFileEnrichment-request-s3BucketTarget"></a>
The S3 configuration specifying the target location where the enriched import file will be stored.
Type: [EnrichmentTargetS3Configuration](API_EnrichmentTargetS3Configuration.md) object
Required: Yes

## Response Syntax
<a name="API_StartImportFileEnrichment_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "jobID": "string"
}
```

## Response Elements
<a name="API_StartImportFileEnrichment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [jobID](#API_StartImportFileEnrichment_ResponseSyntax) **   <a name="mgn-StartImportFileEnrichment-response-jobID"></a>
The unique identifier of the import file enrichment job that was started.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_StartImportFileEnrichment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
The request could not be completed because it exceeded the service quota.
 ** quotaCode **
Exceeded the service quota code.
 ** quotaValue **
Exceeded the service quota value.
 ** resourceId **
Exceeded the service quota resource ID.
 ** resourceType **
Exceeded the service quota resource type.
 ** serviceCode **
Exceeded the service quota service code.
HTTP Status Code: 402

 ** ThrottlingException **
Reached throttling quota exception.
 ** quotaCode **
Reached throttling quota exception.
 ** retryAfterSeconds **
Reached throttling quota exception will retry after x seconds.
 ** serviceCode **
Reached throttling quota exception service code.
HTTP Status Code: 429

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_StartImportFileEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/StartImportFileEnrichment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/StartImportFileEnrichment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/StartImportFileEnrichment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/StartImportFileEnrichment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/StartImportFileEnrichment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/StartImportFileEnrichment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/StartImportFileEnrichment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/StartImportFileEnrichment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/StartImportFileEnrichment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/StartImportFileEnrichment)
