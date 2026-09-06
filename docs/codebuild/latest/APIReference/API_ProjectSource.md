---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectSource.html
---

# ProjectSource
<a name="API_ProjectSource"></a>

Information about the build input source code for the build project.

## Contents
<a name="API_ProjectSource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** type **   <a name="CodeBuild-Type-ProjectSource-type"></a>
The type of repository that contains the source code to be built. Valid values include:
+  `BITBUCKET`: The source code is in a Bitbucket repository.
+  `CODECOMMIT`: The source code is in an CodeCommit repository.
+  `CODEPIPELINE`: The source code settings are specified in the source action of a pipeline in CodePipeline.
+  `GITHUB`: The source code is in a GitHub repository.
+  `GITHUB_ENTERPRISE`: The source code is in a GitHub Enterprise Server repository.
+  `GITLAB`: The source code is in a GitLab repository.
+  `GITLAB_SELF_MANAGED`: The source code is in a self-managed GitLab repository.
+  `NO_SOURCE`: The project does not have input source code.
+  `S3`: The source code is in an Amazon S3 bucket.
Type: String
Valid Values: `CODECOMMIT | CODEPIPELINE | GITHUB | GITLAB | GITLAB_SELF_MANAGED | S3 | BITBUCKET | GITHUB_ENTERPRISE | NO_SOURCE`
Required: Yes

 ** auth **   <a name="CodeBuild-Type-ProjectSource-auth"></a>
Information about the authorization settings for AWS CodeBuild to access the source code to be built.
Type: [SourceAuth](API_SourceAuth.md) object
Required: No

 ** buildspec **   <a name="CodeBuild-Type-ProjectSource-buildspec"></a>
The buildspec file declaration to use for the builds in this build project.
 If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in `CODEBUILD_SRC_DIR` environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, `arn:aws:s3:::my-codebuild-sample2/buildspec.yml`). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see [Buildspec File Name and Storage Location](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage).
Type: String
Required: No

 ** buildStatusConfig **   <a name="CodeBuild-Type-ProjectSource-buildStatusConfig"></a>
Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is `GITHUB`, `GITHUB_ENTERPRISE`, or `BITBUCKET`.
Type: [BuildStatusConfig](API_BuildStatusConfig.md) object
Required: No

 ** gitCloneDepth **   <a name="CodeBuild-Type-ProjectSource-gitCloneDepth"></a>
Information about the Git clone depth for the build project.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** gitSubmodulesConfig **   <a name="CodeBuild-Type-ProjectSource-gitSubmodulesConfig"></a>
 Information about the Git submodules configuration for the build project.
Type: [GitSubmodulesConfig](API_GitSubmodulesConfig.md) object
Required: No

 ** insecureSsl **   <a name="CodeBuild-Type-ProjectSource-insecureSsl"></a>
Enable this flag to ignore SSL warnings while connecting to the project source code.
Type: Boolean
Required: No

 ** location **   <a name="CodeBuild-Type-ProjectSource-location"></a>
Information about the location of the source code to be built. Valid values include:
+ For source code settings that are specified in the source action of a pipeline in CodePipeline, `location` should not be specified. If it is specified, CodePipeline ignores it. This is because CodePipeline uses the settings in a pipeline's source action instead of this value.
+ For source code in an CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, `https://git-codecommit.<region-ID>.amazonaws.com/v1/repos/<repo-name>`).
+ For source code in an Amazon S3 input bucket, one of the following.
  + The path to the ZIP file that contains the source code (for example, `<bucket-name>/<path>/<object-name>.zip`).
  + The path to the folder that contains the source code (for example, `<bucket-name>/<path-to-source-code>/<folder>/`).
+ For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for **Organization access**, choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize application**. (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the `source` object, set the `auth` object's `type` value to `OAUTH`.
+ For source code in an GitLab or self-managed GitLab repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitLab account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitLab, on the Connections **Authorize application** page, choose **Authorize**. Then on the AWS CodeConnections **Create GitLab connection** page, choose **Connect to GitLab**. (After you have connected to your GitLab account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to override the default connection and use this connection instead, set the `auth` object's `type` value to `CODECONNECTIONS` in the `source` object.
+ For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose **Grant access**. (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the `source` object, set the `auth` object's `type` value to `OAUTH`.
 If you specify `CODEPIPELINE` for the `Type` property, don't specify this property. For all of the other types, you must specify `Location`.
Type: String
Required: No

 ** reportBuildStatus **   <a name="CodeBuild-Type-ProjectSource-reportBuildStatus"></a>
 Set to true to report the status of a build's start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, GitLab, GitLab Self Managed, or Bitbucket. If this is set and you use a different source provider, an `invalidInputException` is thrown.
To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see [Source provider access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html) in the * AWS CodeBuild User Guide*.
The status of a build triggered by a webhook is always reported to your source provider.
If your project's builds are triggered by a webhook, you must push a new commit to the repo for a change to this property to take effect.
Type: Boolean
Required: No

 ** sourceIdentifier **   <a name="CodeBuild-Type-ProjectSource-sourceIdentifier"></a>
An identifier for this project source. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.
Type: String
Required: No

## See Also
<a name="API_ProjectSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ProjectSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ProjectSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ProjectSource)
