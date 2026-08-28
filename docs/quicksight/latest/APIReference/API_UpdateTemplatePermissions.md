---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTemplatePermissions.html
---

# UpdateTemplatePermissions
<a name="API_UpdateTemplatePermissions"></a>

Updates the resource permissions for a template.

## Request Syntax
<a name="API_UpdateTemplatePermissions_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/templates/{{TemplateId}}/permissions HTTP/1.1
Content-type: application/json

{
   "GrantPermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "RevokePermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateTemplatePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateTemplatePermissions_RequestSyntax) **   <a name="QS-UpdateTemplatePermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the template.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [TemplateId](#API_UpdateTemplatePermissions_RequestSyntax) **   <a name="QS-UpdateTemplatePermissions-request-uri-TemplateId"></a>
The ID for the template.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateTemplatePermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantPermissions](#API_UpdateTemplatePermissions_RequestSyntax) **   <a name="QS-UpdateTemplatePermissions-request-GrantPermissions"></a>
A list of resource permissions to be granted on the template.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** [RevokePermissions](#API_UpdateTemplatePermissions_RequestSyntax) **   <a name="QS-UpdateTemplatePermissions-request-RevokePermissions"></a>
A list of resource permissions to be revoked from the template.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_UpdateTemplatePermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Permissions": [
      {
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string",
   "TemplateArn": "string",
   "TemplateId": "string"
}
```

## Response Elements
<a name="API_UpdateTemplatePermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateTemplatePermissions_ResponseSyntax) **   <a name="QS-UpdateTemplatePermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Permissions](#API_UpdateTemplatePermissions_ResponseSyntax) **   <a name="QS-UpdateTemplatePermissions-response-Permissions"></a>
A list of resource permissions to be set on the template.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.

 ** [RequestId](#API_UpdateTemplatePermissions_ResponseSyntax) **   <a name="QS-UpdateTemplatePermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [TemplateArn](#API_UpdateTemplatePermissions_ResponseSyntax) **   <a name="QS-UpdateTemplatePermissions-response-TemplateArn"></a>
The Amazon Resource Name (ARN) of the template.
Type: String

 ** [TemplateId](#API_UpdateTemplatePermissions_ResponseSyntax) **   <a name="QS-UpdateTemplatePermissions-response-TemplateId"></a>
The ID for the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

## Errors
<a name="API_UpdateTemplatePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateTemplatePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateTemplatePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateTemplatePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateTemplatePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateTemplatePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateTemplatePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateTemplatePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateTemplatePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateTemplatePermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateTemplatePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateTemplatePermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
