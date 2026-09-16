---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_DeleteApplication.html
---

# DeleteApplication
<a name="API_app-registry_DeleteApplication"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Deletes an application that is specified either by its application ID, name, or ARN. All associated attribute groups and resources must be disassociated from it before deleting an application.

## Request Syntax
<a name="API_app-registry_DeleteApplication_RequestSyntax"></a>

```
DELETE /applications/{{application}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_DeleteApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application](#API_app-registry_DeleteApplication_RequestSyntax) **   <a name="servicecatalog-app-registry_DeleteApplication-request-uri-application"></a>
 The name, ID, or ARN of the application.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
Required: Yes

## Request Body
<a name="API_app-registry_DeleteApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_DeleteApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "application": {
      "arn": "string",
      "creationTime": "string",
      "description": "string",
      "id": "string",
      "lastUpdateTime": "string",
      "name": "string"
   }
}
```

## Response Elements
<a name="API_app-registry_DeleteApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [application](#API_app-registry_DeleteApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_DeleteApplication-response-application"></a>
Information about the deleted application.
Type: [ApplicationSummary](API_app-registry_ApplicationSummary.md) object

## Errors
<a name="API_app-registry_DeleteApplication_Errors"></a>

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_app-registry_DeleteApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/DeleteApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DeleteApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DeleteApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DeleteApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DeleteApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DeleteApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DeleteApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DeleteApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/DeleteApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DeleteApplication)
