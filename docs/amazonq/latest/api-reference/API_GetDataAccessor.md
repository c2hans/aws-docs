---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDataAccessor.html
---

# GetDataAccessor
<a name="API_GetDataAccessor"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Retrieves information about a specified data accessor. This operation returns details about the data accessor, including its display name, unique identifier, Amazon Resource Name (ARN), the associated Amazon Q Business application and IAM Identity Center application, the IAM role for the ISV, the action configurations, and the timestamps for when the data accessor was created and last updated.

## Request Syntax
<a name="API_GetDataAccessor_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/dataaccessors/{{dataAccessorId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataAccessor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetDataAccessor_RequestSyntax) **   <a name="qbusiness-GetDataAccessor-request-uri-applicationId"></a>
The unique identifier of the Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [dataAccessorId](#API_GetDataAccessor_RequestSyntax) **   <a name="qbusiness-GetDataAccessor-request-uri-dataAccessorId"></a>
The unique identifier of the data accessor to retrieve.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_GetDataAccessor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataAccessor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionConfigurations": [
      {
         "action": "string",
         "filterConfiguration": {
            "documentAttributeFilter": {
               "andAllFilters": [
                  "AttributeFilter"
               ],
               "containsAll": {
                  "name": "string",
                  "value": { ... }
               },
               "containsAny": {
                  "name": "string",
                  "value": { ... }
               },
               "equalsTo": {
                  "name": "string",
                  "value": { ... }
               },
               "greaterThan": {
                  "name": "string",
                  "value": { ... }
               },
               "greaterThanOrEquals": {
                  "name": "string",
                  "value": { ... }
               },
               "lessThan": {
                  "name": "string",
                  "value": { ... }
               },
               "lessThanOrEquals": {
                  "name": "string",
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
   "applicationId": "string",
   "authenticationDetail": {
      "authenticationConfiguration": { ... },
      "authenticationType": "string",
      "externalIds": [ "string" ]
   },
   "createdAt": number,
   "dataAccessorArn": "string",
   "dataAccessorId": "string",
   "displayName": "string",
   "idcApplicationArn": "string",
   "principal": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetDataAccessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionConfigurations](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-actionConfigurations"></a>
The list of action configurations specifying the allowed actions and any associated filters.
Type: Array of [ActionConfiguration](API_ActionConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [applicationId](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-applicationId"></a>
The unique identifier of the Amazon Q Business application associated with this data accessor.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [authenticationDetail](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-authenticationDetail"></a>
The authentication configuration details for the data accessor. This specifies how the ISV authenticates when accessing data through this data accessor.
Type: [DataAccessorAuthenticationDetail](API_DataAccessorAuthenticationDetail.md) object

 ** [createdAt](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-createdAt"></a>
The timestamp when the data accessor was created.
Type: Timestamp

 ** [dataAccessorArn](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-dataAccessorArn"></a>
The Amazon Resource Name (ARN) of the data accessor.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [dataAccessorId](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-dataAccessorId"></a>
The unique identifier of the data accessor.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [displayName](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-displayName"></a>
The friendly name of the data accessor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

 ** [idcApplicationArn](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-idcApplicationArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center application associated with this data accessor.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`

 ** [principal](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-principal"></a>
The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1284.
Pattern: `arn:aws:iam::[0-9]{12}:role/[a-zA-Z0-9_/+=,.@-]+`

 ** [updatedAt](#API_GetDataAccessor_ResponseSyntax) **   <a name="qbusiness-GetDataAccessor-response-updatedAt"></a>
The timestamp when the data accessor was last updated.
Type: Timestamp

## Errors
<a name="API_GetDataAccessor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

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
<a name="API_GetDataAccessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/GetDataAccessor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/GetDataAccessor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GetDataAccessor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/GetDataAccessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GetDataAccessor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/GetDataAccessor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/GetDataAccessor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/GetDataAccessor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/GetDataAccessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GetDataAccessor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
