---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListResourceEndpointAssociations.html
---

# ListResourceEndpointAssociations
<a name="API_ListResourceEndpointAssociations"></a>

Lists the associations for the specified VPC endpoint.

## Request Syntax
<a name="API_ListResourceEndpointAssociations_RequestSyntax"></a>

```
GET /resourceendpointassociations?maxResults={{maxResults}}&nextToken={{nextToken}}&resourceConfigurationIdentifier={{resourceConfigurationIdentifier}}&resourceEndpointAssociationIdentifier={{resourceEndpointAssociationIdentifier}}&vpcEndpointId={{vpcEndpointId}}&vpcEndpointOwner={{vpcEndpointOwner}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListResourceEndpointAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListResourceEndpointAssociations_RequestSyntax) **   <a name="vpclattice-ListResourceEndpointAssociations-request-uri-maxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListResourceEndpointAssociations_RequestSyntax) **   <a name="vpclattice-ListResourceEndpointAssociations-request-uri-nextToken"></a>
A pagination token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [resourceConfigurationIdentifier](#API_ListResourceEndpointAssociations_RequestSyntax) **   <a name="vpclattice-ListResourceEndpointAssociations-request-uri-resourceConfigurationIdentifier"></a>
The ID for the resource configuration associated with the VPC endpoint.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
Required: Yes

 ** [resourceEndpointAssociationIdentifier](#API_ListResourceEndpointAssociations_RequestSyntax) **   <a name="vpclattice-ListResourceEndpointAssociations-request-uri-resourceEndpointAssociationIdentifier"></a>
The ID of the association.
Length Constraints: Minimum length of 21. Maximum length of 2048.
Pattern: `((rea-[0-9a-f]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceendpointassociation/rea-[0-9a-f]{17}))`

 ** [vpcEndpointId](#API_ListResourceEndpointAssociations_RequestSyntax) **   <a name="vpclattice-ListResourceEndpointAssociations-request-uri-vpcEndpointId"></a>
The ID of the VPC endpoint in the association.
Length Constraints: Fixed length of 22.
Pattern: `vpce-[0-9a-f]{17}`

 ** [vpcEndpointOwner](#API_ListResourceEndpointAssociations_RequestSyntax) **   <a name="vpclattice-ListResourceEndpointAssociations-request-uri-vpcEndpointOwner"></a>
The owner of the VPC endpoint in the association.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

## Request Body
<a name="API_ListResourceEndpointAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListResourceEndpointAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "createdAt": "string",
         "createdBy": "string",
         "id": "string",
         "resourceConfigurationArn": "string",
         "resourceConfigurationId": "string",
         "resourceConfigurationName": "string",
         "vpcEndpointId": "string",
         "vpcEndpointOwner": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListResourceEndpointAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListResourceEndpointAssociations_ResponseSyntax) **   <a name="vpclattice-ListResourceEndpointAssociations-response-items"></a>
Information about the VPC endpoint associations.
Type: Array of [ResourceEndpointAssociationSummary](API_ResourceEndpointAssociationSummary.md) objects

 ** [nextToken](#API_ListResourceEndpointAssociations_ResponseSyntax) **   <a name="vpclattice-ListResourceEndpointAssociations-response-nextToken"></a>
If there are additional results, a pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListResourceEndpointAssociations_Errors"></a>

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
<a name="API_ListResourceEndpointAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ListResourceEndpointAssociations)
