---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_GetApplication.html
---

# GetApplication
<a name="API_app-registry_GetApplication"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

 Retrieves metadata information about one of your applications. The application can be specified by its ARN, ID, or name (which is unique within one account in one region at a given point in time). Specify by ARN or ID in automated workflows if you want to make sure that the exact same application is returned or a `ResourceNotFoundException` is thrown, avoiding the ABA addressing problem.

## Request Syntax
<a name="API_app-registry_GetApplication_RequestSyntax"></a>

```
GET /applications/{{application}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_GetApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application](#API_app-registry_GetApplication_RequestSyntax) **   <a name="servicecatalog-app-registry_GetApplication-request-uri-application"></a>
 The name, ID, or ARN of the application.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
Required: Yes

## Request Body
<a name="API_app-registry_GetApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_GetApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationTag": {
      "string" : "string"
   },
   "arn": "string",
   "associatedResourceCount": number,
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "integrations": {
      "applicationTagResourceGroup": {
         "arn": "string",
         "errorMessage": "string",
         "state": "string"
      },
      "resourceGroup": {
         "arn": "string",
         "errorMessage": "string",
         "state": "string"
      }
   },
   "lastUpdateTime": "string",
   "name": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_app-registry_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationTag](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-applicationTag"></a>
 A key-value pair that identifies an associated resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

 ** [arn](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-arn"></a>
The Amazon resource name (ARN) that specifies the application across services.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

 ** [associatedResourceCount](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-associatedResourceCount"></a>
The number of top-level resources that were registered as part of this application.
Type: Integer
Valid Range: Minimum value of 0.

 ** [creationTime](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-creationTime"></a>
The ISO-8601 formatted timestamp of the moment when the application was created.
Type: Timestamp

 ** [description](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-description"></a>
The description of the application.
Type: String
Length Constraints: Maximum length of 1024.

 ** [id](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-id"></a>
The identifier of the application.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `[a-z0-9]+`

 ** [integrations](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-integrations"></a>
 The information about the integration of the application with other services, such as AWS Resource Groups.
Type: [Integrations](API_app-registry_Integrations.md) object

 ** [lastUpdateTime](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-lastUpdateTime"></a>
The ISO-8601 formatted timestamp of the moment when the application was last updated.
Type: Timestamp

 ** [name](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-name"></a>
The name of the application. The name must be unique in the region in which you are creating the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`

 ** [tags](#API_app-registry_GetApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetApplication-response-tags"></a>
Key-value pairs associated with the application.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

## Errors
<a name="API_app-registry_GetApplication_Errors"></a>

 ** ConflictException **
There was a conflict when processing the request (for example, a resource with the given name already exists within the account).
HTTP Status Code: 409

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
<a name="API_app-registry_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetApplication)
