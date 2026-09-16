---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdateTransformer.html
---

# UpdateTransformer
<a name="API_UpdateTransformer"></a>

Updates the specified parameters for a transformer. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.

## Request Syntax
<a name="API_UpdateTransformer_RequestSyntax"></a>

```
{
   "ediType": { ... },
   "fileFormat": "{{string}}",
   "inputConversion": {
      "advancedOptions": {
         "x12": {
            "splitOptions": {
               "splitBy": "{{string}}"
            },
            "validationOptions": {
               "validationRules": [
                  { ... }
               ]
            }
         }
      },
      "formatOptions": { ... },
      "fromFormat": "{{string}}"
   },
   "mapping": {
      "template": "{{string}}",
      "templateLanguage": "{{string}}"
   },
   "mappingTemplate": "{{string}}",
   "name": "{{string}}",
   "outputConversion": {
      "advancedOptions": {
         "x12": {
            "splitOptions": {
               "splitBy": "{{string}}"
            },
            "validationOptions": {
               "validationRules": [
                  { ... }
               ]
            }
         }
      },
      "formatOptions": { ... },
      "toFormat": "{{string}}"
   },
   "sampleDocument": "{{string}}",
   "sampleDocuments": {
      "bucketName": "{{string}}",
      "keys": [
         {
            "input": "{{string}}",
            "output": "{{string}}"
         }
      ]
   },
   "status": "{{string}}",
   "transformerId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTransformer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ediType](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-ediType"></a>
 *This parameter has been deprecated.*
Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.
Type: [EdiType](API_EdiType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [fileFormat](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-fileFormat"></a>
 *This parameter has been deprecated.*
Specifies that the currently supported file formats for EDI transformations are `JSON` and `XML`.
Type: String
Valid Values: `XML | JSON | NOT_USED`
Required: No

 ** [inputConversion](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-inputConversion"></a>
To update, specify the `InputConversion` object, which contains the format options for the inbound transformation.
Type: [InputConversion](API_InputConversion.md) object
Required: No

 ** [mapping](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-mapping"></a>
Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).
Type: [Mapping](API_Mapping.md) object
Required: No

 ** [mappingTemplate](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-mappingTemplate"></a>
 *This parameter has been deprecated.*
Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.
This parameter is available for backwards compatibility. Use the [Mapping](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html) data type instead.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350000.
Required: No

 ** [name](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-name"></a>
Specify a new name for the transformer, if you want to update it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9_-]{1,512}`
Required: No

 ** [outputConversion](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-outputConversion"></a>
To update, specify the `OutputConversion` object, which contains the format options for the outbound transformation.
Type: [OutputConversion](API_OutputConversion.md) object
Required: No

 ** [sampleDocument](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-sampleDocument"></a>
 *This parameter has been deprecated.*
Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [sampleDocuments](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-sampleDocuments"></a>
Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.
Type: [SampleDocuments](API_SampleDocuments.md) object
Required: No

 ** [status](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-status"></a>
Specifies the transformer's status. You can update the state of the transformer from `inactive` to `active`.
Type: String
Valid Values: `active | inactive`
Required: No

 ** [transformerId](#API_UpdateTransformer_RequestSyntax) **   <a name="b2bi-UpdateTransformer-request-transformerId"></a>
Specifies the system-assigned unique identifier for the transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateTransformer_ResponseSyntax"></a>

```
{
   "createdAt": "string",
   "ediType": { ... },
   "fileFormat": "string",
   "inputConversion": {
      "advancedOptions": {
         "x12": {
            "splitOptions": {
               "splitBy": "string"
            },
            "validationOptions": {
               "validationRules": [
                  { ... }
               ]
            }
         }
      },
      "formatOptions": { ... },
      "fromFormat": "string"
   },
   "mapping": {
      "template": "string",
      "templateLanguage": "string"
   },
   "mappingTemplate": "string",
   "modifiedAt": "string",
   "name": "string",
   "outputConversion": {
      "advancedOptions": {
         "x12": {
            "splitOptions": {
               "splitBy": "string"
            },
            "validationOptions": {
               "validationRules": [
                  { ... }
               ]
            }
         }
      },
      "formatOptions": { ... },
      "toFormat": "string"
   },
   "sampleDocument": "string",
   "sampleDocuments": {
      "bucketName": "string",
      "keys": [
         {
            "input": "string",
            "output": "string"
         }
      ]
   },
   "status": "string",
   "transformerArn": "string",
   "transformerId": "string"
}
```

## Response Elements
<a name="API_UpdateTransformer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-createdAt"></a>
Returns a timestamp for creation date and time of the transformer.
Type: Timestamp

 ** [ediType](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-ediType"></a>
 *This parameter has been deprecated.*
Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.
Type: [EdiType](API_EdiType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [fileFormat](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-fileFormat"></a>
 *This parameter has been deprecated.*
Returns that the currently supported file formats for EDI transformations are `JSON` and `XML`.
Type: String
Valid Values: `XML | JSON | NOT_USED`

 ** [inputConversion](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-inputConversion"></a>
Returns the `InputConversion` object, which contains the format options for the inbound transformation.
Type: [InputConversion](API_InputConversion.md) object

 ** [mapping](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-mapping"></a>
Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).
Type: [Mapping](API_Mapping.md) object

 ** [mappingTemplate](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-mappingTemplate"></a>
 *This parameter has been deprecated.*
Returns the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350000.

 ** [modifiedAt](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-modifiedAt"></a>
Returns a timestamp for last time the transformer was modified.
Type: Timestamp

 ** [name](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-name"></a>
Returns the name of the transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9_-]{1,512}`

 ** [outputConversion](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-outputConversion"></a>
Returns the `OutputConversion` object, which contains the format options for the outbound transformation.
Type: [OutputConversion](API_OutputConversion.md) object

 ** [sampleDocument](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-sampleDocument"></a>
 *This parameter has been deprecated.*
Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [sampleDocuments](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-sampleDocuments"></a>
Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.
Type: [SampleDocuments](API_SampleDocuments.md) object

 ** [status](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-status"></a>
Returns the state of the newly created transformer. The transformer can be either `active` or `inactive`. For the transformer to be used in a capability, its status must `active`.
Type: String
Valid Values: `active | inactive`

 ** [transformerArn](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-transformerArn"></a>
Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [transformerId](#API_UpdateTransformer_ResponseSyntax) **   <a name="b2bi-UpdateTransformer-response-transformerId"></a>
Returns the system-assigned unique identifier for the transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_UpdateTransformer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.
HTTP Status Code: 400

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.
 ** quotaCode **
The quota that was exceeded, which caused the exception.
 ** resourceId **
The ID for the resource that exceeded the quota, which caused the exception.
 ** resourceType **
The resource type (profile, partnership, transformer, or capability) that exceeded the quota, which caused the exception.
 ** serviceCode **
The code responsible for exceeding the quota, which caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.
 ** retryAfterSeconds **
The server attempts to retry a command that was throttled.
HTTP Status Code: 400

 ** ValidationException **
When you use Transformer APIs, `TestConversion`, or `TestParsing`, the service throws a validation exception if a rule is configured incorrectly. For example, a validation exception occurs when:
+ A rule references an element that doesn't exist in the selected transaction set
+ An element length rule specifies a minimum length less than 0
If your custom validation rules are configured correctly but the EDI validation fails due to those rules, this is expected behavior and doesn't result in a `ValidationException`.
For all other API operations, a validation exception occurs when a Trading Partner object can't be validated against a request from another object. This can happen during:
+ Standard EDI validation
+ Custom validation rule evaluation, such as when:
  + Element lengths don't meet specified constraints
  + Code list validations contain invalid codes
  + Required elements are missing based on your element requirement rules
HTTP Status Code: 400

## Examples
<a name="API_UpdateTransformer_Examples"></a>

### Example
<a name="API_UpdateTransformer_Example_1"></a>

The following example updates a transformer.

#### Sample Request
<a name="API_UpdateTransformer_Example_1_Request"></a>

```
{
    "ediType": {
        "x12Details": {
            "transactionSet": "X12_110",
            "version": "VERSION_4010"
        }
    },
    "mapping": {
       "templateLanguage": "JSONATA",
       "template": "{}"
    },
    "name": "transformJSON",
    "sampleDocument": "s3://amzn-s3-demo-bucket/sampleDoc.txt",
    "status": "inactive",
    "transformerId": "tr-1234abcd5678efghj"
}
```

#### Sample Response
<a name="API_UpdateTransformer_Example_1_Response"></a>

```
{
    "createdAt": "2023-11-01T21:51:05.504Z",
    "ediType": {
        "x12Details": {
            "transactionSet": "X12_110",
            "version": "VERSION_4010"
        }
    },
    "mapping": {
       "templateLanguage": "JSONATA",
       "template": "$"
    },
    "modifiedAt": "2023-11-01T21:51:05.504Z",
    "name": "transformJSON",
    "sampleDocument": "s3://amzn-s3-demo-bucket/sampleDoc.txt",
    "status": "inactive",
    "transformerArn": "arn:aws:b2bi:us-west-2:607686414464:transformer/tr-1234abcd5678efghj",
    "transformerId": "tr-1234abcd5678efghj"
}
```

## See Also
<a name="API_UpdateTransformer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/UpdateTransformer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/UpdateTransformer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/UpdateTransformer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/UpdateTransformer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/UpdateTransformer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/UpdateTransformer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/UpdateTransformer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/UpdateTransformer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/UpdateTransformer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/UpdateTransformer)
