---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateWave.html
---

# CreateWave
<a name="API_CreateWave"></a>

Create wave.

## Request Syntax
<a name="API_CreateWave_RequestSyntax"></a>

```
POST /CreateWave HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateWave_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWave_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_CreateWave_RequestSyntax) **   <a name="mgn-CreateWave-request-accountID"></a>
Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [description](#API_CreateWave_RequestSyntax) **   <a name="mgn-CreateWave-request-description"></a>
Wave description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`
Required: No

 ** [name](#API_CreateWave_RequestSyntax) **   <a name="mgn-CreateWave-request-name"></a>
Wave name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`
Required: Yes

 ** [tags](#API_CreateWave_RequestSyntax) **   <a name="mgn-CreateWave-request-tags"></a>
Wave tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateWave_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "creationDateTime": "string",
   "description": "string",
   "isArchived": boolean,
   "lastModifiedDateTime": "string",
   "name": "string",
   "tags": {
      "string" : "string"
   },
   "waveAggregatedStatus": {
      "healthStatus": "string",
      "lastUpdateDateTime": "string",
      "progressStatus": "string",
      "replicationStartedDateTime": "string",
      "totalApplications": number
   },
   "waveID": "string"
}
```

## Response Elements
<a name="API_CreateWave_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateWave_ResponseSyntax) **   <a name="mgn-CreateWave-response-arn"></a>
Wave ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [creationDateTime](#API_CreateWave_ResponseSyntax) **   <a name="mgn-CreateWave-response-creationDateTime"></a>
Wave creation dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`

 ** [description](#API_CreateWave_ResponseSyntax) **   <a name="mgn-CreateWave-response-description"></a>
Wave description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`

 ** [isArchived](#API_CreateWave_ResponseSyntax) **   <a name="mgn-CreateWave-response-isArchived"></a>
Wave archival status.
Type: Boolean

 ** [lastModifiedDateTime](#API_CreateWave_ResponseSyntax) **   <a name="mgn-CreateWave-response-lastModifiedDateTime"></a>
Wave last modified dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`

 ** [name](#API_CreateWave_ResponseSyntax) **   <a name="mgn-CreateWave-response-name"></a>
Wave name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`

 ** [tags](#API_CreateWave_ResponseSyntax) **   <a name="mgn-CreateWave-response-tags"></a>
Wave tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [waveAggregatedStatus](#API_CreateWave_ResponseSyntax) **   <a name="mgn-CreateWave-response-waveAggregatedStatus"></a>
Wave aggregated status.
Type: [WaveAggregatedStatus](API_WaveAggregatedStatus.md) object

 ** [waveID](#API_CreateWave_ResponseSyntax) **   <a name="mgn-CreateWave-response-waveID"></a>
Wave ID.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `wave-[0-9a-zA-Z]{17}`

## Errors
<a name="API_CreateWave_Errors"></a>

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

## See Also
<a name="API_CreateWave_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/CreateWave)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/CreateWave)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/CreateWave)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/CreateWave)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/CreateWave)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/CreateWave)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/CreateWave)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/CreateWave)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/CreateWave)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/CreateWave)
