---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateEnvironmentTemplate.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CreateEnvironmentTemplate
<a name="API_CreateEnvironmentTemplate"></a>

Create an environment template for AWS Proton. For more information, see [Environment Templates](https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html) in the * AWS Proton User Guide*.

You can create an environment template in one of the two following ways:
+ Register and publish a *standard* environment template that instructs AWS Proton to deploy and manage environment infrastructure.
+ Register and publish a *customer managed* environment template that connects AWS Proton to your existing provisioned infrastructure that you manage. AWS Proton *doesn't* manage your existing provisioned infrastructure. To create an environment template for customer provisioned and managed infrastructure, include the `provisioning` parameter and set the value to `CUSTOMER_MANAGED`. For more information, see [Register and publish an environment template](https://docs.aws.amazon.com/proton/latest/userguide/template-create.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_CreateEnvironmentTemplate_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "displayName": "{{string}}",
   "encryptionKey": "{{string}}",
   "name": "{{string}}",
   "provisioning": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateEnvironmentTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateEnvironmentTemplate_RequestSyntax) **   <a name="proton-CreateEnvironmentTemplate-request-description"></a>
A description of the environment template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [displayName](#API_CreateEnvironmentTemplate_RequestSyntax) **   <a name="proton-CreateEnvironmentTemplate-request-displayName"></a>
The environment template name as displayed in the developer interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [encryptionKey](#API_CreateEnvironmentTemplate_RequestSyntax) **   <a name="proton-CreateEnvironmentTemplate-request-encryptionKey"></a>
A customer provided encryption key that AWS Proton uses to encrypt data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** [name](#API_CreateEnvironmentTemplate_RequestSyntax) **   <a name="proton-CreateEnvironmentTemplate-request-name"></a>
The name of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [provisioning](#API_CreateEnvironmentTemplate_RequestSyntax) **   <a name="proton-CreateEnvironmentTemplate-request-provisioning"></a>
When included, indicates that the environment template is for customer provisioned and managed infrastructure.
Type: String
Valid Values: `CUSTOMER_MANAGED`
Required: No

 ** [tags](#API_CreateEnvironmentTemplate_RequestSyntax) **   <a name="proton-CreateEnvironmentTemplate-request-tags"></a>
An optional list of metadata items that you can associate with the AWS Proton environment template. A tag is a key-value pair.
For more information, see [AWS Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the * AWS Proton User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateEnvironmentTemplate_ResponseSyntax"></a>

```
{
   "environmentTemplate": {
      "arn": "string",
      "createdAt": number,
      "description": "string",
      "displayName": "string",
      "encryptionKey": "string",
      "lastModifiedAt": number,
      "name": "string",
      "provisioning": "string",
      "recommendedVersion": "string"
   }
}
```

## Response Elements
<a name="API_CreateEnvironmentTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentTemplate](#API_CreateEnvironmentTemplate_ResponseSyntax) **   <a name="proton-CreateEnvironmentTemplate-response-environmentTemplate"></a>
The environment template detail data that's returned by AWS Proton.
Type: [EnvironmentTemplate](API_EnvironmentTemplate.md) object

## Errors
<a name="API_CreateEnvironmentTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** ConflictException **
The request *couldn't* be made due to a conflicting operation or resource.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
A quota was exceeded. For more information, see [AWS Proton Quotas](https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html) in the * AWS Proton User Guide*.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_CreateEnvironmentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CreateEnvironmentTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CreateEnvironmentTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CreateEnvironmentTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CreateEnvironmentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CreateEnvironmentTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CreateEnvironmentTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CreateEnvironmentTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CreateEnvironmentTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CreateEnvironmentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CreateEnvironmentTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
