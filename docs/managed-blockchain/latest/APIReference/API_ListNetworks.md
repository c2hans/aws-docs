---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListNetworks.html
---

# ListNetworks
<a name="API_ListNetworks"></a>

Returns information about the networks in which the current AWS account participates.

Applies to Hyperledger Fabric and Ethereum.

## Request Syntax
<a name="API_ListNetworks_RequestSyntax"></a>

```
GET /networks?framework={{Framework}}&maxResults={{MaxResults}}&name={{Name}}&nextToken={{NextToken}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNetworks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Framework](#API_ListNetworks_RequestSyntax) **   <a name="ManagedBlockchain-ListNetworks-request-uri-Framework"></a>
An optional framework specifier. If provided, only networks of this framework type are listed.
Valid Values: `HYPERLEDGER_FABRIC | ETHEREUM`

 ** [MaxResults](#API_ListNetworks_RequestSyntax) **   <a name="ManagedBlockchain-ListNetworks-request-uri-MaxResults"></a>
The maximum number of networks to list.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [Name](#API_ListNetworks_RequestSyntax) **   <a name="ManagedBlockchain-ListNetworks-request-uri-Name"></a>
The name of the network.

 ** [NextToken](#API_ListNetworks_RequestSyntax) **   <a name="ManagedBlockchain-ListNetworks-request-uri-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Length Constraints: Maximum length of 128.

 ** [Status](#API_ListNetworks_RequestSyntax) **   <a name="ManagedBlockchain-ListNetworks-request-uri-Status"></a>
An optional status specifier. If provided, only networks currently in this status are listed.
Applies only to Hyperledger Fabric.
Valid Values: `CREATING | AVAILABLE | CREATE_FAILED | DELETING | DELETED`

## Request Body
<a name="API_ListNetworks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNetworks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Networks": [
      {
         "Arn": "string",
         "CreationDate": "string",
         "Description": "string",
         "Framework": "string",
         "FrameworkVersion": "string",
         "Id": "string",
         "Name": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListNetworks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Networks](#API_ListNetworks_ResponseSyntax) **   <a name="ManagedBlockchain-ListNetworks-response-Networks"></a>
An array of `NetworkSummary` objects that contain configuration properties for each network.
Type: Array of [NetworkSummary](API_NetworkSummary.md) objects

 ** [NextToken](#API_ListNetworks_ResponseSyntax) **   <a name="ManagedBlockchain-ListNetworks-response-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Maximum length of 128.

## Errors
<a name="API_ListNetworks_Errors"></a>

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

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.
HTTP Status Code: 429

## See Also
<a name="API_ListNetworks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/ListNetworks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/ListNetworks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/ListNetworks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/ListNetworks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/ListNetworks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/ListNetworks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/ListNetworks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/ListNetworks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/ListNetworks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/ListNetworks)
