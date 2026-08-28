---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListServiceNetworkServiceAssociations.html
---

# ListServiceNetworkServiceAssociations
<a name="API_ListServiceNetworkServiceAssociations"></a>

Lists the associations between a service network and a service. You can filter the list either by service or service network. You must provide either the service network identifier or the service identifier.

Every association in Amazon VPC Lattice has a unique Amazon Resource Name (ARN), such as when a service network is associated with a VPC or when a service is associated with a service network. If the association is for a resource is shared with another account, the association includes the local account ID as the prefix in the ARN.

## Request Syntax
<a name="API_ListServiceNetworkServiceAssociations_RequestSyntax"></a>

```
GET /servicenetworkserviceassociations?maxResults={{maxResults}}&nextToken={{nextToken}}&serviceIdentifier={{serviceIdentifier}}&serviceNetworkIdentifier={{serviceNetworkIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListServiceNetworkServiceAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListServiceNetworkServiceAssociations_RequestSyntax) **   <a name="vpclattice-ListServiceNetworkServiceAssociations-request-uri-maxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListServiceNetworkServiceAssociations_RequestSyntax) **   <a name="vpclattice-ListServiceNetworkServiceAssociations-request-uri-nextToken"></a>
A pagination token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [serviceIdentifier](#API_ListServiceNetworkServiceAssociations_RequestSyntax) **   <a name="vpclattice-ListServiceNetworkServiceAssociations-request-uri-serviceIdentifier"></a>
The ID or ARN of the service.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`

 ** [serviceNetworkIdentifier](#API_ListServiceNetworkServiceAssociations_RequestSyntax) **   <a name="vpclattice-ListServiceNetworkServiceAssociations-request-uri-serviceNetworkIdentifier"></a>
The ID or ARN of the service network.
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `((sn-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}))`

## Request Body
<a name="API_ListServiceNetworkServiceAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListServiceNetworkServiceAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "createdAt": "string",
         "createdBy": "string",
         "customDomainName": "string",
         "dnsEntry": {
            "domainName": "string",
            "hostedZoneId": "string"
         },
         "id": "string",
         "serviceArn": "string",
         "serviceId": "string",
         "serviceName": "string",
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
<a name="API_ListServiceNetworkServiceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListServiceNetworkServiceAssociations_ResponseSyntax) **   <a name="vpclattice-ListServiceNetworkServiceAssociations-response-items"></a>
Information about the associations.
Type: Array of [ServiceNetworkServiceAssociationSummary](API_ServiceNetworkServiceAssociationSummary.md) objects

 ** [nextToken](#API_ListServiceNetworkServiceAssociations_ResponseSyntax) **   <a name="vpclattice-ListServiceNetworkServiceAssociations-response-nextToken"></a>
If there are additional results, a pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListServiceNetworkServiceAssociations_Errors"></a>

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
<a name="API_ListServiceNetworkServiceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ListServiceNetworkServiceAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
