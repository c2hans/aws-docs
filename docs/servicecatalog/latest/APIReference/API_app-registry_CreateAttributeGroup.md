---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_CreateAttributeGroup.html
---

# CreateAttributeGroup
<a name="API_app-registry_CreateAttributeGroup"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Creates a new attribute group as a container for user-defined attributes. This feature enables users to have full control over their cloud application's metadata in a rich machine-readable format to facilitate integration with automated workflows and third-party tools.

## Request Syntax
<a name="API_app-registry_CreateAttributeGroup_RequestSyntax"></a>

```
POST /attribute-groups HTTP/1.1
Content-type: application/json

{
   "attributes": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_app-registry_CreateAttributeGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_app-registry_CreateAttributeGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_app-registry_CreateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_CreateAttributeGroup-request-attributes"></a>
A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 ** [clientToken](#API_app-registry_CreateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_CreateAttributeGroup-request-clientToken"></a>
A unique identifier that you provide to ensure idempotency. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [description](#API_app-registry_CreateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_CreateAttributeGroup-request-description"></a>
The description of the attribute group that the user provides.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [name](#API_app-registry_CreateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_CreateAttributeGroup-request-name"></a>
The name of the attribute group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: Yes

 ** [tags](#API_app-registry_CreateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_CreateAttributeGroup-request-tags"></a>
Key-value pairs you can use to associate with the attribute group.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: No

## Response Syntax
<a name="API_app-registry_CreateAttributeGroup_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_app-registry_CreateAttributeGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [attributeGroup](#API_app-registry_CreateAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_CreateAttributeGroup-response-attributeGroup"></a>
Information about the attribute group.
Type: [AttributeGroup](API_app-registry_AttributeGroup.md) object

## Errors
<a name="API_app-registry_CreateAttributeGroup_Errors"></a>

 ** ConflictException **
There was a conflict when processing the request (for example, a resource with the given name already exists within the account).
HTTP Status Code: 409

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
 The maximum number of resources per account has been reached.
HTTP Status Code: 402

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_app-registry_CreateAttributeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/CreateAttributeGroup)
