---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_FileVersion.html
---

# FileVersion
<a name="API_FileVersion"></a>

Information about a version of a file.

## Contents
<a name="API_FileVersion_Contents"></a>

 ** blobId **   <a name="CodeCommit-Type-FileVersion-blobId"></a>
The blob ID of the object that represents the content of the file in this version.
Type: String
Required: No

 ** commit **   <a name="CodeCommit-Type-FileVersion-commit"></a>
Returns information about a specific commit.
Type: [Commit](API_Commit.md) object
Required: No

 ** path **   <a name="CodeCommit-Type-FileVersion-path"></a>
The name and path of the file at which this blob is indexed which contains the data for this version of the file. This value will vary between file versions if a file is renamed or if its path changes.
Type: String
Required: No

 ** revisionChildren **   <a name="CodeCommit-Type-FileVersion-revisionChildren"></a>
An array of commit IDs that contain more recent versions of this file. If there are no additional versions of the file, this array will be empty.
Type: Array of strings
Required: No

## See Also
<a name="API_FileVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/FileVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/FileVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/FileVersion)
