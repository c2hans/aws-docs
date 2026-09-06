---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListResourceConfigurations.html
---

# ListResourceConfigurations
<a name="API_ListResourceConfigurations"></a>

Lists the resource configurations owned by or shared with this account.

## Request Syntax
<a name="API_ListResourceConfigurations_RequestSyntax"></a>

```
GET /resourceconfigurations?domainVerificationIdentifier={{domainVerificationIdentifier}}&maxResults={{maxResults}}&nextToken={{nextToken}}&resourceConfigurationGroupIdentifier={{resourceConfigurationGroupIdentifier}}&resourceGatewayIdentifier={{resourceGatewayIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListResourceConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainVerificationIdentifier](#API_ListResourceConfigurations_RequestSyntax) **   <a name="vpclattice-ListResourceConfigurations-request-uri-domainVerificationIdentifier"></a>
 The domain verification ID.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((dv-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:domainverification/dv-[a-fA-F0-9]{17}))`

 ** [maxResults](#API_ListResourceConfigurations_RequestSyntax) **   <a name="vpclattice-ListResourceConfigurations-request-uri-maxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListResourceConfigurations_RequestSyntax) **   <a name="vpclattice-ListResourceConfigurations-request-uri-nextToken"></a>
A pagination token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [resourceConfigurationGroupIdentifier](#API_ListResourceConfigurations_RequestSyntax) **   <a name="vpclattice-ListResourceConfigurations-request-uri-resourceConfigurationGroupIdentifier"></a>
The ID of the resource configuration of type `Group`.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`

 ** [resourceGatewayIdentifier](#API_ListResourceConfigurations_RequestSyntax) **   <a name="vpclattice-ListResourceConfigurations-request-uri-resourceGatewayIdentifier"></a>
The ID of the resource gateway for the resource configuration.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((rgw-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}))`

## Request Body
<a name="API_ListResourceConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListResourceConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "amazonManaged": boolean,
         "arn": "string",
         "createdAt": "string",
         "customDomainName": "string",
         "domainVerificationId": "string",
         "groupDomain": "string",
         "id": "string",
         "lastUpdatedAt": "string",
         "name": "string",
         "resourceConfigurationGroupId": "string",
         "resourceGatewayId": "string",
         "status": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListResourceConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListResourceConfigurations_ResponseSyntax) **   <a name="vpclattice-ListResourceConfigurations-response-items"></a>
Information about the resource configurations.
Type: Array of [ResourceConfigurationSummary](API_ResourceConfigurationSummary.md) objects

 ** [nextToken](#API_ListResourceConfigurations_ResponseSyntax) **   <a name="vpclattice-ListResourceConfigurations-response-nextToken"></a>
If there are additional results, a pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListResourceConfigurations_Errors"></a>

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
<a name="API_ListResourceConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/ListResourceConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/ListResourceConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ListResourceConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/ListResourceConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ListResourceConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/ListResourceConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/ListResourceConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/ListResourceConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/ListResourceConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ListResourceConfigurations)
