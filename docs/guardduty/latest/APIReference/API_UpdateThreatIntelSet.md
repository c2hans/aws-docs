---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateThreatIntelSet.html
---

# UpdateThreatIntelSet
<a name="API_UpdateThreatIntelSet"></a>

Updates the ThreatIntelSet specified by the ThreatIntelSet ID.

## Request Syntax
<a name="API_UpdateThreatIntelSet_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/threatintelset/{{ThreatIntelSetId}} HTTP/1.1
Content-type: application/json

{
   "activate": {{boolean}},
   "expectedBucketOwner": "{{string}}",
   "location": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateThreatIntelSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_UpdateThreatIntelSet_RequestSyntax) **   <a name="guardduty-UpdateThreatIntelSet-request-uri-DetectorId"></a>
The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to update.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [ThreatIntelSetId](#API_UpdateThreatIntelSet_RequestSyntax) **   <a name="guardduty-UpdateThreatIntelSet-request-uri-ThreatIntelSetId"></a>
The unique ID that specifies the ThreatIntelSet that you want to update.
Required: Yes

## Request Body
<a name="API_UpdateThreatIntelSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [activate](#API_UpdateThreatIntelSet_RequestSyntax) **   <a name="guardduty-UpdateThreatIntelSet-request-activate"></a>
The updated Boolean value that specifies whether the ThreateIntelSet is active or not.
Type: Boolean
Required: No

 ** [expectedBucketOwner](#API_UpdateThreatIntelSet_RequestSyntax) **   <a name="guardduty-UpdateThreatIntelSet-request-expectedBucketOwner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the **location** parameter.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** [location](#API_UpdateThreatIntelSet_RequestSyntax) **   <a name="guardduty-UpdateThreatIntelSet-request-location"></a>
The updated URI of the file that contains the ThreateIntelSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** [name](#API_UpdateThreatIntelSet_RequestSyntax) **   <a name="guardduty-UpdateThreatIntelSet-request-name"></a>
The unique ID that specifies the ThreatIntelSet that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## Response Syntax
<a name="API_UpdateThreatIntelSet_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateThreatIntelSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateThreatIntelSet_Errors"></a>

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
<a name="API_UpdateThreatIntelSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/UpdateThreatIntelSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/UpdateThreatIntelSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdateThreatIntelSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/UpdateThreatIntelSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdateThreatIntelSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/UpdateThreatIntelSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/UpdateThreatIntelSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/UpdateThreatIntelSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/UpdateThreatIntelSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdateThreatIntelSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
