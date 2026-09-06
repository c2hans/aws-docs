---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ScriptDetails.html
---

# ScriptDetails
<a name="API_ScriptDetails"></a>

Describes the details of the script.

## Contents
<a name="API_ScriptDetails_Contents"></a>

 ** ExecutablePath **   <a name="WorkSpacesApplications-Type-ScriptDetails-ExecutablePath"></a>
The run path for the script.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** ScriptS3Location **   <a name="WorkSpacesApplications-Type-ScriptDetails-ScriptS3Location"></a>
The S3 object location for the script.
Type: [S3Location](API_S3Location.md) object
Required: Yes

 ** TimeoutInSeconds **   <a name="WorkSpacesApplications-Type-ScriptDetails-TimeoutInSeconds"></a>
The run timeout, in seconds, for the script.
Type: Integer
Required: Yes

 ** ExecutableParameters **   <a name="WorkSpacesApplications-Type-ScriptDetails-ExecutableParameters"></a>
The runtime parameters passed to the run path for the script.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ScriptDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ScriptDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ScriptDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ScriptDetails)
