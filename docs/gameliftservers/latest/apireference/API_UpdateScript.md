---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateScript.html
---

# UpdateScript
<a name="API_UpdateScript"></a>

 **This API works with the following fleet types:** EC2

Updates Realtime script metadata and content.

To update script metadata, specify the script ID and provide updated name and/or version values.

To update script content, provide an updated zip file by pointing to either a local file or an Amazon S3 bucket location. You can use either method regardless of how the original script was uploaded. Use the *Version* parameter to track updates to the script.

If the call is successful, the updated metadata is stored in the script record and a revised script is uploaded to the Amazon GameLift Servers service. Once the script is updated and acquired by a fleet instance, the new version is used for all new game sessions.

 **Learn more**

 [Amazon GameLift Servers Amazon GameLift Servers Realtime](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html)

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_UpdateScript_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "ScriptId": "{{string}}",
   "StorageLocation": {
      "Bucket": "{{string}}",
      "Key": "{{string}}",
      "ObjectVersion": "{{string}}",
      "RoleArn": "{{string}}"
   },
   "Version": "{{string}}",
   "ZipFile": {{blob}}
}
```

## Request Parameters
<a name="API_UpdateScript_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ScriptId](#API_UpdateScript_RequestSyntax) **   <a name="gameliftservers-UpdateScript-request-ScriptId"></a>
A unique identifier for the Realtime script to update. You can use either the script ID or ARN value.
Type: String
Pattern: `^script-\S+|^arn:.*:script\/script-\S+`
Required: Yes

 ** [Name](#API_UpdateScript_RequestSyntax) **   <a name="gameliftservers-UpdateScript-request-Name"></a>
A descriptive label that is associated with a script. Script names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [StorageLocation](#API_UpdateScript_RequestSyntax) **   <a name="gameliftservers-UpdateScript-request-StorageLocation"></a>
The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the `ObjectVersion` parameter to specify an earlier version.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** [Version](#API_UpdateScript_RequestSyntax) **   <a name="gameliftservers-UpdateScript-request-Version"></a>
Version information that is associated with a build or script. Version strings do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [ZipFile](#API_UpdateScript_RequestSyntax) **   <a name="gameliftservers-UpdateScript-request-ZipFile"></a>
A data object containing your Realtime scripts and dependencies as a zip file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
When using the AWS CLI tool to create a script, this parameter is set to the zip file name. It must be prepended with the string "fileb://" to indicate that the file data is a binary object. For example: `--zip-file fileb://myRealtimeScript.zip`.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 5000000.
Required: No

## Response Syntax
<a name="API_UpdateScript_ResponseSyntax"></a>

```
{
   "Script": {
      "CreationTime": number,
      "Name": "string",
      "NodeJsVersion": "string",
      "ScriptArn": "string",
      "ScriptId": "string",
      "SizeOnDisk": number,
      "StorageLocation": {
         "Bucket": "string",
         "Key": "string",
         "ObjectVersion": "string",
         "RoleArn": "string"
      },
      "Version": "string"
   }
}
```

## Response Elements
<a name="API_UpdateScript_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Script](#API_UpdateScript_ResponseSyntax) **   <a name="gameliftservers-UpdateScript-response-Script"></a>
The newly created script record with a unique script ID. The new script's storage location reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your account, the storage location reflects the information that was provided in the *CreateScript* request; (2) If the script file was uploaded from a local zip file, the storage location reflects an S3 location controls by the Amazon GameLift Servers service.
Type: [Script](API_Script.md) object

## Errors
<a name="API_UpdateScript_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_UpdateScript_Examples"></a>

### Update a script from a local zip file
<a name="API_UpdateScript_Example_1"></a>

This example updates the Realtime script with a zip file that is stored locally.

#### Sample Request
<a name="API_UpdateScript_Example_1_Request"></a>

```
{
    "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "Version": "1.0.2",
    "ZipFile": <zip file data>
}

CLI syntax:

aws gamelift create-script
	--script-id "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
	--script-version "1.0.2"
	--zip-file fileb://myrealtime_script.zip
```

#### Sample Response
<a name="API_UpdateScript_Example_1_Response"></a>

```
{
    "Script": {
        "CreationTime": 1496708916.18,
        "Name": "My_Realtime_Script_1",
        "NodeJsVersion": "24.x",
        "ScriptArn": "arn:aws:gamelift:us-west-2::script/script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "SizeOnDisk": 10000,
        "StorageLocation": {
            "Bucket": "prod-gamescale-scripts-us-west-2",
             "Key": "123456789012/script-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
        },
        "Version": "1.0.2"
    }
}
```

### Update a script with a file in Amazon S3
<a name="API_UpdateScript_Example_2"></a>

This example updates the Realtime server script with a zip file that is stored in an S3 account.

#### Sample Request
<a name="API_UpdateScript_Example_2_Request"></a>

```
{
    "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "Version": "1.0.2",
    "StorageLocation": {
        "Bucket": "my_realtime_script_files",
        "Key": "myRealtimeScript.zip",
        "RoleArn": "arn:aws:iam::111122223333:role/GameLiftAccess"
    }
}

CLI syntax:

aws gamelift update-script
	--script-id "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
	--script-version "1.0.2"
	--storage-location
		"Bucket=my_realtime_script_files,
		Key=myRealtimeScript.zip,
		RoleArn=arn:aws:iam::123456789012:role/GameLiftAccess"
```

#### Sample Response
<a name="API_UpdateScript_Example_2_Response"></a>

```
{
    "Script": {
        "CreationTime": 1496708916.18,
        "Name": "My_Realtime_Script_1",
        "NodeJsVersion": "24.x",
        "ScriptArn": "arn:aws:gamelift:us-west-2::script/script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "SizeOnDisk": 0,
        "StorageLocation": {
            "Bucket": "my_realtime_script_files",
             "Key": "myRealtimeScript.zip"
            "RoleArn": "arn:aws:iam::111122223333:role/GameLiftAccess"
            "ObjectVersion": null
        },
        "Version": "1.0.2"
    }
}
```

## See Also
<a name="API_UpdateScript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateScript)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateScript)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateScript)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateScript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateScript)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateScript)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateScript)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateScript)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateScript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateScript)
