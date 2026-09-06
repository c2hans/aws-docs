---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_Script.html
---

# Script
<a name="API_Script"></a>

Properties describing a Realtime script.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Contents
<a name="API_Script_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreationTime **   <a name="gameliftservers-Type-Script-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** Name **   <a name="gameliftservers-Type-Script-Name"></a>
A descriptive label that is associated with a script. Script names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** NodeJsVersion **   <a name="gameliftservers-Type-Script-NodeJsVersion"></a>
The Node.js version used for execution of your Realtime script. The valid values are `10.x | 24.x`. By default, `NodeJsVersion` is `10.x`. This value cannot be updated later.
Node.js 10 will reach end of support on September 30, 2026. See more details in the [Node.js 10 FAQs](http://aws.amazon.com/gamelift/faq/nodejs10/). For migration guidance, see [ Migrating from Node.js 10 to 24](https://docs.aws.amazon.com/gamelift/latest/realtimeguide/realtime-script.html#realtime-script-nodejs-migration).
Type: String
Length Constraints: Maximum length of 16.
Pattern: `^[0-9]+\.(?:x|[0-9]+)$`
Required: No

 ** ScriptArn **   <a name="gameliftservers-Type-Script-ScriptArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers script resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift script ARN, the resource ID matches the *ScriptId* value.
Type: String
Pattern: `^arn:.*:script\/script-\S+`
Required: No

 ** ScriptId **   <a name="gameliftservers-Type-Script-ScriptId"></a>
A unique identifier for the Realtime script
Type: String
Pattern: `^script-\S+`
Required: No

 ** SizeOnDisk **   <a name="gameliftservers-Type-Script-SizeOnDisk"></a>
The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at "0".
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** StorageLocation **   <a name="gameliftservers-Type-Script-StorageLocation"></a>
The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the `ObjectVersion` parameter to specify an earlier version.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** Version **   <a name="gameliftservers-Type-Script-Version"></a>
Version information that is associated with a build or script. Version strings do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_Script_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/Script)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/Script)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/Script)
