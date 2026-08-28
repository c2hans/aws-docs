---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeletePolicy.html
---

# DeletePolicy
<a name="API_DeletePolicy"></a>

Permanently deletes an AWS Firewall Manager policy.

## Request Syntax
<a name="API_DeletePolicy_RequestSyntax"></a>

```
{
   "DeleteAllPolicyResources": {{boolean}},
   "PolicyId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeleteAllPolicyResources](#API_DeletePolicy_RequestSyntax) **   <a name="fms-DeletePolicy-request-DeleteAllPolicyResources"></a>
When set to `True`, the request performs cleanup according to the policy type.
For AWS WAF and Shield Advanced policies, the cleanup performs these actions:
+ Removes rule groups created by AWS Firewall Manager
+ Removes web ACLs from in-scope resources
+ Removes web ACLs that contain no rules or rule groups
For AWS WAF and Shield Advanced policies, Firewall Manager removes Firewall Manager generated web ACLs that are not associated with any resources, even if `DeleteAllPolicyResources` is set to `False`.
For security group policies, the cleanup performs these actions for each security group in the policy:
+ Disassociates the security group from in-scope resources
+ Removes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy
For security group common policies, Firewall Manager removes all Firewall Manager generated security groups that aren't associated with any other resources through another policy, even if `DeleteAllPolicyResources` is set to `False`.
After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope.
Type: Boolean
Required: No

 ** [PolicyId](#API_DeletePolicy_RequestSyntax) **   <a name="fms-DeletePolicy-request-PolicyId"></a>
The ID of the policy that you want to delete. You can retrieve this ID from `PutPolicy` and `ListPolicies`.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: Yes

## Response Elements
<a name="API_DeletePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** LimitExceededException **
The operation exceeds a resource limit, for example, the maximum number of `policy` objects that you can create for an AWS account. For more information, see [Firewall Manager Limits](https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html) in the * AWS WAF Developer Guide*.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DeletePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/DeletePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/DeletePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/DeletePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/DeletePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/DeletePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/DeletePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/DeletePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/DeletePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/DeletePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/DeletePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
