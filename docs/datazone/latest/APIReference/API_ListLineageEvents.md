---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListLineageEvents.html
---

# ListLineageEvents
<a name="API_ListLineageEvents"></a>

Lists lineage events.

## Request Syntax
<a name="API_ListLineageEvents_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/lineage/events?maxResults={{maxResults}}&nextToken={{nextToken}}&processingStatus={{processingStatus}}&sortOrder={{sortOrder}}&timestampAfter={{timestampAfter}}&timestampBefore={{timestampBefore}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLineageEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListLineageEvents_RequestSyntax) **   <a name="datazone-ListLineageEvents-request-uri-domainIdentifier"></a>
The ID of the domain where you want to list lineage events.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListLineageEvents_RequestSyntax) **   <a name="datazone-ListLineageEvents-request-uri-maxResults"></a>
The maximum number of lineage events to return in a single call to ListLineageEvents. When the number of lineage events to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListLineageEvents to list the next set of lineage events.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListLineageEvents_RequestSyntax) **   <a name="datazone-ListLineageEvents-request-uri-nextToken"></a>
When the number of lineage events is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of lineage events, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageEvents to list the next set of lineage events.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [processingStatus](#API_ListLineageEvents_RequestSyntax) **   <a name="datazone-ListLineageEvents-request-uri-processingStatus"></a>
The processing status of a lineage event.
Valid Values: `REQUESTED | PROCESSING | SUCCESS | FAILED`

 ** [sortOrder](#API_ListLineageEvents_RequestSyntax) **   <a name="datazone-ListLineageEvents-request-uri-sortOrder"></a>
The sort order of the lineage events.
Valid Values: `ASCENDING | DESCENDING`

 ** [timestampAfter](#API_ListLineageEvents_RequestSyntax) **   <a name="datazone-ListLineageEvents-request-uri-timestampAfter"></a>
The after timestamp of a lineage event.

 ** [timestampBefore](#API_ListLineageEvents_RequestSyntax) **   <a name="datazone-ListLineageEvents-request-uri-timestampBefore"></a>
The before timestamp of a lineage event.

## Request Body
<a name="API_ListLineageEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLineageEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": number,
         "createdBy": "string",
         "domainId": "string",
         "eventSummary": { ... },
         "eventTime": number,
         "id": "string",
         "processingStatus": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLineageEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListLineageEvents_ResponseSyntax) **   <a name="datazone-ListLineageEvents-response-items"></a>
The results of the ListLineageEvents action.
Type: Array of [LineageEventSummary](API_LineageEventSummary.md) objects

 ** [nextToken](#API_ListLineageEvents_ResponseSyntax) **   <a name="datazone-ListLineageEvents-response-nextToken"></a>
When the number of lineage events is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of lineage events, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageEvents to list the next set of lineage events.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListLineageEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListLineageEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListLineageEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListLineageEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListLineageEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListLineageEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListLineageEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListLineageEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListLineageEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListLineageEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListLineageEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListLineageEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
