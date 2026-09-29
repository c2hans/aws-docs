---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_GetAssetContract.html
---

# GetAssetContract
<a name="API_GetAssetContract"></a>

**Note**
End of support notice: Amazon Managed Blockchain will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain. For more information, see [Amazon Managed Blockchain availability change](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

Gets the information about a specific contract deployed on the blockchain.

**Note**
The Bitcoin blockchain networks do not support this operation.
Metadata is currently only available for some `ERC-20` contracts. Metadata will be available for additional contracts in the future.

## Request Syntax
<a name="API_GetAssetContract_RequestSyntax"></a>

```
POST /get-asset-contract HTTP/1.1
Content-type: application/json

{
   "contractIdentifier": {
      "contractAddress": "{{string}}",
      "network": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_GetAssetContract_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAssetContract_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [contractIdentifier](#API_GetAssetContract_RequestSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetAssetContract-request-contractIdentifier"></a>
Contains the blockchain address and network information about the contract.
Type: [ContractIdentifier](API_ContractIdentifier.md) object
Required: Yes

## Response Syntax
<a name="API_GetAssetContract_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contractIdentifier": {
      "contractAddress": "string",
      "network": "string"
   },
   "deployerAddress": "string",
   "metadata": {
      "decimals": number,
      "name": "string",
      "symbol": "string"
   },
   "tokenStandard": "string"
}
```

## Response Elements
<a name="API_GetAssetContract_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contractIdentifier](#API_GetAssetContract_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetAssetContract-response-contractIdentifier"></a>
Contains the blockchain address and network information about the contract.
Type: [ContractIdentifier](API_ContractIdentifier.md) object

 ** [deployerAddress](#API_GetAssetContract_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetAssetContract-response-deployerAddress"></a>
The address of the deployer of contract.
Type: String
Pattern: `[-A-Za-z0-9]{13,74}`

 ** [metadata](#API_GetAssetContract_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetAssetContract-response-metadata"></a>
The metadata of the contract.
Type: [ContractMetadata](API_ContractMetadata.md) object

 ** [tokenStandard](#API_GetAssetContract_ResponseSyntax) **   <a name="ManagedBlockchainQueryAPIReference-GetAssetContract-response-tokenStandard"></a>
The token standard of the contract requested.
Type: String
Valid Values: `ERC20 | ERC721 | ERC1155`

## Errors
<a name="API_GetAssetContract_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
The AWS account doesn’t have access to this resource.
 ** message **
The container for the exception message.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The request processing has failed because of an internal error in the service.
 ** message **
The container for the exception message.
 ** retryAfterSeconds **
Specifies the `retryAfterSeconds` value.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The resource was not found.
 ** message **
The container for the exception message.
 ** resourceId **
The `resourceId` of the resource that caused the exception.
 ** resourceType **
The `resourceType` of the resource that caused the exception.
HTTP Status Code: 404

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The service quota has been exceeded for this resource.
 ** message **
The container for the exception message.
 ** quotaCode **
The container for the `quotaCode`.
 ** resourceId **
The `resourceId` of the resource that caused the exception.
 ** resourceType **
The `resourceType` of the resource that caused the exception.
 ** serviceCode **
The container for the `serviceCode`.
HTTP Status Code: 402

 [ThrottlingException](API_ThrottlingException.md)
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.
 ** message **
The container for the exception message.
 ** quotaCode **
The container for the `quotaCode`.
 ** retryAfterSeconds **
The container of the `retryAfterSeconds` value.
 ** serviceCode **
The container for the `serviceCode`.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The resource passed is invalid.
 ** fieldList **
The container for the `fieldList` of the exception.
 ** message **
The container for the exception message.
 ** reason **
The container for the reason for the exception
HTTP Status Code: 400

## See Also
<a name="API_GetAssetContract_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-query-2023-05-04/GetAssetContract)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-query-2023-05-04/GetAssetContract)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/GetAssetContract)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-query-2023-05-04/GetAssetContract)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/GetAssetContract)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-query-2023-05-04/GetAssetContract)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-query-2023-05-04/GetAssetContract)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-query-2023-05-04/GetAssetContract)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-query-2023-05-04/GetAssetContract)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/GetAssetContract)
