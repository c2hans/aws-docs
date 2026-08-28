---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FileUploaderFieldConfig.html
---

# FileUploaderFieldConfig
<a name="API_FileUploaderFieldConfig"></a>

Describes the configuration for the file uploader field.

## Contents
<a name="API_FileUploaderFieldConfig_Contents"></a>

 ** acceptedFileTypes **   <a name="amplifyuibuilder-Type-FileUploaderFieldConfig-acceptedFileTypes"></a>
The file types that are allowed to be uploaded by the file uploader. Provide this information in an array of strings specifying the valid file extensions.
Type: Array of strings
Required: Yes

 ** accessLevel **   <a name="amplifyuibuilder-Type-FileUploaderFieldConfig-accessLevel"></a>
The access level to assign to the uploaded files in the Amazon S3 bucket where they are stored. The valid values for this property are `private`, `protected`, or `public`. For detailed information about the permissions associated with each access level, see [File access levels](https://docs.amplify.aws/lib/storage/configureaccess/q/platform/js/) in the *Amplify documentation*.
Type: String
Valid Values: `public | protected | private`
Required: Yes

 ** isResumable **   <a name="amplifyuibuilder-Type-FileUploaderFieldConfig-isResumable"></a>
Allows the file upload operation to be paused and resumed. The default value is `false`.
When `isResumable` is set to `true`, the file uploader uses a multipart upload to break the files into chunks before upload. The progress of the upload isn't continuous, because the file uploader uploads a chunk at a time.
Type: Boolean
Required: No

 ** maxFileCount **   <a name="amplifyuibuilder-Type-FileUploaderFieldConfig-maxFileCount"></a>
Specifies the maximum number of files that can be selected to upload. The default value is an unlimited number of files.
Type: Integer
Required: No

 ** maxSize **   <a name="amplifyuibuilder-Type-FileUploaderFieldConfig-maxSize"></a>
The maximum file size in bytes that the file uploader will accept. The default value is an unlimited file size.
Type: Integer
Required: No

 ** showThumbnails **   <a name="amplifyuibuilder-Type-FileUploaderFieldConfig-showThumbnails"></a>
Specifies whether to display or hide the image preview after selecting a file for upload. The default value is `true` to display the image preview.
Type: Boolean
Required: No

## See Also
<a name="API_FileUploaderFieldConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/FileUploaderFieldConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/FileUploaderFieldConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/FileUploaderFieldConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
