---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeResourceGroups.html
---

# DescribeResourceGroups
<a name="API_DescribeResourceGroups"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Describes the resource groups that are specified by the ARNs of the resource groups.

## Request Syntax
<a name="API_DescribeResourceGroups_RequestSyntax"></a>

```
{
   "resourceGroupArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeResourceGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceGroupArns](#API_DescribeResourceGroups_RequestSyntax) **   <a name="Inspector-DescribeResourceGroups-request-resourceGroupArns"></a>
The ARN that specifies the resource group that you want to describe.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_DescribeResourceGroups_ResponseSyntax"></a>

```
{
   "failedItems": {
      "string" : {
         "failureCode": "string",
         "retryable": boolean
      }
   },
   "resourceGroups": [
      {
         "arn": "string",
         "createdAt": number,
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeResourceGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedItems](#API_DescribeResourceGroups_ResponseSyntax) **   <a name="Inspector-DescribeResourceGroups-response-failedItems"></a>
Resource group details that cannot be described. An error code is provided for each failed item.
Type: String to [FailedItemDetails](API_FailedItemDetails.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [resourceGroups](#API_DescribeResourceGroups_ResponseSyntax) **   <a name="Inspector-DescribeResourceGroups-response-resourceGroups"></a>
Information about a resource group.
Type: Array of [ResourceGroup](API_ResourceGroup.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_DescribeResourceGroups_Errors"></a>

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

## Examples
<a name="API_DescribeResourceGroups_Examples"></a>

### Example
<a name="API_DescribeResourceGroups_Example_1"></a>

This example illustrates one usage of DescribeResourceGroups.

#### Sample Request
<a name="API_DescribeResourceGroups_Example_1_Request"></a>

```

               POST / HTTP/1.1
               Host: inspector.us-west-2.amazonaws.com
               Accept-Encoding: identity
               Content-Length: 92
               X-Amz-Target: InspectorService.DescribeResourceGroups
               X-Amz-Date: 20160323T220453Z
               User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
               Content-Type: application/x-amz-json-1.1
               Authorization: AUTHPARAMS
               {
                 "resourceGroupArns": [
                   "arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI"
                 ]
               }
```

#### Sample Response
<a name="API_DescribeResourceGroups_Example_1_Response"></a>

```

               HTTP/1.1 200 OK
               x-amzn-RequestId: 4636d6a9-f143-11e5-9f03-eb6e194efa59
               Content-Type: application/x-amz-json-1.1
               Content-Length: 191
               Date: Wed, 23 Mar 2016 22:04:54 GMT
               {
                 "failedItems": {},
                 "resourceGroups": [
                   {
                     "arn": "arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI",
                     "createdAt": 1458074191.098,
                     "tags": [
                       {
                         "key": "Name",
                         "value": "example"
                       }
                     ]
                   }
                 ]
               }
```

## See Also
<a name="API_DescribeResourceGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/DescribeResourceGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/DescribeResourceGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/DescribeResourceGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/DescribeResourceGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DescribeResourceGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/DescribeResourceGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/DescribeResourceGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/DescribeResourceGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DescribeResourceGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/DescribeResourceGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
