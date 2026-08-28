---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListIntegrationAssociations.html
---

# ListIntegrationAssociations
<a name="API_ListIntegrationAssociations"></a>

Provides summary information about the AWS resource associations for the specified Connect Customer instance.

## Request Syntax
<a name="API_ListIntegrationAssociations_RequestSyntax"></a>

```
GET /instance/{{InstanceId}}/integration-associations?integrationArn={{IntegrationArn}}&integrationType={{IntegrationType}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIntegrationAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListIntegrationAssociations_RequestSyntax) **   <a name="connect-ListIntegrationAssociations-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [IntegrationArn](#API_ListIntegrationAssociations_RequestSyntax) **   <a name="connect-ListIntegrationAssociations-request-uri-IntegrationArn"></a>
The Amazon Resource Name (ARN) of the integration.

 ** [IntegrationType](#API_ListIntegrationAssociations_RequestSyntax) **   <a name="connect-ListIntegrationAssociations-request-uri-IntegrationType"></a>
The integration type.
Valid Values: `EVENT | VOICE_ID | PINPOINT_APP | WISDOM_ASSISTANT | WISDOM_KNOWLEDGE_BASE | WISDOM_QUICK_RESPONSES | Q_MESSAGE_TEMPLATES | CASES_DOMAIN | APPLICATION | FILE_SCANNER | SES_IDENTITY | ANALYTICS_CONNECTOR | CALL_TRANSFER_CONNECTOR | COGNITO_USER_POOL | MESSAGE_PROCESSOR`

 ** [MaxResults](#API_ListIntegrationAssociations_RequestSyntax) **   <a name="connect-ListIntegrationAssociations-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListIntegrationAssociations_RequestSyntax) **   <a name="connect-ListIntegrationAssociations-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListIntegrationAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIntegrationAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IntegrationAssociationSummaryList": [
      {
         "InstanceId": "string",
         "IntegrationArn": "string",
         "IntegrationAssociationArn": "string",
         "IntegrationAssociationId": "string",
         "IntegrationType": "string",
         "SourceApplicationName": "string",
         "SourceApplicationUrl": "string",
         "SourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIntegrationAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IntegrationAssociationSummaryList](#API_ListIntegrationAssociations_ResponseSyntax) **   <a name="connect-ListIntegrationAssociations-response-IntegrationAssociationSummaryList"></a>
The associations.
Type: Array of [IntegrationAssociationSummary](API_IntegrationAssociationSummary.md) objects

 ** [NextToken](#API_ListIntegrationAssociations_ResponseSyntax) **   <a name="connect-ListIntegrationAssociations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListIntegrationAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListIntegrationAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListIntegrationAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListIntegrationAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListIntegrationAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListIntegrationAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListIntegrationAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListIntegrationAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListIntegrationAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListIntegrationAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListIntegrationAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListIntegrationAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
