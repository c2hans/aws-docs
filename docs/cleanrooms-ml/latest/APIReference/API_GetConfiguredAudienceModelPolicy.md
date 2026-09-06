---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetConfiguredAudienceModelPolicy.html
---

# GetConfiguredAudienceModelPolicy
<a name="API_GetConfiguredAudienceModelPolicy"></a>

Returns information about a configured audience model policy.

## Request Syntax
<a name="API_GetConfiguredAudienceModelPolicy_RequestSyntax"></a>

```
GET /configured-audience-model/{{configuredAudienceModelArn}}/policy HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfiguredAudienceModelPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredAudienceModelArn](#API_GetConfiguredAudienceModelPolicy_RequestSyntax) **   <a name="API-GetConfiguredAudienceModelPolicy-request-uri-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_GetConfiguredAudienceModelPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfiguredAudienceModelPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredAudienceModelArn": "string",
   "configuredAudienceModelPolicy": "string",
   "policyHash": "string"
}
```

## Response Elements
<a name="API_GetConfiguredAudienceModelPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredAudienceModelArn](#API_GetConfiguredAudienceModelPolicy_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModelPolicy-response-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`

 ** [configuredAudienceModelPolicy](#API_GetConfiguredAudienceModelPolicy_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModelPolicy-response-configuredAudienceModelPolicy"></a>
The configured audience model policy. This is a JSON IAM resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.

 ** [policyHash](#API_GetConfiguredAudienceModelPolicy_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModelPolicy-response-policyHash"></a>
A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `[0-9a-f]+`

## Errors
<a name="API_GetConfiguredAudienceModelPolicy_Errors"></a>

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
<a name="API_GetConfiguredAudienceModelPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetConfiguredAudienceModelPolicy)
