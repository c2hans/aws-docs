---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribePublishingDestination.html
---

# DescribePublishingDestination
<a name="API_DescribePublishingDestination"></a>

Returns information about the publishing destination specified by the provided `destinationId`.

## Request Syntax
<a name="API_DescribePublishingDestination_RequestSyntax"></a>

```
GET /detector/{{DetectorId}}/publishingDestination/{{DestinationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePublishingDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DestinationId](#API_DescribePublishingDestination_RequestSyntax) **   <a name="guardduty-DescribePublishingDestination-request-uri-DestinationId"></a>
The ID of the publishing destination to retrieve.
Required: Yes

 ** [DetectorId](#API_DescribePublishingDestination_RequestSyntax) **   <a name="guardduty-DescribePublishingDestination-request-uri-DetectorId"></a>
The unique ID of the detector associated with the publishing destination to retrieve.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_DescribePublishingDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePublishingDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "destinationId": "string",
   "destinationProperties": {
      "destinationArn": "string",
      "kmsKeyArn": "string"
   },
   "destinationType": "string",
   "publishingFailureStartTimestamp": number,
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DescribePublishingDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinationId](#API_DescribePublishingDestination_ResponseSyntax) **   <a name="guardduty-DescribePublishingDestination-response-destinationId"></a>
The ID of the publishing destination.
Type: String

 ** [destinationProperties](#API_DescribePublishingDestination_ResponseSyntax) **   <a name="guardduty-DescribePublishingDestination-response-destinationProperties"></a>
A `DestinationProperties` object that includes the `DestinationArn` and `KmsKeyArn` of the publishing destination.
Type: [DestinationProperties](API_DestinationProperties.md) object

 ** [destinationType](#API_DescribePublishingDestination_ResponseSyntax) **   <a name="guardduty-DescribePublishingDestination-response-destinationType"></a>
The type of publishing destination. Currently, only Amazon S3 buckets are supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `S3`

 ** [publishingFailureStartTimestamp](#API_DescribePublishingDestination_ResponseSyntax) **   <a name="guardduty-DescribePublishingDestination-response-publishingFailureStartTimestamp"></a>
The time, in epoch millisecond format, at which GuardDuty was first unable to publish findings to the destination.
Type: Long

 ** [status](#API_DescribePublishingDestination_ResponseSyntax) **   <a name="guardduty-DescribePublishingDestination-response-status"></a>
The status of the publishing destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `PENDING_VERIFICATION | PUBLISHING | UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY | STOPPED`

 ** [tags](#API_DescribePublishingDestination_ResponseSyntax) **   <a name="guardduty-DescribePublishingDestination-response-tags"></a>
The tags of the publishing destination resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_DescribePublishingDestination_Errors"></a>

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
<a name="API_DescribePublishingDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/DescribePublishingDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/DescribePublishingDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DescribePublishingDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/DescribePublishingDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DescribePublishingDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/DescribePublishingDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/DescribePublishingDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/DescribePublishingDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/DescribePublishingDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DescribePublishingDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
