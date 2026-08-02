---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetJobManifest.html
---

# GetJobManifest
<a name="API_GetJobManifest"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Returns a link to an Amazon S3 presigned URL for the manifest file associated with the specified `JobId` value. You can access the manifest file for up to 60 minutes after this request has been made. To access the manifest file after 60 minutes have passed, you'll have to make another call to the `GetJobManifest` action.

The manifest is an encrypted file that you can download after your job enters the `WithCustomer` status. This is the only valid status for calling this API as the manifest and `UnlockCode` code value are used for securing your device and should only be used when you have the device. The manifest is decrypted by using the `UnlockCode` code value, when you pass both values to the Snow device through the Snowball client when the client is started for the first time.

As a best practice, we recommend that you don't save a copy of an `UnlockCode` value in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snow device associated with that job.

The credentials of a given job, including its manifest file and unlock code, expire 360 days after the job is created.

## Request Syntax
<a name="API_GetJobManifest_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetJobManifest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_GetJobManifest_RequestSyntax) **   <a name="Snowball-GetJobManifest-request-JobId"></a>
The ID for a job that you want to get the manifest file for, for example `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_GetJobManifest_ResponseSyntax"></a>

```
{
   "ManifestURI": "string"
}
```

## Response Elements
<a name="API_GetJobManifest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManifestURI](#API_GetJobManifest_ResponseSyntax) **   <a name="Snowball-GetJobManifest-response-ManifestURI"></a>
The Amazon S3 presigned URL for the manifest file associated with the specified `JobId` value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_GetJobManifest_Errors"></a>

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
<a name="API_GetJobManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/GetJobManifest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/GetJobManifest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/GetJobManifest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/GetJobManifest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/GetJobManifest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/GetJobManifest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/GetJobManifest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/GetJobManifest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/GetJobManifest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/GetJobManifest)
