---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateApprovalPolicy.html
---

# UpdateApprovalPolicy
<a name="API_UpdateApprovalPolicy"></a>

Updates an approval policy in Quick Sight.

## Request Syntax
<a name="API_UpdateApprovalPolicy_RequestSyntax"></a>

```
PATCH /governance/approvalworkflows/policies/{{PolicyId}} HTTP/1.1
Content-type: application/json

{
   "Actions": [ "{{string}}" ],
   "ApplicableTo": {
      "GroupArns": [ "{{string}}" ],
      "Type": "{{string}}"
   },
   "ApprovalGroups": [ "{{string}}" ],
   "AssetTypes": [ "{{string}}" ],
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApprovalPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PolicyId](#API_UpdateApprovalPolicy_RequestSyntax) **   <a name="QS-UpdateApprovalPolicy-request-uri-PolicyId"></a>
The unique identifier of the approval policy to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-_]+`
Required: Yes

## Request Body
<a name="API_UpdateApprovalPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Actions](#API_UpdateApprovalPolicy_RequestSyntax) **   <a name="QS-UpdateApprovalPolicy-request-Actions"></a>
The list of governed actions that trigger the approval workflow.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `SHARE`
Required: No

 ** [ApplicableTo](#API_UpdateApprovalPolicy_RequestSyntax) **   <a name="QS-UpdateApprovalPolicy-request-ApplicableTo"></a>
The scoping configuration that determines who the approval policy applies to.
Type: [ApplicableTo](API_ApplicableTo.md) object
Required: No

 ** [ApprovalGroups](#API_UpdateApprovalPolicy_RequestSyntax) **   <a name="QS-UpdateApprovalPolicy-request-ApprovalGroups"></a>
The list of group ARNs whose members can approve requests.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** [AssetTypes](#API_UpdateApprovalPolicy_RequestSyntax) **   <a name="QS-UpdateApprovalPolicy-request-AssetTypes"></a>
The list of asset types that the approval policy applies to.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `AGENT | SPACE | KNOWLEDGE_BASE`
Required: No

 ** [Description](#API_UpdateApprovalPolicy_RequestSyntax) **   <a name="QS-UpdateApprovalPolicy-request-Description"></a>
A description of the approval policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Name](#API_UpdateApprovalPolicy_RequestSyntax) **   <a name="QS-UpdateApprovalPolicy-request-Name"></a>
The name of the approval policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_UpdateApprovalPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": {
      "Actions": [ "string" ],
      "ApplicableTo": {
         "GroupArns": [ "string" ],
         "Type": "string"
      },
      "ApprovalGroups": [ "string" ],
      "AssetTypes": [ "string" ],
      "CreatedAt": number,
      "Description": "string",
      "Name": "string",
      "PolicyArn": "string",
      "PolicyId": "string",
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_UpdateApprovalPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_UpdateApprovalPolicy_ResponseSyntax) **   <a name="QS-UpdateApprovalPolicy-response-Policy"></a>
The updated approval policy.
Type: [ApprovalPolicy](API_ApprovalPolicy.md) object

## Errors
<a name="API_UpdateApprovalPolicy_Errors"></a>

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
<a name="API_UpdateApprovalPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateApprovalPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateApprovalPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateApprovalPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateApprovalPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateApprovalPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateApprovalPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateApprovalPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateApprovalPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateApprovalPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateApprovalPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
