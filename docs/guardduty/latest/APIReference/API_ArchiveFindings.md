---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ArchiveFindings.html
---

# ArchiveFindings
<a name="API_ArchiveFindings"></a>

Archives GuardDuty findings that are specified by the list of finding IDs.

**Note**
Only the administrator account can archive findings. Member accounts don't have permission to archive findings from their accounts.

## Request Syntax
<a name="API_ArchiveFindings_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/findings/archive HTTP/1.1
Content-type: application/json

{
   "findingIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ArchiveFindings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_ArchiveFindings_RequestSyntax) **   <a name="guardduty-ArchiveFindings-request-uri-DetectorId"></a>
The ID of the detector that specifies the GuardDuty service whose findings you want to archive.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_ArchiveFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [findingIds](#API_ArchiveFindings_RequestSyntax) **   <a name="guardduty-ArchiveFindings-request-findingIds"></a>
The IDs of the findings that you want to archive.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_ArchiveFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ArchiveFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ArchiveFindings_Errors"></a>

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
<a name="API_ArchiveFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ArchiveFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ArchiveFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ArchiveFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ArchiveFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ArchiveFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ArchiveFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ArchiveFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ArchiveFindings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ArchiveFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ArchiveFindings)
