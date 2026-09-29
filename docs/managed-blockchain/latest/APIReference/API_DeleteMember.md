---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_DeleteMember.html
---

# DeleteMember
<a name="API_DeleteMember"></a>

**Note**
End of support notice: Amazon Managed Blockchain will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain. For more information, see [Amazon Managed Blockchain availability change](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

Deletes a member. Deleting a member removes the member and all associated resources from the network. `DeleteMember` can only be called for a specified `MemberId` if the principal performing the action is associated with the AWS account that owns the member. In all other cases, the `DeleteMember` action is carried out as the result of an approved proposal to remove a member. If `MemberId` is the last member in a network specified by the last AWS account, the network is deleted also.

Applies only to Hyperledger Fabric.

## Request Syntax
<a name="API_DeleteMember_RequestSyntax"></a>

```
DELETE /networks/{{networkId}}/members/{{memberId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteMember_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memberId](#API_DeleteMember_RequestSyntax) **   <a name="ManagedBlockchain-DeleteMember-request-uri-MemberId"></a>
The unique identifier of the member to remove.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [networkId](#API_DeleteMember_RequestSyntax) **   <a name="ManagedBlockchain-DeleteMember-request-uri-NetworkId"></a>
The unique identifier of the network from which the member is removed.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Request Body
<a name="API_DeleteMember_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteMember_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteMember_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteMember_Errors"></a>

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

 ** ResourceNotFoundException **
A requested resource doesn't exist. It may have been deleted or referenced incorrectly.
 ** ResourceName **
A requested resource doesn't exist. It may have been deleted or referenced inaccurately.
HTTP Status Code: 404

 ** ResourceNotReadyException **
The requested resource exists but isn't in a status that can complete the operation.
HTTP Status Code: 409

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.
HTTP Status Code: 429

## See Also
<a name="API_DeleteMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/DeleteMember)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/DeleteMember)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/DeleteMember)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/DeleteMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/DeleteMember)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/DeleteMember)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/DeleteMember)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/DeleteMember)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/DeleteMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/DeleteMember)
