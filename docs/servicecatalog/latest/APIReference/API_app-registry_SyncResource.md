---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_SyncResource.html
---

# SyncResource
<a name="API_app-registry_SyncResource"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Syncs the resource with current AppRegistry records.

Specifically, the resource’s AppRegistry system tags sync with its associated application. We remove the resource's AppRegistry system tags if it does not associate with the application. The caller must have permissions to read and update the resource.

## Request Syntax
<a name="API_app-registry_SyncResource_RequestSyntax"></a>

```
POST /sync/{{resourceType}}/{{resource}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_SyncResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resource](#API_app-registry_SyncResource_RequestSyntax) **   <a name="servicecatalog-app-registry_SyncResource-request-uri-resource"></a>
An entity you can work with and specify with a name or ID. Examples include an Amazon EC2 instance, an AWS CloudFormation stack, or an Amazon S3 bucket.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** [resourceType](#API_app-registry_SyncResource_RequestSyntax) **   <a name="servicecatalog-app-registry_SyncResource-request-uri-resourceType"></a>
The type of resource of which the application will be associated.
Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`
Required: Yes

## Request Body
<a name="API_app-registry_SyncResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_SyncResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionTaken": "string",
   "applicationArn": "string",
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_app-registry_SyncResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionTaken](#API_app-registry_SyncResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_SyncResource-response-actionTaken"></a>
The results of the output if an application is associated with an ARN value, which could be `syncStarted` or None.
Type: String
Valid Values: `START_SYNC | NO_ACTION`

 ** [applicationArn](#API_app-registry_SyncResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_SyncResource-response-applicationArn"></a>
The Amazon resource name (ARN) that specifies the application.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

 ** [resourceArn](#API_app-registry_SyncResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_SyncResource-response-resourceArn"></a>
The Amazon resource name (ARN) that specifies the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

## Errors
<a name="API_app-registry_SyncResource_Errors"></a>

 ** ConflictException **
There was a conflict when processing the request (for example, a resource with the given name already exists within the account).
HTTP Status Code: 409

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
 The maximum number of API requests has been exceeded.
 ** message **
A message associated with the Throttling exception.
 ** serviceCode **
The originating service code.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_app-registry_SyncResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/SyncResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/SyncResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/SyncResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/SyncResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/SyncResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/SyncResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/SyncResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/SyncResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/SyncResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/SyncResource)
