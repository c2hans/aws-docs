---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateNetwork.html
---

# CreateNetwork
<a name="API_CreateNetwork"></a>

**Note**
End of support notice: Amazon Managed Blockchain will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain. For more information, see [Amazon Managed Blockchain availability change](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

Creates a new blockchain network using Amazon Managed Blockchain.

Applies only to Hyperledger Fabric.

## Request Syntax
<a name="API_CreateNetwork_RequestSyntax"></a>

```
POST /networks HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "Framework": "{{string}}",
   "FrameworkConfiguration": {
      "Fabric": {
         "Edition": "{{string}}"
      }
   },
   "FrameworkVersion": "{{string}}",
   "MemberConfiguration": {
      "Description": "{{string}}",
      "FrameworkConfiguration": {
         "Fabric": {
            "AdminPassword": "{{string}}",
            "AdminUsername": "{{string}}"
         }
      },
      "KmsKeyArn": "{{string}}",
      "LogPublishingConfiguration": {
         "Fabric": {
            "CaLogs": {
               "Cloudwatch": {
                  "Enabled": {{boolean}}
               }
            }
         }
      },
      "Name": "{{string}}",
      "Tags": {
         "{{string}}" : "{{string}}"
      }
   },
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "VotingPolicy": {
      "ApprovalThresholdPolicy": {
         "ProposalDurationInHours": {{number}},
         "ThresholdComparator": "{{string}}",
         "ThresholdPercentage": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateNetwork_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateNetwork_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateNetwork_RequestSyntax) **   <a name="ManagedBlockchain-CreateNetwork-request-ClientRequestToken"></a>
This is a unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an AWS SDK or the AWS CLI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Description](#API_CreateNetwork_RequestSyntax) **   <a name="ManagedBlockchain-CreateNetwork-request-Description"></a>
An optional description for the network.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** [Framework](#API_CreateNetwork_RequestSyntax) **   <a name="ManagedBlockchain-CreateNetwork-request-Framework"></a>
The blockchain framework that the network uses.
Type: String
Valid Values: `HYPERLEDGER_FABRIC | ETHEREUM`
Required: Yes

 ** [FrameworkConfiguration](#API_CreateNetwork_RequestSyntax) **   <a name="ManagedBlockchain-CreateNetwork-request-FrameworkConfiguration"></a>
 Configuration properties of the blockchain framework relevant to the network configuration.
Type: [NetworkFrameworkConfiguration](API_NetworkFrameworkConfiguration.md) object
Required: No

 ** [FrameworkVersion](#API_CreateNetwork_RequestSyntax) **   <a name="ManagedBlockchain-CreateNetwork-request-FrameworkVersion"></a>
The version of the blockchain framework that the network uses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Required: Yes

 ** [MemberConfiguration](#API_CreateNetwork_RequestSyntax) **   <a name="ManagedBlockchain-CreateNetwork-request-MemberConfiguration"></a>
Configuration properties for the first member within the network.
Type: [MemberConfiguration](API_MemberConfiguration.md) object
Required: Yes

 ** [Name](#API_CreateNetwork_RequestSyntax) **   <a name="ManagedBlockchain-CreateNetwork-request-Name"></a>
The name of the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

 ** [Tags](#API_CreateNetwork_RequestSyntax) **   <a name="ManagedBlockchain-CreateNetwork-request-Tags"></a>
Tags to assign to the network.
 Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [VotingPolicy](#API_CreateNetwork_RequestSyntax) **   <a name="ManagedBlockchain-CreateNetwork-request-VotingPolicy"></a>
 The voting rules used by the network to determine if a proposal is approved.
Type: [VotingPolicy](API_VotingPolicy.md) object
Required: Yes

## Response Syntax
<a name="API_CreateNetwork_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MemberId": "string",
   "NetworkId": "string"
}
```

## Response Elements
<a name="API_CreateNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MemberId](#API_CreateNetwork_ResponseSyntax) **   <a name="ManagedBlockchain-CreateNetwork-response-MemberId"></a>
The unique identifier for the first member within the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.

 ** [NetworkId](#API_CreateNetwork_ResponseSyntax) **   <a name="ManagedBlockchain-CreateNetwork-response-NetworkId"></a>
The unique identifier for the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.

## Errors
<a name="API_CreateNetwork_Errors"></a>

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
<a name="API_CreateNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/CreateNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/CreateNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/CreateNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/CreateNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/CreateNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/CreateNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/CreateNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/CreateNetwork)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/CreateNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/CreateNetwork)
