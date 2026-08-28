---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateGroup.html
---

# UpdateGroup
<a name="API_UpdateGroup"></a>

Changes a group description.

## Request Syntax
<a name="API_UpdateGroup_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/groups/{{GroupName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateGroup_RequestSyntax) **   <a name="QS-UpdateGroup-request-uri-AwsAccountId"></a>
The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon Quick Sight account.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [GroupName](#API_UpdateGroup_RequestSyntax) **   <a name="QS-UpdateGroup-request-uri-GroupName"></a>
The name of the group that you want to update.
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: Yes

 ** [Namespace](#API_UpdateGroup_RequestSyntax) **   <a name="QS-UpdateGroup-request-uri-Namespace"></a>
The namespace of the group that you want to update.
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

## Request Body
<a name="API_UpdateGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateGroup_RequestSyntax) **   <a name="QS-UpdateGroup-request-Description"></a>
The description for the group that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_UpdateGroup_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Group": {
      "Arn": "string",
      "Description": "string",
      "GroupName": "string",
      "PrincipalId": "string"
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateGroup_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateGroup_ResponseSyntax) **   <a name="QS-UpdateGroup-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Group](#API_UpdateGroup_ResponseSyntax) **   <a name="QS-UpdateGroup-response-Group"></a>
The name of the group.
Type: [Group](API_Group.md) object

 ** [RequestId](#API_UpdateGroup_ResponseSyntax) **   <a name="QS-UpdateGroup-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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

 ** PreconditionNotMetException **
One or more preconditions aren't met.
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

 ** ResourceUnavailableException **
This resource is currently unavailable.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
