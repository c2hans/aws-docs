---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeExclusions.html
---

# DescribeExclusions
<a name="API_DescribeExclusions"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Describes the exclusions that are specified by the exclusions' ARNs.

## Request Syntax
<a name="API_DescribeExclusions_RequestSyntax"></a>

```
{
   "exclusionArns": [ "{{string}}" ],
   "locale": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeExclusions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [exclusionArns](#API_DescribeExclusions_RequestSyntax) **   <a name="Inspector-DescribeExclusions-request-exclusionArns"></a>
The list of ARNs that specify the exclusions that you want to describe.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [locale](#API_DescribeExclusions_RequestSyntax) **   <a name="Inspector-DescribeExclusions-request-locale"></a>
The locale into which you want to translate the exclusion's title, description, and recommendation.
Type: String
Valid Values: `EN_US`
Required: No

## Response Syntax
<a name="API_DescribeExclusions_ResponseSyntax"></a>

```
{
   "exclusions": {
      "string" : {
         "arn": "string",
         "attributes": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "description": "string",
         "recommendation": "string",
         "scopes": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "title": "string"
      }
   },
   "failedItems": {
      "string" : {
         "failureCode": "string",
         "retryable": boolean
      }
   }
}
```

## Response Elements
<a name="API_DescribeExclusions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exclusions](#API_DescribeExclusions_ResponseSyntax) **   <a name="Inspector-DescribeExclusions-response-exclusions"></a>
Information about the exclusions.
Type: String to [Exclusion](API_Exclusion.md) object map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [failedItems](#API_DescribeExclusions_ResponseSyntax) **   <a name="Inspector-DescribeExclusions-response-failedItems"></a>
Exclusion details that cannot be described. An error code is provided for each failed item.
Type: String to [FailedItemDetails](API_FailedItemDetails.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_DescribeExclusions_Errors"></a>

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

## See Also
<a name="API_DescribeExclusions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/DescribeExclusions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/DescribeExclusions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/DescribeExclusions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/DescribeExclusions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DescribeExclusions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/DescribeExclusions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/DescribeExclusions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/DescribeExclusions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DescribeExclusions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/DescribeExclusions)
