---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteField.html
---

# DeleteField
<a name="API_connect-cases_DeleteField"></a>

Deletes a field from a Cases template.

After a field is deleted:
+ You can still retrieve the field by calling `BatchGetField`.
+ You cannot update a deleted field by calling `UpdateField`; it throws a `ValidationException`.
+ Deleted fields are not included in the `ListFields` response.
+ Calling `CreateCase` with a deleted field throws a `ValidationException` denoting which field identifiers in the request have been deleted.
+ Calling `GetCase` with a deleted field identifier returns the deleted field's value if one exists.
+ Calling `UpdateCase` with a deleted field ID throws a `ValidationException` if the case does not already contain a value for the deleted field. Otherwise it succeeds, allowing you to update or remove (using `emptyValue: {}`) the field's value from the case.
+  `GetTemplate` does not return field IDs for deleted fields.
+  `GetLayout` does not return field IDs for deleted fields.
+ Calling `SearchCases` with the deleted field ID as a filter returns any cases that have a value for the deleted field that matches the filter criteria.
+ Calling `SearchCases` with a `searchTerm` value that matches a deleted field's value on a case returns the case in the response.
+ Calling `BatchPutFieldOptions` with a deleted field ID throw a `ValidationException`.
+ Calling `GetCaseEventConfiguration` does not return field IDs for deleted fields.

## Request Syntax
<a name="API_connect-cases_DeleteField_RequestSyntax"></a>

```
DELETE /domains/{{domainId}}/fields/{{fieldId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-cases_DeleteField_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_DeleteField_RequestSyntax) **   <a name="connect-connect-cases_DeleteField-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [fieldId](#API_connect-cases_DeleteField_RequestSyntax) **   <a name="connect-connect-cases_DeleteField-request-uri-fieldId"></a>
Unique identifier of the field.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_DeleteField_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-cases_DeleteField_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-cases_DeleteField_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-cases_DeleteField_Errors"></a>

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

## See Also
<a name="API_connect-cases_DeleteField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/DeleteField)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/DeleteField)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/DeleteField)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/DeleteField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/DeleteField)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/DeleteField)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/DeleteField)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/DeleteField)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/DeleteField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/DeleteField)
