---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ProcessDetails.html
---

# ProcessDetails
<a name="API_ProcessDetails"></a>

The details of process-related information about a finding.

## Contents
<a name="API_ProcessDetails_Contents"></a>

 ** LaunchedAt **   <a name="securityhub-Type-ProcessDetails-LaunchedAt"></a>
Indicates when the process was launched.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-ProcessDetails-Name"></a>
The name of the process.
Length Constraints: Minimum of 1. Maximum of 64.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ParentPid **   <a name="securityhub-Type-ProcessDetails-ParentPid"></a>
The parent process ID. This field accepts positive integers between `O` and `2147483647`.
Type: Integer
Required: No

 ** Path **   <a name="securityhub-Type-ProcessDetails-Path"></a>
The path to the process executable.
Length Constraints: Minimum of 1. Maximum of 512.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Pid **   <a name="securityhub-Type-ProcessDetails-Pid"></a>
The process ID.
Type: Integer
Required: No

 ** TerminatedAt **   <a name="securityhub-Type-ProcessDetails-TerminatedAt"></a>
Indicates when the process was terminated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ProcessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ProcessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ProcessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ProcessDetails)
