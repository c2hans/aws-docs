---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_UpdateTemplate.html
---

# UpdateTemplate
<a name="API_UpdateTemplate"></a>

Update template configuration to define the information included in certificates.

## Request Syntax
<a name="API_UpdateTemplate_RequestSyntax"></a>

```
PATCH /templates/{{TemplateArn}} HTTP/1.1
Content-type: application/json

{
   "Definition": { ... },
   "ReenrollAllCertificateHolders": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TemplateArn](#API_UpdateTemplate_RequestSyntax) **   <a name="PcaConnectorAd-UpdateTemplate-request-uri-TemplateArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html).
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/template\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Definition](#API_UpdateTemplate_RequestSyntax) **   <a name="PcaConnectorAd-UpdateTemplate-request-Definition"></a>
Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.
Type: [TemplateDefinition](API_TemplateDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [ReenrollAllCertificateHolders](#API_UpdateTemplate_RequestSyntax) **   <a name="PcaConnectorAd-UpdateTemplate-request-ReenrollAllCertificateHolders"></a>
This setting allows the major version of a template to be increased automatically. All members of Active Directory groups that are allowed to enroll with a template will receive a new certificate issued using that template.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your AWS Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an AWS Organizations service control policy (SCP) that affects your AWS account.
HTTP Status Code: 403

 ** ConflictException **
This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.
 ** ResourceId **
The identifier of the AWS resource.
 ** ResourceType **
The resource type, which can be one of `Connector`, `Template`, `TemplateGroupAccessControlEntry`, `ServicePrincipalName`, or `DirectoryRegistration`.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.
 ** ResourceId **
The identifier of the AWS resource.
 ** ResourceType **
The resource type, which can be one of `Connector`, `Template`, `TemplateGroupAccessControlEntry`, `ServicePrincipalName`, or `DirectoryRegistration`.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** QuotaCode **
The code associated with the quota.
 ** ServiceCode **
Identifies the originating service.
HTTP Status Code: 429

 ** ValidationException **
An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid.
 ** Reason **
The reason for the validation error. This won't be return for every validation exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pca-connector-ad-2018-05-10/UpdateTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pca-connector-ad-2018-05-10/UpdateTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/UpdateTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pca-connector-ad-2018-05-10/UpdateTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/UpdateTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pca-connector-ad-2018-05-10/UpdateTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pca-connector-ad-2018-05-10/UpdateTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pca-connector-ad-2018-05-10/UpdateTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pca-connector-ad-2018-05-10/UpdateTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/UpdateTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
