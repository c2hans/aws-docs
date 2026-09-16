---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateThreatEntitySet.html
---

# UpdateThreatEntitySet
<a name="API_UpdateThreatEntitySet"></a>

Updates the threat entity set associated with the specified `threatEntitySetId`.

## Request Syntax
<a name="API_UpdateThreatEntitySet_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/threatentityset/{{ThreatEntitySetId}} HTTP/1.1
Content-type: application/json

{
   "activate": {{boolean}},
   "expectedBucketOwner": "{{string}}",
   "location": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateThreatEntitySet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_UpdateThreatEntitySet_RequestSyntax) **   <a name="guardduty-UpdateThreatEntitySet-request-uri-DetectorId"></a>
The unique ID of the GuardDuty detector associated with the threat entity set that you want to update.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [ThreatEntitySetId](#API_UpdateThreatEntitySet_RequestSyntax) **   <a name="guardduty-UpdateThreatEntitySet-request-uri-ThreatEntitySetId"></a>
The ID returned by GuardDuty after updating the threat entity set resource.
Required: Yes

## Request Body
<a name="API_UpdateThreatEntitySet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [activate](#API_UpdateThreatEntitySet_RequestSyntax) **   <a name="guardduty-UpdateThreatEntitySet-request-activate"></a>
A boolean value that indicates whether GuardDuty is to start using this updated threat entity set. After you update an entity set, you will need to activate it again. It might take up to 15 minutes for the updated entity set to be effective.
Type: Boolean
Required: No

 ** [expectedBucketOwner](#API_UpdateThreatEntitySet_RequestSyntax) **   <a name="guardduty-UpdateThreatEntitySet-request-expectedBucketOwner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the **location** parameter.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** [location](#API_UpdateThreatEntitySet_RequestSyntax) **   <a name="guardduty-UpdateThreatEntitySet-request-location"></a>
The URI of the file that contains the trusted entity set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** [name](#API_UpdateThreatEntitySet_RequestSyntax) **   <a name="guardduty-UpdateThreatEntitySet-request-name"></a>
A user-friendly name to identify the trusted entity set.
The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (\_).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## Response Syntax
<a name="API_UpdateThreatEntitySet_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateThreatEntitySet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateThreatEntitySet_Errors"></a>

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
<a name="API_UpdateThreatEntitySet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/UpdateThreatEntitySet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/UpdateThreatEntitySet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdateThreatEntitySet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/UpdateThreatEntitySet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdateThreatEntitySet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/UpdateThreatEntitySet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/UpdateThreatEntitySet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/UpdateThreatEntitySet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/UpdateThreatEntitySet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdateThreatEntitySet)
