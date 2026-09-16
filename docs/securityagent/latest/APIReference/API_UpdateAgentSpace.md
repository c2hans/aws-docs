---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateAgentSpace.html
---

# UpdateAgentSpace
<a name="API_UpdateAgentSpace"></a>

Updates the configuration of an existing agent space, including its name, description, AWS resources, target domains, and code review settings.

## Request Syntax
<a name="API_UpdateAgentSpace_RequestSyntax"></a>

```
POST /UpdateAgentSpace HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
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
   "name": "{{string}}",
   "targetDomainIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateAgentSpace_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAgentSpace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_UpdateAgentSpace_RequestSyntax) **   <a name="securityagent-UpdateAgentSpace-request-agentSpaceId"></a>
The unique identifier of the agent space to update.
Type: String
Required: Yes

 ** [awsResources](#API_UpdateAgentSpace_RequestSyntax) **   <a name="securityagent-UpdateAgentSpace-request-awsResources"></a>
The updated AWS resources to associate with the agent space.
Type: [AWSResources](API_AWSResources.md) object
Required: No

 ** [codeReviewSettings](#API_UpdateAgentSpace_RequestSyntax) **   <a name="securityagent-UpdateAgentSpace-request-codeReviewSettings"></a>
The updated code review settings for the agent space.
Type: [CodeReviewSettings](API_CodeReviewSettings.md) object
Required: No

 ** [description](#API_UpdateAgentSpace_RequestSyntax) **   <a name="securityagent-UpdateAgentSpace-request-description"></a>
The updated description of the agent space.
Type: String
Required: No

 ** [name](#API_UpdateAgentSpace_RequestSyntax) **   <a name="securityagent-UpdateAgentSpace-request-name"></a>
The updated name of the agent space.
Type: String
Required: No

 ** [targetDomainIds](#API_UpdateAgentSpace_RequestSyntax) **   <a name="securityagent-UpdateAgentSpace-request-targetDomainIds"></a>
The updated list of target domain identifiers to associate with the agent space.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_UpdateAgentSpace_ResponseSyntax"></a>

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
   "name": "string",
   "targetDomainIds": [ "string" ],
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateAgentSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceId](#API_UpdateAgentSpace_ResponseSyntax) **   <a name="securityagent-UpdateAgentSpace-response-agentSpaceId"></a>
The unique identifier of the updated agent space.
Type: String

 ** [awsResources](#API_UpdateAgentSpace_ResponseSyntax) **   <a name="securityagent-UpdateAgentSpace-response-awsResources"></a>
The AWS resources associated with the agent space.
Type: [AWSResources](API_AWSResources.md) object

 ** [codeReviewSettings](#API_UpdateAgentSpace_ResponseSyntax) **   <a name="securityagent-UpdateAgentSpace-response-codeReviewSettings"></a>
The code review settings for the agent space.
Type: [CodeReviewSettings](API_CodeReviewSettings.md) object

 ** [createdAt](#API_UpdateAgentSpace_ResponseSyntax) **   <a name="securityagent-UpdateAgentSpace-response-createdAt"></a>
The date and time the agent space was created, in UTC format.
Type: Timestamp

 ** [description](#API_UpdateAgentSpace_ResponseSyntax) **   <a name="securityagent-UpdateAgentSpace-response-description"></a>
The description of the agent space.
Type: String

 ** [name](#API_UpdateAgentSpace_ResponseSyntax) **   <a name="securityagent-UpdateAgentSpace-response-name"></a>
The name of the agent space.
Type: String

 ** [targetDomainIds](#API_UpdateAgentSpace_ResponseSyntax) **   <a name="securityagent-UpdateAgentSpace-response-targetDomainIds"></a>
The list of target domain identifiers associated with the agent space.
Type: Array of strings

 ** [updatedAt](#API_UpdateAgentSpace_ResponseSyntax) **   <a name="securityagent-UpdateAgentSpace-response-updatedAt"></a>
The date and time the agent space was last updated, in UTC format.
Type: Timestamp

## Errors
<a name="API_UpdateAgentSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UpdateAgentSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdateAgentSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdateAgentSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateAgentSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdateAgentSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateAgentSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdateAgentSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdateAgentSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdateAgentSpace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdateAgentSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateAgentSpace)
