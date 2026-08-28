---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListLineageNodeHistory.html
---

# ListLineageNodeHistory
<a name="API_ListLineageNodeHistory"></a>

Lists the history of the specified data lineage node.

## Request Syntax
<a name="API_ListLineageNodeHistory_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/lineage/nodes/{{identifier}}/history?direction={{direction}}&maxResults={{maxResults}}&nextToken={{nextToken}}&sortOrder={{sortOrder}}&timestampGTE={{eventTimestampGTE}}&timestampLTE={{eventTimestampLTE}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLineageNodeHistory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [direction](#API_ListLineageNodeHistory_RequestSyntax) **   <a name="datazone-ListLineageNodeHistory-request-uri-direction"></a>
The direction of the data lineage node refers to the lineage node having neighbors in that direction. For example, if direction is `UPSTREAM`, the `ListLineageNodeHistory` API responds with historical versions with upstream neighbors only.
Valid Values: `UPSTREAM | DOWNSTREAM`

 ** [domainIdentifier](#API_ListLineageNodeHistory_RequestSyntax) **   <a name="datazone-ListLineageNodeHistory-request-uri-domainIdentifier"></a>
The ID of the domain where you want to list the history of the specified data lineage node.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [eventTimestampGTE](#API_ListLineageNodeHistory_RequestSyntax) **   <a name="datazone-ListLineageNodeHistory-request-uri-eventTimestampGTE"></a>
Specifies whether the action is to return data lineage node history from the time after the event timestamp.

 ** [eventTimestampLTE](#API_ListLineageNodeHistory_RequestSyntax) **   <a name="datazone-ListLineageNodeHistory-request-uri-eventTimestampLTE"></a>
Specifies whether the action is to return data lineage node history from the time prior of the event timestamp.

 ** [identifier](#API_ListLineageNodeHistory_RequestSyntax) **   <a name="datazone-ListLineageNodeHistory-request-uri-identifier"></a>
The ID of the data lineage node whose history you want to list.
Length Constraints: Minimum length of 1. Maximum length of 2086.
Required: Yes

 ** [maxResults](#API_ListLineageNodeHistory_RequestSyntax) **   <a name="datazone-ListLineageNodeHistory-request-uri-maxResults"></a>
The maximum number of history items to return in a single call to ListLineageNodeHistory. When the number of memberships to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListLineageNodeHistory to list the next set of items.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListLineageNodeHistory_RequestSyntax) **   <a name="datazone-ListLineageNodeHistory-request-uri-nextToken"></a>
When the number of history items is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of items, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageNodeHistory to list the next set of items.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [sortOrder](#API_ListLineageNodeHistory_RequestSyntax) **   <a name="datazone-ListLineageNodeHistory-request-uri-sortOrder"></a>
The order by which you want data lineage node history to be sorted.
Valid Values: `ASCENDING | DESCENDING`

## Request Body
<a name="API_ListLineageNodeHistory_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLineageNodeHistory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "nodes": [
      {
         "createdAt": number,
         "createdBy": "string",
         "description": "string",
         "domainId": "string",
         "eventTimestamp": number,
         "id": "string",
         "name": "string",
         "sourceIdentifier": "string",
         "typeName": "string",
         "typeRevision": "string",
         "updatedAt": number,
         "updatedBy": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListLineageNodeHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListLineageNodeHistory_ResponseSyntax) **   <a name="datazone-ListLineageNodeHistory-response-nextToken"></a>
When the number of history items is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of items, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageNodeHistory to list the next set of items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [nodes](#API_ListLineageNodeHistory_ResponseSyntax) **   <a name="datazone-ListLineageNodeHistory-response-nodes"></a>
The nodes returned by the ListLineageNodeHistory action.
Type: Array of [LineageNodeSummary](API_LineageNodeSummary.md) objects

## Errors
<a name="API_ListLineageNodeHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

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
<a name="API_ListLineageNodeHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListLineageNodeHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListLineageNodeHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListLineageNodeHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListLineageNodeHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListLineageNodeHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListLineageNodeHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListLineageNodeHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListLineageNodeHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListLineageNodeHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListLineageNodeHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
