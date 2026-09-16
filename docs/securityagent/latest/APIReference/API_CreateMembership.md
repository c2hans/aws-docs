---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CreateMembership.html
---

# CreateMembership
<a name="API_CreateMembership"></a>

Creates a new membership, granting a user access to an agent space within an application.

## Request Syntax
<a name="API_CreateMembership_RequestSyntax"></a>

```
POST /CreateMembership HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "applicationId": "{{string}}",
   "config": { ... },
   "membershipId": "{{string}}",
   "memberType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateMembership_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_CreateMembership_RequestSyntax) **   <a name="securityagent-CreateMembership-request-agentSpaceId"></a>
The unique identifier of the agent space to grant access to.
Type: String
Required: Yes

 ** [applicationId](#API_CreateMembership_RequestSyntax) **   <a name="securityagent-CreateMembership-request-applicationId"></a>
The unique identifier of the application that contains the agent space.
Type: String
Required: Yes

 ** [config](#API_CreateMembership_RequestSyntax) **   <a name="securityagent-CreateMembership-request-config"></a>
The configuration for the membership, such as the user role.
Type: [MembershipConfig](API_MembershipConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [membershipId](#API_CreateMembership_RequestSyntax) **   <a name="securityagent-CreateMembership-request-membershipId"></a>
The unique identifier for the membership.
Type: String
Required: Yes

 ** [memberType](#API_CreateMembership_RequestSyntax) **   <a name="securityagent-CreateMembership-request-memberType"></a>
The type of member. Currently, only USER is supported.
Type: String
Valid Values: `USER`
Required: Yes

## Response Syntax
<a name="API_CreateMembership_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateMembership_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/CreateMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/CreateMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CreateMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/CreateMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CreateMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/CreateMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/CreateMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/CreateMembership)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/CreateMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CreateMembership)
