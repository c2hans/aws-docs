---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StartConfigurationPolicyDisassociation.html
---

# StartConfigurationPolicyDisassociation
<a name="API_StartConfigurationPolicyDisassociation"></a>

 Disassociates a target account, organizational unit, or the root from a specified configuration. When you disassociate a configuration from its target, the target inherits the configuration of the closest parent. If there’s no configuration to inherit, the target retains its settings but becomes a self-managed account. A target can be disassociated from a configuration policy or self-managed behavior. Only the AWS Security Hub CSPM delegated administrator can invoke this operation from the home Region.

## Request Syntax
<a name="API_StartConfigurationPolicyDisassociation_RequestSyntax"></a>

```
POST /configurationPolicyAssociation/disassociate HTTP/1.1
Content-type: application/json

{
   "ConfigurationPolicyIdentifier": "{{string}}",
   "Target": { ... }
}
```

## URI Request Parameters
<a name="API_StartConfigurationPolicyDisassociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartConfigurationPolicyDisassociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationPolicyIdentifier](#API_StartConfigurationPolicyDisassociation_RequestSyntax) **   <a name="securityhub-StartConfigurationPolicyDisassociation-request-ConfigurationPolicyIdentifier"></a>
 The Amazon Resource Name (ARN) of a configuration policy, the universally unique identifier (UUID) of a configuration policy, or a value of `SELF_MANAGED_SECURITY_HUB` for a self-managed configuration.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [Target](#API_StartConfigurationPolicyDisassociation_RequestSyntax) **   <a name="securityhub-StartConfigurationPolicyDisassociation-request-Target"></a>
 The identifier of the target account, organizational unit, or the root to disassociate from the specified configuration.
Type: [Target](API_Target.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_StartConfigurationPolicyDisassociation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StartConfigurationPolicyDisassociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartConfigurationPolicyDisassociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_StartConfigurationPolicyDisassociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StartConfigurationPolicyDisassociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
