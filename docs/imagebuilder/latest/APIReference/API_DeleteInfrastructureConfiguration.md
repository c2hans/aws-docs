---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteInfrastructureConfiguration.html
---

# DeleteInfrastructureConfiguration
<a name="API_DeleteInfrastructureConfiguration"></a>

Deletes an infrastructure configuration. You can't delete a configuration that an image pipeline still references. The request fails with `ResourceDependencyException`. Update or delete the referencing pipelines first.

## Request Syntax
<a name="API_DeleteInfrastructureConfiguration_RequestSyntax"></a>

```
DELETE /DeleteInfrastructureConfiguration?infrastructureConfigurationArn={{infrastructureConfigurationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteInfrastructureConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [infrastructureConfigurationArn](#API_DeleteInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-DeleteInfrastructureConfiguration-request-uri-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration to delete.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

## Request Body
<a name="API_DeleteInfrastructureConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteInfrastructureConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "infrastructureConfigurationArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_DeleteInfrastructureConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [infrastructureConfigurationArn](#API_DeleteInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-DeleteInfrastructureConfiguration-response-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that was deleted.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`

 ** [requestId](#API_DeleteInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-DeleteInfrastructureConfiguration-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DeleteInfrastructureConfiguration_Errors"></a>

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

 ** ResourceDependencyException **
You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_DeleteInfrastructureConfiguration_Examples"></a>

### Delete an infrastructure configuration
<a name="API_DeleteInfrastructureConfiguration_Example_1"></a>

The following example deletes the infrastructure configuration with the specified ARN.

#### Sample Request
<a name="API_DeleteInfrastructureConfiguration_Example_1_Request"></a>

```
DELETE /DeleteInfrastructureConfiguration?infrastructureConfigurationArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Ainfrastructure-configuration%2Fmy-example-infrastructure HTTP/1.1
```

#### Sample Response
<a name="API_DeleteInfrastructureConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "fbae57f4-59fc-48ab-a25e-c67b0d9b454c",
    "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure"
}
```

## See Also
<a name="API_DeleteInfrastructureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DeleteInfrastructureConfiguration)
