---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_PutConfiguredAudienceModelPolicy.html
---

# PutConfiguredAudienceModelPolicy
<a name="API_PutConfiguredAudienceModelPolicy"></a>

Create or update the resource policy for a configured audience model.

## Request Syntax
<a name="API_PutConfiguredAudienceModelPolicy_RequestSyntax"></a>

```
PUT /configured-audience-model/{{configuredAudienceModelArn}}/policy HTTP/1.1
Content-type: application/json

{
   "configuredAudienceModelPolicy": "{{string}}",
   "policyExistenceCondition": "{{string}}",
   "previousPolicyHash": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutConfiguredAudienceModelPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredAudienceModelArn](#API_PutConfiguredAudienceModelPolicy_RequestSyntax) **   <a name="API-PutConfiguredAudienceModelPolicy-request-uri-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that the resource policy will govern.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_PutConfiguredAudienceModelPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuredAudienceModelPolicy](#API_PutConfiguredAudienceModelPolicy_RequestSyntax) **   <a name="API-PutConfiguredAudienceModelPolicy-request-configuredAudienceModelPolicy"></a>
The IAM resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Required: Yes

 ** [policyExistenceCondition](#API_PutConfiguredAudienceModelPolicy_RequestSyntax) **   <a name="API-PutConfiguredAudienceModelPolicy-request-policyExistenceCondition"></a>
Use this to prevent unexpected concurrent modification of the policy.
Type: String
Valid Values: `POLICY_MUST_EXIST | POLICY_MUST_NOT_EXIST`
Required: No

 ** [previousPolicyHash](#API_PutConfiguredAudienceModelPolicy_RequestSyntax) **   <a name="API-PutConfiguredAudienceModelPolicy-request-previousPolicyHash"></a>
A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `[0-9a-f]+`
Required: No

## Response Syntax
<a name="API_PutConfiguredAudienceModelPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredAudienceModelPolicy": "string",
   "policyHash": "string"
}
```

## Response Elements
<a name="API_PutConfiguredAudienceModelPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredAudienceModelPolicy](#API_PutConfiguredAudienceModelPolicy_ResponseSyntax) **   <a name="API-PutConfiguredAudienceModelPolicy-response-configuredAudienceModelPolicy"></a>
The IAM resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.

 ** [policyHash](#API_PutConfiguredAudienceModelPolicy_ResponseSyntax) **   <a name="API-PutConfiguredAudienceModelPolicy-response-policyHash"></a>
A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `[0-9a-f]+`

## Errors
<a name="API_PutConfiguredAudienceModelPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_PutConfiguredAudienceModelPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/PutConfiguredAudienceModelPolicy)
