---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListPublishingDestinations.html
---

# ListPublishingDestinations
<a name="API_ListPublishingDestinations"></a>

Returns a list of publishing destinations associated with the specified `detectorId`.

## Request Syntax
<a name="API_ListPublishingDestinations_RequestSyntax"></a>

```
GET /detector/{{DetectorId}}/publishingDestination?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPublishingDestinations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_ListPublishingDestinations_RequestSyntax) **   <a name="guardduty-ListPublishingDestinations-request-uri-DetectorId"></a>
The detector ID for which you want to retrieve the publishing destination.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [MaxResults](#API_ListPublishingDestinations_RequestSyntax) **   <a name="guardduty-ListPublishingDestinations-request-uri-MaxResults"></a>
The maximum number of results to return in the response.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListPublishingDestinations_RequestSyntax) **   <a name="guardduty-ListPublishingDestinations-request-uri-NextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.

## Request Body
<a name="API_ListPublishingDestinations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPublishingDestinations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "destinations": [
      {
         "destinationId": "string",
         "destinationType": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPublishingDestinations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinations](#API_ListPublishingDestinations_ResponseSyntax) **   <a name="guardduty-ListPublishingDestinations-response-destinations"></a>
A `Destinations` object that includes information about each publishing destination returned.
Type: Array of [Destination](API_Destination.md) objects

 ** [nextToken](#API_ListPublishingDestinations_ResponseSyntax) **   <a name="guardduty-ListPublishingDestinations-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Type: String

## Errors
<a name="API_ListPublishingDestinations_Errors"></a>

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
<a name="API_ListPublishingDestinations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListPublishingDestinations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListPublishingDestinations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListPublishingDestinations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListPublishingDestinations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListPublishingDestinations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListPublishingDestinations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListPublishingDestinations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListPublishingDestinations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListPublishingDestinations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListPublishingDestinations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
