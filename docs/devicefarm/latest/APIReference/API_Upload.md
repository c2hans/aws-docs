---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html
---

# Upload
<a name="API_Upload"></a>

An app or a set of one or more tests to upload or that have been uploaded.

## Contents
<a name="API_Upload_Contents"></a>

 ** arn **   <a name="devicefarm-Type-Upload-arn"></a>
The upload's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** category **   <a name="devicefarm-Type-Upload-category"></a>
The upload's category. Allowed values include:
+ CURATED: An upload managed by AWS Device Farm.
+ PRIVATE: An upload managed by the AWS Device Farm customer.
Type: String
Valid Values: `CURATED | PRIVATE`
Required: No

 ** contentType **   <a name="devicefarm-Type-Upload-contentType"></a>
The upload's content type (for example, `application/octet-stream`).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** created **   <a name="devicefarm-Type-Upload-created"></a>
When the upload was created.
Type: Timestamp
Required: No

 ** message **   <a name="devicefarm-Type-Upload-message"></a>
A message about the upload's result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** metadata **   <a name="devicefarm-Type-Upload-metadata"></a>
The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** name **   <a name="devicefarm-Type-Upload-name"></a>
The upload's file name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** status **   <a name="devicefarm-Type-Upload-status"></a>
The upload's status.
Must be one of the following values:
+ FAILED
+ INITIALIZED
+ PROCESSING
+ SUCCEEDED
Type: String
Valid Values: `INITIALIZED | PROCESSING | SUCCEEDED | FAILED`
Required: No

 ** type **   <a name="devicefarm-Type-Upload-type"></a>
The upload's type.
Must be one of the following values:
+ ANDROID\_APP
+ IOS\_APP
+ WEB\_APP
+ EXTERNAL\_DATA
+ APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE
+ APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE
+ APPIUM\_PYTHON\_TEST\_PACKAGE
+ APPIUM\_NODE\_TEST\_PACKAGE
+ APPIUM\_RUBY\_TEST\_PACKAGE
+ APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE
+ APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE
+ APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE
+ APPIUM\_WEB\_NODE\_TEST\_PACKAGE
+ APPIUM\_WEB\_RUBY\_TEST\_PACKAGE
+ INSTRUMENTATION\_TEST\_PACKAGE
+ XCTEST\_TEST\_PACKAGE
+ XCTEST\_UI\_TEST\_PACKAGE
+ APPIUM\_JAVA\_JUNIT\_TEST\_SPEC
+ APPIUM\_JAVA\_TESTNG\_TEST\_SPEC
+ APPIUM\_PYTHON\_TEST\_SPEC
+ APPIUM\_NODE\_TEST\_SPEC
+ APPIUM\_RUBY\_TEST\_SPEC
+ APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_SPEC
+ APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_SPEC
+ APPIUM\_WEB\_PYTHON\_TEST\_SPEC
+ APPIUM\_WEB\_NODE\_TEST\_SPEC
+ APPIUM\_WEB\_RUBY\_TEST\_SPEC
+ INSTRUMENTATION\_TEST\_SPEC
+ XCTEST\_UI\_TEST\_SPEC
Type: String
Valid Values: `ANDROID_APP | IOS_APP | WEB_APP | EXTERNAL_DATA | APPIUM_JAVA_JUNIT_TEST_PACKAGE | APPIUM_JAVA_TESTNG_TEST_PACKAGE | APPIUM_PYTHON_TEST_PACKAGE | APPIUM_NODE_TEST_PACKAGE | APPIUM_RUBY_TEST_PACKAGE | APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE | APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE | APPIUM_WEB_PYTHON_TEST_PACKAGE | APPIUM_WEB_NODE_TEST_PACKAGE | APPIUM_WEB_RUBY_TEST_PACKAGE | CALABASH_TEST_PACKAGE | INSTRUMENTATION_TEST_PACKAGE | UIAUTOMATION_TEST_PACKAGE | UIAUTOMATOR_TEST_PACKAGE | XCTEST_TEST_PACKAGE | XCTEST_UI_TEST_PACKAGE | APPIUM_JAVA_JUNIT_TEST_SPEC | APPIUM_JAVA_TESTNG_TEST_SPEC | APPIUM_PYTHON_TEST_SPEC | APPIUM_NODE_TEST_SPEC | APPIUM_RUBY_TEST_SPEC | APPIUM_WEB_JAVA_JUNIT_TEST_SPEC | APPIUM_WEB_JAVA_TESTNG_TEST_SPEC | APPIUM_WEB_PYTHON_TEST_SPEC | APPIUM_WEB_NODE_TEST_SPEC | APPIUM_WEB_RUBY_TEST_SPEC | INSTRUMENTATION_TEST_SPEC | XCTEST_UI_TEST_SPEC`
Required: No

 ** url **   <a name="devicefarm-Type-Upload-url"></a>
The presigned Amazon S3 URL that was used to store a file using a PUT request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_Upload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Upload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Upload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Upload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
