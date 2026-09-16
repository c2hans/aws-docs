---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateAccessor.html
---

# CreateAccessor
<a name="API_CreateAccessor"></a>

Creates a new accessor for use with Amazon Managed Blockchain service that supports token based access. The accessor contains information required for token based access.

## Request Syntax
<a name="API_CreateAccessor_RequestSyntax"></a>

```
POST /accessors HTTP/1.1
Content-type: application/json

{
   "AccessorType": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "NetworkType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAccessor_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAccessor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccessorType](#API_CreateAccessor_RequestSyntax) **   <a name="ManagedBlockchain-CreateAccessor-request-AccessorType"></a>
The type of accessor.
Currently, accessor type is restricted to `BILLING_TOKEN`.
Type: String
Valid Values: `BILLING_TOKEN`
Required: Yes

 ** [ClientRequestToken](#API_CreateAccessor_RequestSyntax) **   <a name="ManagedBlockchain-CreateAccessor-request-ClientRequestToken"></a>
This is a unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an AWS SDK or the AWS AWS CLI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [NetworkType](#API_CreateAccessor_RequestSyntax) **   <a name="ManagedBlockchain-CreateAccessor-request-NetworkType"></a>
The blockchain network that the `Accessor` token is created for.
+ Use the actual `networkType` value for the blockchain network that you are creating the `Accessor` token for.
+ With the shut down of the *Ethereum Goerli* and *Polygon Mumbai Testnet* networks the following `networkType` values are no longer available for selection and use.
  +  `ETHEREUM_MAINNET_AND_GOERLI`
  +  `ETHEREUM_GOERLI`
  +  `POLYGON_MUMBAI`

  However, your existing `Accessor` tokens with these `networkType` values will remain unchanged.
Type: String
Valid Values: `ETHEREUM_GOERLI | ETHEREUM_MAINNET | ETHEREUM_MAINNET_AND_GOERLI | POLYGON_MAINNET | POLYGON_MUMBAI`
Required: No

 ** [Tags](#API_CreateAccessor_RequestSyntax) **   <a name="ManagedBlockchain-CreateAccessor-request-Tags"></a>
Tags to assign to the Accessor.
 Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAccessor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessorId": "string",
   "BillingToken": "string",
   "NetworkType": "string"
}
```

## Response Elements
<a name="API_CreateAccessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessorId](#API_CreateAccessor_ResponseSyntax) **   <a name="ManagedBlockchain-CreateAccessor-response-AccessorId"></a>
The unique identifier of the accessor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.

 ** [BillingToken](#API_CreateAccessor_ResponseSyntax) **   <a name="ManagedBlockchain-CreateAccessor-response-BillingToken"></a>
The billing token is a property of the Accessor. Use this token to when making calls to the blockchain network. The billing token is used to track your accessor token for billing requests.
Type: String
Length Constraints: Fixed length of 42.

 ** [NetworkType](#API_CreateAccessor_ResponseSyntax) **   <a name="ManagedBlockchain-CreateAccessor-response-NetworkType"></a>
The blockchain network that the accessor token is created for.
Type: String
Valid Values: `ETHEREUM_GOERLI | ETHEREUM_MAINNET | ETHEREUM_MAINNET_AND_GOERLI | POLYGON_MAINNET | POLYGON_MUMBAI`

## Errors
<a name="API_CreateAccessor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceErrorException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** InvalidRequestException **
The action or operation requested is invalid. Verify that the action is typed correctly.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
A resource request is issued for a resource that already exists.
HTTP Status Code: 409

 ** ResourceLimitExceededException **
The maximum number of resources of that type already exist. Ensure the resources requested are within the boundaries of the service edition and your account limits.
HTTP Status Code: 429

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.
HTTP Status Code: 429

 ** TooManyTagsException **

 ** ResourceName **

HTTP Status Code: 400

## See Also
<a name="API_CreateAccessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/CreateAccessor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/CreateAccessor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/CreateAccessor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/CreateAccessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/CreateAccessor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/CreateAccessor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/CreateAccessor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/CreateAccessor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/CreateAccessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/CreateAccessor)
