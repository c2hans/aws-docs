---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataAccessor.html
---

# CreateDataAccessor
<a name="API_CreateDataAccessor"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates a new data accessor for an ISV to access data from a Amazon Q Business application. The data accessor is an entity that represents the ISV's access to the Amazon Q Business application's data. It includes the IAM role ARN for the ISV, a friendly name, and a set of action configurations that define the specific actions the ISV is allowed to perform and any associated data filters. When the data accessor is created, an IAM Identity Center application is also created to manage the ISV's identity and authentication for accessing the Amazon Q Business application.

## Request Syntax
<a name="API_CreateDataAccessor_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/dataaccessors HTTP/1.1
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
   "clientToken": "{{string}}",
   "displayName": "{{string}}",
   "principal": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateDataAccessor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CreateDataAccessor_RequestSyntax) **   <a name="qbusiness-CreateDataAccessor-request-uri-applicationId"></a>
The unique identifier of the Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_CreateDataAccessor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionConfigurations](#API_CreateDataAccessor_RequestSyntax) **   <a name="qbusiness-CreateDataAccessor-request-actionConfigurations"></a>
A list of action configurations specifying the allowed actions and any associated filters.
Type: Array of [ActionConfiguration](API_ActionConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [authenticationDetail](#API_CreateDataAccessor_RequestSyntax) **   <a name="qbusiness-CreateDataAccessor-request-authenticationDetail"></a>
The authentication configuration details for the data accessor. This specifies how the ISV will authenticate when accessing data through this data accessor.
Type: [DataAccessorAuthenticationDetail](API_DataAccessorAuthenticationDetail.md) object
Required: No

 ** [clientToken](#API_CreateDataAccessor_RequestSyntax) **   <a name="qbusiness-CreateDataAccessor-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [displayName](#API_CreateDataAccessor_RequestSyntax) **   <a name="qbusiness-CreateDataAccessor-request-displayName"></a>
A friendly name for the data accessor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [principal](#API_CreateDataAccessor_RequestSyntax) **   <a name="qbusiness-CreateDataAccessor-request-principal"></a>
The Amazon Resource Name (ARN) of the IAM role for the ISV that will be accessing the data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1284.
Pattern: `arn:aws:iam::[0-9]{12}:role/[a-zA-Z0-9_/+=,.@-]+`
Required: Yes

 ** [tags](#API_CreateDataAccessor_RequestSyntax) **   <a name="qbusiness-CreateDataAccessor-request-tags"></a>
The tags to associate with the data accessor.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateDataAccessor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataAccessorArn": "string",
   "dataAccessorId": "string",
   "idcApplicationArn": "string"
}
```

## Response Elements
<a name="API_CreateDataAccessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataAccessorArn](#API_CreateDataAccessor_ResponseSyntax) **   <a name="qbusiness-CreateDataAccessor-response-dataAccessorArn"></a>
The Amazon Resource Name (ARN) of the created data accessor.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [dataAccessorId](#API_CreateDataAccessor_ResponseSyntax) **   <a name="qbusiness-CreateDataAccessor-response-dataAccessorId"></a>
The unique identifier of the created data accessor.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [idcApplicationArn](#API_CreateDataAccessor_ResponseSyntax) **   <a name="qbusiness-CreateDataAccessor-response-idcApplicationArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center application created for this data accessor.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`

## Errors
<a name="API_CreateDataAccessor_Errors"></a>

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
<a name="API_CreateDataAccessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CreateDataAccessor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CreateDataAccessor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CreateDataAccessor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CreateDataAccessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CreateDataAccessor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CreateDataAccessor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CreateDataAccessor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CreateDataAccessor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CreateDataAccessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CreateDataAccessor)
