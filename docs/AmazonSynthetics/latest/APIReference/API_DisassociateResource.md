---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DisassociateResource.html
---

# DisassociateResource
<a name="API_DisassociateResource"></a>

Removes a canary from a group. You must run this operation in the Region where the canary exists.

## Request Syntax
<a name="API_DisassociateResource_RequestSyntax"></a>

```
PATCH /group/{{groupIdentifier}}/disassociate HTTP/1.1
Content-type: application/json

{
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisassociateResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [groupIdentifier](#API_DisassociateResource_RequestSyntax) **   <a name="synthetics-DisassociateResource-request-uri-GroupIdentifier"></a>
Specifies the group. You can specify the group name, the ARN, or the group ID as the `GroupIdentifier`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_DisassociateResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_DisassociateResource_RequestSyntax) **   <a name="synthetics-DisassociateResource-request-ResourceArn"></a>
The ARN of the canary that you want to remove from the specified group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2,4}(-[a-z]{2,4})?-[a-z]+-\d{1}:\d{12}:canary:[0-9a-z_\-]{1,255}`
Required: Yes

## Response Syntax
<a name="API_DisassociateResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A conflicting operation is already in progress.
HTTP Status Code: 409

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One of the specified resources was not found.
HTTP Status Code: 404

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/DisassociateResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/DisassociateResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/DisassociateResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/DisassociateResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/DisassociateResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/DisassociateResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/DisassociateResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/DisassociateResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/DisassociateResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/DisassociateResource)
