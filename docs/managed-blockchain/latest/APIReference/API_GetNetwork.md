---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetNetwork.html
---

# GetNetwork
<a name="API_GetNetwork"></a>

Returns detailed information about a network.

Applies to Hyperledger Fabric and Ethereum.

## Request Syntax
<a name="API_GetNetwork_RequestSyntax"></a>

```
GET /networks/{{networkId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNetwork_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_GetNetwork_RequestSyntax) **   <a name="ManagedBlockchain-GetNetwork-request-uri-NetworkId"></a>
The unique identifier of the network to get information about.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Request Body
<a name="API_GetNetwork_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNetwork_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Network": {
      "Arn": "string",
      "CreationDate": "string",
      "Description": "string",
      "Framework": "string",
      "FrameworkAttributes": {
         "Ethereum": {
            "ChainId": "string"
         },
         "Fabric": {
            "Edition": "string",
            "OrderingServiceEndpoint": "string"
         }
      },
      "FrameworkVersion": "string",
      "Id": "string",
      "Name": "string",
      "Status": "string",
      "Tags": {
         "string" : "string"
      },
      "VotingPolicy": {
         "ApprovalThresholdPolicy": {
            "ProposalDurationInHours": number,
            "ThresholdComparator": "string",
            "ThresholdPercentage": number
         }
      },
      "VpcEndpointServiceName": "string"
   }
}
```

## Response Elements
<a name="API_GetNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Network](#API_GetNetwork_ResponseSyntax) **   <a name="ManagedBlockchain-GetNetwork-response-Network"></a>
An object containing network configuration parameters.
Type: [Network](API_Network.md) object

## Errors
<a name="API_GetNetwork_Errors"></a>

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

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.
HTTP Status Code: 429

## See Also
<a name="API_GetNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/GetNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/GetNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/GetNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/GetNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/GetNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/GetNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/GetNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/GetNetwork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/GetNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/GetNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
