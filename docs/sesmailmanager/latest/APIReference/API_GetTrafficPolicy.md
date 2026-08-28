---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetTrafficPolicy.html
---

# GetTrafficPolicy
<a name="API_GetTrafficPolicy"></a>

Fetch attributes of a traffic policy resource.

## Request Syntax
<a name="API_GetTrafficPolicy_RequestSyntax"></a>

```
{
   "TrafficPolicyId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTrafficPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrafficPolicyId](#API_GetTrafficPolicy_RequestSyntax) **   <a name="sesmailmanager-GetTrafficPolicy-request-TrafficPolicyId"></a>
The identifier of the traffic policy resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_GetTrafficPolicy_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DefaultAction": "string",
   "LastUpdatedTimestamp": number,
   "MaxMessageSizeBytes": number,
   "PolicyStatements": [
      {
         "Action": "string",
         "Conditions": [
            { ... }
         ]
      }
   ],
   "TrafficPolicyArn": "string",
   "TrafficPolicyId": "string",
   "TrafficPolicyName": "string"
}
```

## Response Elements
<a name="API_GetTrafficPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="sesmailmanager-GetTrafficPolicy-response-CreatedTimestamp"></a>
The timestamp of when the traffic policy was created.
Type: Timestamp

 ** [DefaultAction](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="sesmailmanager-GetTrafficPolicy-response-DefaultAction"></a>
The default action of the traffic policy.
Type: String
Valid Values: `ALLOW | DENY`

 ** [LastUpdatedTimestamp](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="sesmailmanager-GetTrafficPolicy-response-LastUpdatedTimestamp"></a>
The timestamp of when the traffic policy was last updated.
Type: Timestamp

 ** [MaxMessageSizeBytes](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="sesmailmanager-GetTrafficPolicy-response-MaxMessageSizeBytes"></a>
The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.
Type: Integer
Valid Range: Minimum value of 1.

 ** [PolicyStatements](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="sesmailmanager-GetTrafficPolicy-response-PolicyStatements"></a>
The list of conditions which are in the traffic policy resource.
Type: Array of [PolicyStatement](API_PolicyStatement.md) objects

 ** [TrafficPolicyArn](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="sesmailmanager-GetTrafficPolicy-response-TrafficPolicyArn"></a>
The Amazon Resource Name (ARN) of the traffic policy resource.
Type: String

 ** [TrafficPolicyId](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="sesmailmanager-GetTrafficPolicy-response-TrafficPolicyId"></a>
The identifier of the traffic policy resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [TrafficPolicyName](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="sesmailmanager-GetTrafficPolicy-response-TrafficPolicyName"></a>
A user-friendly name for the traffic policy resource.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[A-Za-z0-9_\-]+`

## Errors
<a name="API_GetTrafficPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetTrafficPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetTrafficPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetTrafficPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetTrafficPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetTrafficPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetTrafficPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetTrafficPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetTrafficPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetTrafficPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetTrafficPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetTrafficPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
