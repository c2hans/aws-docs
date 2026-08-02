---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListFlowAssociations.html
---

# ListFlowAssociations
<a name="API_ListFlowAssociations"></a>

List the flow association based on the filters.

## Request Syntax
<a name="API_ListFlowAssociations_RequestSyntax"></a>

```
GET /flow-associations-summary/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}}&ResourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFlowAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListFlowAssociations_RequestSyntax) **   <a name="connect-ListFlowAssociations-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListFlowAssociations_RequestSyntax) **   <a name="connect-ListFlowAssociations-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListFlowAssociations_RequestSyntax) **   <a name="connect-ListFlowAssociations-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

 ** [ResourceType](#API_ListFlowAssociations_RequestSyntax) **   <a name="connect-ListFlowAssociations-request-uri-ResourceType"></a>
A valid resource type.
Valid Values: `WHATSAPP_MESSAGING_PHONE_NUMBER | VOICE_PHONE_NUMBER | INBOUND_EMAIL | OUTBOUND_EMAIL | ANALYTICS_CONNECTOR`

## Request Body
<a name="API_ListFlowAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFlowAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FlowAssociationSummaryList": [
      {
         "FlowId": "string",
         "ResourceId": "string",
         "ResourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFlowAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FlowAssociationSummaryList](#API_ListFlowAssociations_ResponseSyntax) **   <a name="connect-ListFlowAssociations-response-FlowAssociationSummaryList"></a>
Summary of flow associations.
Type: Array of [FlowAssociationSummary](API_FlowAssociationSummary.md) objects

 ** [NextToken](#API_ListFlowAssociations_ResponseSyntax) **   <a name="connect-ListFlowAssociations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListFlowAssociations_Errors"></a>

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
<a name="API_ListFlowAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListFlowAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListFlowAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListFlowAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListFlowAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListFlowAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListFlowAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListFlowAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListFlowAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListFlowAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListFlowAssociations)
