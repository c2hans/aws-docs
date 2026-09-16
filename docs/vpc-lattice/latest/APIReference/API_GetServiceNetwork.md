---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetServiceNetwork.html
---

# GetServiceNetwork
<a name="API_GetServiceNetwork"></a>

Retrieves information about the specified service network.

## Request Syntax
<a name="API_GetServiceNetwork_RequestSyntax"></a>

```
GET /servicenetworks/{{serviceNetworkIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetServiceNetwork_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceNetworkIdentifier](#API_GetServiceNetwork_RequestSyntax) **   <a name="vpclattice-GetServiceNetwork-request-uri-serviceNetworkIdentifier"></a>
The ID or ARN of the service network.
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `((sn-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetServiceNetwork_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetServiceNetwork_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "authType": "string",
   "createdAt": "string",
   "id": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "numberOfAssociatedServices": number,
   "numberOfAssociatedVPCs": number,
   "sharingConfig": {
      "enabled": boolean
   }
}
```

## Response Elements
<a name="API_GetServiceNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetServiceNetwork_ResponseSyntax) **   <a name="vpclattice-GetServiceNetwork-response-arn"></a>
The Amazon Resource Name (ARN) of the service network.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}`

 ** [authType](#API_GetServiceNetwork_ResponseSyntax) **   <a name="vpclattice-GetServiceNetwork-response-authType"></a>
The type of IAM policy.
Type: String
Valid Values: `NONE | AWS_IAM`

 ** [createdAt](#API_GetServiceNetwork_ResponseSyntax) **   <a name="vpclattice-GetServiceNetwork-response-createdAt"></a>
The date and time that the service network was created, in ISO-8601 format.
Type: Timestamp

 ** [id](#API_GetServiceNetwork_ResponseSyntax) **   <a name="vpclattice-GetServiceNetwork-response-id"></a>
The ID of the service network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-z]{17}`

 ** [lastUpdatedAt](#API_GetServiceNetwork_ResponseSyntax) **   <a name="vpclattice-GetServiceNetwork-response-lastUpdatedAt"></a>
The date and time of the last update, in ISO-8601 format.
Type: Timestamp

 ** [name](#API_GetServiceNetwork_ResponseSyntax) **   <a name="vpclattice-GetServiceNetwork-response-name"></a>
The name of the service network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [numberOfAssociatedServices](#API_GetServiceNetwork_ResponseSyntax) **   <a name="vpclattice-GetServiceNetwork-response-numberOfAssociatedServices"></a>
The number of services associated with the service network.
Type: Long

 ** [numberOfAssociatedVPCs](#API_GetServiceNetwork_ResponseSyntax) **   <a name="vpclattice-GetServiceNetwork-response-numberOfAssociatedVPCs"></a>
The number of VPCs associated with the service network.
Type: Long

 ** [sharingConfig](#API_GetServiceNetwork_ResponseSyntax) **   <a name="vpclattice-GetServiceNetwork-response-sharingConfig"></a>
Specifies if the service network is enabled for sharing.
Type: [SharingConfig](API_SharingConfig.md) object

## Errors
<a name="API_GetServiceNetwork_Errors"></a>

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
<a name="API_GetServiceNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetServiceNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetServiceNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetServiceNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetServiceNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetServiceNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetServiceNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetServiceNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetServiceNetwork)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetServiceNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetServiceNetwork)
