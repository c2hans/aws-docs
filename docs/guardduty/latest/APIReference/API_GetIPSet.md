---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetIPSet.html
---

# GetIPSet
<a name="API_GetIPSet"></a>

Retrieves the IPSet specified by the `ipSetId`.

## Request Syntax
<a name="API_GetIPSet_RequestSyntax"></a>

```
GET /detector/{{DetectorId}}/ipset/{{IpSetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIPSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetIPSet_RequestSyntax) **   <a name="guardduty-GetIPSet-request-uri-DetectorId"></a>
The unique ID of the detector that is associated with the IPSet.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [IpSetId](#API_GetIPSet_RequestSyntax) **   <a name="guardduty-GetIPSet-request-uri-IpSetId"></a>
The unique ID of the IPSet to retrieve.
Required: Yes

## Request Body
<a name="API_GetIPSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIPSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "expectedBucketOwner": "string",
   "format": "string",
   "location": "string",
   "name": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetIPSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [expectedBucketOwner](#API_GetIPSet_ResponseSyntax) **   <a name="guardduty-GetIPSet-response-expectedBucketOwner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the **location** parameter. This field appears in the response only if it was provided during IPSet creation or update.
Type: String
Length Constraints: Fixed length of 12.

 ** [format](#API_GetIPSet_ResponseSyntax) **   <a name="guardduty-GetIPSet-response-format"></a>
The format of the file that contains the IPSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `TXT | STIX | OTX_CSV | ALIEN_VAULT | PROOF_POINT | FIRE_EYE`

 ** [location](#API_GetIPSet_ResponseSyntax) **   <a name="guardduty-GetIPSet-response-location"></a>
The URI of the file that contains the IPSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [name](#API_GetIPSet_ResponseSyntax) **   <a name="guardduty-GetIPSet-response-name"></a>
The user-friendly name for the IPSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [status](#API_GetIPSet_ResponseSyntax) **   <a name="guardduty-GetIPSet-response-status"></a>
The status of IPSet file that was uploaded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `INACTIVE | ACTIVATING | ACTIVE | DEACTIVATING | ERROR | DELETE_PENDING | DELETED`

 ** [tags](#API_GetIPSet_ResponseSyntax) **   <a name="guardduty-GetIPSet-response-tags"></a>
The tags of the IPSet resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetIPSet_Errors"></a>

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
<a name="API_GetIPSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetIPSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetIPSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetIPSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetIPSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetIPSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetIPSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetIPSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetIPSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetIPSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetIPSet)
