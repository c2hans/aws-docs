---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreatePrivacyBudgetTemplate.html
---

# CreatePrivacyBudgetTemplate
<a name="API_CreatePrivacyBudgetTemplate"></a>

Creates a privacy budget template for a specified collaboration. Each collaboration can have only one privacy budget template. If you need to change the privacy budget template, use the [UpdatePrivacyBudgetTemplate](API_UpdatePrivacyBudgetTemplate.md) operation.

## Request Syntax
<a name="API_CreatePrivacyBudgetTemplate_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/privacybudgettemplates HTTP/1.1
Content-type: application/json

{
   "autoRefresh": "{{string}}",
   "parameters": { ... },
   "privacyBudgetType": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePrivacyBudgetTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_CreatePrivacyBudgetTemplate_RequestSyntax) **   <a name="API-CreatePrivacyBudgetTemplate-request-uri-membershipIdentifier"></a>
A unique identifier for one of your memberships for a collaboration. The privacy budget template is created in the collaboration that this membership belongs to. Accepts a membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreatePrivacyBudgetTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [autoRefresh](#API_CreatePrivacyBudgetTemplate_RequestSyntax) **   <a name="API-CreatePrivacyBudgetTemplate-request-autoRefresh"></a>
How often the privacy budget refreshes.
If you plan to regularly bring new data into the collaboration, you can use `CALENDAR_MONTH` to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queries across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.
Type: String
Valid Values: `CALENDAR_MONTH | NONE`
Required: No

 ** [parameters](#API_CreatePrivacyBudgetTemplate_RequestSyntax) **   <a name="API-CreatePrivacyBudgetTemplate-request-parameters"></a>
Specifies your parameters for the privacy budget template.
Type: [PrivacyBudgetTemplateParametersInput](API_PrivacyBudgetTemplateParametersInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [privacyBudgetType](#API_CreatePrivacyBudgetTemplate_RequestSyntax) **   <a name="API-CreatePrivacyBudgetTemplate-request-privacyBudgetType"></a>
Specifies the type of the privacy budget template.
Type: String
Valid Values: `DIFFERENTIAL_PRIVACY | ACCESS_BUDGET`
Required: Yes

 ** [tags](#API_CreatePrivacyBudgetTemplate_RequestSyntax) **   <a name="API-CreatePrivacyBudgetTemplate-request-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePrivacyBudgetTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "privacyBudgetTemplate": {
      "arn": "string",
      "autoRefresh": "string",
      "collaborationArn": "string",
      "collaborationId": "string",
      "createTime": number,
      "id": "string",
      "membershipArn": "string",
      "membershipId": "string",
      "parameters": { ... },
      "privacyBudgetType": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_CreatePrivacyBudgetTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [privacyBudgetTemplate](#API_CreatePrivacyBudgetTemplate_ResponseSyntax) **   <a name="API-CreatePrivacyBudgetTemplate-response-privacyBudgetTemplate"></a>
A summary of the elements in the privacy budget template.
Type: [PrivacyBudgetTemplate](API_PrivacyBudgetTemplate.md) object

## Errors
<a name="API_CreatePrivacyBudgetTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** reason **
A reason code for the exception.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request denied because service quota has been exceeded.
 ** quotaName **
The name of the quota.
 ** quotaValue **
The value of the quota.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreatePrivacyBudgetTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreatePrivacyBudgetTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
