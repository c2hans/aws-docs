---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListDataIntegrationAssociations.html
---

# ListDataIntegrationAssociations
<a name="API_connect-app-integrations_ListDataIntegrationAssociations"></a>

Returns a paginated list of DataIntegration associations in the account.

**Note**
You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the [CreateDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html) API.

## Request Syntax
<a name="API_connect-app-integrations_ListDataIntegrationAssociations_RequestSyntax"></a>

```
GET /dataIntegrations/{{Identifier}}/associations?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-app-integrations_ListDataIntegrationAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_connect-app-integrations_ListDataIntegrationAssociations_RequestSyntax) **   <a name="connect-connect-app-integrations_ListDataIntegrationAssociations-request-uri-DataIntegrationIdentifier"></a>
A unique identifier for the DataIntegration.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: Yes

 ** [MaxResults](#API_connect-app-integrations_ListDataIntegrationAssociations_RequestSyntax) **   <a name="connect-connect-app-integrations_ListDataIntegrationAssociations-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_connect-app-integrations_ListDataIntegrationAssociations_RequestSyntax) **   <a name="connect-connect-app-integrations_ListDataIntegrationAssociations-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Request Body
<a name="API_connect-app-integrations_ListDataIntegrationAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-app-integrations_ListDataIntegrationAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataIntegrationAssociations": [
      {
         "ClientId": "string",
         "DataIntegrationArn": "string",
         "DataIntegrationAssociationArn": "string",
         "DestinationURI": "string",
         "ExecutionConfiguration": {
            "ExecutionMode": "string",
            "OnDemandConfiguration": {
               "EndTime": "string",
               "StartTime": "string"
            },
            "ScheduleConfiguration": {
               "FirstExecutionFrom": "string",
               "Object": "string",
               "ScheduleExpression": "string"
            }
         },
         "LastExecutionStatus": {
            "ExecutionStatus": "string",
            "StatusMessage": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-app-integrations_ListDataIntegrationAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataIntegrationAssociations](#API_connect-app-integrations_ListDataIntegrationAssociations_ResponseSyntax) **   <a name="connect-connect-app-integrations_ListDataIntegrationAssociations-response-DataIntegrationAssociations"></a>
The Amazon Resource Name (ARN) and unique ID of the DataIntegration association.
Type: Array of [DataIntegrationAssociationSummary](API_connect-app-integrations_DataIntegrationAssociationSummary.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [NextToken](#API_connect-app-integrations_ListDataIntegrationAssociations_ResponseSyntax) **   <a name="connect-connect-app-integrations_ListDataIntegrationAssociations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Errors
<a name="API_connect-app-integrations_ListDataIntegrationAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceError **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_connect-app-integrations_ListDataIntegrationAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/ListDataIntegrationAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/ListDataIntegrationAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/ListDataIntegrationAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/ListDataIntegrationAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/ListDataIntegrationAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/ListDataIntegrationAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/ListDataIntegrationAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/ListDataIntegrationAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/ListDataIntegrationAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/ListDataIntegrationAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
