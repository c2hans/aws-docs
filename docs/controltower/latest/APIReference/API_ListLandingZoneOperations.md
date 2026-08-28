---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZoneOperations.html
---

# ListLandingZoneOperations
<a name="API_ListLandingZoneOperations"></a>

Lists all landing zone operations from the past 90 days. Results are sorted by time, with the most recent operation first.

## Request Syntax
<a name="API_ListLandingZoneOperations_RequestSyntax"></a>

```
POST /list-landingzone-operations HTTP/1.1
Content-type: application/json

{
   "filter": {
      "statuses": [ "{{string}}" ],
      "types": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListLandingZoneOperations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLandingZoneOperations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListLandingZoneOperations_RequestSyntax) **   <a name="controltower-ListLandingZoneOperations-request-filter"></a>
An input filter for the `ListLandingZoneOperations` API that lets you select the types of landing zone operations to view.
Type: [LandingZoneOperationFilter](API_LandingZoneOperationFilter.md) object
Required: No

 ** [maxResults](#API_ListLandingZoneOperations_RequestSyntax) **   <a name="controltower-ListLandingZoneOperations-request-maxResults"></a>
How many results to return per API call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListLandingZoneOperations_RequestSyntax) **   <a name="controltower-ListLandingZoneOperations-request-nextToken"></a>
The token to continue the list from a previous API call with the same parameters.
Type: String
Required: No

## Response Syntax
<a name="API_ListLandingZoneOperations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "landingZoneOperations": [
      {
         "operationIdentifier": "string",
         "operationType": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLandingZoneOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [landingZoneOperations](#API_ListLandingZoneOperations_ResponseSyntax) **   <a name="controltower-ListLandingZoneOperations-response-landingZoneOperations"></a>
Lists landing zone operations.
Type: Array of [LandingZoneOperationSummary](API_LandingZoneOperationSummary.md) objects

 ** [nextToken](#API_ListLandingZoneOperations_ResponseSyntax) **   <a name="controltower-ListLandingZoneOperations-response-nextToken"></a>
Retrieves the next page of results. If the string is empty, the response is the end of the results.
Type: String

## Errors
<a name="API_ListLandingZoneOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListLandingZoneOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/ListLandingZoneOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/ListLandingZoneOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ListLandingZoneOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/ListLandingZoneOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ListLandingZoneOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/ListLandingZoneOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/ListLandingZoneOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/ListLandingZoneOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListLandingZoneOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ListLandingZoneOperations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
