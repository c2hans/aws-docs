---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListServiceNetworkResourceAssociations.html
---

# ListServiceNetworkResourceAssociations
<a name="API_ListServiceNetworkResourceAssociations"></a>

Lists the associations between a service network and a resource configuration.

## Request Syntax
<a name="API_ListServiceNetworkResourceAssociations_RequestSyntax"></a>

```
GET /servicenetworkresourceassociations?includeChildren={{includeChildren}}&maxResults={{maxResults}}&nextToken={{nextToken}}&resourceConfigurationIdentifier={{resourceConfigurationIdentifier}}&serviceNetworkIdentifier={{serviceNetworkIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListServiceNetworkResourceAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [includeChildren](#API_ListServiceNetworkResourceAssociations_RequestSyntax) **   <a name="vpclattice-ListServiceNetworkResourceAssociations-request-uri-includeChildren"></a>
Include service network resource associations of the child resource configuration with the grouped resource configuration.
The type is boolean and the default value is false.

 ** [maxResults](#API_ListServiceNetworkResourceAssociations_RequestSyntax) **   <a name="vpclattice-ListServiceNetworkResourceAssociations-request-uri-maxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListServiceNetworkResourceAssociations_RequestSyntax) **   <a name="vpclattice-ListServiceNetworkResourceAssociations-request-uri-nextToken"></a>
If there are additional results, a pagination token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [resourceConfigurationIdentifier](#API_ListServiceNetworkResourceAssociations_RequestSyntax) **   <a name="vpclattice-ListServiceNetworkResourceAssociations-request-uri-resourceConfigurationIdentifier"></a>
The ID of the resource configuration.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`

 ** [serviceNetworkIdentifier](#API_ListServiceNetworkResourceAssociations_RequestSyntax) **   <a name="vpclattice-ListServiceNetworkResourceAssociations-request-uri-serviceNetworkIdentifier"></a>
The ID of the service network.
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `((sn-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}))`

## Request Body
<a name="API_ListServiceNetworkResourceAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListServiceNetworkResourceAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "createdAt": "string",
         "createdBy": "string",
         "dnsEntry": {
            "domainName": "string",
            "hostedZoneId": "string"
         },
         "failureCode": "string",
         "id": "string",
         "isManagedAssociation": boolean,
         "privateDnsEnabled": boolean,
         "privateDnsEntry": {
            "domainName": "string",
            "hostedZoneId": "string"
         },
         "resourceConfigurationArn": "string",
         "resourceConfigurationId": "string",
         "resourceConfigurationName": "string",
         "serviceNetworkArn": "string",
         "serviceNetworkId": "string",
         "serviceNetworkName": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListServiceNetworkResourceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListServiceNetworkResourceAssociations_ResponseSyntax) **   <a name="vpclattice-ListServiceNetworkResourceAssociations-response-items"></a>
Information about the associations.
Type: Array of [ServiceNetworkResourceAssociationSummary](API_ServiceNetworkResourceAssociationSummary.md) objects

 ** [nextToken](#API_ListServiceNetworkResourceAssociations_ResponseSyntax) **   <a name="vpclattice-ListServiceNetworkResourceAssociations-response-nextToken"></a>
If there are additional results, a pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListServiceNetworkResourceAssociations_Errors"></a>

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
<a name="API_ListServiceNetworkResourceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ListServiceNetworkResourceAssociations)
