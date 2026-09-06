---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectCache.html
---

# ProjectCache
<a name="API_ProjectCache"></a>

Information about the cache for the build project.

## Contents
<a name="API_ProjectCache_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** type **   <a name="CodeBuild-Type-ProjectCache-type"></a>
The type of cache used by the build project. Valid values include:
+  `NO_CACHE`: The build project does not use any cache.
+  `S3`: The build project reads and writes from and to S3.
+  `LOCAL`: The build project stores a cache locally on a build host that is only available to that build host.
Type: String
Valid Values: `NO_CACHE | S3 | LOCAL`
Required: Yes

 ** cacheNamespace **   <a name="CodeBuild-Type-ProjectCache-cacheNamespace"></a>
Defines the scope of the cache. You can use this namespace to share a cache across multiple projects. For more information, see [Cache sharing between projects](https://docs.aws.amazon.com/codebuild/latest/userguide/caching-s3.html#caching-s3-sharing) in the * AWS CodeBuild User Guide*.
Type: String
Required: No

 ** location **   <a name="CodeBuild-Type-ProjectCache-location"></a>
Information about the cache location:
+  `NO_CACHE` or `LOCAL`: This value is ignored.
+  `S3`: This is the S3 bucket name/prefix.
Type: String
Required: No

 ** modes **   <a name="CodeBuild-Type-ProjectCache-modes"></a>
An array of strings that specify the local cache modes. You can use one or more local cache modes at the same time. This is only used for `LOCAL` cache types.
Possible values are:
LOCAL\_SOURCE\_CACHE
Caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.
LOCAL\_DOCKER\_LAYER\_CACHE
Caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.
+ You can use a Docker layer cache in the Linux environment only.
+ The `privileged` flag must be set so that your project has the required Docker permissions.
+ You should consider the security implications before you use a Docker layer cache.
LOCAL\_CUSTOM\_CACHE
Caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:
+ Only directories can be specified for caching. You cannot specify individual files.
+ Symlinks are used to reference cached directories.
+ Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.
Type: Array of strings
Valid Values: `LOCAL_DOCKER_LAYER_CACHE | LOCAL_SOURCE_CACHE | LOCAL_CUSTOM_CACHE`
Required: No

## See Also
<a name="API_ProjectCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ProjectCache)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ProjectCache)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ProjectCache)
