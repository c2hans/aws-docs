---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetResourcePolicies.html
---

# GetResourcePolicies
<a name="API_GetResourcePolicies"></a>

Returns an array of the `Policy` object.

## Request Syntax
<a name="API_GetResourcePolicies_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourcePolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetResourcePolicies_RequestSyntax) **   <a name="systemsmanager-GetResourcePolicies-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_GetResourcePolicies_RequestSyntax) **   <a name="systemsmanager-GetResourcePolicies-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

 ** [ResourceArn](#API_GetResourcePolicies_RequestSyntax) **   <a name="systemsmanager-GetResourcePolicies-request-ResourceArn"></a>
Amazon Resource Name (ARN) of the resource to which the policies are attached.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_GetResourcePolicies_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Policies": [
      {
         "Policy": "string",
         "PolicyHash": "string",
         "PolicyId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetResourcePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetResourcePolicies_ResponseSyntax) **   <a name="systemsmanager-GetResourcePolicies-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

 ** [Policies](#API_GetResourcePolicies_ResponseSyntax) **   <a name="systemsmanager-GetResourcePolicies-response-Policies"></a>
An array of the `Policy` object.
Type: Array of [GetResourcePoliciesResponseEntry](API_GetResourcePoliciesResponseEntry.md) objects

## Errors
<a name="API_GetResourcePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified parameter to be shared could not be found.
HTTP Status Code: 400

 ** ResourcePolicyInvalidParameterException **
One or more parameters specified for the call aren't valid. Verify the parameters and their values and try again.
HTTP Status Code: 400

## See Also
<a name="API_GetResourcePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetResourcePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetResourcePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetResourcePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetResourcePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetResourcePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetResourcePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetResourcePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetResourcePolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetResourcePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetResourcePolicies)
