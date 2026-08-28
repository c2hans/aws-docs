---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeRulesPackages.html
---

# DescribeRulesPackages
<a name="API_DescribeRulesPackages"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Describes the rules packages that are specified by the ARNs of the rules packages.

## Request Syntax
<a name="API_DescribeRulesPackages_RequestSyntax"></a>

```
{
   "locale": "{{string}}",
   "rulesPackageArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeRulesPackages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [locale](#API_DescribeRulesPackages_RequestSyntax) **   <a name="Inspector-DescribeRulesPackages-request-locale"></a>
The locale that you want to translate a rules package description into.
Type: String
Valid Values: `EN_US`
Required: No

 ** [rulesPackageArns](#API_DescribeRulesPackages_RequestSyntax) **   <a name="Inspector-DescribeRulesPackages-request-rulesPackageArns"></a>
The ARN that specifies the rules package that you want to describe.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_DescribeRulesPackages_ResponseSyntax"></a>

```
{
   "failedItems": {
      "string" : {
         "failureCode": "string",
         "retryable": boolean
      }
   },
   "rulesPackages": [
      {
         "arn": "string",
         "description": "string",
         "name": "string",
         "provider": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRulesPackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedItems](#API_DescribeRulesPackages_ResponseSyntax) **   <a name="Inspector-DescribeRulesPackages-response-failedItems"></a>
Rules package details that cannot be described. An error code is provided for each failed item.
Type: String to [FailedItemDetails](API_FailedItemDetails.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [rulesPackages](#API_DescribeRulesPackages_ResponseSyntax) **   <a name="Inspector-DescribeRulesPackages-response-rulesPackages"></a>
Information about the rules package.
Type: Array of [RulesPackage](API_RulesPackage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_DescribeRulesPackages_Errors"></a>

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
<a name="API_DescribeRulesPackages_Examples"></a>

### Example
<a name="API_DescribeRulesPackages_Example_1"></a>

This example illustrates one usage of DescribeRulesPackages.

#### Sample Request
<a name="API_DescribeRulesPackages_Example_1_Request"></a>

```

               POST / HTTP/1.1
               Host: inspector.us-west-2.amazonaws.com
               Accept-Encoding: identity
               Content-Length: 90
               X-Amz-Target: InspectorService.DescribeRulesPackages
               X-Amz-Date: 20160323T220919Z
               User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
               Content-Type: application/x-amz-json-1.1
               Authorization: AUTHPARAMS
               {
                 "rulesPackageArns": [
                   "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p"
                 ]
               }
```

#### Sample Response
<a name="API_DescribeRulesPackages_Example_1_Response"></a>

```

               HTTP/1.1 200 OK
               x-amzn-RequestId: e4a6aee0-f143-11e5-a5ad-73b7f19c946c
               Content-Type: application/x-amz-json-1.1
               Content-Length: 387
               Date: Wed, 23 Mar 2016 22:09:20 GMT
               {
                 "failedItems": {},
                 "rulesPackages": [
                   {
                     "arn": "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p",
                     "description": "The rules in this package help verify whether the EC2 instances in your application are exposed to Common Vulnerabilities and
                     Exposures (CVEs). Attacks can exploit unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of your service
                     or data. The CVE system provides a reference for publicly known information security vulnerabilities and exposures. For more information, see
                     [https://cve.mitre.org/](https://cve.mitre.org/). If a particular CVE appears in one of the produced Findings at the end of a completed
                     Inspector Classic assessment, you can search [https://cve.mitre.org/](https://cve.mitre.org/) using the CVE's ID (for example, \"CVE-2009-0021\") to
                     find detailed information about this CVE, its severity, and how to mitigate it. ",
                     "name": "Common Vulnerabilities and Exposures",
                     "provider": "Amazon Web Services, Inc.",
                     "version": "1.1"
                   }
                 ]
               }
```

## See Also
<a name="API_DescribeRulesPackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/DescribeRulesPackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/DescribeRulesPackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/DescribeRulesPackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/DescribeRulesPackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DescribeRulesPackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/DescribeRulesPackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/DescribeRulesPackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/DescribeRulesPackages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DescribeRulesPackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/DescribeRulesPackages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
