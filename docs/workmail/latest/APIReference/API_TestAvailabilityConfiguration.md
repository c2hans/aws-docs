---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_TestAvailabilityConfiguration.html
---

# TestAvailabilityConfiguration
<a name="API_TestAvailabilityConfiguration"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Performs a test on an availability provider to ensure that access is allowed. For EWS, it verifies the provided credentials can be used to successfully log in. For Lambda, it verifies that the Lambda function can be invoked and that the resource access policy was configured to deny anonymous access. An anonymous invocation is one done without providing either a `SourceArn` or `SourceAccount` header.

**Note**
The request must contain either one provider definition (`EwsProvider` or `LambdaProvider`) or the `DomainName` parameter. If the `DomainName` parameter is provided, the configuration stored under the `DomainName` will be tested.

## Request Syntax
<a name="API_TestAvailabilityConfiguration_RequestSyntax"></a>

```
{
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
<a name="API_TestAvailabilityConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_TestAvailabilityConfiguration_RequestSyntax) **   <a name="workmail-TestAvailabilityConfiguration-request-DomainName"></a>
The domain to which the provider applies. If this field is provided, a stored availability provider associated to this domain name will be tested.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** [EwsProvider](#API_TestAvailabilityConfiguration_RequestSyntax) **   <a name="workmail-TestAvailabilityConfiguration-request-EwsProvider"></a>
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
Describes an EWS based availability provider. This is only used as input to the service.
Type: [EwsAvailabilityProvider](API_EwsAvailabilityProvider.md) object
Required: No

 ** [LambdaProvider](#API_TestAvailabilityConfiguration_RequestSyntax) **   <a name="workmail-TestAvailabilityConfiguration-request-LambdaProvider"></a>
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
Describes a Lambda based availability provider.
Type: [LambdaAvailabilityProvider](API_LambdaAvailabilityProvider.md) object
Required: No

 ** [OrganizationId](#API_TestAvailabilityConfiguration_RequestSyntax) **   <a name="workmail-TestAvailabilityConfiguration-request-OrganizationId"></a>
The WorkMail organization where the availability provider will be tested.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_TestAvailabilityConfiguration_ResponseSyntax"></a>

```
{
   "FailureReason": "string",
   "TestPassed": boolean
}
```

## Response Elements
<a name="API_TestAvailabilityConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailureReason](#API_TestAvailabilityConfiguration_ResponseSyntax) **   <a name="workmail-TestAvailabilityConfiguration-response-FailureReason"></a>
String containing the reason for a failed test if `TestPassed` is false.
Type: String
Length Constraints: Maximum length of 256.

 ** [TestPassed](#API_TestAvailabilityConfiguration_ResponseSyntax) **   <a name="workmail-TestAvailabilityConfiguration-response-TestPassed"></a>
Boolean indicating whether the test passed or failed.
Type: Boolean

## Errors
<a name="API_TestAvailabilityConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

 ** ResourceNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_TestAvailabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/TestAvailabilityConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/TestAvailabilityConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/TestAvailabilityConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/TestAvailabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/TestAvailabilityConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/TestAvailabilityConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/TestAvailabilityConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/TestAvailabilityConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/TestAvailabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/TestAvailabilityConfiguration)
