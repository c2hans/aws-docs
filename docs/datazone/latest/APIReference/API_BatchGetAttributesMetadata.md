---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_BatchGetAttributesMetadata.html
---

# BatchGetAttributesMetadata
<a name="API_BatchGetAttributesMetadata"></a>

Gets the attribute metadata.

## Request Syntax
<a name="API_BatchGetAttributesMetadata_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/entities/{{entityType}}/{{entityIdentifier}}/attributes-metadata?attributeIdentifier={{attributeIdentifiers}}&entityRevision={{entityRevision}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BatchGetAttributesMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attributeIdentifiers](#API_BatchGetAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchGetAttributesMetadata-request-uri-attributeIdentifiers"></a>
The attribute identifier.
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [domainIdentifier](#API_BatchGetAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchGetAttributesMetadata-request-uri-domainIdentifier"></a>
The domain ID where you want to get the attribute metadata.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_BatchGetAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchGetAttributesMetadata-request-uri-entityIdentifier"></a>
The entity ID for which you want to get attribute metadata.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityRevision](#API_BatchGetAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchGetAttributesMetadata-request-uri-entityRevision"></a>
The entity revision for which you want to get attribute metadata.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [entityType](#API_BatchGetAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchGetAttributesMetadata-request-uri-entityType"></a>
The entity type for which you want to get attribute metadata.
Valid Values: `ASSET | LISTING`
Required: Yes

## Request Body
<a name="API_BatchGetAttributesMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BatchGetAttributesMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributes": [
      {
         "attributeIdentifier": "string",
         "forms": [
            {
               "content": "string",
               "formName": "string",
               "typeName": "string",
               "typeRevision": "string"
            }
         ]
      }
   ],
   "errors": [
      {
         "attributeIdentifier": "string",
         "code": "string",
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetAttributesMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributes](#API_BatchGetAttributesMetadata_ResponseSyntax) **   <a name="datazone-BatchGetAttributesMetadata-response-attributes"></a>
The results of the BatchGetAttributesMetadata action.
Type: Array of [BatchGetAttributeOutput](API_BatchGetAttributeOutput.md) objects

 ** [errors](#API_BatchGetAttributesMetadata_ResponseSyntax) **   <a name="datazone-BatchGetAttributesMetadata-response-errors"></a>
The errors generated when the BatchGetAttributesMetadata action is invoked.
Type: Array of [AttributeError](API_AttributeError.md) objects

## Errors
<a name="API_BatchGetAttributesMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## Examples
<a name="API_BatchGetAttributesMetadata_Examples"></a>

### Example
<a name="API_BatchGetAttributesMetadata_Example_1"></a>

This example illustrates how to get readme and metadata form for the attribute.

#### Sample Request
<a name="API_BatchGetAttributesMetadata_Example_1_Request"></a>

```
                   aws datazone batch-get-attributes-metadata \
                   --domain-identifier dzd-dn3htlki2g96xz \
                   --entity-identifier 4nzaanzjgwoisn \
                   --entity-type ASSET \
                   --attribute-identifiers "foodname" "attribute-id-2" \
                   --region us-east-1
```

#### Sample Response
<a name="API_BatchGetAttributesMetadata_Example_1_Response"></a>

```
                   {
      "attributes": [{
          "attributeIdentifier": "foodname",
          "forms": [{
                  "content": "{\"readMe\":\"readme testing\"}",
                  "formName": "AttributeCommonFormType",
                  "typeName": "AttributeCommonFormType",
                  "typeRevision": "2"
              },
              {
                  "content": "{\"testing_field\":\"name\"}",
                  "formName": "testing_form",
                  "typeName": "testing_form",
                  "typeRevision": "3"
              }
          ]
      }],
      "errors": [{
          "attributeIdentifier": "attribute-id-2",
          "code": "404",
          "message": "Attribute 'attribute-id-2' not found"
      }]
  }
```

## See Also
<a name="API_BatchGetAttributesMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/BatchGetAttributesMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/BatchGetAttributesMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/BatchGetAttributesMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/BatchGetAttributesMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/BatchGetAttributesMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/BatchGetAttributesMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/BatchGetAttributesMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/BatchGetAttributesMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/BatchGetAttributesMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/BatchGetAttributesMetadata)
