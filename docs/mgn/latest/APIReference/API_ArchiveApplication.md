---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ArchiveApplication.html
---

# ArchiveApplication
<a name="API_ArchiveApplication"></a>

Archive application.

## Request Syntax
<a name="API_ArchiveApplication_RequestSyntax"></a>

```
POST /ArchiveApplication HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "applicationID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ArchiveApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ArchiveApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_ArchiveApplication_RequestSyntax) **   <a name="mgn-ArchiveApplication-request-accountID"></a>
Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [applicationID](#API_ArchiveApplication_RequestSyntax) **   <a name="mgn-ArchiveApplication-request-applicationID"></a>
Application ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `app-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_ArchiveApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationAggregatedStatus": {
      "healthStatus": "string",
      "lastUpdateDateTime": "string",
      "progressStatus": "string",
      "totalSourceServers": number
   },
   "applicationID": "string",
   "arn": "string",
   "creationDateTime": "string",
   "description": "string",
   "isArchived": boolean,
   "lastModifiedDateTime": "string",
   "name": "string",
   "tags": {
      "string" : "string"
   },
   "waveID": "string"
}
```

## Response Elements
<a name="API_ArchiveApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationAggregatedStatus](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-applicationAggregatedStatus"></a>
Application aggregated status.
Type: [ApplicationAggregatedStatus](API_ApplicationAggregatedStatus.md) object

 ** [applicationID](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-applicationID"></a>
Application ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `app-[0-9a-zA-Z]{17}`

 ** [arn](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-arn"></a>
Application ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [creationDateTime](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-creationDateTime"></a>
Application creation dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`

 ** [description](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-description"></a>
Application description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`

 ** [isArchived](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-isArchived"></a>
Application archival status.
Type: Boolean

 ** [lastModifiedDateTime](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-lastModifiedDateTime"></a>
Application last modified dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`

 ** [name](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-name"></a>
Application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`

 ** [tags](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-tags"></a>
Application tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [waveID](#API_ArchiveApplication_ResponseSyntax) **   <a name="mgn-ArchiveApplication-response-waveID"></a>
Application wave ID.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `wave-[0-9a-zA-Z]{17}`

## Errors
<a name="API_ArchiveApplication_Errors"></a>

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
The request could not be completed because its exceeded the service quota.
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

## See Also
<a name="API_ArchiveApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ArchiveApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ArchiveApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ArchiveApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ArchiveApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ArchiveApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ArchiveApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ArchiveApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ArchiveApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ArchiveApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ArchiveApplication)
