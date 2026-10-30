---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetFixture.html
---

# GetFixture
<a name="API_GetFixture"></a>

Retrieves information about the specified fixture (a sports event, such as a specific basketball game). You obtain a fixtureId from SearchFixtures, or from the clipping output of a feed.

## Request Syntax
<a name="API_GetFixture_RequestSyntax"></a>

```
GET /v1/fixtures/{{fixtureId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFixture_RequestParameters"></a>

The request uses the following URI parameters.

 ** [fixtureId](#API_GetFixture_RequestSyntax) **   <a name="elementalinference-GetFixture-request-uri-fixtureId"></a>
The ID of the fixture to retrieve, as returned by SearchFixtures.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_GetFixture_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFixture_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "competitors": [
      {
         "isHome": boolean,
         "name": "string"
      }
   ],
   "fixtureGroup": "string",
   "fixtureId": "string",
   "name": "string",
   "scheduledStart": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetFixture_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [competitors](#API_GetFixture_ResponseSyntax) **   <a name="elementalinference-GetFixture-response-competitors"></a>
An array of the competitors (the teams or individuals) in the fixture.
Type: Array of [Competitor](API_Competitor.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.

 ** [fixtureGroup](#API_GetFixture_ResponseSyntax) **   <a name="elementalinference-GetFixture-response-fixtureGroup"></a>
The group that the fixture belongs to, such as the competition, league, or tournament. The data source doesn't provide this information for every fixture.
Type: String

 ** [fixtureId](#API_GetFixture_ResponseSyntax) **   <a name="elementalinference-GetFixture-response-fixtureId"></a>
The ID that you specified in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [name](#API_GetFixture_ResponseSyntax) **   <a name="elementalinference-GetFixture-response-name"></a>
The name of the fixture, as provided by the data source. For example, the names of the two competing teams.
Type: String

 ** [scheduledStart](#API_GetFixture_ResponseSyntax) **   <a name="elementalinference-GetFixture-response-scheduledStart"></a>
The scheduled start time of the fixture, as provided by the data source. The actual start time might differ.
Type: Timestamp

 ** [status](#API_GetFixture_ResponseSyntax) **   <a name="elementalinference-GetFixture-response-status"></a>
The status of the fixture in its lifecycle, as provided by the data source. For example, Scheduled or Completed.
Type: String

## Errors
<a name="API_GetFixture_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** GatewayTimedOutException **
The request timed out before the service returned a response. This is a temporary condition. Retry the request. If the problem persists, contact AWS Support.
HTTP Status Code: 504

 ** InternalServerErrorException **
An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the action doesn't exist.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unable to handle the request. Retry the request. If the problem persists, contact AWS Support.
HTTP Status Code: 503

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying.
HTTP Status Code: 400

## See Also
<a name="API_GetFixture_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/GetFixture)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/GetFixture)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/GetFixture)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/GetFixture)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/GetFixture)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/GetFixture)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/GetFixture)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/GetFixture)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/GetFixture)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/GetFixture)
