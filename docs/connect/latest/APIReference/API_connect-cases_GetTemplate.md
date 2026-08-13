---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html
---

# GetTemplate
<a name="API_connect-cases_GetTemplate"></a>

Returns the details for the requested template. Other template APIs are:
+  [CreateTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html)
+  [DeleteTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html)
+  [ListTemplates](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html)
+  [UpdateTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html)

## Request Syntax
<a name="API_connect-cases_GetTemplate_RequestSyntax"></a>

```
POST /domains/{{domainId}}/templates/{{templateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-cases_GetTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_GetTemplate_RequestSyntax) **   <a name="connect-connect-cases_GetTemplate-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [templateId](#API_connect-cases_GetTemplate_RequestSyntax) **   <a name="connect-connect-cases_GetTemplate-request-uri-templateId"></a>
A unique identifier of a template.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_GetTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-cases_GetTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdTime": "string",
   "deleted": boolean,
   "description": "string",
   "lastModifiedTime": "string",
   "layoutConfiguration": {
      "defaultLayout": "string"
   },
   "name": "string",
   "requiredFields": [
      {
         "fieldId": "string"
      }
   ],
   "rules": [
      {
         "caseRuleId": "string",
         "fieldId": "string"
      }
   ],
   "status": "string",
   "tagPropagationConfigurations": [
      {
         "resourceType": "string",
         "tagMap": {
            "string" : "string"
         }
      }
   ],
   "tags": {
      "string" : "string"
   },
   "templateArn": "string",
   "templateId": "string"
}
```

## Response Elements
<a name="API_connect-cases_GetTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdTime](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-createdTime"></a>
Timestamp at which the resource was created.
Type: Timestamp

 ** [deleted](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-deleted"></a>
Denotes whether or not the resource has been deleted.
Type: Boolean

 ** [description](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-description"></a>
A brief description of the template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [lastModifiedTime](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-lastModifiedTime"></a>
Timestamp at which the resource was created or last modified.
Type: Timestamp

 ** [layoutConfiguration](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-layoutConfiguration"></a>
Configuration of layouts associated to the template.
Type: [LayoutConfiguration](API_connect-cases_LayoutConfiguration.md) object

 ** [name](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-name"></a>
The name of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`

 ** [requiredFields](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-requiredFields"></a>
A list of fields that must contain a value for a case to be successfully created with this template.
Type: Array of [RequiredField](API_connect-cases_RequiredField.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [rules](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-rules"></a>
A list of case rules (also known as [case field conditions](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html)) on a template.
Type: Array of [TemplateRule](API_connect-cases_TemplateRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [status](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-status"></a>
The status of the template.
Type: String
Valid Values: `Active | Inactive`

 ** [tagPropagationConfigurations](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-tagPropagationConfigurations"></a>
Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.
Type: Array of [TagPropagationConfiguration](API_connect-cases_TagPropagationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [tags](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-tags"></a>
A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
Type: String to string map

 ** [templateArn](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-templateArn"></a>
The Amazon Resource Name (ARN) of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [templateId](#API_connect-cases_GetTemplate_ResponseSyntax) **   <a name="connect-connect-cases_GetTemplate-response-templateId"></a>
A unique identifier of a template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_connect-cases_GetTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_GetTemplate_Examples"></a>

### Request and Response example
<a name="API_connect-cases_GetTemplate_Example_1"></a>

This example illustrates one usage of GetTemplate.

```
{ }
```

```
{
  "templateId": "[template_id]",
  "templateArn": "[template_arn]",
  "name": "Shipping",
  "layoutConfiguration": {
  "defaultLayout": "[layout_id]"
    },
  "requiredFields": [
    {
    "fieldId": "[field_id]"
    }
  ],
  "description": "This is an example template for shipping issues",
  "status": "Inactive",
  "tagPropagationConfigurations": [
    {
      "resourceType": "Cases",
      "tagMap": {
        "Department" : "Shipping"
      }
    }
  ]
}
```

## See Also
<a name="API_connect-cases_GetTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/GetTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/GetTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/GetTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/GetTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/GetTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/GetTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/GetTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/GetTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/GetTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/GetTemplate)
