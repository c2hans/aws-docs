---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetResourcePolicy.html
---

# GetResourcePolicy
<a name="API_billing_GetResourcePolicy"></a>

Returns the resource-based policy document attached to the resource in `JSON` format.

## Request Syntax
<a name="API_billing_GetResourcePolicy_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_GetResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_billing_GetResourcePolicy_RequestSyntax) **   <a name="awscostmanagement-billing_GetResourcePolicy-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the billing view resource to which the policy is attached to.
Type: String
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:[a-zA-Z0-9/:_\+=\.\@-]{0,70}[a-zA-Z0-9]`
Required: Yes

## Response Syntax
<a name="API_billing_GetResourcePolicy_ResponseSyntax"></a>

```
{
   "policy": "string",
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_billing_GetResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_billing_GetResourcePolicy_ResponseSyntax) **   <a name="awscostmanagement-billing_GetResourcePolicy-response-policy"></a>
The resource-based policy document attached to the resource in `JSON` format.
Type: String

 ** [resourceArn](#API_billing_GetResourcePolicy_ResponseSyntax) **   <a name="awscostmanagement-billing_GetResourcePolicy-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the billing view resource to which the policy is attached to.
Type: String
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:[a-zA-Z0-9/:_\+=\.\@-]{0,70}[a-zA-Z0-9]`

## Errors
<a name="API_billing_GetResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
 ** resourceId **
 Value is a list of resource IDs that were not found.
 ** resourceType **
 Value is the type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_billing_GetResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/GetResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/GetResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/GetResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/GetResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/GetResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/GetResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/GetResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/GetResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/GetResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/GetResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
