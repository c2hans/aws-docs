---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_AssociateAttributeGroup.html
---

# AssociateAttributeGroup
<a name="API_app-registry_AssociateAttributeGroup"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Associates an attribute group with an application to augment the application's metadata with the group's attributes. This feature enables applications to be described with user-defined details that are machine-readable, such as third-party integrations.

## Request Syntax
<a name="API_app-registry_AssociateAttributeGroup_RequestSyntax"></a>

```
PUT /applications/{{application}}/attribute-groups/{{attributeGroup}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_AssociateAttributeGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application](#API_app-registry_AssociateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_AssociateAttributeGroup-request-uri-application"></a>
 The name, ID, or ARN of the application.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
Required: Yes

 ** [attributeGroup](#API_app-registry_AssociateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_AssociateAttributeGroup-request-uri-attributeGroup"></a>
 The name, ID, or ARN of the attribute group that holds the attributes to describe the application.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+)`
Required: Yes

## Request Body
<a name="API_app-registry_AssociateAttributeGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_AssociateAttributeGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string",
   "attributeGroupArn": "string"
}
```

## Response Elements
<a name="API_app-registry_AssociateAttributeGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_app-registry_AssociateAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_AssociateAttributeGroup-response-applicationArn"></a>
The Amazon resource name (ARN) of the application that was augmented with attributes.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

 ** [attributeGroupArn](#API_app-registry_AssociateAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_AssociateAttributeGroup-response-attributeGroupArn"></a>
The Amazon resource name (ARN) of the attribute group that contains the application's new attributes.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`

## Errors
<a name="API_app-registry_AssociateAttributeGroup_Errors"></a>

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

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_app-registry_AssociateAttributeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/AssociateAttributeGroup)
