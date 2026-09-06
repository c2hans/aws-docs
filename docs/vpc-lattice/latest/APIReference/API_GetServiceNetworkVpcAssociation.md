---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetServiceNetworkVpcAssociation.html
---

# GetServiceNetworkVpcAssociation
<a name="API_GetServiceNetworkVpcAssociation"></a>

Retrieves information about the specified association between a service network and a VPC.

## Request Syntax
<a name="API_GetServiceNetworkVpcAssociation_RequestSyntax"></a>

```
GET /servicenetworkvpcassociations/{{serviceNetworkVpcAssociationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetServiceNetworkVpcAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceNetworkVpcAssociationIdentifier](#API_GetServiceNetworkVpcAssociation_RequestSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-request-uri-serviceNetworkVpcAssociationIdentifier"></a>
The ID or ARN of the association.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((snva-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkvpcassociation/snva-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetServiceNetworkVpcAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetServiceNetworkVpcAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "createdBy": "string",
   "dnsOptions": {
      "privateDnsPreference": "string",
      "privateDnsSpecifiedDomains": [ "string" ]
   },
   "failureCode": "string",
   "failureMessage": "string",
   "id": "string",
   "lastUpdatedAt": "string",
   "privateDnsEnabled": boolean,
   "securityGroupIds": [ "string" ],
   "serviceNetworkArn": "string",
   "serviceNetworkId": "string",
   "serviceNetworkName": "string",
   "status": "string",
   "vpcId": "string"
}
```

## Response Elements
<a name="API_GetServiceNetworkVpcAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkvpcassociation/snva-[0-9a-z]{17}`

 ** [createdAt](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-createdAt"></a>
The date and time that the association was created, in ISO-8601 format.
Type: Timestamp

 ** [createdBy](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-createdBy"></a>
The account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`

 ** [dnsOptions](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-dnsOptions"></a>
 DNS options for the service network VPC association.
Type: [DnsOptions](API_DnsOptions.md) object

 ** [failureCode](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-failureCode"></a>
The failure code.
Type: String

 ** [failureMessage](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-failureMessage"></a>
The failure message.
Type: String

 ** [id](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-id"></a>
The ID of the association.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `snva-[0-9a-z]{17}`

 ** [lastUpdatedAt](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-lastUpdatedAt"></a>
The date and time that the association was last updated, in ISO-8601 format.
Type: Timestamp

 ** [privateDnsEnabled](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-privateDnsEnabled"></a>
 Indicates if private DNS is enabled in the VPC association.
Type: Boolean

 ** [securityGroupIds](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-securityGroupIds"></a>
The IDs of the security groups.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`

 ** [serviceNetworkArn](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-serviceNetworkArn"></a>
The Amazon Resource Name (ARN) of the service network.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}`

 ** [serviceNetworkId](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-serviceNetworkId"></a>
The ID of the service network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-z]{17}`

 ** [serviceNetworkName](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-serviceNetworkName"></a>
The name of the service network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [status](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-status"></a>
The status of the association.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED | UPDATE_FAILED`

 ** [vpcId](#API_GetServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-GetServiceNetworkVpcAssociation-response-vpcId"></a>
The ID of the VPC.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`

## Errors
<a name="API_GetServiceNetworkVpcAssociation_Errors"></a>

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
<a name="API_GetServiceNetworkVpcAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetServiceNetworkVpcAssociation)
