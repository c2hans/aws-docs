---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateSpace.html
---

# UpdateSpace
<a name="API_UpdateSpace"></a>

Updates the metadata of an Amazon QuickSight space.

## Request Syntax
<a name="API_UpdateSpace_RequestSyntax"></a>

```
PUT /v1/accounts/{{AwsAccountId}}/spaces/{{SpaceId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSpace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateSpace_RequestSyntax) **   <a name="QS-UpdateSpace-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the space.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [SpaceId](#API_UpdateSpace_RequestSyntax) **   <a name="QS-UpdateSpace-request-uri-SpaceId"></a>
The ID of the space that you want to update.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

## Request Body
<a name="API_UpdateSpace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateSpace_RequestSyntax) **   <a name="QS-UpdateSpace-request-Description"></a>
A new description for the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\P{C}\n\r\t\f\v\p{Cf}]*`
Required: No

 ** [Name](#API_UpdateSpace_RequestSyntax) **   <a name="QS-UpdateSpace-request-Name"></a>
A new display name for the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\P{C}\n\r\t\f\v\p{Cf}]*`
Required: No

## Response Syntax
<a name="API_UpdateSpace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RequestId": "string",
   "spaceArn": "string",
   "spaceId": "string"
}
```

## Response Elements
<a name="API_UpdateSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [spaceId](#API_UpdateSpace_ResponseSyntax) **   <a name="QS-UpdateSpace-response-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z-_=.+]+`

 ** [RequestId](#API_UpdateSpace_ResponseSyntax) **   <a name="QS-UpdateSpace-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [spaceArn](#API_UpdateSpace_ResponseSyntax) **   <a name="QS-UpdateSpace-response-spaceArn"></a>
The ARN of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

## Errors
<a name="API_UpdateSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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

## See Also
<a name="API_UpdateSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateSpace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
