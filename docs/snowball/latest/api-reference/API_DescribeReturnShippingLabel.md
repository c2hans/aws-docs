---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeReturnShippingLabel.html
---

# DescribeReturnShippingLabel
<a name="API_DescribeReturnShippingLabel"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Information on the shipping label of a Snow device that is being returned to AWS.

## Request Syntax
<a name="API_DescribeReturnShippingLabel_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReturnShippingLabel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_DescribeReturnShippingLabel_RequestSyntax) **   <a name="Snowball-DescribeReturnShippingLabel-request-JobId"></a>
The automatically generated ID for a job, for example `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeReturnShippingLabel_ResponseSyntax"></a>

```
{
   "ExpirationDate": number,
   "ReturnShippingLabelURI": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeReturnShippingLabel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExpirationDate](#API_DescribeReturnShippingLabel_ResponseSyntax) **   <a name="Snowball-DescribeReturnShippingLabel-response-ExpirationDate"></a>
The expiration date of the current return shipping label.
Type: Timestamp

 ** [ReturnShippingLabelURI](#API_DescribeReturnShippingLabel_ResponseSyntax) **   <a name="Snowball-DescribeReturnShippingLabel-response-ReturnShippingLabelURI"></a>
The pre-signed Amazon S3 URI used to download the return shipping label.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

 ** [Status](#API_DescribeReturnShippingLabel_ResponseSyntax) **   <a name="Snowball-DescribeReturnShippingLabel-response-Status"></a>
The status information of the task on a Snow device that is being returned to AWS.
Type: String
Valid Values: `InProgress | TimedOut | Succeeded | Failed`

## Errors
<a name="API_DescribeReturnShippingLabel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
You get this exception when you call `CreateReturnShippingLabel` more than once when other requests are not completed.
 ** ConflictResource **
You get this resource when you call `CreateReturnShippingLabel` more than once when other requests are not completed. .
HTTP Status Code: 400

 ** InvalidJobStateException **
The action can't be performed because the job's current state doesn't allow that action to be performed.
HTTP Status Code: 400

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeReturnShippingLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/DescribeReturnShippingLabel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/DescribeReturnShippingLabel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/DescribeReturnShippingLabel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/DescribeReturnShippingLabel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/DescribeReturnShippingLabel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/DescribeReturnShippingLabel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/DescribeReturnShippingLabel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/DescribeReturnShippingLabel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/DescribeReturnShippingLabel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/DescribeReturnShippingLabel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
