---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_DisassociateResource.html
---

# DisassociateResource
<a name="API_app-registry_DisassociateResource"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

 Disassociates a resource from application. Both the resource and the application can be specified either by ID or name.

 **Minimum permissions**

 You must have the following permissions to remove a resource that's been associated with an application using the `APPLY_APPLICATION_TAG` option for [AssociateResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AssociateResource.html).
+  `tag:GetResources`
+  `tag:UntagResources`

 You must also have the following permissions if you don't use the `AWSServiceCatalogAppRegistryFullAccess` policy. For more information, see [AWSServiceCatalogAppRegistryFullAccess](https://docs.aws.amazon.com/servicecatalog/latest/arguide/full.html) in the AppRegistry Administrator Guide.
+  `resource-groups:DisassociateResource`
+  `cloudformation:UpdateStack`
+  `cloudformation:DescribeStacks`

**Note**
 In addition, you must have the tagging permission defined by the AWS service that creates the resource. For more information, see [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntTagResources.html) in the *Resource Groups Tagging API Reference*.

## Request Syntax
<a name="API_app-registry_DisassociateResource_RequestSyntax"></a>

```
DELETE /applications/{{application}}/resources/{{resourceType}}/{{resource}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_DisassociateResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application](#API_app-registry_DisassociateResource_RequestSyntax) **   <a name="servicecatalog-app-registry_DisassociateResource-request-uri-application"></a>
The name or ID of the application.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
Required: Yes

 ** [resource](#API_app-registry_DisassociateResource_RequestSyntax) **   <a name="servicecatalog-app-registry_DisassociateResource-request-uri-resource"></a>
The name or ID of the resource.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** [resourceType](#API_app-registry_DisassociateResource_RequestSyntax) **   <a name="servicecatalog-app-registry_DisassociateResource-request-uri-resourceType"></a>
The type of the resource that is being disassociated.
Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`
Required: Yes

## Request Body
<a name="API_app-registry_DisassociateResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_DisassociateResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string",
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_app-registry_DisassociateResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_app-registry_DisassociateResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_DisassociateResource-response-applicationArn"></a>
The Amazon resource name (ARN) that specifies the application.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

 ** [resourceArn](#API_app-registry_DisassociateResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_DisassociateResource-response-resourceArn"></a>
The Amazon resource name (ARN) that specifies the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

## Errors
<a name="API_app-registry_DisassociateResource_Errors"></a>

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
<a name="API_app-registry_DisassociateResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/DisassociateResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DisassociateResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DisassociateResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DisassociateResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DisassociateResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DisassociateResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DisassociateResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DisassociateResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/DisassociateResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DisassociateResource)
