---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetTrustedEntitySet.html
---

# GetTrustedEntitySet
<a name="API_GetTrustedEntitySet"></a>

Retrieves the trusted entity set associated with the specified `trustedEntitySetId`.

## Request Syntax
<a name="API_GetTrustedEntitySet_RequestSyntax"></a>

```
GET /detector/{{DetectorId}}/trustedentityset/{{TrustedEntitySetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTrustedEntitySet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetTrustedEntitySet_RequestSyntax) **   <a name="guardduty-GetTrustedEntitySet-request-uri-DetectorId"></a>
The unique ID of the GuardDuty detector associated with this trusted entity set.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [TrustedEntitySetId](#API_GetTrustedEntitySet_RequestSyntax) **   <a name="guardduty-GetTrustedEntitySet-request-uri-TrustedEntitySetId"></a>
The unique ID that helps GuardDuty identify the trusted entity set.
Required: Yes

## Request Body
<a name="API_GetTrustedEntitySet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTrustedEntitySet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "errorDetails": "string",
   "expectedBucketOwner": "string",
   "format": "string",
   "location": "string",
   "name": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetTrustedEntitySet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-GetTrustedEntitySet-response-createdAt"></a>
The timestamp when the associated trusted entity set was created.
Type: Timestamp

 ** [errorDetails](#API_GetTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-GetTrustedEntitySet-response-errorDetails"></a>
The error details when the status is shown as `ERROR`.
Type: String

 ** [expectedBucketOwner](#API_GetTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-GetTrustedEntitySet-response-expectedBucketOwner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the **location** parameter.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`

 ** [format](#API_GetTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-GetTrustedEntitySet-response-format"></a>
The format of the file that contains the trusted entity set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `TXT | STIX | OTX_CSV | ALIEN_VAULT | PROOF_POINT | FIRE_EYE`

 ** [location](#API_GetTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-GetTrustedEntitySet-response-location"></a>
The URI of the file that contains the trusted entity set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [name](#API_GetTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-GetTrustedEntitySet-response-name"></a>
The name of the threat entity set associated with the specified `trustedEntitySetId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [status](#API_GetTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-GetTrustedEntitySet-response-status"></a>
The status of the associated trusted entity set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `INACTIVE | ACTIVATING | ACTIVE | DEACTIVATING | ERROR | DELETE_PENDING | DELETED`

 ** [tags](#API_GetTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-GetTrustedEntitySet-response-tags"></a>
The tags associated with trusted entity set resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updatedAt](#API_GetTrustedEntitySet_ResponseSyntax) **   <a name="guardduty-GetTrustedEntitySet-response-updatedAt"></a>
The timestamp when the associated trusted entity set was updated.
Type: Timestamp

## Errors
<a name="API_GetTrustedEntitySet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_GetTrustedEntitySet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetTrustedEntitySet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetTrustedEntitySet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetTrustedEntitySet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetTrustedEntitySet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetTrustedEntitySet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetTrustedEntitySet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetTrustedEntitySet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetTrustedEntitySet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetTrustedEntitySet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetTrustedEntitySet)
