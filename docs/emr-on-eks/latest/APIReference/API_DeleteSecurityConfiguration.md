---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DeleteSecurityConfiguration.html
---

# DeleteSecurityConfiguration
<a name="API_DeleteSecurityConfiguration"></a>

Deletes a security configuration.

## Request Syntax
<a name="API_DeleteSecurityConfiguration_RequestSyntax"></a>

```
DELETE /securityconfigurations/{{securityConfigurationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteSecurityConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [securityConfigurationId](#API_DeleteSecurityConfiguration_RequestSyntax) **   <a name="emroneks-DeleteSecurityConfiguration-request-uri-id"></a>
The ID of the security configuration to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_DeleteSecurityConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteSecurityConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string"
}
```

## Response Elements
<a name="API_DeleteSecurityConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_DeleteSecurityConfiguration_ResponseSyntax) **   <a name="emroneks-DeleteSecurityConfiguration-response-id"></a>
The ID of the deleted security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

## Errors
<a name="API_DeleteSecurityConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSecurityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/DeleteSecurityConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/DeleteSecurityConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/DeleteSecurityConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/DeleteSecurityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/DeleteSecurityConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/DeleteSecurityConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/DeleteSecurityConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/DeleteSecurityConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/DeleteSecurityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/DeleteSecurityConfiguration)
