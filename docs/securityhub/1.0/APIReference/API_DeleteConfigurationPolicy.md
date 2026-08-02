---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteConfigurationPolicy.html
---

# DeleteConfigurationPolicy
<a name="API_DeleteConfigurationPolicy"></a>

 Deletes a configuration policy. Only the AWS Security Hub CSPM delegated administrator can invoke this operation from the home Region. For the deletion to succeed, you must first disassociate a configuration policy from target accounts, organizational units, or the root by invoking the `StartConfigurationPolicyDisassociation` operation.

## Request Syntax
<a name="API_DeleteConfigurationPolicy_RequestSyntax"></a>

```
DELETE /configurationPolicy/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteConfigurationPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_DeleteConfigurationPolicy_RequestSyntax) **   <a name="securityhub-DeleteConfigurationPolicy-request-uri-Identifier"></a>
 The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_DeleteConfigurationPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteConfigurationPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteConfigurationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteConfigurationPolicy_Errors"></a>

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

 ** ResourceConflictException **
The resource specified in the request conflicts with an existing resource.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_DeleteConfigurationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DeleteConfigurationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DeleteConfigurationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DeleteConfigurationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DeleteConfigurationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DeleteConfigurationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DeleteConfigurationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DeleteConfigurationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DeleteConfigurationPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DeleteConfigurationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DeleteConfigurationPolicy)
