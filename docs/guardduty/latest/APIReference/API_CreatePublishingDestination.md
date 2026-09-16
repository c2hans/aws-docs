---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreatePublishingDestination.html
---

# CreatePublishingDestination
<a name="API_CreatePublishingDestination"></a>

Creates a publishing destination where you can export your GuardDuty findings. Before you start exporting the findings, the destination resource must exist.

## Request Syntax
<a name="API_CreatePublishingDestination_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/publishingDestination HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "destinationProperties": {
      "destinationArn": "{{string}}",
      "kmsKeyArn": "{{string}}"
   },
   "destinationType": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePublishingDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_CreatePublishingDestination_RequestSyntax) **   <a name="guardduty-CreatePublishingDestination-request-uri-DetectorId"></a>
The ID of the GuardDuty detector associated with the publishing destination.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_CreatePublishingDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreatePublishingDestination_RequestSyntax) **   <a name="guardduty-CreatePublishingDestination-request-clientToken"></a>
The idempotency token for the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [destinationProperties](#API_CreatePublishingDestination_RequestSyntax) **   <a name="guardduty-CreatePublishingDestination-request-destinationProperties"></a>
The properties of the publishing destination, including the ARNs for the destination and the KMS key used for encryption.
Type: [DestinationProperties](API_DestinationProperties.md) object
Required: Yes

 ** [destinationType](#API_CreatePublishingDestination_RequestSyntax) **   <a name="guardduty-CreatePublishingDestination-request-destinationType"></a>
The type of resource for the publishing destination. Currently only Amazon S3 buckets are supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `S3`
Required: Yes

 ** [tags](#API_CreatePublishingDestination_RequestSyntax) **   <a name="guardduty-CreatePublishingDestination-request-tags"></a>
The tags to be added to a new publishing destination resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePublishingDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "destinationId": "string"
}
```

## Response Elements
<a name="API_CreatePublishingDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinationId](#API_CreatePublishingDestination_ResponseSyntax) **   <a name="guardduty-CreatePublishingDestination-response-destinationId"></a>
The ID of the publishing destination that is created.
Type: String

## Errors
<a name="API_CreatePublishingDestination_Errors"></a>

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
<a name="API_CreatePublishingDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/CreatePublishingDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/CreatePublishingDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CreatePublishingDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/CreatePublishingDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CreatePublishingDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/CreatePublishingDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/CreatePublishingDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/CreatePublishingDestination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/CreatePublishingDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CreatePublishingDestination)
