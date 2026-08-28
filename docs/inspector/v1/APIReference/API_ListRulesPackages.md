---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListRulesPackages.html
---

# ListRulesPackages
<a name="API_ListRulesPackages"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Lists all available Amazon Inspector Classic rules packages.

## Request Syntax
<a name="API_ListRulesPackages_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRulesPackages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListRulesPackages_RequestSyntax) **   <a name="Inspector-ListRulesPackages-request-maxResults"></a>
You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.
Type: Integer
Required: No

 ** [nextToken](#API_ListRulesPackages_RequestSyntax) **   <a name="Inspector-ListRulesPackages-request-nextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListRulesPackages** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## Response Syntax
<a name="API_ListRulesPackages_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "rulesPackageArns": [ "string" ]
}
```

## Response Elements
<a name="API_ListRulesPackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRulesPackages_ResponseSyntax) **   <a name="Inspector-ListRulesPackages-response-nextToken"></a>
 When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [rulesPackageArns](#API_ListRulesPackages_ResponseSyntax) **   <a name="Inspector-ListRulesPackages-response-rulesPackageArns"></a>
The list of ARNs that specifies the rules packages returned by the action.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_ListRulesPackages_Errors"></a>

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
<a name="API_ListRulesPackages_Examples"></a>

### Example
<a name="API_ListRulesPackages_Example_1"></a>

This example illustrates one usage of ListRulesPackages.

#### Sample Request
<a name="API_ListRulesPackages_Example_1_Request"></a>

```

                  POST / HTTP/1.1
                  Host: inspector.us-west-2.amazonaws.com
                  Accept-Encoding: identity
                  Content-Length: 2
                  X-Amz-Target: InspectorService.ListRulesPackages
                  X-Amz-Date: 20160323T203727Z
                  User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
                  Content-Type: application/x-amz-json-1.1
                  Authorization: AUTHPARAMS
                  {}
```

#### Sample Response
<a name="API_ListRulesPackages_Example_1_Response"></a>

```

                  HTTP/1.1 200 OK
                  x-amzn-RequestId: 0e3779a9-f137-11e5-be28-e130082e2a98
                  Content-Type: application/x-amz-json-1.1
                  Content-Length: 424
                  Date: Wed, 23 Mar 2016 20:37:26 GMT
                  {
                    "rulesPackageArns": [
                      "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p",
                      "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-H5hpSawc",
                      "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ",
                      "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-vg5GGHSD"
                    ]
                  }
```

## See Also
<a name="API_ListRulesPackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/ListRulesPackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/ListRulesPackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/ListRulesPackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/ListRulesPackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListRulesPackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/ListRulesPackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/ListRulesPackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/ListRulesPackages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListRulesPackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/ListRulesPackages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
