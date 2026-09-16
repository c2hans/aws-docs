---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListTransformers.html
---

# ListTransformers
<a name="API_ListTransformers"></a>

Lists the available transformers. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.

## Request Syntax
<a name="API_ListTransformers_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTransformers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListTransformers_RequestSyntax) **   <a name="b2bi-ListTransformers-request-maxResults"></a>
Specifies the number of items to return for the API response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListTransformers_RequestSyntax) **   <a name="b2bi-ListTransformers-request-nextToken"></a>
When additional results are obtained from the command, a `NextToken` parameter is returned in the output. You can then pass the `NextToken` parameter in a subsequent command to continue listing additional resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListTransformers_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "transformers": [
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
         "transformerId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTransformers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTransformers_ResponseSyntax) **   <a name="b2bi-ListTransformers-response-nextToken"></a>
When additional results are obtained from the command, a `NextToken` parameter is returned in the output. You can then pass the `NextToken` parameter in a subsequent command to continue listing additional resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [transformers](#API_ListTransformers_ResponseSyntax) **   <a name="b2bi-ListTransformers-response-transformers"></a>
Returns an array of one or more transformer objects.
For each transformer, a `TransformerSummary` object is returned. The `TransformerSummary` contains all the details for a specific transformer.
Type: Array of [TransformerSummary](API_TransformerSummary.md) objects

## Errors
<a name="API_ListTransformers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

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
<a name="API_ListTransformers_Examples"></a>

### Example
<a name="API_ListTransformers_Example_1"></a>

The following example lists the transformers for your account and in your region. Note that in this example, there is only one transformer listed: however, this call would return up to 50 transformers.

#### Sample Request
<a name="API_ListTransformers_Example_1_Request"></a>

```
{
    "maxResults": 50,
    "nextToken": "foo"
}
```

#### Sample Response
<a name="API_ListTransformers_Example_1_Response"></a>

```
{
    "nextToken": "foo",
    "transformers": [
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
            "modifiedAt": "2023-11-01T21:51:05.504Z",
            "name": "transformJSON",
            "sampleDocument": "s3://amzn-s3-demo-bucket/sampleDoc.txt",
            "status": "inactive",
            "transformerId": "tr-1234abcd5678efghj"
        }
    ]
}
```

## See Also
<a name="API_ListTransformers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/ListTransformers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/ListTransformers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/ListTransformers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/ListTransformers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/ListTransformers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/ListTransformers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/ListTransformers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/ListTransformers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/ListTransformers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/ListTransformers)
