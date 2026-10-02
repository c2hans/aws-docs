---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentPreferences.html
---

# GetAgentPreferences
<a name="API_GetAgentPreferences"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Returns the caller's complete set of Well-Architected Agent preferences with their current states.

## Request Syntax
<a name="API_GetAgentPreferences_RequestSyntax"></a>

```
GET /api/v1/agent-preferences HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentPreferences_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAgentPreferences_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentPreferences_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "preferences": [
      {
         "detail": "string",
         "key": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetAgentPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [preferences](#API_GetAgentPreferences_ResponseSyntax) **   <a name="wellarchitected-GetAgentPreferences-response-preferences"></a>
The caller's complete set of preferences.
Type: Array of [PreferenceEntry](API_PreferenceEntry.md) objects

## Errors
<a name="API_GetAgentPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

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
<a name="API_GetAgentPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetAgentPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetAgentPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetAgentPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetAgentPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetAgentPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetAgentPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetAgentPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetAgentPreferences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetAgentPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetAgentPreferences)
