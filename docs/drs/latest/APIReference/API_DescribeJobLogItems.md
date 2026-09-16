---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeJobLogItems.html
---

# DescribeJobLogItems
<a name="API_DescribeJobLogItems"></a>

Retrieves a detailed Job log with pagination.

## Request Syntax
<a name="API_DescribeJobLogItems_RequestSyntax"></a>

```
POST /DescribeJobLogItems HTTP/1.1
Content-type: application/json

{
   "jobID": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeJobLogItems_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeJobLogItems_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobID](#API_DescribeJobLogItems_RequestSyntax) **   <a name="drs-DescribeJobLogItems-request-jobID"></a>
The ID of the Job for which Job log items will be retrieved.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `drsjob-[0-9a-zA-Z]{17}`
Required: Yes

 ** [maxResults](#API_DescribeJobLogItems_RequestSyntax) **   <a name="drs-DescribeJobLogItems-request-maxResults"></a>
Maximum number of Job log items to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_DescribeJobLogItems_RequestSyntax) **   <a name="drs-DescribeJobLogItems-request-nextToken"></a>
The token of the next Job log items to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeJobLogItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "event": "string",
         "eventData": {
            "attemptCount": number,
            "conversionProperties": {
               "dataTimestamp": "string",
               "forceUefi": boolean,
               "rootVolumeName": "string",
               "volumeToConversionMap": {
                  "string" : {
                     "string" : "string"
                  }
               },
               "volumeToProductCodes": {
                  "string" : [
                     {
                        "productCodeId": "string",
                        "productCodeMode": "string"
                     }
                  ]
               },
               "volumeToVolumeSize": {
                  "string" : number
               }
            },
            "conversionServerID": "string",
            "eventResourceData": { ... },
            "maxAttemptsCount": number,
            "rawError": "string",
            "sourceServerID": "string",
            "targetInstanceID": "string"
         },
         "logDateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeJobLogItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeJobLogItems_ResponseSyntax) **   <a name="drs-DescribeJobLogItems-response-items"></a>
An array of Job log items.
Type: Array of [JobLog](API_JobLog.md) objects

 ** [nextToken](#API_DescribeJobLogItems_ResponseSyntax) **   <a name="drs-DescribeJobLogItems-response-nextToken"></a>
The token of the next Job log items to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeJobLogItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeJobLogItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeJobLogItems)
