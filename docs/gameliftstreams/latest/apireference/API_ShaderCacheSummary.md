---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ShaderCacheSummary.html
---

# ShaderCacheSummary
<a name="API_ShaderCacheSummary"></a>

Describes a shader cache associated with an Amazon GameLift Streams application.

## Contents
<a name="API_ShaderCacheSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApplicationArn **   <a name="gameliftstreams-Type-ShaderCacheSummary-ApplicationArn"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`
Required: Yes

 ** Identifier **   <a name="gameliftstreams-Type-ShaderCacheSummary-Identifier"></a>
A unique identifier for the shader cache, formatted as a 32-character hexadecimal string. Format is `1271e693c50b940e228582f1ccdd4e27`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** AssociatedStreamGroups **   <a name="gameliftstreams-Type-ShaderCacheSummary-AssociatedStreamGroups"></a>
The stream groups compatible with this shader cache. Compatibility is based on GPU type and GPU driver version. For more information on shader cache compatibility, see [Shader caches](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/shader-caches.html) in the *Amazon GameLift Streams Developer Guide*.
This value is a set of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identify stream group resources. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`
Required: No

 ** LastUpdatedAt **   <a name="gameliftstreams-Type-ShaderCacheSummary-LastUpdatedAt"></a>
A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp
Required: No

 ** Status **   <a name="gameliftstreams-Type-ShaderCacheSummary-Status"></a>
The current status of the shader cache. Possible statuses include the following:
+  `INITIALIZED`: Amazon GameLift Streams received the request and is preparing the shader cache.
+  `PROCESSING`: Amazon GameLift Streams is replicating the shader cache to the streaming locations in the associated stream groups.
+  `READY`: The shader cache is replicated and available for use in stream sessions.
+  `DELETING`: Amazon GameLift Streams is deleting the shader cache.
+  `ERROR`: An error occurred during shader cache processing. Create a new shader cache to try again.
Type: String
Valid Values: `INITIALIZED | PROCESSING | READY | DELETING | ERROR`
Required: No

 ** StorageBytes **   <a name="gameliftstreams-Type-ShaderCacheSummary-StorageBytes"></a>
The total storage used by all compiled shader files in this shader cache, in bytes.
Type: Long
Required: No

## See Also
<a name="API_ShaderCacheSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ShaderCacheSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ShaderCacheSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ShaderCacheSummary)
