---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateCase.html
---

# UpdateCase
<a name="API_connect-cases_UpdateCase"></a>

**Note**
If you provide a value for `PerformedBy.UserArn`, you must also have the [connect:DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) permission on the user ARN that you provide.

Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the `CreateCase` input.

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Request Syntax
<a name="API_connect-cases_UpdateCase_RequestSyntax"></a>

```
PUT /domains/{{domainId}}/cases/{{caseId}} HTTP/1.1
Content-type: application/json

{
   "fields": [
      {
         "id": "{{string}}",
         "value": { ... }
      }
   ],
   "performedBy": { ... }
}
```

## URI Request Parameters
<a name="API_connect-cases_UpdateCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_connect-cases_UpdateCase_RequestSyntax) **   <a name="connect-connect-cases_UpdateCase-request-uri-caseId"></a>
A unique identifier of the case.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [domainId](#API_connect-cases_UpdateCase_RequestSyntax) **   <a name="connect-connect-cases_UpdateCase-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_UpdateCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [fields](#API_connect-cases_UpdateCase_RequestSyntax) **   <a name="connect-connect-cases_UpdateCase-request-fields"></a>
An array of objects with `fieldId` (matching ListFields/DescribeField) and value union data, structured identical to `CreateCase`.
Type: Array of [FieldValue](API_connect-cases_FieldValue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 220 items.
Required: Yes

 ** [performedBy](#API_connect-cases_UpdateCase_RequestSyntax) **   <a name="connect-connect-cases_UpdateCase-request-performedBy"></a>
Represents the entity that performed the action.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_connect-cases_UpdateCase_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-cases_UpdateCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-cases_UpdateCase_Errors"></a>

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
<a name="API_connect-cases_UpdateCase_Examples"></a>

### Request and Response example
<a name="API_connect-cases_UpdateCase_Example_1"></a>

This example illustrates one usage of UpdateCase.

```
{
  "fields": [
    {
      "id": "title",
      "value": {
        "stringValue": "New Title"
        }
      }
  ]
}
```

```
{ }
```

## See Also
<a name="API_connect-cases_UpdateCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/UpdateCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/UpdateCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/UpdateCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/UpdateCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/UpdateCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/UpdateCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/UpdateCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/UpdateCase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/UpdateCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/UpdateCase)
