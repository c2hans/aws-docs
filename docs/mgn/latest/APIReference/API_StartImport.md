---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartImport.html
---

# StartImport
<a name="API_StartImport"></a>

Start import.

## Request Syntax
<a name="API_StartImport_RequestSyntax"></a>

```
POST /StartImport HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "s3BucketSource": {
      "s3Bucket": "{{string}}",
      "s3BucketOwner": "{{string}}",
      "s3Key": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartImport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartImport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartImport_RequestSyntax) **   <a name="mgn-StartImport-request-clientToken"></a>
Start import request client token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [s3BucketSource](#API_StartImport_RequestSyntax) **   <a name="mgn-StartImport-request-s3BucketSource"></a>
Start import request s3 bucket source.
Type: [S3BucketSource](API_S3BucketSource.md) object
Required: Yes

 ** [tags](#API_StartImport_RequestSyntax) **   <a name="mgn-StartImport-request-tags"></a>
Start import request tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartImport_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "importTask": {
      "arn": "string",
      "creationDateTime": "string",
      "endDateTime": "string",
      "importID": "string",
      "progressPercentage": number,
      "s3BucketSource": {
         "s3Bucket": "string",
         "s3BucketOwner": "string",
         "s3Key": "string"
      },
      "status": "string",
      "summary": {
         "applications": {
            "createdCount": number,
            "modifiedCount": number
         },
         "servers": {
            "createdCount": number,
            "modifiedCount": number
         },
         "waves": {
            "createdCount": number,
            "modifiedCount": number
         }
      },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_StartImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [importTask](#API_StartImport_ResponseSyntax) **   <a name="mgn-StartImport-response-importTask"></a>
Start import response import task.
Type: [ImportTask](API_ImportTask.md) object

## Errors
<a name="API_StartImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

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
<a name="API_StartImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/StartImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/StartImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/StartImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/StartImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/StartImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/StartImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/StartImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/StartImport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/StartImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/StartImport)
