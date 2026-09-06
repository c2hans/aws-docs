---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_GetAttributeGroup.html
---

# GetAttributeGroup
<a name="API_app-registry_GetAttributeGroup"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

 Retrieves an attribute group by its ARN, ID, or name. The attribute group can be specified by its ARN, ID, or name.

## Request Syntax
<a name="API_app-registry_GetAttributeGroup_RequestSyntax"></a>

```
GET /attribute-groups/{{attributeGroup}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_GetAttributeGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attributeGroup](#API_app-registry_GetAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-request-uri-attributeGroup"></a>
 The name, ID, or ARN of the attribute group that holds the attributes to describe the application.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+)`
Required: Yes

## Request Body
<a name="API_app-registry_GetAttributeGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_GetAttributeGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "attributes": "string",
   "createdBy": "string",
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "lastUpdateTime": "string",
   "name": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_app-registry_GetAttributeGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_app-registry_GetAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-response-arn"></a>
The Amazon resource name (ARN) that specifies the attribute group across services.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`

 ** [attributes](#API_app-registry_GetAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-response-attributes"></a>
A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

 ** [createdBy](#API_app-registry_GetAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-response-createdBy"></a>
The service principal that created the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!-)([a-z0-9-]+\.)+(aws\.internal|amazonaws\.com(\.cn)?)$`

 ** [creationTime](#API_app-registry_GetAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-response-creationTime"></a>
The ISO-8601 formatted timestamp of the moment the attribute group was created.
Type: Timestamp

 ** [description](#API_app-registry_GetAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-response-description"></a>
The description of the attribute group that the user provides.
Type: String
Length Constraints: Maximum length of 1024.

 ** [id](#API_app-registry_GetAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-response-id"></a>
The identifier of the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`

 ** [lastUpdateTime](#API_app-registry_GetAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-response-lastUpdateTime"></a>
The ISO-8601 formatted timestamp of the moment the attribute group was last updated. This time is the same as the creationTime for a newly created attribute group.
Type: Timestamp

 ** [name](#API_app-registry_GetAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-response-name"></a>
The name of the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`

 ** [tags](#API_app-registry_GetAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetAttributeGroup-response-tags"></a>
Key-value pairs associated with the attribute group.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

## Errors
<a name="API_app-registry_GetAttributeGroup_Errors"></a>

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
<a name="API_app-registry_GetAttributeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetAttributeGroup)
