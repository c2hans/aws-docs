---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteThreatEntitySet.html
---

# DeleteThreatEntitySet
<a name="API_DeleteThreatEntitySet"></a>

Deletes the threat entity set that is associated with the specified `threatEntitySetId`.

## Request Syntax
<a name="API_DeleteThreatEntitySet_RequestSyntax"></a>

```
DELETE /detector/{{DetectorId}}/threatentityset/{{ThreatEntitySetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteThreatEntitySet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_DeleteThreatEntitySet_RequestSyntax) **   <a name="guardduty-DeleteThreatEntitySet-request-uri-DetectorId"></a>
The unique ID of the detector associated with the threat entity set resource.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [ThreatEntitySetId](#API_DeleteThreatEntitySet_RequestSyntax) **   <a name="guardduty-DeleteThreatEntitySet-request-uri-ThreatEntitySetId"></a>
The unique ID that helps GuardDuty identify which threat entity set needs to be deleted.
Required: Yes

## Request Body
<a name="API_DeleteThreatEntitySet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteThreatEntitySet_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteThreatEntitySet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteThreatEntitySet_Errors"></a>

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
<a name="API_DeleteThreatEntitySet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/DeleteThreatEntitySet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/DeleteThreatEntitySet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DeleteThreatEntitySet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/DeleteThreatEntitySet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DeleteThreatEntitySet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/DeleteThreatEntitySet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/DeleteThreatEntitySet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/DeleteThreatEntitySet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/DeleteThreatEntitySet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DeleteThreatEntitySet)
