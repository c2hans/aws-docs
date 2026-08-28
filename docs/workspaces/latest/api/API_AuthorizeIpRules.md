---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_AuthorizeIpRules.html
---

# AuthorizeIpRules
<a name="API_AuthorizeIpRules"></a>

Adds one or more rules to the specified IP access control group.

This action gives users permission to access their WorkSpaces from the CIDR address ranges specified in the rules.

## Request Syntax
<a name="API_AuthorizeIpRules_RequestSyntax"></a>

```
{
   "GroupId": "{{string}}",
   "UserRules": [
      {
         "ipRule": "{{string}}",
         "ruleDesc": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_AuthorizeIpRules_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [GroupId](#API_AuthorizeIpRules_RequestSyntax) **   <a name="WorkSpaces-AuthorizeIpRules-request-GroupId"></a>
The identifier of the group.
Type: String
Pattern: `wsipg-[0-9a-z]{8,63}$`
Required: Yes

 ** [UserRules](#API_AuthorizeIpRules_RequestSyntax) **   <a name="WorkSpaces-AuthorizeIpRules-request-UserRules"></a>
The rules to add to the group.
Type: Array of [IpRuleItem](API_IpRuleItem.md) objects
Required: Yes

## Response Elements
<a name="API_AuthorizeIpRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AuthorizeIpRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InvalidResourceStateException **
The state of the resource is not valid for this operation.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_AuthorizeIpRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/AuthorizeIpRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/AuthorizeIpRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/AuthorizeIpRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/AuthorizeIpRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/AuthorizeIpRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/AuthorizeIpRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/AuthorizeIpRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/AuthorizeIpRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/AuthorizeIpRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/AuthorizeIpRules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
