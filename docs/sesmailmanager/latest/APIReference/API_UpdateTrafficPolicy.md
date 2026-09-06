---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_UpdateTrafficPolicy.html
---

# UpdateTrafficPolicy
<a name="API_UpdateTrafficPolicy"></a>

Update attributes of an already provisioned traffic policy resource.

## Request Syntax
<a name="API_UpdateTrafficPolicy_RequestSyntax"></a>

```
{
   "DefaultAction": "{{string}}",
   "MaxMessageSizeBytes": {{number}},
   "PolicyStatements": [
      {
         "Action": "{{string}}",
         "Conditions": [
            { ... }
         ]
      }
   ],
   "TrafficPolicyId": "{{string}}",
   "TrafficPolicyName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTrafficPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DefaultAction](#API_UpdateTrafficPolicy_RequestSyntax) **   <a name="sesmailmanager-UpdateTrafficPolicy-request-DefaultAction"></a>
Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** [MaxMessageSizeBytes](#API_UpdateTrafficPolicy_RequestSyntax) **   <a name="sesmailmanager-UpdateTrafficPolicy-request-MaxMessageSizeBytes"></a>
The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [PolicyStatements](#API_UpdateTrafficPolicy_RequestSyntax) **   <a name="sesmailmanager-UpdateTrafficPolicy-request-PolicyStatements"></a>
The list of conditions to be updated for filtering email traffic.
Type: Array of [PolicyStatement](API_PolicyStatement.md) objects
Required: No

 ** [TrafficPolicyId](#API_UpdateTrafficPolicy_RequestSyntax) **   <a name="sesmailmanager-UpdateTrafficPolicy-request-TrafficPolicyId"></a>
The identifier of the traffic policy that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [TrafficPolicyName](#API_UpdateTrafficPolicy_RequestSyntax) **   <a name="sesmailmanager-UpdateTrafficPolicy-request-TrafficPolicyName"></a>
A user-friendly name for the traffic policy resource.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[A-Za-z0-9_\-]+`
Required: No

## Response Elements
<a name="API_UpdateTrafficPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTrafficPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTrafficPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/UpdateTrafficPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/UpdateTrafficPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/UpdateTrafficPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/UpdateTrafficPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/UpdateTrafficPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/UpdateTrafficPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/UpdateTrafficPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/UpdateTrafficPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/UpdateTrafficPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/UpdateTrafficPolicy)
