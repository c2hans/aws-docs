---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Note.html
---

# Note
<a name="API_Note"></a>

A user-defined note added to a finding.

## Contents
<a name="API_Note_Contents"></a>

 ** Text **   <a name="securityhub-Type-Note-Text"></a>
The text of a note.
Length Constraints: Minimum of 1. Maximum of 512.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** UpdatedAt **   <a name="securityhub-Type-Note-UpdatedAt"></a>
A timestamp that indicates when the note was updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** UpdatedBy **   <a name="securityhub-Type-Note-UpdatedBy"></a>
The principal that created a note.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_Note_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Note)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Note)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Note)
