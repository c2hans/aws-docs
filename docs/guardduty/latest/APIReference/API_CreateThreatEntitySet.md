---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateThreatEntitySet.html
---

# CreateThreatEntitySet
<a name="API_CreateThreatEntitySet"></a>

Creates a new threat entity set. In a threat entity set, you can provide known malicious threat entities for your AWS environment. GuardDuty generates findings based on the entries in the threat entity sets. Only users of the administrator account can manage entity sets, which automatically apply to member accounts.

## Request Syntax
<a name="API_CreateThreatEntitySet_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/threatentityset HTTP/1.1
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
<a name="API_CreateThreatEntitySet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_CreateThreatEntitySet_RequestSyntax) **   <a name="guardduty-CreateThreatEntitySet-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty account for which you want to create a threat entity set.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_CreateThreatEntitySet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [activate](#API_CreateThreatEntitySet_RequestSyntax) **   <a name="guardduty-CreateThreatEntitySet-request-activate"></a>
A boolean value that indicates whether GuardDuty should start using the uploaded threat entity set to generate findings.
Type: Boolean
Required: Yes

 ** [clientToken](#API_CreateThreatEntitySet_RequestSyntax) **   <a name="guardduty-CreateThreatEntitySet-request-clientToken"></a>
The idempotency token for the create request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [expectedBucketOwner](#API_CreateThreatEntitySet_RequestSyntax) **   <a name="guardduty-CreateThreatEntitySet-request-expectedBucketOwner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the **location** parameter.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** [format](#API_CreateThreatEntitySet_RequestSyntax) **   <a name="guardduty-CreateThreatEntitySet-request-format"></a>
The format of the file that contains the threat entity set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `TXT | STIX | OTX_CSV | ALIEN_VAULT | PROOF_POINT | FIRE_EYE`
Required: Yes

 ** [location](#API_CreateThreatEntitySet_RequestSyntax) **   <a name="guardduty-CreateThreatEntitySet-request-location"></a>
The URI of the file that contains the threat entity set. The format of the `Location` URL must be a valid Amazon S3 URL format. Invalid URL formats will result in an error, regardless of whether you activate the entity set or not. For more information about format of the location URLs, see [Format of location URL under Step 2: Adding trusted or threat intelligence data](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-create-activate.html) in the *Amazon GuardDuty User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [name](#API_CreateThreatEntitySet_RequestSyntax) **   <a name="guardduty-CreateThreatEntitySet-request-name"></a>
A user-friendly name to identify the threat entity set.
The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [tags](#API_CreateThreatEntitySet_RequestSyntax) **   <a name="guardduty-CreateThreatEntitySet-request-tags"></a>
The tags to be added to a new threat entity set resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateThreatEntitySet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "threatEntitySetId": "string"
}
```

## Response Elements
<a name="API_CreateThreatEntitySet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [threatEntitySetId](#API_CreateThreatEntitySet_ResponseSyntax) **   <a name="guardduty-CreateThreatEntitySet-response-threatEntitySetId"></a>
The ID returned by GuardDuty after creation of the threat entity set resource.
Type: String

## Errors
<a name="API_CreateThreatEntitySet_Errors"></a>

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
<a name="API_CreateThreatEntitySet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/CreateThreatEntitySet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/CreateThreatEntitySet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CreateThreatEntitySet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/CreateThreatEntitySet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CreateThreatEntitySet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/CreateThreatEntitySet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/CreateThreatEntitySet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/CreateThreatEntitySet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/CreateThreatEntitySet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CreateThreatEntitySet)
