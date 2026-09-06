---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_UnarchiveWave.html
---

# UnarchiveWave
<a name="API_UnarchiveWave"></a>

Unarchive wave.

## Request Syntax
<a name="API_UnarchiveWave_RequestSyntax"></a>

```
POST /UnarchiveWave HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "waveID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UnarchiveWave_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UnarchiveWave_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_UnarchiveWave_RequestSyntax) **   <a name="mgn-UnarchiveWave-request-accountID"></a>
Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [waveID](#API_UnarchiveWave_RequestSyntax) **   <a name="mgn-UnarchiveWave-request-waveID"></a>
Wave ID.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `wave-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_UnarchiveWave_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UnarchiveWave_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UnarchiveWave_ResponseSyntax) **   <a name="mgn-UnarchiveWave-response-arn"></a>
Wave ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [creationDateTime](#API_UnarchiveWave_ResponseSyntax) **   <a name="mgn-UnarchiveWave-response-creationDateTime"></a>
Wave creation dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`

 ** [description](#API_UnarchiveWave_ResponseSyntax) **   <a name="mgn-UnarchiveWave-response-description"></a>
Wave description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`

 ** [isArchived](#API_UnarchiveWave_ResponseSyntax) **   <a name="mgn-UnarchiveWave-response-isArchived"></a>
Wave archival status.
Type: Boolean

 ** [lastModifiedDateTime](#API_UnarchiveWave_ResponseSyntax) **   <a name="mgn-UnarchiveWave-response-lastModifiedDateTime"></a>
Wave last modified dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`

 ** [name](#API_UnarchiveWave_ResponseSyntax) **   <a name="mgn-UnarchiveWave-response-name"></a>
Wave name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`

 ** [tags](#API_UnarchiveWave_ResponseSyntax) **   <a name="mgn-UnarchiveWave-response-tags"></a>
Wave tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [waveAggregatedStatus](#API_UnarchiveWave_ResponseSyntax) **   <a name="mgn-UnarchiveWave-response-waveAggregatedStatus"></a>
Wave aggregated status.
Type: [WaveAggregatedStatus](API_WaveAggregatedStatus.md) object

 ** [waveID](#API_UnarchiveWave_ResponseSyntax) **   <a name="mgn-UnarchiveWave-response-waveID"></a>
Wave ID.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `wave-[0-9a-zA-Z]{17}`

## Errors
<a name="API_UnarchiveWave_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_UnarchiveWave_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/UnarchiveWave)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/UnarchiveWave)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/UnarchiveWave)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/UnarchiveWave)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/UnarchiveWave)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/UnarchiveWave)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/UnarchiveWave)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/UnarchiveWave)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/UnarchiveWave)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/UnarchiveWave)
