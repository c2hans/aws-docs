---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PutAgentPreferences.html
---

# PutAgentPreferences
<a name="API_PutAgentPreferences"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Creates or replaces the caller's Well-Architected Agent preferences. Each supplied update sets the desired state of one preference. Preferences not named in the request are left unchanged. Enabling or disabling is performed synchronously, so a failure to reach the requested state is returned as a modeled exception rather than a FAILED status. On success the operation returns an empty response. Call GetAgentPreferences to read the resulting state. The account the preferences belong to is inferred from the caller's authorization context.

## Request Syntax
<a name="API_PutAgentPreferences_RequestSyntax"></a>

```
PUT /api/v1/agent-preferences HTTP/1.1
Content-type: application/json

{
   "preferences": [
      {
         "key": "{{string}}",
         "state": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_PutAgentPreferences_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAgentPreferences_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [preferences](#API_PutAgentPreferences_RequestSyntax) **   <a name="wellarchitected-PutAgentPreferences-request-preferences"></a>
Preference updates to apply. A given preference key may appear at most once.
Type: Array of [PreferenceUpdate](API_PreferenceUpdate.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_PutAgentPreferences_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutAgentPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAgentPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_PutAgentPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/PutAgentPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/PutAgentPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/PutAgentPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/PutAgentPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/PutAgentPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/PutAgentPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/PutAgentPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/PutAgentPreferences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/PutAgentPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/PutAgentPreferences)
