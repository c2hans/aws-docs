---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImagePackages.html
---

# ListImagePackages
<a name="API_ListImagePackages"></a>

Lists the packages that are associated with an image build version, as determined by AWS Systems Manager Inventory at build time.

## Request Syntax
<a name="API_ListImagePackages_RequestSyntax"></a>

```
POST /ListImagePackages HTTP/1.1
Content-type: application/json

{
   "imageBuildVersionArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImagePackages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImagePackages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [imageBuildVersionArn](#API_ListImagePackages_RequestSyntax) **   <a name="imagebuilder-ListImagePackages-request-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image build version whose packages you want to list. The value must be a full build version ARN.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: Yes

 ** [maxResults](#API_ListImagePackages_RequestSyntax) **   <a name="imagebuilder-ListImagePackages-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListImagePackages_RequestSyntax) **   <a name="imagebuilder-ListImagePackages-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListImagePackages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imagePackageList": [
      {
         "packageName": "string",
         "packageVersion": "string"
      }
   ],
   "nextToken": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ListImagePackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imagePackageList](#API_ListImagePackages_ResponseSyntax) **   <a name="imagebuilder-ListImagePackages-response-imagePackageList"></a>
The list of Image Packages returned in the response.
Type: Array of [ImagePackage](API_ImagePackage.md) objects

 ** [nextToken](#API_ListImagePackages_ResponseSyntax) **   <a name="imagebuilder-ListImagePackages-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListImagePackages_ResponseSyntax) **   <a name="imagebuilder-ListImagePackages-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListImagePackages_Errors"></a>

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

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
At least one of the resources referenced by your request does not exist.
HTTP Status Code: 404

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_ListImagePackages_Examples"></a>

### List the packages in an image build version
<a name="API_ListImagePackages_Example_1"></a>

The following example lists the operating system packages that Image Builder detected in the specified image build version.

#### Sample Request
<a name="API_ListImagePackages_Example_1_Request"></a>

```
POST /ListImagePackages HTTP/1.1
Content-type: application/json

{
    "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1"
}
```

#### Sample Response
<a name="API_ListImagePackages_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "0363bd96-1a54-4736-a307-7ac6095744e0",
    "imagePackageList": [
        {
            "packageName": "passwd",
            "packageVersion": "0.80"
        },
        {
            "packageName": "dracut-config-ec2",
            "packageVersion": "3.1"
        },
        {
            "packageName": "libsolv",
            "packageVersion": "0.7.22"
        },
        {
            "packageName": "libxcrypt",
            "packageVersion": "4.4.33"
        },
        {
            "packageName": "python3-policycoreutils",
            "packageVersion": "3.4"
        }
    ]
}
```

## See Also
<a name="API_ListImagePackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListImagePackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListImagePackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListImagePackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListImagePackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListImagePackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListImagePackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListImagePackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListImagePackages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImagePackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImagePackages)
