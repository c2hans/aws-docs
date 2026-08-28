---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_DescribeCrossAccountAccessRole.html
---

# DescribeCrossAccountAccessRole
<a name="API_DescribeCrossAccountAccessRole"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Describes the IAM role that enables Amazon Inspector Classic to access your AWS account.

## Response Syntax
<a name="API_DescribeCrossAccountAccessRole_ResponseSyntax"></a>

```
{
   "registeredAt": number,
   "roleArn": "string",
   "valid": boolean
}
```

## Response Elements
<a name="API_DescribeCrossAccountAccessRole_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registeredAt](#API_DescribeCrossAccountAccessRole_ResponseSyntax) **   <a name="Inspector-DescribeCrossAccountAccessRole-response-registeredAt"></a>
The date when the cross-account access role was registered.
Type: Timestamp

 ** [roleArn](#API_DescribeCrossAccountAccessRole_ResponseSyntax) **   <a name="Inspector-DescribeCrossAccountAccessRole-response-roleArn"></a>
The ARN that specifies the IAM role that Amazon Inspector Classic uses to access your AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [valid](#API_DescribeCrossAccountAccessRole_ResponseSyntax) **   <a name="Inspector-DescribeCrossAccountAccessRole-response-valid"></a>
A Boolean value that specifies whether the IAM role has the necessary policies attached to enable Amazon Inspector Classic to access your AWS account.
Type: Boolean

## Errors
<a name="API_DescribeCrossAccountAccessRole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

## Examples
<a name="API_DescribeCrossAccountAccessRole_Examples"></a>

### Example
<a name="API_DescribeCrossAccountAccessRole_Example_1"></a>

This example illustrates one usage of DescribeCrossAccountAccessRole.

#### Sample Request
<a name="API_DescribeCrossAccountAccessRole_Example_1_Request"></a>

```

               POST / HTTP/1.1
               Host: inspector.us-west-2.amazonaws.com
               Accept-Encoding: identity
               Content-Length: 2
               X-Amz-Target: InspectorService.DescribeCrossAccountAccessRole
               X-Amz-Date: 20160323T215330Z
               User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
               Content-Type: application/x-amz-json-1.1
               Authorization: AUTHPARAMS
               {}
```

#### Sample Response
<a name="API_DescribeCrossAccountAccessRole_Example_1_Response"></a>

```

               HTTP/1.1 200 OK
               x-amzn-RequestId: aef491a7-f141-11e5-bf1e-bbcaffe8bf2e
               Content-Type: application/x-amz-json-1.1
               Content-Length: 99
               Date: Wed, 23 Mar 2016 21:53:32 GMT
               {
                 "registeredAt": 1458069182.826,
                 "roleArn": "arn:aws:iam::123456789012:role/inspector",
                 "valid": true
               }
```

## See Also
<a name="API_DescribeCrossAccountAccessRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/DescribeCrossAccountAccessRole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/DescribeCrossAccountAccessRole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/DescribeCrossAccountAccessRole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/DescribeCrossAccountAccessRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DescribeCrossAccountAccessRole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/DescribeCrossAccountAccessRole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/DescribeCrossAccountAccessRole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/DescribeCrossAccountAccessRole)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DescribeCrossAccountAccessRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/DescribeCrossAccountAccessRole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
