---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectFileSystemLocation.html
---

# ProjectFileSystemLocation
<a name="API_ProjectFileSystemLocation"></a>

 Information about a file system created by Amazon Elastic File System (EFS). For more information, see [What Is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

## Contents
<a name="API_ProjectFileSystemLocation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** identifier **   <a name="CodeBuild-Type-ProjectFileSystemLocation-identifier"></a>
The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the `identifier` in all capital letters to `CODEBUILD_`. For example, if you specify `my_efs` for `identifier`, a new environment variable is create named `CODEBUILD_MY_EFS`.
 The `identifier` is used to mount your file system.
Type: String
Required: No

 ** location **   <a name="CodeBuild-Type-ProjectFileSystemLocation-location"></a>
A string that specifies the location of the file system created by Amazon EFS. Its format is `efs-dns-name:/directory-path`. You can find the DNS name of file system when you view it in the Amazon EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is `fs-abcd1234.efs.us-west-2.amazonaws.com`, and its mount directory is `my-efs-mount-directory`, then the `location` is `fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory`.
The directory path in the format `efs-dns-name:/directory-path` is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.
Type: String
Required: No

 ** mountOptions **   <a name="CodeBuild-Type-ProjectFileSystemLocation-mountOptions"></a>
 The mount options for a file system created by Amazon EFS. The default mount options used by CodeBuild are `nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2`. For more information, see [Recommended NFS Mount Options](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-nfs-mount-settings.html).
Type: String
Required: No

 ** mountPoint **   <a name="CodeBuild-Type-ProjectFileSystemLocation-mountPoint"></a>
The location in the container where you mount the file system.
Type: String
Required: No

 ** type **   <a name="CodeBuild-Type-ProjectFileSystemLocation-type"></a>
 The type of the file system. The one supported type is `EFS`.
Type: String
Valid Values: `EFS`
Required: No

## See Also
<a name="API_ProjectFileSystemLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ProjectFileSystemLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ProjectFileSystemLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ProjectFileSystemLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
