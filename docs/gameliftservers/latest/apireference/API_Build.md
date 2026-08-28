---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_Build.html
---

# Build
<a name="API_Build"></a>

Properties describing a custom game build.

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Contents
<a name="API_Build_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BuildArn **   <a name="gameliftservers-Type-Build-BuildArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers build resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::build/build-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`. In a GameLift build ARN, the resource ID matches the *BuildId* value.
Type: String
Pattern: `^arn:.*:build\/build-\S+`
Required: No

 ** BuildId **   <a name="gameliftservers-Type-Build-BuildId"></a>
A unique identifier for the build.
Type: String
Pattern: `^build-\S+`
Required: No

 ** CreationTime **   <a name="gameliftservers-Type-Build-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** Name **   <a name="gameliftservers-Type-Build-Name"></a>
A descriptive label that is associated with a build. Build names do not need to be unique. It can be set using [CreateBuild](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateBuild.html) or [UpdateBuild](https://docs.aws.amazon.com/gamelift/latest/apireference/UpdateBuild).
Type: String
Required: No

 ** OperatingSystem **   <a name="gameliftservers-Type-Build-OperatingSystem"></a>
Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.
Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/). For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
Type: String
Valid Values: `WINDOWS_2012 | AMAZON_LINUX | AMAZON_LINUX_2 | WINDOWS_2016 | AMAZON_LINUX_2023 | WINDOWS_2022`
Required: No

 ** ServerSdkVersion **   <a name="gameliftservers-Type-Build-ServerSdkVersion"></a>
The Amazon GameLift Servers Server SDK version used to develop your game server.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^\d+\.\d+\.\d+$`
Required: No

 ** SizeOnDisk **   <a name="gameliftservers-Type-Build-SizeOnDisk"></a>
File size of the uploaded game build, expressed in bytes. When the build status is `INITIALIZED` or when using a custom Amazon S3 storage location, this value is 0.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** Status **   <a name="gameliftservers-Type-Build-Status"></a>
Current status of the build.
Possible build statuses include the following:
+  **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
+  **READY** -- The game build has been successfully uploaded. You can now create new fleets for this build.
+  **FAILED** -- The game build upload failed. You cannot create new fleets for this build.
Type: String
Valid Values: `INITIALIZED | READY | FAILED`
Required: No

 ** Version **   <a name="gameliftservers-Type-Build-Version"></a>
Version information that is associated with a build or script. Version strings do not need to be unique.
Type: String
Required: No

## See Also
<a name="API_Build_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/Build)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/Build)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/Build)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
