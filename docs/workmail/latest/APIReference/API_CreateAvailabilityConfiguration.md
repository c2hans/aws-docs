---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateAvailabilityConfiguration.html
---

# CreateAvailabilityConfiguration
<a name="API_CreateAvailabilityConfiguration"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Creates an `AvailabilityConfiguration` for the given WorkMail organization and domain.

## Request Syntax
<a name="API_CreateAvailabilityConfiguration_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DomainName": "{{string}}",
   "EwsProvider": {
      "EwsEndpoint": "{{string}}",
      "EwsPassword": "{{string}}",
      "EwsUsername": "{{string}}"
   },
   "LambdaProvider": {
      "LambdaArn": "{{string}}"
   },
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateAvailabilityConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateAvailabilityConfiguration_RequestSyntax) **   <a name="workmail-CreateAvailabilityConfiguration-request-ClientToken"></a>
An idempotent token that ensures that an API request is executed only once.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7e]+`
Required: No

 ** [DomainName](#API_CreateAvailabilityConfiguration_RequestSyntax) **   <a name="workmail-CreateAvailabilityConfiguration-request-DomainName"></a>
The domain to which the provider applies.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9.-]+`
Required: Yes

 ** [EwsProvider](#API_CreateAvailabilityConfiguration_RequestSyntax) **   <a name="workmail-CreateAvailabilityConfiguration-request-EwsProvider"></a>
Exchange Web Services (EWS) availability provider definition. The request must contain exactly one provider definition, either `EwsProvider` or `LambdaProvider`.
Type: [EwsAvailabilityProvider](API_EwsAvailabilityProvider.md) object
Required: No

 ** [LambdaProvider](#API_CreateAvailabilityConfiguration_RequestSyntax) **   <a name="workmail-CreateAvailabilityConfiguration-request-LambdaProvider"></a>
Lambda availability provider definition. The request must contain exactly one provider definition, either `EwsProvider` or `LambdaProvider`.
Type: [LambdaAvailabilityProvider](API_LambdaAvailabilityProvider.md) object
Required: No

 ** [OrganizationId](#API_CreateAvailabilityConfiguration_RequestSyntax) **   <a name="workmail-CreateAvailabilityConfiguration-request-OrganizationId"></a>
The WorkMail organization for which the `AvailabilityConfiguration` will be created.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Elements
<a name="API_CreateAvailabilityConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateAvailabilityConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** LimitExceededException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The request exceeds the limit of the resource.
HTTP Status Code: 400

 ** NameAvailabilityException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The user, group, or resource name isn't unique in WorkMail.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

## See Also
<a name="API_CreateAvailabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/CreateAvailabilityConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/CreateAvailabilityConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/CreateAvailabilityConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/CreateAvailabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/CreateAvailabilityConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/CreateAvailabilityConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/CreateAvailabilityConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/CreateAvailabilityConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/CreateAvailabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/CreateAvailabilityConfiguration)
