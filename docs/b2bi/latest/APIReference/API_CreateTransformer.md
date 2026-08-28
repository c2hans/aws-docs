---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateTransformer.html
---

# CreateTransformer
<a name="API_CreateTransformer"></a>

Creates a transformer. AWS B2B Data Interchange currently supports two scenarios:
+  *Inbound EDI*: the AWS customer receives an EDI file from their trading partner. AWS B2B Data Interchange converts this EDI file into a JSON or XML file with a service-defined structure. A mapping template provided by the customer, in JSONata or XSLT format, is optionally applied to this file to produce a JSON or XML file with the structure the customer requires.
+  *Outbound EDI*: the AWS customer has a JSON or XML file containing data that they wish to use in an EDI file. A mapping template, provided by the customer (in either JSONata or XSLT format) is applied to this file to generate a JSON or XML file in the service-defined structure. This file is then converted to an EDI file.

**Note**
The following fields are provided for backwards compatibility only: `fileFormat`, `mappingTemplate`, `ediType`, and `sampleDocument`.
Use the `mapping` data type in place of `mappingTemplate` and `fileFormat`
Use the `sampleDocuments` data type in place of `sampleDocument`
Use either the `inputConversion` or `outputConversion` in place of `ediType`

## Request Syntax
<a name="API_CreateTransformer_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
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
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateTransformer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-clientToken"></a>
Reserved for future use.
Type: String
Required: No

 ** [ediType](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-ediType"></a>
 *This parameter has been deprecated.*
Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.
Type: [EdiType](API_EdiType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [fileFormat](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-fileFormat"></a>
 *This parameter has been deprecated.*
Specifies that the currently supported file formats for EDI transformations are `JSON` and `XML`.
Type: String
Valid Values: `XML | JSON | NOT_USED`
Required: No

 ** [inputConversion](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-inputConversion"></a>
Specify the `InputConversion` object, which contains the format options for the inbound transformation.
Type: [InputConversion](API_InputConversion.md) object
Required: No

 ** [mapping](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-mapping"></a>
Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).
Type: [Mapping](API_Mapping.md) object
Required: No

 ** [mappingTemplate](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-mappingTemplate"></a>
 *This parameter has been deprecated.*
Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.
This parameter is available for backwards compatibility. Use the [Mapping](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html) data type instead.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350000.
Required: No

 ** [name](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-name"></a>
Specifies the name of the transformer, used to identify it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9_-]{1,512}`
Required: Yes

 ** [outputConversion](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-outputConversion"></a>
A structure that contains the `OutputConversion` object, which contains the format options for the outbound transformation.
Type: [OutputConversion](API_OutputConversion.md) object
Required: No

 ** [sampleDocument](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-sampleDocument"></a>
 *This parameter has been deprecated.*
Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [sampleDocuments](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-sampleDocuments"></a>
Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.
Type: [SampleDocuments](API_SampleDocuments.md) object
Required: No

 ** [tags](#API_CreateTransformer_RequestSyntax) **   <a name="b2bi-CreateTransformer-request-tags"></a>
Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateTransformer_ResponseSyntax"></a>

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
<a name="API_CreateTransformer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-createdAt"></a>
Returns a timestamp for creation date and time of the transformer.
Type: Timestamp

 ** [ediType](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-ediType"></a>
 *This parameter has been deprecated.*
Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.
Type: [EdiType](API_EdiType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [fileFormat](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-fileFormat"></a>
 *This parameter has been deprecated.*
Returns that the currently supported file formats for EDI transformations are `JSON` and `XML`.
Type: String
Valid Values: `XML | JSON | NOT_USED`

 ** [inputConversion](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-inputConversion"></a>
Returns the `InputConversion` object, which contains the format options for the inbound transformation.
Type: [InputConversion](API_InputConversion.md) object

 ** [mapping](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-mapping"></a>
Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).
Type: [Mapping](API_Mapping.md) object

 ** [mappingTemplate](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-mappingTemplate"></a>
 *This parameter has been deprecated.*
Returns the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350000.

 ** [name](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-name"></a>
Returns the name of the transformer, used to identify it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9_-]{1,512}`

 ** [outputConversion](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-outputConversion"></a>
Returns the `OutputConversion` object, which contains the format options for the outbound transformation.
Type: [OutputConversion](API_OutputConversion.md) object

 ** [sampleDocument](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-sampleDocument"></a>
 *This parameter has been deprecated.*
Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [sampleDocuments](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-sampleDocuments"></a>
Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.
Type: [SampleDocuments](API_SampleDocuments.md) object

 ** [status](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-status"></a>
Returns the state of the newly created transformer. The transformer can be either `active` or `inactive`. For the transformer to be used in a capability, its status must `active`.
Type: String
Valid Values: `active | inactive`

 ** [transformerArn](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-transformerArn"></a>
Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [transformerId](#API_CreateTransformer_ResponseSyntax) **   <a name="b2bi-CreateTransformer-response-transformerId"></a>
Returns the system-assigned unique identifier for the transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_CreateTransformer_Errors"></a>

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
<a name="API_CreateTransformer_Examples"></a>

### Example
<a name="API_CreateTransformer_Example_1"></a>

The following example creates a transformer with advanced options for EDI splitting.

#### Sample Request
<a name="API_CreateTransformer_Example_1_Request"></a>

```
{
    "clientToken": "foo",
    "ediType": {
        "x12Details": {
            "transactionSet": "X12_110",
            "version": "VERSION_4010"
        }
    },
    "fileFormat": "JSON",
    "mapping": {
       "templateLanguage": "JSONATA",
       "template": "{}"
    },
    "name": "transformJSON",
    "sampleDocument": "s3://amzn-s3-demo-bucket/sampleDoc.txt",
    "advancedOptions": {
        "x12": {
            "splitOptions": {
                "splitBy": "TRANSACTION"
            }
        }
    },
    "tags": [
        {
            "Key": "sampleKey",
            "Value": "sampleValue"
        }
    ]
}
```

#### Sample Response
<a name="API_CreateTransformer_Example_1_Response"></a>

```
{
    "createdAt": "2023-11-01T21:51:05.504Z",
    "ediType": {
        "x12Details": {
            "transactionSet": "X12_110",
            "version": "VERSION_4010"
        }
    },
    "fileFormat": "JSON",
    "mapping": {
       "templateLanguage": "JSONATA",
       "template": "$"
    },
    "name": "transformJSON",
    "sampleDocument": "s3://amzn-s3-demo-bucket/sampleDoc.txt",
    "advancedOptions": {
        "x12": {
            "splitOptions": {
                "splitBy": "TRANSACTION"
            }
        }
    },
    "status": "inactive",
    "transformerArn": "arn:aws:b2bi:us-west-2:123456789012:transformer/tr-1234abcd5678efghj",
    "transformerId": "tr-1234abcd5678efghj"
}
```

## See Also
<a name="API_CreateTransformer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/CreateTransformer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/CreateTransformer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/CreateTransformer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/CreateTransformer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/CreateTransformer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/CreateTransformer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/CreateTransformer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/CreateTransformer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/CreateTransformer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/CreateTransformer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
