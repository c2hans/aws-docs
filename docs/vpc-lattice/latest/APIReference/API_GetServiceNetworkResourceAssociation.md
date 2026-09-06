---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetServiceNetworkResourceAssociation.html
---

# GetServiceNetworkResourceAssociation
<a name="API_GetServiceNetworkResourceAssociation"></a>

Retrieves information about the specified association between a service network and a resource configuration.

## Request Syntax
<a name="API_GetServiceNetworkResourceAssociation_RequestSyntax"></a>

```
GET /servicenetworkresourceassociations/{{serviceNetworkResourceAssociationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetServiceNetworkResourceAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceNetworkResourceAssociationIdentifier](#API_GetServiceNetworkResourceAssociation_RequestSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-request-uri-serviceNetworkResourceAssociationIdentifier"></a>
The ID of the association.
Length Constraints: Minimum length of 22. Maximum length of 2048.
Pattern: `((snra-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkresourceassociation/snra-[0-9a-f]{17}))`
Required: Yes

## Request Body
<a name="API_GetServiceNetworkResourceAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetServiceNetworkResourceAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "createdBy": "string",
   "dnsEntry": {
      "domainName": "string",
      "hostedZoneId": "string"
   },
   "domainVerificationStatus": "string",
   "failureCode": "string",
   "failureReason": "string",
   "id": "string",
   "isManagedAssociation": boolean,
   "lastUpdatedAt": "string",
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
```

## Response Elements
<a name="API_GetServiceNetworkResourceAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 22. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkresourceassociation/snra-[0-9a-f]{17}`

 ** [createdAt](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-createdAt"></a>
The date and time that the association was created, in ISO-8601 format.
Type: Timestamp

 ** [createdBy](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-createdBy"></a>
The account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`

 ** [dnsEntry](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-dnsEntry"></a>
The DNS entry for the service.
Type: [DnsEntry](API_DnsEntry.md) object

 ** [domainVerificationStatus](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-domainVerificationStatus"></a>
 The domain verification status in the service network resource association.
Type: String
Valid Values: `VERIFIED | PENDING | VERIFICATION_TIMED_OUT`

 ** [failureCode](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-failureCode"></a>
The failure code.
Type: String

 ** [failureReason](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-failureReason"></a>
The reason the association request failed.
Type: String

 ** [id](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-id"></a>
The ID of the association.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `snra-[0-9a-f]{17}`

 ** [isManagedAssociation](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-isManagedAssociation"></a>
Indicates whether the association is managed by Amazon.
Type: Boolean

 ** [lastUpdatedAt](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-lastUpdatedAt"></a>
The most recent date and time that the association was updated, in ISO-8601 format.
Type: Timestamp

 ** [privateDnsEnabled](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-privateDnsEnabled"></a>
 Indicates if private DNS is enabled in the service network resource association.
Type: Boolean

 ** [privateDnsEntry](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-privateDnsEntry"></a>
The private DNS entry for the service.
Type: [DnsEntry](API_DnsEntry.md) object

 ** [resourceConfigurationArn](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-resourceConfigurationArn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`

 ** [resourceConfigurationId](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-resourceConfigurationId"></a>
The ID of the resource configuration that is associated with the service network.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`

 ** [resourceConfigurationName](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-resourceConfigurationName"></a>
The name of the resource configuration that is associated with the service network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rcfg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [serviceNetworkArn](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-serviceNetworkArn"></a>
The Amazon Resource Name (ARN) of the service network that is associated with the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.

 ** [serviceNetworkId](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-serviceNetworkId"></a>
The ID of the service network that is associated with the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.

 ** [serviceNetworkName](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-serviceNetworkName"></a>
The name of the service network that is associated with the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.

 ** [status](#API_GetServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkResourceAssociation-response-status"></a>
The status of the association.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | PARTIAL | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_GetServiceNetworkResourceAssociation_Errors"></a>

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
<a name="API_GetServiceNetworkResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetServiceNetworkResourceAssociation)
