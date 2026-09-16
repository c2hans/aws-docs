---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListInstances.html
---

# ListInstances
<a name="API_ListInstances"></a>

This API is in preview release for Connect Customer and is subject to change.

Return a list of instances which are in active state, creation-in-progress state, and failed state. Instances that aren't successfully created (they are in a failed state) are returned only for 24 hours after the CreateInstance API was invoked.

## Request Syntax
<a name="API_ListInstances_RequestSyntax"></a>

```
GET /instance?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInstances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListInstances_RequestSyntax) **   <a name="connect-ListInstances-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [NextToken](#API_ListInstances_RequestSyntax) **   <a name="connect-ListInstances-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListInstances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InstanceSummaryList": [
      {
         "Arn": "string",
         "CreatedTime": number,
         "Id": "string",
         "IdentityManagementType": "string",
         "InboundCallsEnabled": boolean,
         "InstanceAccessUrl": "string",
         "InstanceAlias": "string",
         "InstanceStatus": "string",
         "OutboundCallsEnabled": boolean,
         "ServiceRole": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceSummaryList](#API_ListInstances_ResponseSyntax) **   <a name="connect-ListInstances-response-InstanceSummaryList"></a>
Information about the instances.
Type: Array of [InstanceSummary](API_InstanceSummary.md) objects

 ** [NextToken](#API_ListInstances_ResponseSyntax) **   <a name="connect-ListInstances-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListInstances_Errors"></a>

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

## See Also
<a name="API_ListInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListInstances)
