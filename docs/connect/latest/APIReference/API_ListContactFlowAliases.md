---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactFlowAliases.html
---

# ListContactFlowAliases
<a name="API_ListContactFlowAliases"></a>

Lists the aliases associated with a flow, including the version that each alias points to.

## Request Syntax
<a name="API_ListContactFlowAliases_RequestSyntax"></a>

```
GET /contact-flows/{{InstanceId}}/{{ContactFlowId}}/aliases?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContactFlowAliases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowId](#API_ListContactFlowAliases_RequestSyntax) **   <a name="connect-ListContactFlowAliases-request-uri-ContactFlowId"></a>
The identifier of the flow.
Required: Yes

 ** [InstanceId](#API_ListContactFlowAliases_RequestSyntax) **   <a name="connect-ListContactFlowAliases-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [MaxResults](#API_ListContactFlowAliases_RequestSyntax) **   <a name="connect-ListContactFlowAliases-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListContactFlowAliases_RequestSyntax) **   <a name="connect-ListContactFlowAliases-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListContactFlowAliases_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContactFlowAliases_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowAliasSummaryList": [
      {
         "AliasDescription": "string",
         "AliasId": "string",
         "AliasName": "string",
         "Arn": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "Version": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContactFlowAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowAliasSummaryList](#API_ListContactFlowAliases_ResponseSyntax) **   <a name="connect-ListContactFlowAliases-response-ContactFlowAliasSummaryList"></a>
Information about the flow aliases.
Type: Array of [ContactFlowAliasSummary](API_ContactFlowAliasSummary.md) objects

 ** [NextToken](#API_ListContactFlowAliases_ResponseSyntax) **   <a name="connect-ListContactFlowAliases-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListContactFlowAliases_Errors"></a>

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
<a name="API_ListContactFlowAliases_Examples"></a>

### Sample Response
<a name="API_ListContactFlowAliases_Example_1"></a>

This example illustrates one usage of ListContactFlowAliases.

```
{
  "NextToken": "NextTokenId",
  "ContactFlowAliasSummaryList": [
    {
      "Arn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-1234-1234-123456789012/contact-flow/abcdefgh-1234-5678-9012-abcdefghijkl",
      "AliasId": "87654321-4321-4321-4321-210987654321",
      "Version": 2,
      "AliasName": "production",
      "AliasDescription": "Production version of the customer service flow",
      "LastModifiedTime": "2026-09-15T10:30:00.000Z",
      "LastModifiedRegion": "us-west-2"
    }
  ]
}
```

## See Also
<a name="API_ListContactFlowAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListContactFlowAliases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListContactFlowAliases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListContactFlowAliases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListContactFlowAliases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListContactFlowAliases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListContactFlowAliases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListContactFlowAliases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListContactFlowAliases)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListContactFlowAliases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListContactFlowAliases)
