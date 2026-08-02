---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateIPSet.html
---

# CreateIPSet
<a name="API_CreateIPSet"></a>

Creates a new IPSet, which is called a trusted IP list in the console user interface. An IPSet is a list of IP addresses that are trusted for secure communication with AWS infrastructure and applications. GuardDuty doesn't generate findings for IP addresses that are included in IPSets. Only users from the administrator account can use this operation.

## Request Syntax
<a name="API_CreateIPSet_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/ipset HTTP/1.1
Content-type: application/json

{
   "activate": {{boolean}},
   "clientToken": "{{string}}",
   "expectedBucketOwner": "{{string}}",
   "format": "{{string}}",
   "location": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateIPSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_CreateIPSet_RequestSyntax) **   <a name="guardduty-CreateIPSet-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty account for which you want to create an IPSet.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_CreateIPSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [activate](#API_CreateIPSet_RequestSyntax) **   <a name="guardduty-CreateIPSet-request-activate"></a>
A Boolean value that indicates whether GuardDuty is to start using the uploaded IPSet.
Type: Boolean
Required: Yes

 ** [clientToken](#API_CreateIPSet_RequestSyntax) **   <a name="guardduty-CreateIPSet-request-clientToken"></a>
The idempotency token for the create request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [expectedBucketOwner](#API_CreateIPSet_RequestSyntax) **   <a name="guardduty-CreateIPSet-request-expectedBucketOwner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the **location** parameter.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** [format](#API_CreateIPSet_RequestSyntax) **   <a name="guardduty-CreateIPSet-request-format"></a>
The format of the file that contains the IPSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `TXT | STIX | OTX_CSV | ALIEN_VAULT | PROOF_POINT | FIRE_EYE`
Required: Yes

 ** [location](#API_CreateIPSet_RequestSyntax) **   <a name="guardduty-CreateIPSet-request-location"></a>
The URI of the file that contains the IPSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [name](#API_CreateIPSet_RequestSyntax) **   <a name="guardduty-CreateIPSet-request-name"></a>
The user-friendly name to identify the IPSet.
 Allowed characters are alphanumeric, whitespace, dash (-), and underscores (\_).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [tags](#API_CreateIPSet_RequestSyntax) **   <a name="guardduty-CreateIPSet-request-tags"></a>
The tags to be added to a new IP set resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateIPSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ipSetId": "string"
}
```

## Response Elements
<a name="API_CreateIPSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ipSetId](#API_CreateIPSet_ResponseSyntax) **   <a name="guardduty-CreateIPSet-response-ipSetId"></a>
The ID of the IPSet resource.
Type: String

## Errors
<a name="API_CreateIPSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An access denied exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 403

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
<a name="API_CreateIPSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/CreateIPSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/CreateIPSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CreateIPSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/CreateIPSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CreateIPSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/CreateIPSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/CreateIPSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/CreateIPSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/CreateIPSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CreateIPSet)
