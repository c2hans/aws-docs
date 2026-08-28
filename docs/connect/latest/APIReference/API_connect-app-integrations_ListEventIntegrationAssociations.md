---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_ListEventIntegrationAssociations.html
---

# ListEventIntegrationAssociations
<a name="API_connect-app-integrations_ListEventIntegrationAssociations"></a>

Returns a paginated list of event integration associations in the account.

## Request Syntax
<a name="API_connect-app-integrations_ListEventIntegrationAssociations_RequestSyntax"></a>

```
GET /eventIntegrations/{{Name}}/associations?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-app-integrations_ListEventIntegrationAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_connect-app-integrations_ListEventIntegrationAssociations_RequestSyntax) **   <a name="connect-connect-app-integrations_ListEventIntegrationAssociations-request-uri-EventIntegrationName"></a>
The name of the event integration.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: Yes

 ** [MaxResults](#API_connect-app-integrations_ListEventIntegrationAssociations_RequestSyntax) **   <a name="connect-connect-app-integrations_ListEventIntegrationAssociations-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_connect-app-integrations_ListEventIntegrationAssociations_RequestSyntax) **   <a name="connect-connect-app-integrations_ListEventIntegrationAssociations-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Request Body
<a name="API_connect-app-integrations_ListEventIntegrationAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-app-integrations_ListEventIntegrationAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EventIntegrationAssociations": [
      {
         "ClientAssociationMetadata": {
            "string" : "string"
         },
         "ClientId": "string",
         "EventBridgeRuleName": "string",
         "EventIntegrationAssociationArn": "string",
         "EventIntegrationAssociationId": "string",
         "EventIntegrationName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-app-integrations_ListEventIntegrationAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventIntegrationAssociations](#API_connect-app-integrations_ListEventIntegrationAssociations_ResponseSyntax) **   <a name="connect-connect-app-integrations_ListEventIntegrationAssociations-response-EventIntegrationAssociations"></a>
The event integration associations.
Type: Array of [EventIntegrationAssociation](API_connect-app-integrations_EventIntegrationAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [NextToken](#API_connect-app-integrations_ListEventIntegrationAssociations_ResponseSyntax) **   <a name="connect-connect-app-integrations_ListEventIntegrationAssociations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Errors
<a name="API_connect-app-integrations_ListEventIntegrationAssociations_Errors"></a>

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
<a name="API_connect-app-integrations_ListEventIntegrationAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/ListEventIntegrationAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/ListEventIntegrationAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/ListEventIntegrationAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/ListEventIntegrationAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/ListEventIntegrationAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/ListEventIntegrationAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/ListEventIntegrationAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/ListEventIntegrationAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/ListEventIntegrationAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/ListEventIntegrationAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
