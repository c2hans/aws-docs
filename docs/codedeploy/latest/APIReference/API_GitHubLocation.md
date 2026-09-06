---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GitHubLocation.html
---

# GitHubLocation
<a name="API_GitHubLocation"></a>

Information about the location of application artifacts stored in GitHub.

## Contents
<a name="API_GitHubLocation_Contents"></a>

 ** commitId **   <a name="CodeDeploy-Type-GitHubLocation-commitId"></a>
The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.
Type: String
Required: No

 ** repository **   <a name="CodeDeploy-Type-GitHubLocation-repository"></a>
The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.
Type: String
Required: No

## See Also
<a name="API_GitHubLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GitHubLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GitHubLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GitHubLocation)
