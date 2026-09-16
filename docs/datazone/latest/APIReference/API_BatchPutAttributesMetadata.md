---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_BatchPutAttributesMetadata.html
---

# BatchPutAttributesMetadata
<a name="API_BatchPutAttributesMetadata"></a>

Writes the attribute metadata.

## Request Syntax
<a name="API_BatchPutAttributesMetadata_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/entities/{{entityType}}/{{entityIdentifier}}/attributes-metadata HTTP/1.1
Content-type: application/json

{
   "attributes": [
      {
         "attributeIdentifier": "{{string}}",
         "forms": [
            {
               "content": "{{string}}",
               "formName": "{{string}}",
               "typeIdentifier": "{{string}}",
               "typeRevision": "{{string}}"
            }
         ]
      }
   ],
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchPutAttributesMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_BatchPutAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchPutAttributesMetadata-request-uri-domainIdentifier"></a>
The domain ID where you want to write the attribute metadata.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_BatchPutAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchPutAttributesMetadata-request-uri-entityIdentifier"></a>
The entity ID for which you want to write the attribute metadata.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityType](#API_BatchPutAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchPutAttributesMetadata-request-uri-entityType"></a>
The entity type for which you want to write the attribute metadata.
Valid Values: `ASSET | LISTING`
Required: Yes

## Request Body
<a name="API_BatchPutAttributesMetadata_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_BatchPutAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchPutAttributesMetadata-request-attributes"></a>
The attributes of the metadata.
Type: Array of [AttributeInput](API_AttributeInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: Yes

 ** [clientToken](#API_BatchPutAttributesMetadata_RequestSyntax) **   <a name="datazone-BatchPutAttributesMetadata-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

## Response Syntax
<a name="API_BatchPutAttributesMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributes": [
      {
         "attributeIdentifier": "string"
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
<a name="API_BatchPutAttributesMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributes](#API_BatchPutAttributesMetadata_ResponseSyntax) **   <a name="datazone-BatchPutAttributesMetadata-response-attributes"></a>
The results of the BatchPutAttributeMetadata action.
Type: Array of [BatchPutAttributeOutput](API_BatchPutAttributeOutput.md) objects

 ** [errors](#API_BatchPutAttributesMetadata_ResponseSyntax) **   <a name="datazone-BatchPutAttributesMetadata-response-errors"></a>
The errors generated when the BatchPutAttributeMetadata action is invoked.
Type: Array of [AttributeError](API_AttributeError.md) objects

## Errors
<a name="API_BatchPutAttributesMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

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
<a name="API_BatchPutAttributesMetadata_Examples"></a>

### Example
<a name="API_BatchPutAttributesMetadata_Example_1"></a>

This example illustrates how to update readme and metadata form for the attribute.

#### Sample Request
<a name="API_BatchPutAttributesMetadata_Example_1_Request"></a>

```
                     aws datazone batch-put-attributes-metadata \
                     --domain-identifier "dzd-dn3htlki2g96xz" \
                     --entity-identifier "4nzaanzjgwoisn" \
                     --entity-type "ASSET" \
                     --attributes '[
                        {
                           "attributeIdentifier": "foodname",
                           "forms": [
                           {
                              "formName": "AttributeCommonFormType",
                              "typeIdentifier": "amazon.datazone.AttributeCommonFormType",
                              "content": "{\"readMe\":\"readme testing\"}"
                           },
                           {
                              "formName": "testing_form",
                              "typeIdentifier": "testing_form",
                              "typeRevision": "3",
                              "content": "{\"testing_field\":\"name\"}"
                           }
                           ]
                        }
                     ]' \
                     --client-token "ahwgcuywagcuywgtuyqfctyfq" \
                     --region us-east-1
```

#### Sample Response
<a name="API_BatchPutAttributesMetadata_Example_1_Response"></a>

```
                   {
     "attributes": [{
         "attributeIdentifier": "foodname"
     }]
 }
```

## See Also
<a name="API_BatchPutAttributesMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/BatchPutAttributesMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/BatchPutAttributesMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/BatchPutAttributesMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/BatchPutAttributesMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/BatchPutAttributesMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/BatchPutAttributesMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/BatchPutAttributesMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/BatchPutAttributesMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/BatchPutAttributesMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/BatchPutAttributesMetadata)
