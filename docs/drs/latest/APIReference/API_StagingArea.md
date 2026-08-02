---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_StagingArea.html
---

# StagingArea
<a name="API_StagingArea"></a>

Staging information related to source server.

## Contents
<a name="API_StagingArea_Contents"></a>

 ** errorMessage **   <a name="drs-Type-StagingArea-errorMessage"></a>
Shows an error message that occurred when DRS tried to access the staging source server. In this case StagingArea$status will have value EXTENSION\_ERROR
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

 ** stagingAccountID **   <a name="drs-Type-StagingArea-stagingAccountID"></a>
Account ID of the account to which source server belongs. If this source server is extended - shows Account ID of staging source server.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** stagingSourceServerArn **   <a name="drs-Type-StagingArea-stagingSourceServerArn"></a>
Arn of the staging source server if this source server is extended
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** status **   <a name="drs-Type-StagingArea-status"></a>
Status of Source server extension. Possible values: (a) NOT\_EXTENDED - This is a source server that is replicating in the current account. (b) EXTENDED - Source server is extended from a staging source server. In this case, the value of stagingSourceServerArn is pointing to the Arn of the source server in the staging account. (c) EXTENSION\_ERROR - Some issue occurred when accessing staging source server. In this case, errorMessage field will contain an error message that explains what happened.
Type: String
Valid Values: `EXTENDED | EXTENSION_ERROR | NOT_EXTENDED`
Required: No

## See Also
<a name="API_StagingArea_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/StagingArea)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/StagingArea)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/StagingArea)
