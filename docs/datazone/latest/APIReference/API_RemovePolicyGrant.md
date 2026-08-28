---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RemovePolicyGrant.html
---

# RemovePolicyGrant
<a name="API_RemovePolicyGrant"></a>

Removes a policy grant.

## Request Syntax
<a name="API_RemovePolicyGrant_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/policies/managed/{{entityType}}/{{entityIdentifier}}/removeGrant HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "grantIdentifier": "{{string}}",
   "policyType": "{{string}}",
   "principal": { ... }
}
```

## URI Request Parameters
<a name="API_RemovePolicyGrant_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_RemovePolicyGrant_RequestSyntax) **   <a name="datazone-RemovePolicyGrant-request-uri-domainIdentifier"></a>
The ID of the domain where you want to remove a policy grant.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_RemovePolicyGrant_RequestSyntax) **   <a name="datazone-RemovePolicyGrant-request-uri-entityIdentifier"></a>
The ID of the entity from which you want to remove a policy grant.
Required: Yes

 ** [entityType](#API_RemovePolicyGrant_RequestSyntax) **   <a name="datazone-RemovePolicyGrant-request-uri-entityType"></a>
The type of the entity from which you want to remove a policy grant.
Valid Values: `DOMAIN_UNIT | ENVIRONMENT_BLUEPRINT_CONFIGURATION | ENVIRONMENT_PROFILE | ASSET_TYPE`
Required: Yes

## Request Body
<a name="API_RemovePolicyGrant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_RemovePolicyGrant_RequestSyntax) **   <a name="datazone-RemovePolicyGrant-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [grantIdentifier](#API_RemovePolicyGrant_RequestSyntax) **   <a name="datazone-RemovePolicyGrant-request-grantIdentifier"></a>
The ID of the policy grant that is to be removed from a specified entity.
Type: String
Pattern: `[A-Za-z0-9+/]{10}`
Required: No

 ** [policyType](#API_RemovePolicyGrant_RequestSyntax) **   <a name="datazone-RemovePolicyGrant-request-policyType"></a>
The type of the policy that you want to remove.
Type: String
Valid Values: `CREATE_DOMAIN_UNIT | OVERRIDE_DOMAIN_UNIT_OWNERS | ADD_TO_PROJECT_MEMBER_POOL | OVERRIDE_PROJECT_OWNERS | CREATE_GLOSSARY | CREATE_FORM_TYPE | CREATE_ASSET_TYPE | CREATE_PROJECT | CREATE_ENVIRONMENT_PROFILE | DELEGATE_CREATE_ENVIRONMENT_PROFILE | CREATE_ENVIRONMENT | CREATE_ENVIRONMENT_FROM_BLUEPRINT | CREATE_PROJECT_FROM_PROJECT_PROFILE | USE_ASSET_TYPE`
Required: Yes

 ** [principal](#API_RemovePolicyGrant_RequestSyntax) **   <a name="datazone-RemovePolicyGrant-request-principal"></a>
The principal from which you want to remove a policy grant.
Type: [PolicyGrantPrincipal](API_PolicyGrantPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_RemovePolicyGrant_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_RemovePolicyGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_RemovePolicyGrant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_RemovePolicyGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/RemovePolicyGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/RemovePolicyGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RemovePolicyGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/RemovePolicyGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RemovePolicyGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/RemovePolicyGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/RemovePolicyGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/RemovePolicyGrant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/RemovePolicyGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RemovePolicyGrant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
