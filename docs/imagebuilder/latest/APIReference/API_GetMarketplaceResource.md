---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetMarketplaceResource.html
---

# GetMarketplaceResource
<a name="API_GetMarketplaceResource"></a>

Verifies the subscription and performs resource dependency checks on the requested AWS Marketplace resource. The caller must be entitled to the resource. For AWS Marketplace components, the response contains fields to download the components and their artifacts.

## Request Syntax
<a name="API_GetMarketplaceResource_RequestSyntax"></a>

```
POST /GetMarketplaceResource HTTP/1.1
Content-type: application/json

{
   "resourceArn": "{{string}}",
   "resourceLocation": "{{string}}",
   "resourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetMarketplaceResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetMarketplaceResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceArn](#API_GetMarketplaceResource_RequestSyntax) **   <a name="imagebuilder-GetMarketplaceResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies an AWS Marketplace resource.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: Yes

 ** [resourceLocation](#API_GetMarketplaceResource_RequestSyntax) **   <a name="imagebuilder-GetMarketplaceResource-request-resourceLocation"></a>
The Amazon S3 location of the component artifact to retrieve, in `s3://bucket/key` form.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^s3://[^/]+/.+[^/]$`
Required: No

 ** [resourceType](#API_GetMarketplaceResource_RequestSyntax) **   <a name="imagebuilder-GetMarketplaceResource-request-resourceType"></a>
Specifies which type of AWS Marketplace resource Image Builder retrieves.
Type: String
Valid Values: `COMPONENT_DATA | COMPONENT_ARTIFACT`
Required: Yes

## Response Syntax
<a name="API_GetMarketplaceResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "data": "string",
   "resourceArn": "string",
   "url": "string"
}
```

## Response Elements
<a name="API_GetMarketplaceResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [data](#API_GetMarketplaceResource_ResponseSyntax) **   <a name="imagebuilder-GetMarketplaceResource-response-data"></a>
Returns obfuscated data that contains the YAML content of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [resourceArn](#API_GetMarketplaceResource_ResponseSyntax) **   <a name="imagebuilder-GetMarketplaceResource-response-resourceArn"></a>
The Amazon Resource Name (ARN) for the AWS Marketplace resource that was requested.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`

 ** [url](#API_GetMarketplaceResource_ResponseSyntax) **   <a name="imagebuilder-GetMarketplaceResource-response-url"></a>
A time-limited presigned URL for downloading the component artifact from Amazon S3.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetMarketplaceResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_GetMarketplaceResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetMarketplaceResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetMarketplaceResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetMarketplaceResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetMarketplaceResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetMarketplaceResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetMarketplaceResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetMarketplaceResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetMarketplaceResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetMarketplaceResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetMarketplaceResource)
