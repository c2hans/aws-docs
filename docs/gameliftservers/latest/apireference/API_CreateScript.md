---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateScript.html
---

# CreateScript
<a name="API_CreateScript"></a>

 **This API works with the following fleet types:** EC2, Anywhere

Creates a new script record for your Amazon GameLift Servers Realtime script. Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Amazon GameLift Servers Realtime fleet to host your game sessions. Script logic is executed during an active game session.

To create a new script record, specify a script name and provide the script file(s). The script files and all dependencies must be zipped into a single file. You can pull the zip file from either of these locations:
+ A locally available directory. Use the *ZipFile* parameter for this option.
+ An Amazon Simple Storage Service (Amazon S3) bucket under your AWS account. Use the *StorageLocation* parameter for this option. You'll need to have an Identity Access Management (IAM) role that allows the Amazon GameLift Servers service to access your S3 bucket.

If the call is successful, a new script record is created with a unique script ID. If the script file is provided as a local file, the file is uploaded to an Amazon GameLift Servers-owned S3 bucket and the script record's storage location reflects this location. If the script file is provided as an S3 bucket, Amazon GameLift Servers accesses the file at this storage location as needed for deployment.

 **Learn more**

 [Amazon GameLift Servers Amazon GameLift Servers Realtime](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html)

 [Set Up a Role for Amazon GameLift Servers Access](https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html)

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_CreateScript_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "NodeJsVersion": "{{string}}",
   "StorageLocation": {
      "Bucket": "{{string}}",
      "Key": "{{string}}",
      "ObjectVersion": "{{string}}",
      "RoleArn": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Version": "{{string}}",
   "ZipFile": {{blob}}
}
```

## Request Parameters
<a name="API_CreateScript_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_CreateScript_RequestSyntax) **   <a name="gameliftservers-CreateScript-request-Name"></a>
A descriptive label that is associated with a script. Script names do not need to be unique. You can use [UpdateScript](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateScript.html) to change this value later.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [NodeJsVersion](#API_CreateScript_RequestSyntax) **   <a name="gameliftservers-CreateScript-request-NodeJsVersion"></a>
The Node.js version used for execution of your Realtime script. The valid values are `10.x | 24.x`. By default, `NodeJsVersion` is `10.x`. This value cannot be updated later.
Node.js 10 will reach end of support on September 30, 2026. See more details in the [Node.js 10 FAQs](http://aws.amazon.com/gamelift/faq/nodejs10/). For migration guidance, see [ Migrating from Node.js 10 to 24](https://docs.aws.amazon.com/gamelift/latest/realtimeguide/realtime-script.html#realtime-script-nodejs-migration).
Type: String
Length Constraints: Maximum length of 16.
Pattern: `^[0-9]+\.(?:x|[0-9]+)$`
Required: No

 ** [StorageLocation](#API_CreateScript_RequestSyntax) **   <a name="gameliftservers-CreateScript-request-StorageLocation"></a>
The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the `ObjectVersion` parameter to specify an earlier version.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** [Tags](#API_CreateScript_RequestSyntax) **   <a name="gameliftservers-CreateScript-request-Tags"></a>
A list of labels to assign to the new script resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*. Once the resource is created, you can use [TagResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListTagsForResource.html) to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Version](#API_CreateScript_RequestSyntax) **   <a name="gameliftservers-CreateScript-request-Version"></a>
Version information that is associated with a build or script. Version strings do not need to be unique. You can use [UpdateScript](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateScript.html) to change this value later.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [ZipFile](#API_CreateScript_RequestSyntax) **   <a name="gameliftservers-CreateScript-request-ZipFile"></a>
A data object containing your Realtime scripts and dependencies as a zip file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
When using the AWS CLI tool to create a script, this parameter is set to the zip file name. It must be prepended with the string "fileb://" to indicate that the file data is a binary object. For example: `--zip-file fileb://myRealtimeScript.zip`.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 5000000.
Required: No

## Response Syntax
<a name="API_CreateScript_ResponseSyntax"></a>

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
<a name="API_CreateScript_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Script](#API_CreateScript_ResponseSyntax) **   <a name="gameliftservers-CreateScript-response-Script"></a>
The newly created script record with a unique script ID and ARN. The new script's storage location reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your account, the storage location reflects the information that was provided in the *CreateScript* request; (2) If the script file was uploaded from a local zip file, the storage location reflects an S3 location controls by the Amazon GameLift Servers service.
Type: [Script](API_Script.md) object

## Errors
<a name="API_CreateScript_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** TaggingFailedException **
The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_CreateScript_Examples"></a>

### Create a script from a local zip file
<a name="API_CreateScript_Example_1"></a>

This example creates a script record and uploads a Realtime script from a zip file that is stored locally.

#### Sample Request
<a name="API_CreateScript_Example_1_Request"></a>

```
{
    "Name": "My_Realtime_Script_1",
    "Version": "1.0.1",
    "NodeJsVersion": "24.x",
    "ZipFile": <zip file data>
}

CLI syntax:

aws gamelift create-script
    --name "My_Realtime_Script_1"
    --node-js-version "24.x"
    --script-version "1.0.1"
    --zip-file fileb://myrealtime_script.zip
```

#### Sample Response
<a name="API_CreateScript_Example_1_Response"></a>

```
{
    "Script": {
        "CreationTime": 1496708916.18,
        "Name": "My_Realtime_Script_1",
        "NodeJsVersion": "24.x",
        "ScriptArn": "arn:aws:gamelift:us-west-2::script/script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "SizeOnDisk": 9000,
        "StorageLocation": {
            "Bucket": "prod-gamescale-scripts-us-west-2",
             "Key": "123456789012/script-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
        },
        "Version": "1.0.1"
    }
}
```

### Create a script with a file in Amazon S3
<a name="API_CreateScript_Example_2"></a>

This example creates a script record and uploads a Realtime server script from a zip file that is stored in an Amazon S3 account.

#### Sample Request
<a name="API_CreateScript_Example_2_Request"></a>

```
{
    "Name": "My_Realtime_Script_2",
    "Version": "12345.678",
    "NodeJsVersion": "24.x",
    "StorageLocation": {
        "Bucket": "my_realtime_script_files",
        "Key": "myRealtimeScript.zip",
        "RoleArn": "arn:aws:iam::111122223333:role/GameLiftAccess"
    }
}

CLI syntax:

aws gamelift create-script
	--name "My_Realtime_Script_2"
	--node-js-version "24.x"
	--script-version "12345.678"
	--storage-location
		"Bucket=my_realtime_script_files,
		Key=myRealtimeScript.zip,
		RoleArn=arn:aws:iam::123456789012:role/GameLiftAccess"
```

#### Sample Response
<a name="API_CreateScript_Example_2_Response"></a>

```
{
    "Script": {
        "CreationTime": 1496708916.18,
        "Name": "My_Realtime_Script_2",
        "NodeJsVersion": "24.x",
        "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "ScriptArn": "arn:aws:gamelift:us-west-2::script/script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "SizeOnDisk": 0,
        "StorageLocation": {
            "Bucket": "my_realtime_script_files",
             "Key": "myRealtimeScript.zip"
            "RoleArn": "arn:aws:iam::111122223333:role/GameLiftAccess"
            "ObjectVersion": null
        },
        "Version": "12345.678"
    }
}
```

## See Also
<a name="API_CreateScript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateScript)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateScript)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateScript)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateScript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateScript)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateScript)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateScript)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateScript)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateScript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateScript)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
