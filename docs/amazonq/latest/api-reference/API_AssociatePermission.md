---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AssociatePermission.html
---

# AssociatePermission
<a name="API_AssociatePermission"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Adds or updates a permission policy for a Amazon Q Business application, allowing cross-account access for an ISV. This operation creates a new policy statement for the specified Amazon Q Business application. The policy statement defines the IAM actions that the ISV is allowed to perform on the Amazon Q Business application's resources.

## Request Syntax
<a name="API_AssociatePermission_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/policy HTTP/1.1
Content-type: application/json

{
   "actions": [ "{{string}}" ],
   "conditions": [
      {
         "conditionKey": "{{string}}",
         "conditionOperator": "{{string}}",
         "conditionValues": [ "{{string}}" ]
      }
   ],
   "principal": "{{string}}",
   "statementId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociatePermission_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_AssociatePermission_RequestSyntax) **   <a name="qbusiness-AssociatePermission-request-uri-applicationId"></a>
The unique identifier of the Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_AssociatePermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_AssociatePermission_RequestSyntax) **   <a name="qbusiness-AssociatePermission-request-actions"></a>
The list of Amazon Q Business actions that the ISV is allowed to perform.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `qbusiness:[a-zA-Z]+`
Required: Yes

 ** [conditions](#API_AssociatePermission_RequestSyntax) **   <a name="qbusiness-AssociatePermission-request-conditions"></a>
The conditions that restrict when the permission is effective. These conditions can be used to limit the permission based on specific attributes of the request.
Type: Array of [PermissionCondition](API_PermissionCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [principal](#API_AssociatePermission_RequestSyntax) **   <a name="qbusiness-AssociatePermission-request-principal"></a>
The Amazon Resource Name of the IAM role for the ISV that is being granted permission.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1284.
Pattern: `arn:aws:iam::[0-9]{12}:role/[a-zA-Z0-9_/+=,.@-]+`
Required: Yes

 ** [statementId](#API_AssociatePermission_RequestSyntax) **   <a name="qbusiness-AssociatePermission-request-statementId"></a>
A unique identifier for the policy statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_AssociatePermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "statement": "string"
}
```

## Response Elements
<a name="API_AssociatePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [statement](#API_AssociatePermission_ResponseSyntax) **   <a name="qbusiness-AssociatePermission-response-statement"></a>
The JSON representation of the added permission statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_AssociatePermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded the set limits for your Amazon Q Business service.
 ** message **
The message describing a `ServiceQuotaExceededException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_AssociatePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/AssociatePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/AssociatePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AssociatePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/AssociatePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AssociatePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/AssociatePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/AssociatePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/AssociatePermission)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/AssociatePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AssociatePermission)
