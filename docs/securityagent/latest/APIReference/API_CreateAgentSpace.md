---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CreateAgentSpace.html
---

# CreateAgentSpace
<a name="API_CreateAgentSpace"></a>

Creates a new agent space. An agent space is a dedicated workspace for securing a specific application.

## Request Syntax
<a name="API_CreateAgentSpace_RequestSyntax"></a>

```
POST /CreateAgentSpace HTTP/1.1
Content-type: application/json

{
   "awsResources": {
      "iamRoles": [ "{{string}}" ],
      "lambdaFunctionArns": [ "{{string}}" ],
      "logGroups": [ "{{string}}" ],
      "s3Buckets": [ "{{string}}" ],
      "secretArns": [ "{{string}}" ],
      "vpcs": [
         {
            "securityGroupArns": [ "{{string}}" ],
            "subnetArns": [ "{{string}}" ],
            "vpcArn": "{{string}}"
         }
      ]
   },
   "codeReviewSettings": {
      "controlsScanning": {{boolean}},
      "generalPurposeScanning": {{boolean}}
   },
   "description": "{{string}}",
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targetDomainIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_CreateAgentSpace_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAgentSpace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [awsResources](#API_CreateAgentSpace_RequestSyntax) **   <a name="securityagent-CreateAgentSpace-request-awsResources"></a>
The AWS resources to associate with the agent space.
Type: [AWSResources](API_AWSResources.md) object
Required: No

 ** [codeReviewSettings](#API_CreateAgentSpace_RequestSyntax) **   <a name="securityagent-CreateAgentSpace-request-codeReviewSettings"></a>
The code review settings for the agent space.
Type: [CodeReviewSettings](API_CodeReviewSettings.md) object
Required: No

 ** [description](#API_CreateAgentSpace_RequestSyntax) **   <a name="securityagent-CreateAgentSpace-request-description"></a>
A description of the agent space.
Type: String
Required: No

 ** [kmsKeyId](#API_CreateAgentSpace_RequestSyntax) **   <a name="securityagent-CreateAgentSpace-request-kmsKeyId"></a>
The identifier of the AWS KMS key to use for encrypting data in the agent space.
Type: String
Required: No

 ** [name](#API_CreateAgentSpace_RequestSyntax) **   <a name="securityagent-CreateAgentSpace-request-name"></a>
The name of the agent space.
Type: String
Required: Yes

 ** [tags](#API_CreateAgentSpace_RequestSyntax) **   <a name="securityagent-CreateAgentSpace-request-tags"></a>
The tags to associate with the agent space.
Type: String to string map
Required: No

 ** [targetDomainIds](#API_CreateAgentSpace_RequestSyntax) **   <a name="securityagent-CreateAgentSpace-request-targetDomainIds"></a>
The list of target domain identifiers to associate with the agent space.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_CreateAgentSpace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaceId": "string",
   "awsResources": {
      "iamRoles": [ "string" ],
      "lambdaFunctionArns": [ "string" ],
      "logGroups": [ "string" ],
      "s3Buckets": [ "string" ],
      "secretArns": [ "string" ],
      "vpcs": [
         {
            "securityGroupArns": [ "string" ],
            "subnetArns": [ "string" ],
            "vpcArn": "string"
         }
      ]
   },
   "codeReviewSettings": {
      "controlsScanning": boolean,
      "generalPurposeScanning": boolean
   },
   "createdAt": "string",
   "description": "string",
   "kmsKeyId": "string",
   "name": "string",
   "targetDomainIds": [ "string" ],
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_CreateAgentSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceId](#API_CreateAgentSpace_ResponseSyntax) **   <a name="securityagent-CreateAgentSpace-response-agentSpaceId"></a>
The unique identifier of the created agent space.
Type: String

 ** [awsResources](#API_CreateAgentSpace_ResponseSyntax) **   <a name="securityagent-CreateAgentSpace-response-awsResources"></a>
The AWS resources associated with the agent space.
Type: [AWSResources](API_AWSResources.md) object

 ** [codeReviewSettings](#API_CreateAgentSpace_ResponseSyntax) **   <a name="securityagent-CreateAgentSpace-response-codeReviewSettings"></a>
The code review settings for the agent space.
Type: [CodeReviewSettings](API_CodeReviewSettings.md) object

 ** [createdAt](#API_CreateAgentSpace_ResponseSyntax) **   <a name="securityagent-CreateAgentSpace-response-createdAt"></a>
The date and time the agent space was created, in UTC format.
Type: Timestamp

 ** [description](#API_CreateAgentSpace_ResponseSyntax) **   <a name="securityagent-CreateAgentSpace-response-description"></a>
The description of the agent space.
Type: String

 ** [kmsKeyId](#API_CreateAgentSpace_ResponseSyntax) **   <a name="securityagent-CreateAgentSpace-response-kmsKeyId"></a>
The identifier of the AWS KMS key used to encrypt data in the agent space.
Type: String

 ** [name](#API_CreateAgentSpace_ResponseSyntax) **   <a name="securityagent-CreateAgentSpace-response-name"></a>
The name of the agent space.
Type: String

 ** [targetDomainIds](#API_CreateAgentSpace_ResponseSyntax) **   <a name="securityagent-CreateAgentSpace-response-targetDomainIds"></a>
The list of target domain identifiers associated with the agent space.
Type: Array of strings

 ** [updatedAt](#API_CreateAgentSpace_ResponseSyntax) **   <a name="securityagent-CreateAgentSpace-response-updatedAt"></a>
The date and time the agent space was last updated, in UTC format.
Type: Timestamp

## Errors
<a name="API_CreateAgentSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateAgentSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/CreateAgentSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/CreateAgentSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CreateAgentSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/CreateAgentSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CreateAgentSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/CreateAgentSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/CreateAgentSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/CreateAgentSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/CreateAgentSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CreateAgentSpace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
