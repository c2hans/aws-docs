---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_AssociateResource.html
---

# AssociateResource
<a name="API_AssociateResource"></a>

Associates a canary with a group. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group.

You must run this operation in the Region where the canary exists.

## Request Syntax
<a name="API_AssociateResource_RequestSyntax"></a>

```
PATCH /group/{{groupIdentifier}}/associate HTTP/1.1
Content-type: application/json

{
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [groupIdentifier](#API_AssociateResource_RequestSyntax) **   <a name="synthetics-AssociateResource-request-uri-GroupIdentifier"></a>
Specifies the group. You can specify the group name, the ARN, or the group ID as the `GroupIdentifier`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_AssociateResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_AssociateResource_RequestSyntax) **   <a name="synthetics-AssociateResource-request-ResourceArn"></a>
The ARN of the canary that you want to associate with the specified group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2,4}(-[a-z]{2,4})?-[a-z]+-\d{1}:\d{12}:canary:[0-9a-z_\-]{1,255}`
Required: Yes

## Response Syntax
<a name="API_AssociateResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateResource_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request exceeded a service quota value.
HTTP Status Code: 402

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_AssociateResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/AssociateResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/AssociateResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/AssociateResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/AssociateResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/AssociateResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/AssociateResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/AssociateResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/AssociateResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/AssociateResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/AssociateResource)
