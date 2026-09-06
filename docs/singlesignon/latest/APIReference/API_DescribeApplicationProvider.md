---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplicationProvider.html
---

# DescribeApplicationProvider
<a name="API_DescribeApplicationProvider"></a>

Retrieves details about a provider that can be used to connect an AWS managed application or customer managed application to IAM Identity Center.

## Request Syntax
<a name="API_DescribeApplicationProvider_RequestSyntax"></a>

```
{
   "ApplicationProviderArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApplicationProvider_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationProviderArn](#API_DescribeApplicationProvider_RequestSyntax) **   <a name="singlesignon-DescribeApplicationProvider-request-ApplicationProviderArn"></a>
Specifies the ARN of the application provider for which you want details.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::aws:applicationProvider/[a-zA-Z0-9-/]+`
Required: Yes

## Response Syntax
<a name="API_DescribeApplicationProvider_ResponseSyntax"></a>

```
{
   "ApplicationProviderArn": "string",
   "DisplayData": {
      "Description": "string",
      "DisplayName": "string",
      "IconUrl": "string"
   },
   "FederationProtocol": "string",
   "ResourceServerConfig": {
      "Scopes": {
         "string" : {
            "DetailedTitle": "string",
            "LongDescription": "string"
         }
      }
   }
}
```

## Response Elements
<a name="API_DescribeApplicationProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationProviderArn](#API_DescribeApplicationProvider_ResponseSyntax) **   <a name="singlesignon-DescribeApplicationProvider-response-ApplicationProviderArn"></a>
The ARN of the application provider.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::aws:applicationProvider/[a-zA-Z0-9-/]+`

 ** [DisplayData](#API_DescribeApplicationProvider_ResponseSyntax) **   <a name="singlesignon-DescribeApplicationProvider-response-DisplayData"></a>
A structure with details about the display data for the application provider.
Type: [DisplayData](API_DisplayData.md) object

 ** [FederationProtocol](#API_DescribeApplicationProvider_ResponseSyntax) **   <a name="singlesignon-DescribeApplicationProvider-response-FederationProtocol"></a>
The protocol used to federate to the application provider.
Type: String
Valid Values: `SAML | OAUTH`

 ** [ResourceServerConfig](#API_DescribeApplicationProvider_ResponseSyntax) **   <a name="singlesignon-DescribeApplicationProvider-response-ResourceServerConfig"></a>
A structure with details about the receiving application.
Type: [ResourceServerConfig](API_ResourceServerConfig.md) object

## Errors
<a name="API_DescribeApplicationProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates that a requested resource is not found.
 ** Reason **
The reason for the resource not found exception.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
The reason for the throttling exception.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApplicationProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/DescribeApplicationProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/DescribeApplicationProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DescribeApplicationProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/DescribeApplicationProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DescribeApplicationProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/DescribeApplicationProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/DescribeApplicationProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/DescribeApplicationProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/DescribeApplicationProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DescribeApplicationProvider)
