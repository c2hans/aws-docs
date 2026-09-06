---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_UpdateAttributeGroup.html
---

# UpdateAttributeGroup
<a name="API_app-registry_UpdateAttributeGroup"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Updates an existing attribute group with new details.

## Request Syntax
<a name="API_app-registry_UpdateAttributeGroup_RequestSyntax"></a>

```
PATCH /attribute-groups/{{attributeGroup}} HTTP/1.1
Content-type: application/json

{
   "attributes": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_app-registry_UpdateAttributeGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attributeGroup](#API_app-registry_UpdateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_UpdateAttributeGroup-request-uri-attributeGroup"></a>
 The name, ID, or ARN of the attribute group that holds the attributes to describe the application.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+)`
Required: Yes

## Request Body
<a name="API_app-registry_UpdateAttributeGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_app-registry_UpdateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_UpdateAttributeGroup-request-attributes"></a>
A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** [description](#API_app-registry_UpdateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_UpdateAttributeGroup-request-description"></a>
The description of the attribute group that the user provides.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [name](#API_app-registry_UpdateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_UpdateAttributeGroup-request-name"></a>
Deprecated: The new name of the attribute group. The name must be unique in the region in which you are updating the attribute group. Please do not use this field as we have stopped supporting name updates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

## Response Syntax
<a name="API_app-registry_UpdateAttributeGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributeGroup": {
      "arn": "string",
      "creationTime": "string",
      "description": "string",
      "id": "string",
      "lastUpdateTime": "string",
      "name": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_app-registry_UpdateAttributeGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributeGroup](#API_app-registry_UpdateAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_UpdateAttributeGroup-response-attributeGroup"></a>
The updated information of the attribute group.
Type: [AttributeGroup](API_app-registry_AttributeGroup.md) object

## Errors
<a name="API_app-registry_UpdateAttributeGroup_Errors"></a>

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
<a name="API_app-registry_UpdateAttributeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/UpdateAttributeGroup)
