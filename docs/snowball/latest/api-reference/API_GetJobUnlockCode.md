---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetJobUnlockCode.html
---

# GetJobUnlockCode
<a name="API_GetJobUnlockCode"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Returns the `UnlockCode` code value for the specified job. A particular `UnlockCode` value can be accessed for up to 360 days after the associated job has been created.

The `UnlockCode` value is a 29-character code with 25 alphanumeric characters and 4 hyphens. This code is used to decrypt the manifest file when it is passed along with the manifest to the Snow device through the Snowball client when the client is started for the first time. The only valid status for calling this API is `WithCustomer` as the manifest and `Unlock` code values are used for securing your device and should only be used when you have the device.

As a best practice, we recommend that you don't save a copy of the `UnlockCode` in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snow device associated with that job.

## Request Syntax
<a name="API_GetJobUnlockCode_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetJobUnlockCode_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_GetJobUnlockCode_RequestSyntax) **   <a name="Snowball-GetJobUnlockCode-request-JobId"></a>
The ID for the job that you want to get the `UnlockCode` value for, for example `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_GetJobUnlockCode_ResponseSyntax"></a>

```
{
   "UnlockCode": "string"
}
```

## Response Elements
<a name="API_GetJobUnlockCode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UnlockCode](#API_GetJobUnlockCode_ResponseSyntax) **   <a name="Snowball-GetJobUnlockCode-response-UnlockCode"></a>
The `UnlockCode` value for the specified job. The `UnlockCode` value can be accessed for up to 360 days after the job has been created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_GetJobUnlockCode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidJobStateException **
The action can't be performed because the job's current state doesn't allow that action to be performed.
HTTP Status Code: 400

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_GetJobUnlockCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/GetJobUnlockCode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/GetJobUnlockCode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/GetJobUnlockCode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/GetJobUnlockCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/GetJobUnlockCode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/GetJobUnlockCode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/GetJobUnlockCode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/GetJobUnlockCode)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/GetJobUnlockCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/GetJobUnlockCode)
