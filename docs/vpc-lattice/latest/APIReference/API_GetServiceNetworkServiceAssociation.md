---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetServiceNetworkServiceAssociation.html
---

# GetServiceNetworkServiceAssociation
<a name="API_GetServiceNetworkServiceAssociation"></a>

Retrieves information about the specified association between a service network and a service.

## Request Syntax
<a name="API_GetServiceNetworkServiceAssociation_RequestSyntax"></a>

```
GET /servicenetworkserviceassociations/{{serviceNetworkServiceAssociationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetServiceNetworkServiceAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceNetworkServiceAssociationIdentifier](#API_GetServiceNetworkServiceAssociation_RequestSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-request-uri-serviceNetworkServiceAssociationIdentifier"></a>
The ID or ARN of the association.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((snsa-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetServiceNetworkServiceAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetServiceNetworkServiceAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "createdBy": "string",
   "customDomainName": "string",
   "dnsEntry": {
      "domainName": "string",
      "hostedZoneId": "string"
   },
   "failureCode": "string",
   "failureMessage": "string",
   "id": "string",
   "serviceArn": "string",
   "serviceId": "string",
   "serviceName": "string",
   "serviceNetworkArn": "string",
   "serviceNetworkId": "string",
   "serviceNetworkName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetServiceNetworkServiceAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}`

 ** [createdAt](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-createdAt"></a>
The date and time that the association was created, in ISO-8601 format.
Type: Timestamp

 ** [createdBy](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-createdBy"></a>
The account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`

 ** [customDomainName](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-customDomainName"></a>
The custom domain name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [dnsEntry](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-dnsEntry"></a>
The DNS name of the service.
Type: [DnsEntry](API_DnsEntry.md) object

 ** [failureCode](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-failureCode"></a>
The failure code.
Type: String

 ** [failureMessage](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-failureMessage"></a>
The failure message.
Type: String

 ** [id](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-id"></a>
The ID of the service network and service association.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((snsa-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}))`

 ** [serviceArn](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-serviceArn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}`

 ** [serviceId](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-serviceId"></a>
The ID of the service.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `svc-[0-9a-z]{17}`

 ** [serviceName](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-serviceName"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [serviceNetworkArn](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-serviceNetworkArn"></a>
The Amazon Resource Name (ARN) of the service network.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}`

 ** [serviceNetworkId](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-serviceNetworkId"></a>
The ID of the service network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-z]{17}`

 ** [serviceNetworkName](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-serviceNetworkName"></a>
The name of the service network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [status](#API_GetServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkServiceAssociation-response-status"></a>
The status of the association.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_GetServiceNetworkServiceAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

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
<a name="API_GetServiceNetworkServiceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetServiceNetworkServiceAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
