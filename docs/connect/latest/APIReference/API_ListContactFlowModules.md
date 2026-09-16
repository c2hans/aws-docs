---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactFlowModules.html
---

# ListContactFlowModules
<a name="API_ListContactFlowModules"></a>

Provides information about the flow modules for the specified Connect Customer instance.

## Request Syntax
<a name="API_ListContactFlowModules_RequestSyntax"></a>

```
GET /contact-flow-modules-summary/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}}&state={{ContactFlowModuleState}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContactFlowModules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowModuleState](#API_ListContactFlowModules_RequestSyntax) **   <a name="connect-ListContactFlowModules-request-uri-ContactFlowModuleState"></a>
The state of the flow module.
Valid Values: `ACTIVE | ARCHIVED`

 ** [InstanceId](#API_ListContactFlowModules_RequestSyntax) **   <a name="connect-ListContactFlowModules-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListContactFlowModules_RequestSyntax) **   <a name="connect-ListContactFlowModules-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListContactFlowModules_RequestSyntax) **   <a name="connect-ListContactFlowModules-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListContactFlowModules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContactFlowModules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactFlowModulesSummaryList": [
      {
         "Arn": "string",
         "Id": "string",
         "Name": "string",
         "State": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContactFlowModules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactFlowModulesSummaryList](#API_ListContactFlowModules_ResponseSyntax) **   <a name="connect-ListContactFlowModules-response-ContactFlowModulesSummaryList"></a>
Information about the flow module.
Type: Array of [ContactFlowModuleSummary](API_ContactFlowModuleSummary.md) objects

 ** [NextToken](#API_ListContactFlowModules_ResponseSyntax) **   <a name="connect-ListContactFlowModules-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListContactFlowModules_Errors"></a>

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

## See Also
<a name="API_ListContactFlowModules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListContactFlowModules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListContactFlowModules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListContactFlowModules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListContactFlowModules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListContactFlowModules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListContactFlowModules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListContactFlowModules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListContactFlowModules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListContactFlowModules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListContactFlowModules)
