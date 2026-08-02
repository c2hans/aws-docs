---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchSource.html
---

# PatchSource
<a name="API_PatchSource"></a>

Information about the patches to use to update the managed nodes, including target operating systems and source repository. Applies to Linux managed nodes only.

## Contents
<a name="API_PatchSource_Contents"></a>

 ** Configuration **   <a name="systemsmanager-Type-PatchSource-Configuration"></a>
The value of the repo configuration.
 **Example for yum repositories**
 `[main]`
 `name=MyCustomRepository`
 `baseurl=https://my-custom-repository`
 `enabled=1`
For information about other options available for your yum repository configuration, see [dnf.conf(5)](https://man7.org/linux/man-pages/man5/dnf.conf.5.html) on the *man7.org* website.
 **Examples for Ubuntu Server and Debian Server**
 `deb http://security.ubuntu.com/ubuntu jammy main`
 `deb https://site.example.com/debian distribution component1 component2 component3`
Repo information for Ubuntu Server repositories must be specifed in a single line. For more examples and information, see [jammy (5) sources.list.5.gz](https://manpages.ubuntu.com/manpages/jammy/man5/sources.list.5.html) on the *Ubuntu Server Manuals* website and [sources.list format](https://wiki.debian.org/SourcesList#sources.list_format) on the *Debian Wiki*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** Name **   <a name="systemsmanager-Type-PatchSource-Name"></a>
The name specified to identify the patch source.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,50}$`
Required: Yes

 ** Products **   <a name="systemsmanager-Type-PatchSource-Products"></a>
The specific operating system versions a patch repository applies to, such as "Ubuntu16.04", "AmazonLinux2016.09", "RedhatEnterpriseLinux7.2" or "Suse12.7". For lists of supported product values, see [PatchFilter](API_PatchFilter.md).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_PatchSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PatchSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PatchSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PatchSource)
