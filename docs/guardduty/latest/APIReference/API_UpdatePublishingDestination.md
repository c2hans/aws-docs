---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdatePublishingDestination.html
---

# UpdatePublishingDestination
<a name="API_UpdatePublishingDestination"></a>

Updates information about the publishing destination specified by the `destinationId`.

## Request Syntax
<a name="API_UpdatePublishingDestination_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/publishingDestination/{{DestinationId}} HTTP/1.1
Content-type: application/json

{
   "destinationProperties": {
      "destinationArn": "{{string}}",
      "kmsKeyArn": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdatePublishingDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DestinationId](#API_UpdatePublishingDestination_RequestSyntax) **   <a name="guardduty-UpdatePublishingDestination-request-uri-DestinationId"></a>
The ID of the publishing destination to update.
Required: Yes

 ** [DetectorId](#API_UpdatePublishingDestination_RequestSyntax) **   <a name="guardduty-UpdatePublishingDestination-request-uri-DetectorId"></a>
The ID of the detector associated with the publishing destinations to update.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_UpdatePublishingDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationProperties](#API_UpdatePublishingDestination_RequestSyntax) **   <a name="guardduty-UpdatePublishingDestination-request-destinationProperties"></a>
A `DestinationProperties` object that includes the `DestinationArn` and `KmsKeyArn` of the publishing destination.
Type: [DestinationProperties](API_DestinationProperties.md) object
Required: No

## Response Syntax
<a name="API_UpdatePublishingDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdatePublishingDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdatePublishingDestination_Errors"></a>

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
<a name="API_UpdatePublishingDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/UpdatePublishingDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/UpdatePublishingDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdatePublishingDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/UpdatePublishingDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdatePublishingDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/UpdatePublishingDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/UpdatePublishingDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/UpdatePublishingDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/UpdatePublishingDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdatePublishingDestination)
