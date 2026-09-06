---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ServerlessTrack.html
---

# ServerlessTrack
<a name="API_ServerlessTrack"></a>

Defines a track that determines which Amazon Redshift version to apply after a new version is released. If the value for `ServerlessTrack` is `current`, the workgroup is updated to the most recently certified release. If the value is `trailing`, the workgroup is updated to the previously certified release.

## Contents
<a name="API_ServerlessTrack_Contents"></a>

 ** trackName **   <a name="redshiftserverless-Type-ServerlessTrack-trackName"></a>
The name of the track. Valid values are `current` and `trailing`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_]+`
Required: No

 ** updateTargets **   <a name="redshiftserverless-Type-ServerlessTrack-updateTargets"></a>
An array of `UpdateTarget` objects to update with the track.
Type: Array of [UpdateTarget](API_UpdateTarget.md) objects
Required: No

 ** workgroupVersion **   <a name="redshiftserverless-Type-ServerlessTrack-workgroupVersion"></a>
The workgroup version number for the workgroup release.
Type: String
Required: No

## See Also
<a name="API_ServerlessTrack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ServerlessTrack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ServerlessTrack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ServerlessTrack)
