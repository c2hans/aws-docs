---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactFlowModuleAliases.html
---

# ListContactFlowModuleAliases
<a name="API_ListContactFlowModuleAliases"></a>

Lists all aliases associated with a contact flow module, showing their current version mappings and metadata.

## Request Syntax
<a name="API_ListContactFlowModuleAliases_RequestSyntax"></a>

```
GET /contact-flow-modules/{{InstanceId}}/{{ContactFlowModuleId}}/aliases?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContactFlowModuleAliases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowModuleId](#API_ListContactFlowModuleAliases_RequestSyntax) **   <a name="connect-ListContactFlowModuleAliases-request-uri-ContactFlowModuleId"></a>
The identifier of the flow module.
Required: Yes

 ** [InstanceId](#API_ListContactFlowModuleAliases_RequestSyntax) **   <a name="connect-ListContactFlowModuleAliases-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [MaxResults](#API_ListContactFlowModuleAliases_RequestSyntax) **   <a name="connect-ListContactFlowModuleAliases-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListContactFlowModuleAliases_RequestSyntax) **   <a name="connect-ListContactFlowModuleAliases-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListContactFlowModuleAliases_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContactFlowModuleAliases_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowModuleAliasSummaryList": [
      {
         "AliasDescription": "string",
         "AliasId": "string",
         "AliasName": "string",
         "Arn": "string",
         "LastModifiedTime": number,
         "Version": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContactFlowModuleAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowModuleAliasSummaryList](#API_ListContactFlowModuleAliases_ResponseSyntax) **   <a name="connect-ListContactFlowModuleAliases-response-ContactFlowModuleAliasSummaryList"></a>
Information about the flow module aliases.
Type: Array of [ContactFlowModuleAliasSummary](API_ContactFlowModuleAliasSummary.md) objects

 ** [NextToken](#API_ListContactFlowModuleAliases_ResponseSyntax) **   <a name="connect-ListContactFlowModuleAliases-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListContactFlowModuleAliases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

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

## Examples
<a name="API_ListContactFlowModuleAliases_Examples"></a>

### Sample Response
<a name="API_ListContactFlowModuleAliases_Example_1"></a>

This example illustrates one usage of ListContactFlowModuleAliases.

```
{
   "NextToken": "NextTokenId",
   "ContactFlowModuleAliasSummaryList": [
      {
         "Arn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-1234-1234-123456789012/flow-module/abcdefgh-1234-5678-9012-abcdefghijkl",
         "AliasId": "alias-12345678",
         "Version": 2,
         "AliasName": "production",
         "AliasDescription": "Production version of the customer service module",
         "LastModifiedTime": "2024-01-15T10:30:00.000Z"
      },
      {
         "Arn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-1234-1234-123456789012/flow-module/abcdefgh-1234-5678-9012-abcdefghijkl",
         "AliasId": "alias-87654321",
         "Version": 1,
         "AliasName": "staging",
         "AliasDescription": "Staging version for testing",
         "LastModifiedTime": "2024-01-10T14:20:00.000Z"
      }
   ]
}
```

## See Also
<a name="API_ListContactFlowModuleAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListContactFlowModuleAliases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListContactFlowModuleAliases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListContactFlowModuleAliases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListContactFlowModuleAliases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListContactFlowModuleAliases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListContactFlowModuleAliases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListContactFlowModuleAliases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListContactFlowModuleAliases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListContactFlowModuleAliases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListContactFlowModuleAliases)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
