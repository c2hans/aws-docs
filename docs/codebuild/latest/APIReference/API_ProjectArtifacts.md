---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectArtifacts.html
---

# ProjectArtifacts
<a name="API_ProjectArtifacts"></a>

Information about the build output artifacts for the build project.

## Contents
<a name="API_ProjectArtifacts_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** type **   <a name="CodeBuild-Type-ProjectArtifacts-type"></a>
The type of build output artifact. Valid values include:
+  `CODEPIPELINE`: The build project has build output generated through CodePipeline.
**Note**
The `CODEPIPELINE` type is not supported for `secondaryArtifacts`.
+  `NO_ARTIFACTS`: The build project does not produce any build output.
+  `S3`: The build project stores build output in Amazon S3.
Type: String
Valid Values: `CODEPIPELINE | S3 | NO_ARTIFACTS`
Required: Yes

 ** artifactIdentifier **   <a name="CodeBuild-Type-ProjectArtifacts-artifactIdentifier"></a>
 An identifier for this artifact definition.
Type: String
Required: No

 ** bucketOwnerAccess **   <a name="CodeBuild-Type-ProjectArtifacts-bucketOwnerAccess"></a>
Specifies the bucket owner's access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.
To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.
This property can be one of the following values:
NONE
The bucket owner does not have access to the objects. This is the default.
READ\_ONLY
The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.
FULL
The bucket owner has full access to the objects. Object ownership is determined by the following criteria:
+ If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucket's policy.
+ Otherwise, the uploading account retains ownership of the objects.
For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide*.
Type: String
Valid Values: `NONE | READ_ONLY | FULL`
Required: No

 ** encryptionDisabled **   <a name="CodeBuild-Type-ProjectArtifacts-encryptionDisabled"></a>
 Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException is thrown.
Type: Boolean
Required: No

 ** location **   <a name="CodeBuild-Type-ProjectArtifacts-location"></a>
Information about the build output artifact location:
+ If `type` is set to `CODEPIPELINE`, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output locations instead of AWS CodeBuild.
+ If `type` is set to `NO_ARTIFACTS`, this value is ignored if specified, because no build output is produced.
+ If `type` is set to `S3`, this is the name of the output bucket.
Type: String
Required: No

 ** name **   <a name="CodeBuild-Type-ProjectArtifacts-name"></a>
Along with `path` and `namespaceType`, the pattern that AWS CodeBuild uses to name and store the output artifact:
+ If `type` is set to `CODEPIPELINE`, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of AWS CodeBuild.
+ If `type` is set to `NO_ARTIFACTS`, this value is ignored if specified, because no build output is produced.
+ If `type` is set to `S3`, this is the name of the output artifact object. If you set the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.
For example:
+  If `path` is set to `MyArtifacts`, `namespaceType` is set to `BUILD_ID`, and `name` is set to `MyArtifact.zip`, then the output artifact is stored in `MyArtifacts/<build-ID>/MyArtifact.zip`.
+  If `path` is empty, `namespaceType` is set to `NONE`, and `name` is set to "`/`", the output artifact is stored in the root of the output bucket.
+  If `path` is set to `MyArtifacts`, `namespaceType` is set to `BUILD_ID`, and `name` is set to "`/`", the output artifact is stored in `MyArtifacts/<build-ID>`.
Type: String
Required: No

 ** namespaceType **   <a name="CodeBuild-Type-ProjectArtifacts-namespaceType"></a>
Along with `path` and `name`, the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:
+ If `type` is set to `CODEPIPELINE`, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of AWS CodeBuild.
+ If `type` is set to `NO_ARTIFACTS`, this value is ignored if specified, because no build output is produced.
+ If `type` is set to `S3`, valid values include:
  +  `BUILD_ID`: Include the build ID in the location of the build output artifact.
  +  `NONE`: Do not include the build ID. This is the default if `namespaceType` is not specified.
For example, if `path` is set to `MyArtifacts`, `namespaceType` is set to `BUILD_ID`, and `name` is set to `MyArtifact.zip`, the output artifact is stored in `MyArtifacts/<build-ID>/MyArtifact.zip`.
Type: String
Valid Values: `NONE | BUILD_ID`
Required: No

 ** overrideArtifactName **   <a name="CodeBuild-Type-ProjectArtifacts-overrideArtifactName"></a>
 If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.
Type: Boolean
Required: No

 ** packaging **   <a name="CodeBuild-Type-ProjectArtifacts-packaging"></a>
The type of build output artifact to create:
+ If `type` is set to `CODEPIPELINE`, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output artifacts instead of AWS CodeBuild.
+ If `type` is set to `NO_ARTIFACTS`, this value is ignored if specified, because no build output is produced.
+ If `type` is set to `S3`, valid values include:
  +  `NONE`: AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if `packaging` is not specified.
  +  `ZIP`: AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.
Type: String
Valid Values: `NONE | ZIP`
Required: No

 ** path **   <a name="CodeBuild-Type-ProjectArtifacts-path"></a>
Along with `namespaceType` and `name`, the pattern that AWS CodeBuild uses to name and store the output artifact:
+ If `type` is set to `CODEPIPELINE`, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of AWS CodeBuild.
+ If `type` is set to `NO_ARTIFACTS`, this value is ignored if specified, because no build output is produced.
+ If `type` is set to `S3`, this is the path to the output artifact. If `path` is not specified, `path` is not used.
For example, if `path` is set to `MyArtifacts`, `namespaceType` is set to `NONE`, and `name` is set to `MyArtifact.zip`, the output artifact is stored in the output bucket at `MyArtifacts/MyArtifact.zip`.
Type: String
Required: No

## See Also
<a name="API_ProjectArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ProjectArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ProjectArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ProjectArtifacts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
