---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataAccessor.html
---

# UpdateDataAccessor
<a name="API_UpdateDataAccessor"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Updates an existing data accessor. This operation allows modifying the action configurations (the allowed actions and associated filters) and the display name of the data accessor. It does not allow changing the IAM role associated with the data accessor or other core properties of the data accessor.

## Request Syntax
<a name="API_UpdateDataAccessor_RequestSyntax"></a>

```
PUT /applications/{{applicationId}}/dataaccessors/{{dataAccessorId}} HTTP/1.1
Content-type: application/json

{
   "actionConfigurations": [
      {
         "action": "{{string}}",
         "filterConfiguration": {
            "documentAttributeFilter": {
               "andAllFilters": [
                  "AttributeFilter"
               ],
               "containsAll": {
                  "name": "{{string}}",
                  "value": { ... }
               },
               "containsAny": {
                  "name": "{{string}}",
                  "value": { ... }
               },
               "equalsTo": {
                  "name": "{{string}}",
                  "value": { ... }
               },
               "greaterThan": {
                  "name": "{{string}}",
                  "value": { ... }
               },
               "greaterThanOrEquals": {
                  "name": "{{string}}",
                  "value": { ... }
               },
               "lessThan": {
                  "name": "{{string}}",
                  "value": { ... }
               },
               "lessThanOrEquals": {
                  "name": "{{string}}",
                  "value": { ... }
               },
               "notFilter": "AttributeFilter",
               "orAllFilters": [
                  "AttributeFilter"
               ]
            }
         }
      }
   ],
   "authenticationDetail": {
      "authenticationConfiguration": { ... },
      "authenticationType": "{{string}}",
      "externalIds": [ "{{string}}" ]
   },
   "displayName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDataAccessor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_UpdateDataAccessor_RequestSyntax) **   <a name="qbusiness-UpdateDataAccessor-request-uri-applicationId"></a>
The unique identifier of the Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [dataAccessorId](#API_UpdateDataAccessor_RequestSyntax) **   <a name="qbusiness-UpdateDataAccessor-request-uri-dataAccessorId"></a>
The unique identifier of the data accessor to update.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_UpdateDataAccessor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionConfigurations](#API_UpdateDataAccessor_RequestSyntax) **   <a name="qbusiness-UpdateDataAccessor-request-actionConfigurations"></a>
The updated list of action configurations specifying the allowed actions and any associated filters.
Type: Array of [ActionConfiguration](API_ActionConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [authenticationDetail](#API_UpdateDataAccessor_RequestSyntax) **   <a name="qbusiness-UpdateDataAccessor-request-authenticationDetail"></a>
The updated authentication configuration details for the data accessor. This specifies how the ISV will authenticate when accessing data through this data accessor.
Type: [DataAccessorAuthenticationDetail](API_DataAccessorAuthenticationDetail.md) object
Required: No

 ** [displayName](#API_UpdateDataAccessor_RequestSyntax) **   <a name="qbusiness-UpdateDataAccessor-request-displayName"></a>
The updated friendly name for the data accessor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

## Response Syntax
<a name="API_UpdateDataAccessor_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateDataAccessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDataAccessor_Errors"></a>

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
<a name="API_UpdateDataAccessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/UpdateDataAccessor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/UpdateDataAccessor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/UpdateDataAccessor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/UpdateDataAccessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/UpdateDataAccessor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/UpdateDataAccessor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/UpdateDataAccessor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/UpdateDataAccessor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/UpdateDataAccessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/UpdateDataAccessor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
