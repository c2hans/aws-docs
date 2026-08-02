---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListAccessLogSubscriptions.html
---

# ListAccessLogSubscriptions
<a name="API_ListAccessLogSubscriptions"></a>

Lists the access log subscriptions for the specified service network or service.

## Request Syntax
<a name="API_ListAccessLogSubscriptions_RequestSyntax"></a>

```
GET /accesslogsubscriptions?maxResults={{maxResults}}&nextToken={{nextToken}}&resourceIdentifier={{resourceIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAccessLogSubscriptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAccessLogSubscriptions_RequestSyntax) **   <a name="vpclattice-ListAccessLogSubscriptions-request-uri-maxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAccessLogSubscriptions_RequestSyntax) **   <a name="vpclattice-ListAccessLogSubscriptions-request-uri-nextToken"></a>
A pagination token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [resourceIdentifier](#API_ListAccessLogSubscriptions_RequestSyntax) **   <a name="vpclattice-ListAccessLogSubscriptions-request-uri-resourceIdentifier"></a>
The ID or ARN of the service network or service.
Length Constraints: Minimum length of 17. Maximum length of 200.
Pattern: `((((sn)|(svc)|(rcfg))-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(resourceconfiguration/rcfg)|(service/svc))-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_ListAccessLogSubscriptions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAccessLogSubscriptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "createdAt": "string",
         "destinationArn": "string",
         "id": "string",
         "lastUpdatedAt": "string",
         "resourceArn": "string",
         "resourceId": "string",
         "serviceNetworkLogType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAccessLogSubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAccessLogSubscriptions_ResponseSyntax) **   <a name="vpclattice-ListAccessLogSubscriptions-response-items"></a>
Information about the access log subscriptions.
Type: Array of [AccessLogSubscriptionSummary](API_AccessLogSubscriptionSummary.md) objects

 ** [nextToken](#API_ListAccessLogSubscriptions_ResponseSyntax) **   <a name="vpclattice-ListAccessLogSubscriptions-response-nextToken"></a>
A pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListAccessLogSubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
 ** serviceCode **
The service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** fieldList **
The fields that failed validation.
 ** reason **
The reason.
HTTP Status Code: 400

## See Also
<a name="API_ListAccessLogSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ListAccessLogSubscriptions)
