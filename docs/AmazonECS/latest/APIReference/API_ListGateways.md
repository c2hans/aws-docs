---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListGateways.html
---

# ListGateways
<a name="API_ListGateways"></a>

Returns a list of gateways in your account. You can filter the results by gateway name and status. The results are paginated. We recommend that you use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListGateways_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "names": [ "{{string}}" ],
   "nextToken": "{{string}}",
   "status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListGateways_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListGateways_RequestSyntax) **   <a name="ECS-ListGateways-request-maxResults"></a>
The maximum number of gateway results that `ListGateways` returns in a single page. The default is 100.
Type: Integer
Required: No

 ** [names](#API_ListGateways_RequestSyntax) **   <a name="ECS-ListGateways-request-names"></a>
The gateway names to filter the results by. You can specify up to 10 names.
Type: Array of strings
Required: No

 ** [nextToken](#API_ListGateways_RequestSyntax) **   <a name="ECS-ListGateways-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListGateways` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results.
Type: String
Required: No

 ** [status](#API_ListGateways_RequestSyntax) **   <a name="ECS-ListGateways-request-status"></a>
The gateway statuses to filter the results by.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Values: `ACTIVE | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | DELETED`
Required: No

## Response Syntax
<a name="API_ListGateways_ResponseSyntax"></a>

```
{
   "gateways": [
      {
         "createdAt": number,
         "gatewayArn": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGateways_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gateways](#API_ListGateways_ResponseSyntax) **   <a name="ECS-ListGateways-response-gateways"></a>
The list of gateways that match the request.
Type: Array of [GatewaySummary](API_GatewaySummary.md) objects

 ** [nextToken](#API_ListGateways_ResponseSyntax) **   <a name="ECS-ListGateways-response-nextToken"></a>
The `nextToken` value to include in a future `ListGateways` request. When the results of a `ListGateways` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListGateways_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListGateways)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListGateways)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListGateways)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListGateways)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListGateways)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListGateways)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListGateways)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListGateways)
