---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ApplicationInfo.html
---

# ApplicationInfo
<a name="API_ApplicationInfo"></a>

Information about an application.

## Contents
<a name="API_ApplicationInfo_Contents"></a>

 ** applicationId **   <a name="CodeDeploy-Type-ApplicationInfo-applicationId"></a>
The application ID.
Type: String
Required: No

 ** applicationName **   <a name="CodeDeploy-Type-ApplicationInfo-applicationName"></a>
The application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: No

 ** computePlatform **   <a name="CodeDeploy-Type-ApplicationInfo-computePlatform"></a>
The destination platform type for deployment of the application (`Lambda` or `Server`).
Type: String
Valid Values: `Server | Lambda | ECS | Kubernetes`
Required: No

 ** createTime **   <a name="CodeDeploy-Type-ApplicationInfo-createTime"></a>
The time at which the application was created.
Type: Timestamp
Required: No

 ** gitHubAccountName **   <a name="CodeDeploy-Type-ApplicationInfo-gitHubAccountName"></a>
The name for a connection to a GitHub account.
Type: String
Required: No

 ** linkedToGitHub **   <a name="CodeDeploy-Type-ApplicationInfo-linkedToGitHub"></a>
True if the user has authenticated with GitHub for the specified application. Otherwise, false.
Type: Boolean
Required: No

## See Also
<a name="API_ApplicationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ApplicationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ApplicationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ApplicationInfo)
