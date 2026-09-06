---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AddAttributesToFindings.html
---

# AddAttributesToFindings
<a name="API_AddAttributesToFindings"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Assigns attributes (key and value pairs) to the findings that are specified by the ARNs of the findings.

## Request Syntax
<a name="API_AddAttributesToFindings_RequestSyntax"></a>

```
{
   "attributes": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "findingArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_AddAttributesToFindings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attributes](#API_AddAttributesToFindings_RequestSyntax) **   <a name="Inspector-AddAttributesToFindings-request-attributes"></a>
The array of attributes that you want to assign to specified findings.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** [findingArns](#API_AddAttributesToFindings_RequestSyntax) **   <a name="Inspector-AddAttributesToFindings-request-findingArns"></a>
The ARNs that specify the findings that you want to assign attributes to.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_AddAttributesToFindings_ResponseSyntax"></a>

```
{
   "failedItems": {
      "string" : {
         "failureCode": "string",
         "retryable": boolean
      }
   }
}
```

## Response Elements
<a name="API_AddAttributesToFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedItems](#API_AddAttributesToFindings_ResponseSyntax) **   <a name="Inspector-AddAttributesToFindings-response-failedItems"></a>
Attribute details that cannot be described. An error code is provided for each failed item.
Type: String to [FailedItemDetails](API_FailedItemDetails.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_AddAttributesToFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** NoSuchEntityException **
The request was rejected because it referenced an entity that does not exist. The error code describes the entity.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** ServiceTemporarilyUnavailableException **
The serice is temporary unavailable.
 ** canRetry **
You can wait and then retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 400

## Examples
<a name="API_AddAttributesToFindings_Examples"></a>

### Example
<a name="API_AddAttributesToFindings_Example_1"></a>

This example illustrates one usage of AddAttributesToFindings.

#### Sample Request
<a name="API_AddAttributesToFindings_Example_1_Request"></a>

```

                  POST / HTTP/1.1
                  Host: inspector.us-west-2.amazonaws.com
                  Accept-Encoding: identity
                  Content-Length: 189
                  X-Amz-Target: InspectorService.AddAttributesToFindings
                  X-Amz-Date: 20160329T233810Z
                  User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
                  Content-Type: application/x-amz-json-1.1
                  Authorization: AUTHPARAMS
                  {
                    "attributes": [
                      {
                        "key": "Example",
                        "value": "example"
                      }
                    ],
                    "findingArns": [
                      "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU"
                    ]
                  }
```

#### Sample Response
<a name="API_AddAttributesToFindings_Example_1_Response"></a>

```

                  HTTP/1.1 200 OK
                  x-amzn-RequestId: 4c8b9c50-f607-11e5-9380-d76f0924b6d7
                  Content-Type: application/x-amz-json-1.1
                  Content-Length: 18
                  Date: Tue, 29 Mar 2016 23:38:11 GMT
                  {
                    "failedItems": {}
                  }
```

## See Also
<a name="API_AddAttributesToFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/AddAttributesToFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/AddAttributesToFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AddAttributesToFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/AddAttributesToFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AddAttributesToFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/AddAttributesToFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/AddAttributesToFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/AddAttributesToFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/AddAttributesToFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AddAttributesToFindings)
