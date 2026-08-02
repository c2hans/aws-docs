---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateCase.html
---

# CreateCase
<a name="API_connect-cases_CreateCase"></a>

**Note**
If you provide a value for `PerformedBy.UserArn` you must also have [connect:DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) permission on the User ARN resource that you provide

Creates a case in the specified Cases domain. Case system and custom fields are taken as an array id/value pairs with a declared data types.

When creating a case from a template that has tag propagation configurations, the specified tags are automatically applied to the case.

The following fields are required when creating a case:
+  `customer_id` - You must provide the full customer profile ARN in this format: `arn:aws:profile:your_AWS_Region:your_AWS_account ID:domains/your_profiles_domain_name/profiles/profile_ID`
+  `title`

## Request Syntax
<a name="API_connect-cases_CreateCase_RequestSyntax"></a>

```
POST /domains/{{domainId}}/cases HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "fields": [
      {
         "id": "{{string}}",
         "value": { ... }
      }
   ],
   "performedBy": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "templateId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-cases_CreateCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_CreateCase_RequestSyntax) **   <a name="connect-connect-cases_CreateCase-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_CreateCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_connect-cases_CreateCase_RequestSyntax) **   <a name="connect-connect-cases_CreateCase-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [fields](#API_connect-cases_CreateCase_RequestSyntax) **   <a name="connect-connect-cases_CreateCase-request-fields"></a>
An array of objects with field ID (matching ListFields/DescribeField) and value union data.
Type: Array of [FieldValue](API_connect-cases_FieldValue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 220 items.
Required: Yes

 ** [performedBy](#API_connect-cases_CreateCase_RequestSyntax) **   <a name="connect-connect-cases_CreateCase-request-performedBy"></a>
Represents the entity that performed the action.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tags](#API_connect-cases_CreateCase_RequestSyntax) **   <a name="connect-connect-cases_CreateCase-request-tags"></a>
A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?![aA][wW][sS]:)[a-zA-Z0-9 _.:/=+\-@]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([a-zA-Z0-9 _.:/=+\-@]*)`
Required: No

 ** [templateId](#API_connect-cases_CreateCase_RequestSyntax) **   <a name="connect-connect-cases_CreateCase-request-templateId"></a>
A unique identifier of a template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Response Syntax
<a name="API_connect-cases_CreateCase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "caseArn": "string",
   "caseId": "string"
}
```

## Response Elements
<a name="API_connect-cases_CreateCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [caseArn](#API_connect-cases_CreateCase_ResponseSyntax) **   <a name="connect-connect-cases_CreateCase-response-caseArn"></a>
The Amazon Resource Name (ARN) of the case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [caseId](#API_connect-cases_CreateCase_ResponseSyntax) **   <a name="connect-connect-cases_CreateCase-response-caseId"></a>
A unique identifier of the case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_connect-cases_CreateCase_Errors"></a>

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

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_CreateCase_Examples"></a>

### Request and Response example
<a name="API_connect-cases_CreateCase_Example_1"></a>

This example illustrates one usage of CreateCase.

```
{
  "templateId": "[template_id]",
  "fields": [
  {
    "id": "customer_id",
    "value": {
      "stringValue": "[customer_id]"
     },
    {
    "id": "title",
    "value": {
      "stringValue": "Incorrect Shipping Address"
      }
    }
  ],
  "clientToken": "[clientToken]",
  "tags": {
    "Department": "Shipping",
    "Priority": "High"
  }
}
```

```
{
  "caseArn": "arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/case/[case_id]",
  "caseId": "[case_id]"
}
```

## See Also
<a name="API_connect-cases_CreateCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/CreateCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/CreateCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CreateCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/CreateCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CreateCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/CreateCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/CreateCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/CreateCase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/CreateCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CreateCase)
