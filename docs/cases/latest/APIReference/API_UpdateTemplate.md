---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateTemplate.html
---

# UpdateTemplate
<a name="API_connect-cases_UpdateTemplate"></a>

Updates the attributes of an existing template. The template attributes that can be modified include `name`, `description`, `layoutConfiguration`, `requiredFields`, and `status`. At least one of these attributes must not be null. If a null value is provided for a given attribute, that attribute is ignored and its current value is preserved.

Other template APIs are:
+  [CreateTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html)
+  [DeleteTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html)
+  [GetTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html)
+  [ListTemplates](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html)

## Request Syntax
<a name="API_connect-cases_UpdateTemplate_RequestSyntax"></a>

```
PUT /domains/{{domainId}}/templates/{{templateId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "layoutConfiguration": {
      "defaultLayout": "{{string}}"
   },
   "name": "{{string}}",
   "requiredFields": [
      {
         "fieldId": "{{string}}"
      }
   ],
   "rules": [
      {
         "caseRuleId": "{{string}}",
         "fieldId": "{{string}}"
      }
   ],
   "status": "{{string}}",
   "tagPropagationConfigurations": [
      {
         "resourceType": "{{string}}",
         "tagMap": {
            "{{string}}" : "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_connect-cases_UpdateTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_UpdateTemplate_RequestSyntax) **   <a name="connect-connect-cases_UpdateTemplate-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [templateId](#API_connect-cases_UpdateTemplate_RequestSyntax) **   <a name="connect-connect-cases_UpdateTemplate-request-uri-templateId"></a>
A unique identifier for the template.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_UpdateTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_connect-cases_UpdateTemplate_RequestSyntax) **   <a name="connect-connect-cases_UpdateTemplate-request-description"></a>
A brief description of the template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [layoutConfiguration](#API_connect-cases_UpdateTemplate_RequestSyntax) **   <a name="connect-connect-cases_UpdateTemplate-request-layoutConfiguration"></a>
Configuration of layouts associated to the template.
Type: [LayoutConfiguration](API_connect-cases_LayoutConfiguration.md) object
Required: No

 ** [name](#API_connect-cases_UpdateTemplate_RequestSyntax) **   <a name="connect-connect-cases_UpdateTemplate-request-name"></a>
The name of the template. It must be unique per domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: No

 ** [requiredFields](#API_connect-cases_UpdateTemplate_RequestSyntax) **   <a name="connect-connect-cases_UpdateTemplate-request-requiredFields"></a>
A list of fields that must contain a value for a case to be successfully created with this template.
To require a Customer Profile when creating cases, include `customer_id` in this list. If `customer_id` is omitted, the Customer Profile field is optional and can be added, changed, or removed after case creation.
Type: Array of [RequiredField](API_connect-cases_RequiredField.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [rules](#API_connect-cases_UpdateTemplate_RequestSyntax) **   <a name="connect-connect-cases_UpdateTemplate-request-rules"></a>
A list of case rules (also known as [case field conditions](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html)) on a template.
Type: Array of [TemplateRule](API_connect-cases_TemplateRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [status](#API_connect-cases_UpdateTemplate_RequestSyntax) **   <a name="connect-connect-cases_UpdateTemplate-request-status"></a>
The status of the template.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** [tagPropagationConfigurations](#API_connect-cases_UpdateTemplate_RequestSyntax) **   <a name="connect-connect-cases_UpdateTemplate-request-tagPropagationConfigurations"></a>
Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.
Type: Array of [TagPropagationConfiguration](API_connect-cases_TagPropagationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_connect-cases_UpdateTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-cases_UpdateTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-cases_UpdateTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.
HTTP Status Code: 409

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded. For a list of service quotas, see [Connect Customer Service Quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) in the *Connect Customer Administrator Guide*.
HTTP Status Code: 402

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_UpdateTemplate_Examples"></a>

### Request and Response example
<a name="API_connect-cases_UpdateTemplate_Example_1"></a>

This example illustrates one usage of UpdateTemplate.

```
{
  "name": "updated_template_name",
  "tagPropagationConfigurations": [
    {
      "resourceType": "Cases",
      "tagMap": {
        "Department" : "UpdatedShipping"
      }
    }
  ]
}
```

```
{ }
```

## See Also
<a name="API_connect-cases_UpdateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/UpdateTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/UpdateTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/UpdateTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/UpdateTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/UpdateTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/UpdateTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/UpdateTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/UpdateTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/UpdateTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/UpdateTemplate)
