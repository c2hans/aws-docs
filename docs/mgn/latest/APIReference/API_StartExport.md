---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartExport.html
---

# StartExport
<a name="API_StartExport"></a>

Start export.

## Request Syntax
<a name="API_StartExport_RequestSyntax"></a>

```
POST /StartExport HTTP/1.1
Content-type: application/json

{
   "s3Bucket": "{{string}}",
   "s3BucketOwner": "{{string}}",
   "s3Key": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartExport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartExport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [s3Bucket](#API_StartExport_RequestSyntax) **   <a name="mgn-StartExport-request-s3Bucket"></a>
Start export request s3 bucket.
Type: String
Pattern: `[a-zA-Z0-9.\-_]{1,255}`
Required: Yes

 ** [s3BucketOwner](#API_StartExport_RequestSyntax) **   <a name="mgn-StartExport-request-s3BucketOwner"></a>
Start export request s3 bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [s3Key](#API_StartExport_RequestSyntax) **   <a name="mgn-StartExport-request-s3Key"></a>
Start export request s3key.
Type: String
Pattern: `[^\x00]{1,1020}\.csv`
Required: Yes

 ** [tags](#API_StartExport_RequestSyntax) **   <a name="mgn-StartExport-request-tags"></a>
Start export request tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartExport_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "exportTask": {
      "arn": "string",
      "creationDateTime": "string",
      "endDateTime": "string",
      "exportID": "string",
      "progressPercentage": number,
      "s3Bucket": "string",
      "s3BucketOwner": "string",
      "s3Key": "string",
      "status": "string",
      "summary": {
         "applicationsCount": number,
         "serversCount": number,
         "wavesCount": number
      },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_StartExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [exportTask](#API_StartExport_ResponseSyntax) **   <a name="mgn-StartExport-response-exportTask"></a>
Start export response export task.
Type: [ExportTask](API_ExportTask.md) object

## Errors
<a name="API_StartExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_StartExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/StartExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/StartExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/StartExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/StartExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/StartExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/StartExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/StartExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/StartExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/StartExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/StartExport)
