---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildArtifacts.html
---

# BuildArtifacts
<a name="API_BuildArtifacts"></a>

Information about build output artifacts.

## Contents
<a name="API_BuildArtifacts_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** artifactIdentifier **   <a name="CodeBuild-Type-BuildArtifacts-artifactIdentifier"></a>
 An identifier for this artifact definition.
Type: String
Required: No

 ** bucketOwnerAccess **   <a name="CodeBuild-Type-BuildArtifacts-bucketOwnerAccess"></a>
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

 ** encryptionDisabled **   <a name="CodeBuild-Type-BuildArtifacts-encryptionDisabled"></a>
 Information that tells you if encryption for build artifacts is disabled.
Type: Boolean
Required: No

 ** location **   <a name="CodeBuild-Type-BuildArtifacts-location"></a>
Information about the location of the build artifacts.
Type: String
Required: No

 ** md5sum **   <a name="CodeBuild-Type-BuildArtifacts-md5sum"></a>
The MD5 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.
This value is available only if the build project's `packaging` value is set to `ZIP`.
Type: String
Required: No

 ** overrideArtifactName **   <a name="CodeBuild-Type-BuildArtifacts-overrideArtifactName"></a>
 If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.
Type: Boolean
Required: No

 ** sha256sum **   <a name="CodeBuild-Type-BuildArtifacts-sha256sum"></a>
The SHA-256 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.
This value is available only if the build project's `packaging` value is set to `ZIP`.
Type: String
Required: No

## See Also
<a name="API_BuildArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BuildArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BuildArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BuildArtifacts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
