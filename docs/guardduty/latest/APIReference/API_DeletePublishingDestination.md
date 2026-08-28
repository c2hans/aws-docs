---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeletePublishingDestination.html
---

# DeletePublishingDestination
<a name="API_DeletePublishingDestination"></a>

Deletes the publishing definition with the specified `destinationId`.

## Request Syntax
<a name="API_DeletePublishingDestination_RequestSyntax"></a>

```
DELETE /detector/{{DetectorId}}/publishingDestination/{{DestinationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePublishingDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DestinationId](#API_DeletePublishingDestination_RequestSyntax) **   <a name="guardduty-DeletePublishingDestination-request-uri-DestinationId"></a>
The ID of the publishing destination to delete.
Required: Yes

 ** [DetectorId](#API_DeletePublishingDestination_RequestSyntax) **   <a name="guardduty-DeletePublishingDestination-request-uri-DetectorId"></a>
The unique ID of the detector associated with the publishing destination to delete.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_DeletePublishingDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePublishingDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeletePublishingDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePublishingDestination_Errors"></a>

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
<a name="API_DeletePublishingDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/DeletePublishingDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/DeletePublishingDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DeletePublishingDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/DeletePublishingDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DeletePublishingDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/DeletePublishingDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/DeletePublishingDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/DeletePublishingDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/DeletePublishingDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DeletePublishingDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
