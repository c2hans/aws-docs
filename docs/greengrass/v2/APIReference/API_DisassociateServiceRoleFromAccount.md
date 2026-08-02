---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DisassociateServiceRoleFromAccount.html
---

# DisassociateServiceRoleFromAccount
<a name="API_DisassociateServiceRoleFromAccount"></a>

Disassociates the Greengrass service role from AWS IoT Greengrass for your AWS account in this AWS Region. Without a service role, AWS IoT Greengrass can't verify the identity of client devices or manage core device connectivity information. For more information, see [Greengrass service role](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html) in the * AWS IoT Greengrass Version 2 Developer Guide*.

## Request Syntax
<a name="API_DisassociateServiceRoleFromAccount_RequestSyntax"></a>

```
DELETE /greengrass/servicerole HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateServiceRoleFromAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisassociateServiceRoleFromAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateServiceRoleFromAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DisassociatedAt": "string"
}
```

## Response Elements
<a name="API_DisassociateServiceRoleFromAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DisassociatedAt](#API_DisassociateServiceRoleFromAccount_ResponseSyntax) **   <a name="greengrassv2-DisassociateServiceRoleFromAccount-response-DisassociatedAt"></a>
The time when the service role was disassociated from AWS IoT Greengrass for your AWS account in this AWS Region.
Type: String

## Errors
<a name="API_DisassociateServiceRoleFromAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

## See Also
<a name="API_DisassociateServiceRoleFromAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/DisassociateServiceRoleFromAccount)
