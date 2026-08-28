---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactFlowVersions.html
---

# ListContactFlowVersions
<a name="API_ListContactFlowVersions"></a>

Returns all the available versions for the specified Connect Customer instance and flow identifier.

## Request Syntax
<a name="API_ListContactFlowVersions_RequestSyntax"></a>

```
GET /contact-flows/{{InstanceId}}/{{ContactFlowId}}/versions?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContactFlowVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowId](#API_ListContactFlowVersions_RequestSyntax) **   <a name="connect-ListContactFlowVersions-request-uri-ContactFlowId"></a>
The identifier of the flow.
Required: Yes

 ** [InstanceId](#API_ListContactFlowVersions_RequestSyntax) **   <a name="connect-ListContactFlowVersions-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListContactFlowVersions_RequestSyntax) **   <a name="connect-ListContactFlowVersions-request-uri-MaxResults"></a>
The maximum number of results to return per page. The default MaxResult size is 100.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListContactFlowVersions_RequestSyntax) **   <a name="connect-ListContactFlowVersions-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListContactFlowVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContactFlowVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowVersionSummaryList": [
      {
         "Arn": "string",
         "Version": number,
         "VersionDescription": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContactFlowVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowVersionSummaryList](#API_ListContactFlowVersions_ResponseSyntax) **   <a name="connect-ListContactFlowVersions-response-ContactFlowVersionSummaryList"></a>
A list of flow version summaries.
Type: Array of [ContactFlowVersionSummary](API_ContactFlowVersionSummary.md) objects

 ** [NextToken](#API_ListContactFlowVersions_ResponseSyntax) **   <a name="connect-ListContactFlowVersions-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListContactFlowVersions_Errors"></a>

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
<a name="API_ListContactFlowVersions_Examples"></a>

### Sample Response
<a name="API_ListContactFlowVersions_Example_1"></a>

This example illustrates one usage of ListContactFlowVersions.

```
{
   "NextToken": "NextTokenId",
   "ContactFlowVersionSummaryList": [
      {
         "Arn": "[contact_flow_arn]",
         "Version": 1,
         "VersionDescription": "description of the flow version"
      }
   ]
}
```

## See Also
<a name="API_ListContactFlowVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListContactFlowVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListContactFlowVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListContactFlowVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListContactFlowVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListContactFlowVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListContactFlowVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListContactFlowVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListContactFlowVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListContactFlowVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListContactFlowVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
