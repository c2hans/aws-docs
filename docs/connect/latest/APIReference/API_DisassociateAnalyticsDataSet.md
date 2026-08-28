---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateAnalyticsDataSet.html
---

# DisassociateAnalyticsDataSet
<a name="API_DisassociateAnalyticsDataSet"></a>

Removes the dataset ID associated with a given Connect Customer instance.

## Request Syntax
<a name="API_DisassociateAnalyticsDataSet_RequestSyntax"></a>

```
POST /analytics-data/instance/{{InstanceId}}/association HTTP/1.1
Content-type: application/json

{
   "DataSetId": "{{string}}",
   "TargetAccountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisassociateAnalyticsDataSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DisassociateAnalyticsDataSet_RequestSyntax) **   <a name="connect-DisassociateAnalyticsDataSet-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DisassociateAnalyticsDataSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataSetId](#API_DisassociateAnalyticsDataSet_RequestSyntax) **   <a name="connect-DisassociateAnalyticsDataSet-request-DataSetId"></a>
The identifier of the dataset to remove.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [TargetAccountId](#API_DisassociateAnalyticsDataSet_RequestSyntax) **   <a name="connect-DisassociateAnalyticsDataSet-request-TargetAccountId"></a>
The identifier of the target account. Use to associate a dataset to a different account than the one containing the Connect Customer instance. If not specified, by default this value is the AWS account that has the Connect Customer instance.
Type: String
Required: No

## Response Syntax
<a name="API_DisassociateAnalyticsDataSet_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateAnalyticsDataSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateAnalyticsDataSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DisassociateAnalyticsDataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DisassociateAnalyticsDataSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DisassociateAnalyticsDataSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DisassociateAnalyticsDataSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DisassociateAnalyticsDataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DisassociateAnalyticsDataSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DisassociateAnalyticsDataSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DisassociateAnalyticsDataSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DisassociateAnalyticsDataSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DisassociateAnalyticsDataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DisassociateAnalyticsDataSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
