---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_AssociateResource.html
---

# AssociateResource
<a name="API_app-registry_AssociateResource"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

 Associates a resource with an application. The resource can be specified by its ARN or name. The application can be specified by ARN, ID, or name.

 **Minimum permissions**

 You must have the following permissions to associate a resource using the `OPTIONS` parameter set to `APPLY_APPLICATION_TAG`.
+  `tag:GetResources`
+  `tag:TagResources`

 You must also have these additional permissions if you don't use the `AWSServiceCatalogAppRegistryFullAccess` policy. For more information, see [AWSServiceCatalogAppRegistryFullAccess](https://docs.aws.amazon.com/servicecatalog/latest/arguide/full.html) in the AppRegistry Administrator Guide.
+  `resource-groups:AssociateResource`
+  `cloudformation:UpdateStack`
+  `cloudformation:DescribeStacks`

**Note**
 In addition, you must have the tagging permission defined by the AWS service that creates the resource. For more information, see [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html) in the *Resource Groups Tagging API Reference*.

## Request Syntax
<a name="API_app-registry_AssociateResource_RequestSyntax"></a>

```
PUT /applications/{{application}}/resources/{{resourceType}}/{{resource}} HTTP/1.1
Content-type: application/json

{
   "options": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_app-registry_AssociateResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application](#API_app-registry_AssociateResource_RequestSyntax) **   <a name="servicecatalog-app-registry_AssociateResource-request-uri-application"></a>
 The name, ID, or ARN of the application.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
Required: Yes

 ** [resource](#API_app-registry_AssociateResource_RequestSyntax) **   <a name="servicecatalog-app-registry_AssociateResource-request-uri-resource"></a>
The name or ID of the resource of which the application will be associated.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** [resourceType](#API_app-registry_AssociateResource_RequestSyntax) **   <a name="servicecatalog-app-registry_AssociateResource-request-uri-resourceType"></a>
The type of resource of which the application will be associated.
Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`
Required: Yes

## Request Body
<a name="API_app-registry_AssociateResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [options](#API_app-registry_AssociateResource_RequestSyntax) **   <a name="servicecatalog-app-registry_AssociateResource-request-options"></a>
 Determines whether an application tag is applied or skipped.
Type: Array of strings
Valid Values: `APPLY_APPLICATION_TAG | SKIP_APPLICATION_TAG`
Required: No

## Response Syntax
<a name="API_app-registry_AssociateResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string",
   "options": [ "string" ],
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_app-registry_AssociateResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_app-registry_AssociateResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_AssociateResource-response-applicationArn"></a>
The Amazon resource name (ARN) of the application that was augmented with attributes.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

 ** [options](#API_app-registry_AssociateResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_AssociateResource-response-options"></a>
 Determines whether an application tag is applied or skipped.
Type: Array of strings
Valid Values: `APPLY_APPLICATION_TAG | SKIP_APPLICATION_TAG`

 ** [resourceArn](#API_app-registry_AssociateResource_ResponseSyntax) **   <a name="servicecatalog-app-registry_AssociateResource-response-resourceArn"></a>
The Amazon resource name (ARN) that specifies the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

## Errors
<a name="API_app-registry_AssociateResource_Errors"></a>

 ** ConflictException **
There was a conflict when processing the request (for example, a resource with the given name already exists within the account).
HTTP Status Code: 409

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
 The maximum number of resources per account has been reached.
HTTP Status Code: 402

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
<a name="API_app-registry_AssociateResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/AssociateResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/AssociateResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AssociateResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/AssociateResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AssociateResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/AssociateResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/AssociateResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/AssociateResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/AssociateResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AssociateResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
