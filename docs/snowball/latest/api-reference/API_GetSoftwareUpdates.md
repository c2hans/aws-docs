---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetSoftwareUpdates.html
---

# GetSoftwareUpdates
<a name="API_GetSoftwareUpdates"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Returns an Amazon S3 presigned URL for an update file associated with a specified `JobId`.

## Request Syntax
<a name="API_GetSoftwareUpdates_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSoftwareUpdates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_GetSoftwareUpdates_RequestSyntax) **   <a name="Snowball-GetSoftwareUpdates-request-JobId"></a>
The ID for a job that you want to get the software update file for, for example `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_GetSoftwareUpdates_ResponseSyntax"></a>

```
{
   "UpdatesURI": "string"
}
```

## Response Elements
<a name="API_GetSoftwareUpdates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UpdatesURI](#API_GetSoftwareUpdates_ResponseSyntax) **   <a name="Snowball-GetSoftwareUpdates-response-UpdatesURI"></a>
The Amazon S3 presigned URL for the update file associated with the specified `JobId` value. The software update will be available for 2 days after this request is made. To access an update after the 2 days have passed, you'll have to make another call to `GetSoftwareUpdates`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_GetSoftwareUpdates_Errors"></a>

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
<a name="API_GetSoftwareUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/GetSoftwareUpdates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/GetSoftwareUpdates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/GetSoftwareUpdates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/GetSoftwareUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/GetSoftwareUpdates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/GetSoftwareUpdates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/GetSoftwareUpdates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/GetSoftwareUpdates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/GetSoftwareUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/GetSoftwareUpdates)
