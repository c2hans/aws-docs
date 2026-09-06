---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateReturnShippingLabel.html
---

# CreateReturnShippingLabel
<a name="API_CreateReturnShippingLabel"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Creates a shipping label that will be used to return the Snow device to AWS.

## Request Syntax
<a name="API_CreateReturnShippingLabel_RequestSyntax"></a>

```
{
   "JobId": "{{string}}",
   "ShippingOption": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateReturnShippingLabel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_CreateReturnShippingLabel_RequestSyntax) **   <a name="Snowball-CreateReturnShippingLabel-request-JobId"></a>
The ID for a job that you want to create the return shipping label for; for example, `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [ShippingOption](#API_CreateReturnShippingLabel_RequestSyntax) **   <a name="Snowball-CreateReturnShippingLabel-request-ShippingOption"></a>
The shipping speed for a particular job. This speed doesn't dictate how soon the device is returned to AWS. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:
Type: String
Valid Values: `SECOND_DAY | NEXT_DAY | EXPRESS | STANDARD`
Required: No

## Response Syntax
<a name="API_CreateReturnShippingLabel_ResponseSyntax"></a>

```
{
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateReturnShippingLabel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_CreateReturnShippingLabel_ResponseSyntax) **   <a name="Snowball-CreateReturnShippingLabel-response-Status"></a>
The status information of the task on a Snow device that is being returned to AWS.
Type: String
Valid Values: `InProgress | TimedOut | Succeeded | Failed`

## Errors
<a name="API_CreateReturnShippingLabel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
You get this exception when you call `CreateReturnShippingLabel` more than once when other requests are not completed.
 ** ConflictResource **
You get this resource when you call `CreateReturnShippingLabel` more than once when other requests are not completed. .
HTTP Status Code: 400

 ** InvalidInputCombinationException **
Job or cluster creation failed. One or more inputs were invalid. Confirm that the `SnowballType` value supports your `JobType`, and try again.
HTTP Status Code: 400

 ** InvalidJobStateException **
The action can't be performed because the job's current state doesn't allow that action to be performed.
HTTP Status Code: 400

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

 ** ReturnShippingLabelAlreadyExistsException **
You get this exception if you call `CreateReturnShippingLabel` and a valid return shipping label already exists. In this case, use `DescribeReturnShippingLabel` to get the URL.
HTTP Status Code: 400

## See Also
<a name="API_CreateReturnShippingLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/CreateReturnShippingLabel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/CreateReturnShippingLabel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/CreateReturnShippingLabel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/CreateReturnShippingLabel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/CreateReturnShippingLabel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/CreateReturnShippingLabel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/CreateReturnShippingLabel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/CreateReturnShippingLabel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/CreateReturnShippingLabel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/CreateReturnShippingLabel)
