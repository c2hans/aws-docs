---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListResourceGateways.html
---

# ListResourceGateways
<a name="API_ListResourceGateways"></a>

Lists the resource gateways that you own or that were shared with you.

## Request Syntax
<a name="API_ListResourceGateways_RequestSyntax"></a>

```
GET /resourcegateways?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListResourceGateways_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListResourceGateways_RequestSyntax) **   <a name="vpclattice-ListResourceGateways-request-uri-maxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListResourceGateways_RequestSyntax) **   <a name="vpclattice-ListResourceGateways-request-uri-nextToken"></a>
If there are additional results, a pagination token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_ListResourceGateways_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListResourceGateways_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "createdAt": "string",
         "id": "string",
         "ipAddressType": "string",
         "ipv4AddressesPerEni": number,
         "lastUpdatedAt": "string",
         "name": "string",
         "resourceConfigDnsResolution": "string",
         "securityGroupIds": [ "string" ],
         "status": "string",
         "subnetIds": [ "string" ],
         "vpcIdentifier": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListResourceGateways_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListResourceGateways_ResponseSyntax) **   <a name="vpclattice-ListResourceGateways-response-items"></a>
Information about the resource gateways.
Type: Array of [ResourceGatewaySummary](API_ResourceGatewaySummary.md) objects

 ** [nextToken](#API_ListResourceGateways_ResponseSyntax) **   <a name="vpclattice-ListResourceGateways-response-nextToken"></a>
If there are additional results, a pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListResourceGateways_Errors"></a>

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
<a name="API_ListResourceGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/ListResourceGateways)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/ListResourceGateways)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ListResourceGateways)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/ListResourceGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ListResourceGateways)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/ListResourceGateways)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/ListResourceGateways)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/ListResourceGateways)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/ListResourceGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ListResourceGateways)
