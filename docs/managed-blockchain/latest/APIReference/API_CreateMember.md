---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateMember.html
---

# CreateMember
<a name="API_CreateMember"></a>

Creates a member within a Managed Blockchain network.

Applies only to Hyperledger Fabric.

## Request Syntax
<a name="API_CreateMember_RequestSyntax"></a>

```
POST /networks/{{networkId}}/members HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "InvitationId": "{{string}}",
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
   }
}
```

## URI Request Parameters
<a name="API_CreateMember_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_CreateMember_RequestSyntax) **   <a name="ManagedBlockchain-CreateMember-request-uri-NetworkId"></a>
The unique identifier of the network in which the member is created.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Request Body
<a name="API_CreateMember_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateMember_RequestSyntax) **   <a name="ManagedBlockchain-CreateMember-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an AWS SDK or the AWS CLI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [InvitationId](#API_CreateMember_RequestSyntax) **   <a name="ManagedBlockchain-CreateMember-request-InvitationId"></a>
The unique identifier of the invitation that is sent to the member to join the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [MemberConfiguration](#API_CreateMember_RequestSyntax) **   <a name="ManagedBlockchain-CreateMember-request-MemberConfiguration"></a>
Member configuration parameters.
Type: [MemberConfiguration](API_MemberConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_CreateMember_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MemberId": "string"
}
```

## Response Elements
<a name="API_CreateMember_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MemberId](#API_CreateMember_ResponseSyntax) **   <a name="ManagedBlockchain-CreateMember-response-MemberId"></a>
The unique identifier of the member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.

## Errors
<a name="API_CreateMember_Errors"></a>

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

 ** TooManyTagsException **

 ** ResourceName **

HTTP Status Code: 400

## See Also
<a name="API_CreateMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/CreateMember)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/CreateMember)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/CreateMember)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/CreateMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/CreateMember)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/CreateMember)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/CreateMember)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/CreateMember)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/CreateMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/CreateMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
